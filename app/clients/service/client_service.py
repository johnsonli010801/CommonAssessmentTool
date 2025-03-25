from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from typing import Optional
from app.models import Client, ClientCase, User
from app.clients.schema import ClientUpdate, ServiceUpdate


class ClientQueryService:
    # Retrieve a single client by ID
    @staticmethod
    def get_client(db: Session, client_id: int):
        client = db.query(Client).filter(Client.id == client_id).first()
        if not client:
            raise HTTPException(status_code=404, detail=f"Client {client_id} not found")
        return client

    # Retrieve a paginated list of clients
    @staticmethod
    def get_clients(db: Session, skip: int = 0, limit: int = 50):
        if skip < 0 or limit < 1:
            raise HTTPException(status_code=400, detail="Invalid pagination parameters")
        return {
            "clients": db.query(Client).offset(skip).limit(limit).all(),
            "total": db.query(Client).count()
        }

    # Retrieve clients that match various optional criteria filters
    @staticmethod
    def get_clients_by_criteria(
        db: Session,
        employment_status: Optional[bool] = None,
        education_level: Optional[int] = None,
        age_min: Optional[int] = None,
        gender: Optional[int] = None,
        work_experience: Optional[int] = None,
        canada_workex: Optional[int] = None,
        dep_num: Optional[int] = None,
        canada_born: Optional[bool] = None,
        citizen_status: Optional[bool] = None,
        fluent_english: Optional[bool] = None,
        reading_english_scale: Optional[int] = None,
        speaking_english_scale: Optional[int] = None,
        writing_english_scale: Optional[int] = None,
        numeracy_scale: Optional[int] = None,
        computer_scale: Optional[int] = None,
        transportation_bool: Optional[bool] = None,
        caregiver_bool: Optional[bool] = None,
        housing: Optional[int] = None,
        income_source: Optional[int] = None,
        felony_bool: Optional[bool] = None,
        attending_school: Optional[bool] = None,
        substance_use: Optional[bool] = None,
        time_unemployed: Optional[int] = None,
        need_mental_health_support_bool: Optional[bool] = None,
    ):
        """Search clients by any combination of criteria"""
        query = db.query(Client)
        query = ClientQueryService._apply_criteria_filters(
            query,
            employment_status=employment_status,
            education_level=education_level,
            age_min=age_min,
            gender=gender,
            work_experience=work_experience,
            canada_workex=canada_workex,
            dep_num=dep_num,
            canada_born=canada_born,
            citizen_status=citizen_status,
            fluent_english=fluent_english,
            reading_english_scale=reading_english_scale,
            speaking_english_scale=speaking_english_scale,
            writing_english_scale=writing_english_scale,
            numeracy_scale=numeracy_scale,
            computer_scale=computer_scale,
            transportation_bool=transportation_bool,
            caregiver_bool=caregiver_bool,
            housing=housing,
            income_source=income_source,
            felony_bool=felony_bool,
            attending_school=attending_school,
            substance_use=substance_use,
            time_unemployed=time_unemployed,
            need_mental_health_support_bool=need_mental_health_support_bool,
        )
        try:
            return query.all()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error retrieving clients: {str(e)}")

    # Filter clients based on service-related fields
    @staticmethod
    def get_clients_by_services(db: Session, **service_filters: Optional[bool]):
        query = db.query(Client).join(ClientCase)
        for service, status_val in service_filters.items():
            if status_val is not None:
                query = query.filter(getattr(ClientCase, service) == status_val)
        try:
            return query.all()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error retrieving clients: {str(e)}")

    # Get all services associated with a given client
    @staticmethod
    def get_client_services(db: Session, client_id: int):
        services = db.query(ClientCase).filter(ClientCase.client_id == client_id).all()
        if not services:
            raise HTTPException(status_code=404, detail=f"No services found for client {client_id}")
        return services

    # Get clients with a minimum success rate
    @staticmethod
    def get_clients_by_success_rate(db: Session, min_rate: int = 70):
        if not (0 <= min_rate <= 100):
            raise HTTPException(status_code=400, detail="Success rate must be between 0 and 100")
        return db.query(Client).join(ClientCase).filter(ClientCase.success_rate >= min_rate).all()

    # Get all clients assigned to a specific case worker
    @staticmethod
    def get_clients_by_case_worker(db: Session, case_worker_id: int):
        if not db.query(User).filter(User.id == case_worker_id).first():
            raise HTTPException(status_code=404, detail=f"Case worker {case_worker_id} not found")
        return db.query(Client).join(ClientCase).filter(ClientCase.user_id == case_worker_id).all()

    # Internal helper method to apply dynamic filtering logic
    @staticmethod
    def _apply_criteria_filters(query, **filters):
        if filters.get("education_level") and not (1 <= filters["education_level"] <= 14):
            raise HTTPException(status_code=400, detail="Invalid education level")
        if filters.get("age_min") and filters["age_min"] < 18:
            raise HTTPException(status_code=400, detail="Minimum age must be at least 18")
        if filters.get("gender") and filters["gender"] not in [1, 2]:
            raise HTTPException(status_code=400, detail="Gender must be 1 or 2")

        for key, val in filters.items():
            if val is not None and hasattr(Client, key):
                query = query.filter(getattr(Client, key) == val)
        return query


class ClientMutationService:
    # Update client information based on provided fields
    @staticmethod
    def update_client(db: Session, client_id: int, update_data: ClientUpdate):
        client = db.query(Client).filter(Client.id == client_id).first()
        if not client:
            raise HTTPException(status_code=404, detail=f"Client {client_id} not found")
        for field, value in update_data.dict(exclude_unset=True).items():
            setattr(client, field, value)
        try:
            db.commit()
            db.refresh(client)
            return client
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=f"Failed to update client: {str(e)}")

    # Update service info for a specific client-case worker relationship
    @staticmethod
    def update_client_services(db: Session, client_id: int, user_id: int, update_data: ServiceUpdate):
        case = db.query(ClientCase).filter(ClientCase.client_id == client_id, ClientCase.user_id == user_id).first()
        if not case:
            raise HTTPException(status_code=404, detail=f"No case found for client {client_id} and worker {user_id}")
        for field, value in update_data.dict(exclude_unset=True).items():
            setattr(case, field, value)
        try:
            db.commit()
            db.refresh(case)
            return case
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=f"Failed to update client services: {str(e)}")

    # Assign a new case worker to a client, with default service values
    @staticmethod
    def create_case_assignment(db: Session, client_id: int, worker_id: int):
        if not db.query(Client).filter(Client.id == client_id).first():
            raise HTTPException(status_code=404, detail=f"Client {client_id} not found")
        if not db.query(User).filter(User.id == worker_id).first():
            raise HTTPException(status_code=404, detail=f"Case worker {worker_id} not found")
        if db.query(ClientCase).filter(ClientCase.client_id == client_id, ClientCase.user_id == worker_id).first():
            raise HTTPException(status_code=400, detail=f"Assignment already exists")

        case = ClientCase(
            client_id=client_id,
            user_id=worker_id,
            employment_assistance=False,
            life_stabilization=False,
            retention_services=False,
            specialized_services=False,
            employment_related_financial_supports=False,
            employer_financial_supports=False,
            enhanced_referrals=False,
            success_rate=0
        )
        try:
            db.add(case)
            db.commit()
            db.refresh(case)
            return case
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=f"Failed to create assignment: {str(e)}")

    # Delete a client and all related case records
    @staticmethod
    def delete_client(db: Session, client_id: int):
        client = db.query(Client).filter(Client.id == client_id).first()
        if not client:
            raise HTTPException(status_code=404, detail=f"Client {client_id} not found")
        try:
            db.query(ClientCase).filter(ClientCase.client_id == client_id).delete()
            db.delete(client)
            db.commit()
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=f"Failed to delete client: {str(e)}")

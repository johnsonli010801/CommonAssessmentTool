# Use Python 3.11 image as base
FROM python:3.11

# Set working directory
WORKDIR /code

# Copy requirements first to leverage Docker cache
COPY ./requirements.txt /code/requirements.txt

# Install required packages
RUN pip install --no-cache-dir -r /code/requirements.txt

# Copy the rest of your application
COPY . /code/
COPY entrypoint.sh /code/

# Make the entrypoint script executable
RUN chmod +x /code/entrypoint.sh

# Expose the port your app runs on
EXPOSE 8000

# Set the entrypoint script
ENTRYPOINT ["/code/entrypoint.sh"]
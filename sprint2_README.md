Sprint 2:

## Installing Docker

Docker is required to containerize and run the backend application. Follow the instructions below based on your operating system to install Docker.

### Linux Installation

To install Docker on Linux, execute the following commands in your terminal:

```bash
# Download and run the Docker installation script
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Add your user to the Docker group to manage Docker as a non-root user
sudo usermod -aG docker ${USER}
newgrp docker
```
### Macos Installation

# Install Docker on macOS using Homebrew
`brew install --cask docker`

### Window:
# Install Docker on Windows using Chocolatey
`choco install docker-desktop`

### Verify Version:
`docker --version`

### Or Using Official Website:
### Installing Docker

1. **Visit the Docker website**: Go to [Docker's official website](https://docs.docker.com/get-docker/) to download Docker Desktop.
2. **Download Docker**: Choose the version of Docker Desktop that corresponds to your operating system (Windows/MacOS).
3. **Install Docker**: Open the downloaded file and follow the installation instructions.
4. **Start Docker**: Once installed, run Docker from your applications folder. Docker needs to be running for the application to work.

### Type the following command to start the application using Docker-Compose:


`docker-compose up --build`
This command tells Docker to prepare and run the application. It may take a few minutes to complete, especially the first time.

### Run the programming using Docker Run:
`docker build -t my-app-name . `
`docker run -p 8000:8000 my-app-name`


### 5. Accessing the Application
Once the application is running, open your web browser and visit:

```http://localhost:8000/docs```
### 6. Stopping the Application
When you are done using the application, you can stop it by going back to your terminal or command prompt, pressing `Ctrl+C`, and then typing:
`docker-compose down`
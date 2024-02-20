# Hello World, for Docker Compose

This project is designed to demonstrate a simple multi-container application using Docker, consisting of a web app and a FastAPI service. Our goal is to provide an easy-to-understand example of how separate components of an application can be containerized and made to communicate with each other in a Dockerized environment.

## Project Components

- **Web App**: A basic web application that serves as the user interface. Users can interact with this web app through their browser, making requests and receiving responses.

- **FastAPI Service**: A lightweight and efficient API built with FastAPI. This service handles backend logic, processes API calls made from the web app, and performs specified actions or returns the requested data.

The web app and the FastAPI service are each packaged into their own Docker containers. These containers are defined and managed using Docker Compose, which allows them to be launched and run simultaneously with a single command. The web app communicates with the FastAPI service using HTTP requests, demonstrating a simple but effective pattern for separating frontend and backend logic in a microservices architecture.

## Getting Started 

- Ensure you have Docker and Docker Compose installed on your local machine
- Clone the repository. Navigate to the root of the project and run:
``` bash 
docker-compose up 
```
This will build the necessary Docker images (if they're not already built) and start the containers.

## Accessing the Application 
Once the containers are up and running, you can access the web app by visiting http://localhost:8501 in your web browser. The FastAPI service will be available at http://localhost:8000. You can interact with the FastAPI service directly or through the web app, depending on the setup and functionality provided.
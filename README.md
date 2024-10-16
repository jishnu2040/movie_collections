# Movie Collection Backend

This repository contains the backend for the Movie Collection application, built with Django. You can set up and run this application in three different ways:

## API Documentation

This contains the whole documentaion of the api endpoints.

[https://documenter.getpostman.com/view/32963641/2sAXqy3erU](https://documenter.getpostman.com/view/32963641/2sAXxS6WZn)

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Setup Methods](#setup-methods)
   - [1. Pull Docker Image from Docker Hub](#1-pull-docker-image-from-docker-hub)
   - [2. Clone GitHub and Build and Run Docker Image](#2-clone-github-and-build-and-run-docker-image)
   - [3. Clone Git Repo and Run Code in Local Machine](#3-clone-git-repo-and-run-code-in-local-machine)

## Prerequisites
- Ensure you have the following installed on your machine:
  - [Docker](https://www.docker.com/get-started)
  - [Docker Compose](https://docs.docker.com/compose/install/)
  - [Git](https://git-scm.com/downloads)

## Setup Methods

### 1. Pull Docker Image from Docker Hub

To run the application using the Docker image hosted on Docker Hub, follow these steps:
N/A : have to setup other image manually , so recommand to follow 2nd setup!!!
1. Open your terminal.
2. Pull the Docker image:
   ```bash
   docker pull jishnu2040/moviecollection_backend-web:latest

3. Run the Docker container
 ```bash
   docker run -d -p 8000:8000 jishnu2040/moviecollection_backend-web:latest
```

4. Access the application in your browser at.
 ```bash
   http://localhost:8000
```



### 2. Clone GitHub and Build and Run Docker Image

To build and run the Docker image from the GitHub repository:

1. Clone the repository:
   ```bash
   git clone https://github.com/jishnu2040/movie_collections

2.Navigate to the project directory:
```bash
   cd movie_collections
```
3.Build the Docker image:
```bash
   docker-compose up --build
```
4.Migrate database:
```bash
   docker-compose exec web python manage.py migrate
```
5.Access the application in your browser at:
```bash
   http://localhost:8000.
```

### 3. Clone Git Repo and Run Code in Local Machine

To run the application in a local environment without Docker:

1. **Clone the repository**:  
   Open your terminal and run:
   ```bash
   git clone https://github.com/jishnu2040/movie_collections
2.Navigate to the project directory:

```bash
  cd movie_collections

```
3.Create a virtual environment:

```bash
  python -m venv venv

```
4.Activate the virtual environment:

```bash
  # For Linux/macOS
source venv/bin/activate

# For Windows
venv\Scripts\activate

```

5.Install dependencies

```bash
  pip install -r requirements.txt
```

Apply Migrations

```bash
  python manage.py migrate
```
Create a Superuser (Optional)

```bash
  python manage.py createsuperuser

```

6.Start the server

```bash
  python manage.py runserver

```
7.Change postgres config -> settings.py 
  - [comment docker database & uncomment database in local machine](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)



## Tech Stack

Client: PostMan

Server: Django REST, JWT, Docker





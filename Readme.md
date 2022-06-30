# TrojAI Demo Project

Folders:
- api: A FastAPI Rest API To connect to Postgres DB and serve data to frontend, uses SQLModel to model and create database tables
- frontend: A Vue.JS Frontend to display data very simply from the API 
- docker-compose.yaml: A docker-compose file to run the API, frontend and postgres in docker containers

## How to Run:
- Assumptions: you have docker, docker-compose

### Notes:
- Python script must run to create tables but we want to use Uvicorn to run the API 
  - This means docker command should likely run the python script first, then serve the app
  - 
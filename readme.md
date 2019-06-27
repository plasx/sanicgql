# GraphQL + Sanic + SQLAlchemy

I wanted to create a simple minimal starter utilizing SQLAlchemy, Sanic, and GraphQL.

### Running locally

To run install the requirements.txt 
    
    pip install -r requirements.txt


then run the application by running app.py

    python app.py


you'll be able to access the URL of GRAPHIQL at http://localhost:8080/graphql


# Sanic

### Running with Docker
Execute the docker compose file by doing the following:

    docker-compose -f docker-compose.yml build sanicgql
    docker-compose -f docker-compose.yml run --service-ports sanicgql
Then visit the URL below in your browser to access the graphql explorer
    
    http://localhost:8080/graphql
### Usage

    WIP
    
### Unit Tests
    
    WIP

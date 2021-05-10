# What's inside
Process running a schema validation against file with events and reporting summarizing event counts.

# Dependencies
1. Docker installation

# Setup
1. Build the image: `docker build -t taxfix-assignment .`
2. From within root folder inside the project, run the container using that image: ```docker run -d -v `pwd`/output:/schema_validator/output taxfix-assignment:latest```

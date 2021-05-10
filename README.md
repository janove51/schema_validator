# What's inside
Process running a schema validation against file with events and reporting summarizing event counts.

# Dependencies
1. Docker installation

# Setup
1. Build the image: `docker build -t taxfix-assignment .`
2. Run the image: ```docker run -d -v `pwd`/output:/schema_validator/output taxfix-assignment:latest```

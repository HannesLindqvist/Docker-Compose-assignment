# Docker-Compose-assignment

1. To use this API clone the repo to your local machine.

2. To start the application type in: docker compose up

3. To insert data use the Curl command. 
Example: curl -X POST -H "Content-Type: application/json" -d "{\"name\" : \”Hans\”, \"last_name\" : \"Smith\"}" localhost:5000/persons

4. If you want to retrieve you data that you posted you can either use the curl command or the localhost URL.
Example Curl: curl -X GET -H "Content-Type: application/json" localhost:5000/persons
Localhost: Localhost:5000/persons

To quit the app type in: docker compose down

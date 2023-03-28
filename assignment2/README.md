## CS217 PA2
This assignment creates a Flask webserver to access spaCy NER. There is a database on the backend to keep track of counts, and the application is dockerized.

spaCy NER will tag all entities present in a text. There are various labels for entities, including person, location, and organization.

### Flask Webserver
This webserver allows a user to type their text in a textbox and click a button. The user will then be
directed to a new page. The new page displays the result form the request to spaCy. The entities are marked
in place in the sentence, and they are also listed individually. 

##### To run (without Docker): 
Run the flask_webserver.py file:
```bash
python flask_webserver.py
```
Go to the address (http://127.0.0.1:5000).

##### To run (with Docker): 
Create the Docker image by first navigating to the assignment2 folder in the terminal and running the command:
```bash
docker build -t myflaskapp .
```

This builds a Docker image called myflaskapp. Now run this command to start a container from this image:
```bash
docker run -p 5000:5000 myflaskapp
```

This maps port 5000 in the container to port 5000 on the host machine. Now go to http://localhost:5000 or http://127.0.0.1:5000 in a web browser to see the app. 

To stop the container, manually stop it in the Docker app, or run the command:
```bash
docker ps
```

This will provide the name of the container, which can then be used in the command:
```bash
docker stop <name>
```

### Modules and Versions
I used a conda environment and the following: 

conda 4.14.0

conda-build 3.21.5

flask 2.2.2

python 3.9.7

spacy 3.3.1


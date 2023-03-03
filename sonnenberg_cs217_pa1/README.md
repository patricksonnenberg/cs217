##CS217 PA1
This assignment contains three parts:
1. Creating a restful API to access spaCy NER
2. Creating a Flask webserver to access spaCy NER
3. Creating a Streamlit applicaiton to access spaCy NER

spaCy NER will tag all entities present in a text. There are various labels for entities, including person, location, and organization.

### 1. RESTful API
This RESTful API uses Flask. It has a get request to give instructions. The post request processes the result. 
The user can either specify a txt file, or can use a JSON string. If using a JSON string, the entire JSON string will be processed. 

##### To run:
Change directory to this folder. Run the restful_api.py file. 

```bash
python restful_api.py
```

In a different terminal, navigate again to the folder and use the following (example) curl commands:

```bash
$ curl http://127.0.0.1:5000/api
```

txt file:

```bash
$ curl -H "Content-Type: text/plain" -X POST -d@input.txt http://127.0.0.1:5000/api
```

JSON string:

```bash
$ curl http://127.0.0.1:5000/api -H "Content-Type: application/json" -d '{"Add your text here": "And here"}'
```




### 2. Flask Webserver
This webserver allows a user to type their text in a textbox and click a button. The user will then be
directed to a new page. The new page displays the result form the request to spaCy. The entities are marked
in place in the sentence, and they are also listed individually. 

##### To run: 
Run the flask_webserver.py file and go to the address (http://127.0.0.1:5000)

```bash
python flask_webserver.py
```


### 3. Streamlit
This streamlit application allows a user to type their text, along with select the types of entities they wish to mark.
There are additional drop-downs. The first will display the entire text with all entities regardless of the user's request.
The next two list all the entities: the first lists the entities in the order they appear in the text, and the other lists them alphabetically by the entity label.
The last drop-down is a visualizer that displays a bar graph containing the counts of each present entity label. 

##### To run: 
```bash
streamlit run streamlit_app.py
```


### Modules and Versions
I used a conda environment and the following: 

conda 4.14.0

conda-build 3.21.5

flask 2.2.2

flask_restful 0.3.9

matplotlib 3.6.2

pandas 1.5.2

python 3.9.7

spacy 3.3.1

streamlit 1.16.0


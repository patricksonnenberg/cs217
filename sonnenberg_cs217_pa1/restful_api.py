# Patrick Sonnenberg, CS217, PA1

from flask import Flask, request
from flask_restful import Resource, Api
import spacy
import io
import ner

app = Flask(__name__)
api = Api(app)
nlp = spacy.load("en_core_web_sm")

class NamedEntityProcessing(Resource):
    def get(self):
        return {'Welcome': 'This named entity recognizer will label and return all entities. You can provide a txt file to process or a JSON string.'}

    def post(self):
        text = str(request.data)
        sd = ner.SpacyDocument(text)
        return {'returning': sd.get_entities()}, 201

api.add_resource(NamedEntityProcessing, '/api')

if __name__ == '__main__':
    app.run(debug=True)

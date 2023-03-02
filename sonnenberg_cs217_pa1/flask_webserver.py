from flask import Flask, jsonify, request, render_template
import spacy
import ner

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")

@app.route("/")
def index():
    return render_template('form.html')

@app.route('/analyze', methods=["POST"])
def show_result():
    text = request.form["text_input"]
    doc = nlp(text)
    spacyed_text = ner.SpacyDocument(text)  # creates spacy object
    ner_spacyed_text = spacyed_text.get_entities_with_markup()  # calls on this method in ner to NER-ize the text
    return render_template("resultnew.html", text=ner_spacyed_text, entities=doc.ents)

if __name__ == '__main__':
    app.run(debug=True)

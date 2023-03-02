from collections import Counter

import streamlit as st
import spacy
import matplotlib.pyplot as plt

nlp = spacy.load("en_core_web_sm")

ENTITY_COLORS = {
    "PERSON": "#aa9cfc",
    "ORG": "#7aecec",
    "GPE": "#feca74",
    "LOC": "#ff9561",
    "FAC": "#ddd",
    "NORP": "#c887fb",
    "EVENT": "#ffeb80",
    "DATE": "#bfe1d9",
    "TIME": "#bfe1d9",
    "CARDINAL": "#e4e7d2",
    "ORDINAL": "#e4e7d2",
    "QUANTITY": "#e4e7d2",
    "PERCENT": "#e4e7d2",
    "MONEY": "#e4e7d2",
    "LANGUAGE": "#ff8197",
    "PRODUCT": "#bfeeb7",
    "WORK_OF_ART": "#f0d0ff",
}

def main():
    st.title("Find the Named Entities")
    user_input = st.text_area("Enter text here:")
    # Allows users to specify which entities they want to select
    show_entity_types = st.multiselect("Select entity types to show", list(ENTITY_COLORS.keys()), default=list(ENTITY_COLORS.keys()))
    st.button("Submit")

    if user_input:
            load_css()  # To format
            doc = nlp(user_input)
            chosen_entities(doc, user_input, show_entity_types)  # Display the whole string with the user's selected entities highlighted
            all_entities(doc, user_input)  # Display the whole string with all entities regardless of user request
            each_entity_columns(doc)  # Two drop-down columns: each list the entities - one in order, one alphabetical
            visualize(doc)  # Displays a bar chart with the counts of each label present in the text
            add_pizzazz(user_input)  # Adds some pizzazz

def load_css():
    """Loads the css file that specifies formatting"""
    with open("static/css/streamlitmain.css") as f:
        css = f.read()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

def chosen_entities(doc, user_input, show_entity_types):
    """Displays the whole string with the user's selected entities highlighted"""
    entity_positions = [(ent.start_char, ent.end_char, ent.label_) for ent in doc.ents]
    entity_positions.sort(key=lambda x: x[0])
    output_string = ""
    previous_end = 0
    for start, end, label in entity_positions:
        output_string += user_input[previous_end:start]
        if label in show_entity_types:
            output_string += f'<span class="entity {label}">{user_input[start:end]} ({label})</span>'
        else:
            output_string += user_input[start:end]
        previous_end = end
    output_string += user_input[previous_end:]
    st.markdown(f'<div>{output_string}</div>', unsafe_allow_html=True)  # Displays entire sentence
    st.text("")

def all_entities(doc, user_input):
    """Displays the whole string with all entities regardless of user request"""
    for ent in doc.ents:
        user_input = user_input.replace(ent.text, f'<span class="entity {ent.label_}">{ent.text} ({ent.label_})</span>')
    with st.expander("All Entities"):  # Displays all entities highlighted
        st.write(user_input, unsafe_allow_html=True)

def each_entity_columns(doc):
    """Creates two drop-down columns by calling on two functions. Each list the entities - one in order, one alphabetical"""
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            each_entity_in_order(doc)
        with col2:
            each_entity_alphabetical(doc)

def each_entity_in_order(doc):
    """Displays each entity individually in the order they appear in the text"""
    with st.expander("Each Entity (in Order)"):
        for ent in doc.ents:
            st.markdown(f'<span class="entity {ent.label_}">{ent.label_}: {ent.text}</span>', unsafe_allow_html=True)

def each_entity_alphabetical(doc):
    """Displays each entity sorted alphabetically by the label"""
    with st.expander("Each Entity (Alphabetical)"):
        entities = [(entity.text, entity.label_) for entity in doc.ents]
        sorted_entities = sorted(entities, key=lambda x: x[1])
        for entity in sorted_entities:
            st.markdown(f'<span class="entity {entity[1]}">{entity[1]}: {entity[0]}</span>', unsafe_allow_html=True)

def visualize(doc):
    """Displays a bar chart with the counts of each label present in the text"""
    with st.expander("Visualizer"):
        counts = Counter(ent.label_ for ent in doc.ents)
        fig, ax = plt.subplots()
        ax.bar(counts.keys(), counts.values(), color=[ENTITY_COLORS.get(key) for key in counts.keys()])
        ax.set_title("Entity Counts")
        ax.set_xlabel("Entity Labels")
        ax.set_ylabel("Count")
        ax.yaxis.set_major_locator(plt.MaxNLocator(integer=True))
        st.pyplot(fig)

def add_pizzazz(user_input):
    """
    Adds some *pizzazz*
    :return: Snow shall fall, balloons shall rise
    """
    if "Snow" in user_input or "snow" in user_input:
        st.snow()
    if "Balloon" in user_input or "balloon" in user_input:
        st.balloons()


if __name__=="__main__":
    main()
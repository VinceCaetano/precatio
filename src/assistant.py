
import spacy
import os

def read_bible_text():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    bible_path = os.path.join(script_dir, 'bible.txt')

    with open(bible_path, 'r', encoding='utf-8') as file:
        bible_text = file.read()
    return bible_text


from transformers import pipeline

# Load the question-answering model
question_answerer = pipeline("question-answering", model="deepset/roberta-base-squad2")

def process_question(question, bible_text):
    # Process the question and Bible text using the question-answering model
    result = question_answerer(question=question, context=bible_text)

    # Return the answer from the model
    return result["answer"]

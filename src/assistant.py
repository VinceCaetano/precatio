
import spacy
import os
import re
from transformers import pipeline


def read_bible_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        bible_text = file.read()
    return bible_text

question_answerer = pipeline("question-answering", model="deepset/roberta-base-squad2")

def get_context_information(question):
    pattern = r'(\w+) Chapter (\d+)'
    
    match = re.search(pattern, question)
    
    if match:
        chapter = match.group(2)
        line_number = 'Unknown'
        return {'chapter': chapter, 'line_number': line_number}
    else:
        return {'chapter': 'Unknown', 'line_number': 'Unknown'}
def process_question(question, bible_text):
    result = question_answerer(question=question, context=bible_text)

    print("Question:", question)
    print("Answer:", result["answer"])

 # Add context information
    context = get_context_information(question)
    print("Context:", context)


    return {'answer': result["answer"], 'context': context}

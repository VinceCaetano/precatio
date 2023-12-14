import spacy
import os

## sinonimos 
import re

## tranformers com contexto biblico
from transformers import pipeline

def read_bible_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        bible_text = file.read()
    return bible_text

question_answerer = pipeline("question-answering", model="deepset/roberta-base-squad2")

def get_context_information(question, bible_text, result):
    bible_text_lower = bible_text.lower()

    answer_position = bible_text_lower.find(result["answer"].lower())

    if answer_position != -1:
        text_before_answer = bible_text_lower[:answer_position]

        chapter_match = re.findall(r'chapter (\d+)', text_before_answer)
        if chapter_match:
            chapter = chapter_match[-1]
        else:
            chapter = 'Unk'

        book_match = re.findall(r'(\w+)[\n\s]*chapter', text_before_answer)
        if book_match:
            book = book_match[-1]
        else:
            book = 'Unk'

        verse_match = re.findall(r'(\d+)[^\d\n]*(?:\n|$)', text_before_answer)
        if verse_match:
            verse = verse_match[-1]
        else:
            text_after_answer = bible_text_lower[answer_position:]
            verse_match_after = re.findall(r'(\d+)[^\d\n]*(?:\n|$)', text_after_answer)
            if verse_match_after:
                verse = verse_match_after[0]
            else:
                verse = 'Unk'

        line_number = text_before_answer.count('\n') + 1

        return {'book': book, 'chapter': chapter, 'verse': verse, 'line_number': line_number}
    else:
        return {'book': 'Unk', 'chapter': 'Unk', 'verse': 'Unk', 'line_number': 'Unk'}
def process_question(question, bible_text):
    result = question_answerer(question=question, context=bible_text)

    context = get_context_information(question, bible_text, result)
    print("Context:", context)

    print("Question:", question)
    print("Answer:", result["answer"])

    result['context'] = context

    return result




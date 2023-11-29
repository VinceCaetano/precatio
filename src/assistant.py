import spacy
import os
import re
from transformers import pipeline

def read_bible_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        bible_text = file.read()
    return bible_text

question_answerer = pipeline("question-answering", model="deepset/roberta-base-squad2")

def get_context_information(question, bible_text, result):
    # Convert the Bible text and question to lowercase for case-insensitive matching
    bible_text_lower = bible_text.lower()

    # Find the position of the answer in the lowercase text
    answer_position = bible_text_lower.find(result["answer"].lower())

    if answer_position != -1:
        # Extract the text before the answer position
        text_before_answer = bible_text_lower[:answer_position]

        # Find the last occurrence of "Chapter" before the answer
        chapter_match = re.findall(r'chapter (\d+)', text_before_answer)
        if chapter_match:
            chapter = chapter_match[-1]
        else:
            chapter = 'Unknown'

        # Find the last occurrence of "Book" before the answer
        book_match = re.findall(r'(\w+)[\n\s]*chapter', text_before_answer)
        if book_match:
            book = book_match[-1]
        else:
            book = 'Unknown'

        # Find the last occurrence of "Verse" before the answer
        verse_match = re.findall(r'(\d+)[^\d\n]*(?:\n|$)', text_before_answer)
        if verse_match:
            verse = verse_match[-1]
        else:
            # If "Verse" information is not found before the answer, search after the answer
            text_after_answer = bible_text_lower[answer_position:]
            verse_match_after = re.findall(r'(\d+)[^\d\n]*(?:\n|$)', text_after_answer)
            if verse_match_after:
                verse = verse_match_after[0]
            else:
                verse = 'Unknown'

        # Count the number of newline characters in the text before the answer to estimate the line number
        line_number = text_before_answer.count('\n') + 1

        return {'book': book, 'chapter': chapter, 'verse': verse, 'line_number': line_number}
    else:
        return {'book': 'Unknown', 'chapter': 'Unknown', 'verse': 'Unknown', 'line_number': 'Unknown'}
def process_question(question, bible_text):
    result = question_answerer(question=question, context=bible_text)

    # Add context information
    context = get_context_information(question, bible_text, result)
    print("Context:", context)

    print("Question:", question)
    print("Answer:", result["answer"])

    # Include context information in the result
    result['context'] = context

    return result




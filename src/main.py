
from assistant import read_bible_text, process_question
from utils import listen_to_user_input, speak

def main():
    bible_text = read_bible_text()
    user_input = listen_to_user_input()
    spoken_response = process_question(user_input, bible_text)

    print(spoken_response)  # Print the response to the console
    speak(spoken_response)  # Speak the response

if __name__ == "__main__":
    main()
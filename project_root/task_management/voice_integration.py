```python
import speech_recognition as sr
from trello import TrelloClient

# Initialize Trello client
client = TrelloClient(
    api_key='your-key',
    api_secret='your-secret',
    token='your-oauth-token-key',
    token_secret='your-oauth-token-secret'
)

# Initialize speech recognizer
r = sr.Recognizer()

def create_task_from_voice():
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    try:
        # Use Google's speech recognition
        voice_text = r.recognize_google(audio)
        print("You said: " + voice_text)

        # Create a new Trello card with the voice text as the name
        board = client.get_board("board_id")
        list_obj = board.get_list("list_id")
        list_obj.add_card(name=voice_text)

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

def update_task_from_voice(task_id):
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    try:
        # Use Google's speech recognition
        voice_text = r.recognize_google(audio)
        print("You said: " + voice_text)

        # Update the Trello card with the voice text as the new name
        card = client.get_card(task_id)
        card.set_name(voice_text)

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

def check_task_status(task_id):
    # Get the Trello card
    card = client.get_card(task_id)

    # Print the card's name and status
    print("Task: " + card.name)
    print("Status: " + card.list.name)
```
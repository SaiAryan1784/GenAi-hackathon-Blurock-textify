from flask import Flask, render_template, request, jsonify
import os
import whisper
from groq import Groq
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

app = Flask(__name__)

# Load Whisper model


# Load the base Whisper model
model = whisper.load_model("base")

# Groq API client
client = Groq(api_key='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')

SCOPES = ['https://www.googleapis.com/auth/documents']

# Function to handle Google Docs Authentication
def authenticate_google_docs():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

# Serve the index.html page
@app.route('/')
def index():
    return render_template('index.html')

# API route to transcribe audio using Whisper
@app.route('/transcribe', methods=['POST'])
def transcribe():
    # Get audio file
    file = request.files['file']
    file_path = os.path.join("uploads", file.filename)
    file.save(file_path)

    # Transcribe the audio
    result = model.transcribe(file_path)
    transcription = result['text']

    return jsonify({'transcription': transcription})

# API route to modify text using Groq API
@app.route('/modify', methods=['POST'])
def modify_text():
    data = request.json
    user_input = data.get("modification_input")
    transcription = data.get("transcription")

    # Modify transcription using Groq API
    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                "role": "user",
                "content": "modify this content as " + user_input + transcription
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    modified_text = ""
    for chunk in completion:
        modified_text += chunk.choices[0].delta.content or ""

    return jsonify({'modified_text': modified_text})

# API route to save modified text to Google Docs
@app.route('/save_to_docs', methods=['POST'])
def save_to_google_docs():
    data = request.json
    modified_text = data.get("modified_text")

    # Authenticate and save to Google Docs
    creds = authenticate_google_docs()
    service = build('docs', 'v1', credentials=creds)

    doc = {'title': 'Transcription Document'}
    doc = service.documents().create(body=doc).execute()
    document_id = doc['documentId']

    requests = [
        {
            'insertText': {
                'location': {'index': 1},
                'text': modified_text
            }
        }
    ]
    service.documents().batchUpdate(documentId=document_id, body={'requests': requests}).execute()

    doc_url = f'https://docs.google.com/document/d/{document_id}'
    # Sample response after creating a document in your save_to_google_docs function
    return jsonify({'document_url': doc_url})


if __name__ == "__main__":
    # Ensure uploads directory exists
    if not os.path.exists('uploads'):
        os.makedirs('uploads')

    app.run(debug=True)

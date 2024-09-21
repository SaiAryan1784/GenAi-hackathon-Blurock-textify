import os
import whisper as wp
from google.oauth2.credentials import Credentials # used to handle google API credentials
from google_auth_oauthlib.flow import InstalledAppFlow # manages the oauth2.0 flow, allowing app to authenticate user
from google.auth.transport.requests import Request # #Refreshes expired credentials
from googleapiclient.discovery import build # used to build google docs api client to interact with google docs

# load the Whisper model 
model = wp.load_model("base") #pretrained neural network

audio_path = "audio.mp4"

result = model.transcribe(audio_path)

transcription = result['text']

# print("Transcription : ")
# print(result['text'])

SCOPES = ['https://www.googleapis.com/auth/documents']
creds = None

if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json',SCOPES)

if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_tokens:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

service = build ('docs', 'v1', credentials=creds)

doc = {
    'title' : 'Transcription Document'
}

doc = service.documents().create(body=doc).execute()
document_id = doc['documentId']

requests = [
    {
        'insertText' : {
            'location' : {
                'index': 1,
            },
            'text': transcription,
        }
    }
]

# Execute the request
service.documents().batchUpdate(documentId=document_id, body={'requests': requests}).execute()

print(f'Document created: https://docs.google.com/document/d/{document_id}')
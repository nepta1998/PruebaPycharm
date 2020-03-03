from __future__ import print_function
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/documents',
          'https://www.googleapis.com/auth/drive.file']


def create():
    creds = None

    title = 'Copy Title'
    body = {
        'title': title
    }
    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)

    service = build('docs', 'v1', credentials=creds)
    document = service.documents().create().execute()
    print(document.documentId)


def copy():
    creds = None
    documentID = '1qYzlpNUGT8kO_XnIggRLyVb0UtIL6IC850YGF2yUM8g'
    flow = InstalledAppFlow.from_client_secrets_file(
        'credenciales.json', SCOPES)
    creds = flow.run_local_server(port=3740)
    service = build('drive', 'v3', credentials=creds)
    document = service.files().copy(fileId=documentID).execute()
    document_id_copy = document.get('id')
    print(document_id_copy)
    print('https://docs.google.com/document/d/{}'.format(document_id_copy))

copy()

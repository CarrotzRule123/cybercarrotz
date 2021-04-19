import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPE = ['https://www.googleapis.com/auth/classroom.student-submissions.me.readonly']

class Classroom:
    def __init__(self):
        pass

    def main(self):
        creds = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPE)
                creds = flow.run_local_server(port=0)
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('classroom', 'v1', credentials=creds)
        print(service)
        #Add COURSE_ID
        course = service.courses().courseWork().list(courseId="COURSE_ID", pageSize=10).execute()
        result = course.get('courseWork', [])

        print(result)

        data = "Homework:"
        for course in result:
            data = data + "\n" +course['title']
        print(data)
        return data


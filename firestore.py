import firebase_admin
from firebase_admin import credentials, firestore

import loaddata

cred = credentials.Certificate("credentials.json")
app = firebase_admin.initialize_app(cred)

db = firestore.client(app)


def get_data():
    col = db.collection('wpm')
    docs = col.stream()

    data = []

    for doc in docs:
        data.append(doc.to_dict())

    data.sort(key=lambda x: x['wpm'], reverse=True)

    return data[:10]

def set_data(wpm):
    col = db.collection('wpm')
    username = loaddata.get_username()
    col.document().set({'username': username, 'wpm': wpm})


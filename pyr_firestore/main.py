import firebase_admin, requests, dateparser
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
  'projectId': 'wired-compass-230106',
})
db = firestore.client()

def pyr_firestore(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    request_json = request.get_json(silent=True)
    print(request_json)
    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type'
        }
        return ('', 204, headers)

    # Set CORS headers for the main request
    headers = {
        'Access-Control-Allow-Origin': '*'
    }
    print(db.collection('pyr').add(request_json))
    if len(request_json)>3:
        request_json['date']=str(dateparser.parse(request_json['date']))
        print(requests.post(url='----INTEGROMAT-HOOK-------', data=request_json))
    return ('Chal rha hai', 200, headers)
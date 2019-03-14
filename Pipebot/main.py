import requests
import json, smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

category={'':'Artist', '1':'Anchor/Emcee', '2':'Celebrity', '3':'Comedian', '4':'Dancer/Troupe', '5':'DJ', '6':'Instrumentalist', '7':'Live Band', '8':'Magician', '9':'Makeup Artist', '10':'Model', '11':'Photographer', '12':'Singer', '13':'Speaker', '14':'Variety Artist', '296':'International Pole Dancer', '297':'International Flute Mermaid', '298':'Aerial Champagne Chandelier Girl', '299':'International Hula-Hoop Dancer', '300':'International Symphony Band', '301':'International Singer', '302':'International Female DJ'}
category_key='61a501536a4065f5a970be5c6de536cf7ad14078'
event={'15':'Campus', '16':'Charity', '17':'Concert/Festival', '18':'Corporate', '19':'Exhibition', '20':'Fashion Show', '21':'Inauguration', '22':'Kids Party', '23':'Photo/Video Shoot', '24':'Private Party', '25':'Professional Hiring',  '26':'Religious', '27':'Restaurant', '28':'Wedding'}
event_key='755ded0be98b3ee5157cf117566f0443bd93cc63'
looking_key='ef1b3ca0c720a4c39ddf75adbc38ab4f8248597b'
location_key='361085abd375a7eb3964f068295f12fe17d9f280'
source_key='130678495c807efda3c98a312f3061403c1f1b7f'
source={'31':'GTQ', '32':'PYR', '33':'Intercom', '34':'Privy', '35':'Email', '36':'Phone', '37':'WhatsApp', '274':'Comment', '277':'Signup', '38':'FB', '39':'IG', '40':'Twitter', '42':'Landbot', '253':'Calendly', '294':'Email Campaign'}
owner=[{
        'name': 'xyz',
        'phone': '123',
        'photo': 'https://i.imgur.com/png',
        'job': 'Senior Strategist, Client Relations',
        'slack': '@',
        'email': '@starclinch.com',
        'id': '4262200'
    },
    {
        'name': 'xyz',
        'phone': '123',
        'photo': 'https://i.imgur.com/png',
        'job': 'Senior Strategist, Client Relations',
        'slack': '@',
        'email': '@starclinch.com',
        'id': '4262200'
    },
    {
        'name': 'xyz',
        'phone': '123',
        'photo': 'https://i.imgur.com/png',
        'job': 'Senior Strategist, Client Relations',
        'slack': '@',
        'email': '@starclinch.com',
        'id': '4262200'
    }
]

pipedrive_token='----PIPEDRIVE--TOKEN--------'
sender_email = "hello@starclinchmail.com"
dld=0

def pipebot(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    global dld
    request_json = (request.get_json(silent=True))['current']  
    print(request_json)
    if request_json['user_id']==4202436 and request_json['pipeline_id']==1 and dld!=request_json['id'] and request_json[location_key] is not None:
        rr=request_json['id']%len(owner)
        dld=request_json['id']
        print(rr)
        print(owner[rr])        
        url='https://starclinch1.typeform.com/to/oQJFoi?dealid='+str(request_json['id'])+'&name='+request_json['person_name']+'&category='+category[request_json[category_key]]+'&location='+request_json[location_key]+'&budget='+str(request_json['value'])+'&type='+event[request_json[event_key]]+'&size='+str(request_json['1f9805fdb8715d773f1fc9457545b49c5b05d058'])
        person=(requests.get('https://api.pipedrive.com/v1/persons/'+str(request_json['person_id'])+'?api_token='+pipedrive_token).json())['data']
        person_email=person['email'][0]['value']
        person_phone=person['phone'][0]['value']
        looking=request_json[looking_key] or ''
        slack_message='https://starclinch.pipedrive.com/deal/'+str(request_json['id'])+'\nFor '+owner[rr]['name']+':\n'+request_json['person_name']+' '+person_email+' '+person_phone+' '+category[request_json[category_key]]+' '+looking+' '+event[request_json[event_key]]+' '+source[request_json[source_key]]+' '+str(request_json['value'])+' '+request_json[location_key]
        valid=requests.get('https://bpi.briteverify.com/emails.json?address='+person_email+'&apikey=-----BRTIEVERIFY-KEY-----').json()['status']
        if valid!='invalid':
            valid='valid'
            shortLink='https'+(requests.get(url='http://tinyurl.com/api-create.php?url='+url)).text[4:]
            print(shortLink)
            subject='Hi '+request_json['person_name']+', Book '+category[request_json[category_key]]+' for your '+event[request_json[event_key]]+' Event'
            #mail(subject, bitly, rr, request_json['person_name'], category[request_json[category_key]]+' ', looking, event[request_json[event_key]], request_json['19c2c12d8fea52c4709cd4ce256b7852bc2b0259'], person_email)
            name=request_json['person_name']
            date=request_json['19c2c12d8fea52c4709cd4ce256b7852bc2b0259'] or ''
            if date!='':
                date=' on '+date
            receiver_email=person_email
            message = MIMEMultipart("alternative")
            message["From"] ='Team StarClinch <'+sender_email+'>'
            message['To']=receiver_email
            message["Subject"]=subject
            html = '''
            <p>Hello '''+name+'''! </p>

            Please click on '''+shortLink+''' to see price for '''+category[request_json[category_key]]+''' '''+looking+''' for your '''+event[request_json[event_key]]+''' event'''+date+'''.
            <p>Call us on <a href="tel:+91-'''+owner[rr]['phone']+'''">+91-'''+owner[rr]['phone']+'''</a> any time to discuss more :)</p>

            <p>Let's get talking!</p>

            Cheers!<br/>Team StarClinch<br/>
            <br>
            <div style='color:red; font-size:12px; margin-left: 40px'>This is a Bot-Generated Email. Please Do Not Reply!</div>
            '''
            message.attach( MIMEText(html, "html"))
            server=smtplib.SMTP('smtp.elasticemail.com', 2525)
            server.login('connect@starclinch.com', '----ELASTIC-KEY-------')
            server.sendmail(sender_email, [receiver_email], message.as_string())
            sms=request_json['person_name']+',click '+shortLink+' to see price for '+category[request_json[category_key]]+' for '+event[request_json[event_key]]+'. Call '+owner[rr]['name']+' on '+owner[rr]['phone']+' to discuss'
            print(requests.get('http://msg.mtalkz.com/V2/http-api.php?apikey=-----MTALKZ-KEY-----&senderid=STARCL&number='+person_phone+'&format=json&message='+sms))
        requests.put(url='https://api.pipedrive.com/v1/deals/'+str(request_json['id'])+'?api_token='+pipedrive_token,
                             data={'user_id':owner[rr]['id'], '5f6aa3b42903d9b9349342b304ade8f451b6af2c': 'Email '+valid, '18de79b1c9f6826d19f06ef63eff913d64d5afa7':request_json['id']})
        requests.post(url='---------SLACK-HOOK-----------',data=json.dumps({'text':slack_message}))
        requests.post(url='---------SLACK-HOOK-----------',data=json.dumps({'channel':owner[rr]['slack'],'text':slack_message}))
    return 'Chal rha hai'
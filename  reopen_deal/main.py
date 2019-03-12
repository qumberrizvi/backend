import requests

pipedrive_token='----pipedrive-TOKEN---------'

def reopen_deal(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    if request.args and 'deal' in request.args:
        requests.put(url='https://api.pipedrive.com/v1/deals/'+request.args['deal']+'?api_token='+pipedrive_token, data={'status':'open'})
        requests.post(url='https://api.pipedrive.com/v1/notes?api_token='+pipedrive_token, data={'deal_id':request.args['deal'], 'content':'Deal re-opened via email'})
        return '''<title>StarClinch</title>
          <meta name="viewport" content="width=device-width, initial-scale=1">
          <body>
            <div style="margin: 0; padding: 0;">
              <div style="margin: 0 auto; max-width: 600px; min-width: 320px; width: calc(28000% - 167400px); word-wrap: break-word; word-break: break-word;">
                <br><br><br /><br />
                <h1 style="margin-top: 0; margin-bottom: 20px; font-style: normal; font-weight: normal; color: #58595b; font-size: 22px; line-height: 31px; font-family: times,times new roman,serif; text-align: center;"><span style="color: #2fbd95;"><strong><br><br>Thank you for reopening your query with us<br><br>We will get in touch again by the earliest<br><br></strong></span></h1>
              </div>
              <div style="margin: 0 auto; max-width: 600px; min-width: 320px; width: calc(28000% - 167400px); word-wrap: break-word; word-break: break-word;">
                <div style="text-align: left; font-size: 16px; line-height: 19px; color: #99b0b8; font-family: Open Sans,sans-serif; float: left; max-width: 400px; min-width: 320px; width: calc(8000% - 47600px);">
                  <div>Regards,<br />StarClinch<br />connect@starclinch.com<br /></div>
                </div>
              </div>
            </div>
          </body>'''
    else:
        return f'Hello World!'

import json
import io
import cgi

from utils import cors_headers, process_data

def handler(event, context):
    """
    Process csv content o fjob details and return an invoice.

    - Dispatch headers with response to cater to preflight calls from browsers.
    """

    content = event.get('body')
    if not content:
        body = {"message": "Empty payload"}
        response = {"statusCode": 400, "body":json.dumps(body), "headers":cors_headers}
        return response
    
    #Parse multi-part/form into a dict for use
    byte_data = io.BytesIO(event['body'].encode('utf-8'))
    param_dict = cgi.parse_header(event['headers']['Content-Type'])[1]
    
    if 'boundary' in param_dict:
        param_dict['boundary'] = param_dict['boundary'].encode('utf-8')

    param_dict['CONTENT-LENGTH'] = len(event['body'])
    form_data = cgi.parse_multipart(byte_data, param_dict)

    raw_input_data = form_data['data']
    data = raw_input_data[0].decode('utf-8').split('\r')
    header = data[0].split(',')

    if len(header) != 5:
        body = {"message": f"We expect a 5 column csv file. {len(header)} uploaded."}
        response = {"statusCode": 400, "body":json.dumps(body, default=str), "headers": cors_headers}

    #extract rows of the file and calculate invoice figures.
    rows = [line.strip() for line in data[1:]] #drop the first row/head
    ok, response = process_data(rows)
    return response   

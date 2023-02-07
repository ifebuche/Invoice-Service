import json
from datetime import datetime as dt

cors_headers = {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Credentials': True,
      'Access-Control-Allow-Methods': 'OPTIONS,POST,GET',
      'Access-Control-Allow-Headers': '*'
    }

def process_data(rows):
    output = []
    total_cost = 0
    for row in rows:
        if row: #Cater to possible blank row at the end of csv
            result = {}
            row = row.split(',')
            result['Employee ID'] = row[0]
            try:
                unit_price = int(row[1])
            except ValueError as err:
                body = {"message": f"Invalid value in Unit Price - {err}"}
                response = {"statusCode": 400, "body":json.dumps(body, default=str), "headers": cors_headers}
                return False, response

            result['Unit Price'] = unit_price
            try:
                start = dt.strptime(f"{row[3]} : {row[4]}", "%Y-%m-%d : %H:%M")
                end = dt.strptime(f"{row[3]} : {row[5]}", "%Y-%m-%d : %H:%M")
            except ValueError as err:
                body = {"message": f"Bad time format detected. Expected year and time format: 'YYYY-MM-DD' and 'HH:MM' - {err}"}
                response = {"statusCode": 400, "body":json.dumps(body, default=str), "headers": cors_headers}
                return False, response

            total_hours = (end - start).total_seconds()/(60*60)
            result["Number of Hours"] = total_hours
            cost = round((total_hours * unit_price), 2)
            result['Cost'] = cost
            total_cost += cost
            output.append(result)
    body = {"message": "invoice_details", "data":output, "total_cost": total_cost}
    response = {"statusCode": 200, "body":json.dumps(body, default=str), "headers":cors_headers}
    return True, response
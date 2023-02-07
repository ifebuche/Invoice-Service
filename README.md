# distinctai-invoice

#This is a RESTful serverless microservice app built on AWS Lambda and API Gateway, and mangaed + deployed with [Serverless Framework](https://www.serverless.com/). Standard HTTP status codes are in use. This is meant to support agile development by allowing micro ownership of the service.
The service intentionally build with 100% python builtin modules to ensure zero depency issues.

**Deploy**
- To deploy and run this app on AWS, [setup](https://www.serverless.com/framework/docs/getting-started) Serverless Framework and add your AWS keys
- Clone this repo
- Run _sls deploy_ to deploy on AWS and get the associated endpoint url.
- For test purposes, an active endpoint is at: https://cz7pgk7yz9.execute-api.eu-west-1.amazonaws.com/prod/invoice

**Calling the endpoint + Testing**
- This is a POST endpoint accepting form-data bearing a file input with a single key *data* which is a csv file.
- See sample input data as *sample_input*. See also two sample bad input data for testing

**Response**
- The endpoint responds with a *message* key specifying the result of the call and an extra *data* key if successful.
- CORS is enabled for prelight calls.

**Error Hanlding**
- The service will detect bad calls and malformed csv files that thus:
  - Missing payload
  - CSV data Lacking expected the total count of columns: 5
  - Missing data in unit price
  - Wrong data in date and time columns
  
*Sample Output with good input data*
![image](https://user-images.githubusercontent.com/2832737/215881932-bff8b434-3d76-44fa-b9eb-d90d51ee849c.png)

*Sample Call Output with bad input data*
![image](https://user-images.githubusercontent.com/2832737/215880636-6b3a936a-4153-4f3f-8233-8a71f2e2b097.png)

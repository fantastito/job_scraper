from bs4 import BeautifulSoup
import requests
import boto3
from botocore.exceptions import ClientError

#Send email

def send_email(body):
    client = boto3.client("ses")
    message = {"Subject": {"Data": "Today's freshly scraped jobs"}, "Body": {"Html": {"Data": body}}}
    try:    
        response = client.send_email(
            Source='simon.budden@gmail.com',
            Destination={
                'ToAddresses': [
                    'simon.budden@gmail.com',
                ],
            },
            Message = message
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])


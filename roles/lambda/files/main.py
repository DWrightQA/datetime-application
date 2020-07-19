import boto3
import datetime
import uuid
import json

def handler(event, context):

    # create fields for dynamodb table
    timestamp = str(datetime.datetime.now().replace(microsecond=0).isoformat())
    id = str(uuid.uuid4()) 

    # Crate dynamodb resource and put item to table
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('vf-datetime')
    table.put_item(
       Item={
            'id': id,
            'timestamp': timestamp,
        }
    )

    # return 201 response code + success message
    return {
        'statusCode': 201,
        'body': json.dumps('created record')
    }

#API Endpoint - https://71a2rk0wgf.execute-api.us-east-1.amazonaws.com/default/ListPlayers

import json
import datetime 
import boto3
import decimal
from boto3.dynamodb.conditions import Key, Attr


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('A3Players')
    
    params = event['queryStringParameters']
    
    return {
        'statusCode': 200,
        'body': json.dumps(table.scan())
    }
    
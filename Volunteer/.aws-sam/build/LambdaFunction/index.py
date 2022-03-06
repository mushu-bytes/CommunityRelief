# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import boto3
import json
import uuid


# name = event['name']
# phone = event['phone']
# request = event['request']
# print(f" ****** event: ")
# print(event)
# print(f" ****** type of event {type(event)}")
# print(f' ****** event body {event["body"]}')
# print(f' ****** type of event body {type(event["body"])}')

# salutation = f'Hello {myEvent["name"]}'
# print(f" ******* type of salutation: {type(salutation)}")
# print(f" ******* salutation: {salutation}")

def lambda_handler(event, context):

    try:
        dynamodb_client = boto3.client('dynamodb')
        sns_client = boto3.client('sns', region_name='us-west-2')


        body = json.loads(event["body"])
        print(body)
        print("new")
        print("tesssts")
        dynamodb_client.put_item(TableName='volunteer',
                                 Item={'id': {'S': str(uuid.uuid4())}, 'Name': {'S': body["name"]}, 'phone': {'S': body["phone"]}})

        subscription = sns_client.subscribe(
            TopicArn='arn:aws:sns:us-west-2:453734077066:hack',
            Protocol='sms',
            Endpoint="+1" + body["phone"],
            ReturnSubscriptionArn=True)['SubscriptionArn']
    except Exception as e:
        print(e)
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS, POST',
                'Access-Control-Allow-Credentials': 'true'
            },
            "body": "damon"
        }

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Methods': 'OPTIONS, POST',
            'Access-Control-Allow-Credentials': 'true'
        },
        "body": "damon"
    }

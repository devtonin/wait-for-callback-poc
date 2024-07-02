import json
import boto3


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')

    table_name = 'Status'
    table = dynamodb.Table(table_name)

    record = event['Records'][0]
    data = json.loads(record['body'])

    task_token = data['myTaskToken']
    client_id = data['clientId']
    contract_id = data['contractId']

    try:
        table.update_item(
            Key={
                'statusId': client_id
            },
            UpdateExpression="set sf_token = :r, contractId = :c",
            ExpressionAttributeValues={
                ':r': task_token,
                ':c': contract_id
            },
            ReturnValues="UPDATED_NEW"
        )
    except Exception as e:
        print(e)
        raise e

    return {
        'statusCode': 200,
        'body': json.dumps('Processed SQS messages')
    }

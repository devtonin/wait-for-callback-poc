import json
import boto3

def lambda_handler(event, context):
    client = boto3.client('stepfunctions')
    token = event['sf_token']

    params = {
        'output': '"Contract fixed"',
        'taskToken': token
    }

    try:
        client.send_task_success(output=params['output'], taskToken=token)
        response = {
            'statusCode': 200,
            'body': json.dumps({'message': 'Fluxo despausado com sucesso'})
        }
    except Exception as e:
        response = {
            'statusCode': 500,
            'body': json.dumps({'message': f'Erro ao despausar o fluxo: {str(e)}'})
        }

    return response

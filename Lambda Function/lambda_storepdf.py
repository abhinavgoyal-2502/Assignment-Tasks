import boto3
import base64
import json
import os


s3_client = boto3.client('s3')

def lambda_handler(event, context):
    try:
        
        bucket_name = os.environ.get('S3_BUCKET_NAME')  
        file_name = event.get('file_name')
        file_content_base64 = event.get('file_content')  

        if not bucket_name or not file_name or not file_content_base64:
            return {
                'statusCode': 400,
                'body': json.dumps('Error: Missing bucket_name, file_name, or file_content')
            }

        
        file_content = base64.b64decode(file_content_base64)

        
        s3_client.put_object(Bucket=bucket_name, Key=file_name, Body=file_content)

        return {
            'statusCode': 200,
            'body': json.dumps(f'File {file_name} successfully uploaded to bucket {bucket_name}')
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }

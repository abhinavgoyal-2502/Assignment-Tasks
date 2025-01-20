import json

def lambda_handler(event, context):
    
    try:
        num1 = event.get('num1')
        num2 = event.get('num2')

        if num1 is None or num2 is None:
            return {
                'statusCode': 400,
                'body': json.dumps('Error: Missing num1 or num2 in the input')
            }

        
        num1 = float(num1)
        num2 = float(num2)

        
        result = num1 + num2

        return {
            'statusCode': 200,
            'body': json.dumps({'result': result})
        }

    except ValueError as e:
        return {
            'statusCode': 400,
            'body': json.dumps(f'Error: Invalid input. {str(e)}')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }

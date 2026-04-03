import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('users')

def lambda_handler(event, context):
    try:
        body = json.loads(event.get('body', '{}'))
        action = body.get('action')

        if action == "create":
            item = {
                "id": body["id"],
                "name": body["name"]
            }
            table.put_item(Item=item)

            return {
                "statusCode": 200,
                "body": json.dumps({"message": "Item created"})
            }

        elif action == "read":
            response = table.get_item(
                Key={"id": body["id"]}
            )

            return {
                "statusCode": 200,
                "body": json.dumps(response.get("Item", {}))
            }

        else:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Invalid action"})
            }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
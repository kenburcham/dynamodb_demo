import boto3
import os
os.environ["TZ"] = "UTC"

dynamodb_client = boto3.client('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")

existing_tables = dynamodb_client.list_tables()['TableNames']

print(existing_tables);

try:
	response = dynamodb_client.describe_table(TableName='Movies')
	print(response);
except dynamodb_client.exceptions.ResourceNotFoundException:
	print('Not found.')
	pass
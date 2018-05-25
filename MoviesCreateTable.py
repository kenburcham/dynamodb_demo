from __future__ import print_function # Python 2/3 compatibility
import boto3

dynamodb = boto3.client('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")

try:
	table = dynamodb.create_table(
		TableName='Movies',
		KeySchema=[
			{
				'AttributeName': 'year',
				'KeyType': 'HASH'  #Partition key
			},
			{
				'AttributeName': 'title',
				'KeyType': 'RANGE'  #Sort key
			}
		],
		AttributeDefinitions=[
			{
				'AttributeName': 'year',
				'AttributeType': 'N'
			},
			{
				'AttributeName': 'title',
				'AttributeType': 'S'
			},

		],
		ProvisionedThroughput={
			'ReadCapacityUnits': 10,
			'WriteCapacityUnits': 10
		}
	)

	print("Table status:", table.table_status)

except dynamodb.exceptions.ResourceInUseException:
    # do something here as you require
	print('Already exists.');
	pass


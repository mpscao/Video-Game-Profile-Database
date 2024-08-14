import boto3
import pandas as pd
import sys

df = pd.read_csv('profiles.csv')
dynamodb = boto3.client('dynamodb', region_name = 'us-west-1')

table_name = "video_game_profiles"
table_schema = [{'AttributeName': 'username', 'KeyType': 'HASH'}, {'AttributeName': 'email', 'KeyType': 'RANGE'}]
attribute_definitions = [{'AttributeName': 'username', 'AttributeType': 'S'}, {'AttributeName': 'email', 'AttributeType': 'S'}]

dynamodb.create_table(TableName=table_name, KeySchema=table_schema, AttributeDefinitions=attribute_definitions, ProvisionedThroughput={'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5})

# table isn't created immediately, takes a slight amount of time because above line is simply a request to make a table, thus need a "wait for table to be created" function
waiter = dynamodb.get_waiter('table_exists')
waiter.wait(TableName=table_name)

for _, row in df.iterrows():
    item = row.to_dict()
    # Convert numeric values to int
    for key, value in item.items():
        if isinstance(value, float):
            item[key] = int(value)
    # Wrap the item in a dictionary
    item_dict = {'username': {'S': item['username']}, 'email': {'S': item['email']}, 
	'games_played': {'N': str(item['games_played'])},
	'wins': {'N': str(item['wins'])},
	'losses': {'N': str(item['losses'])},
	'kills': {'N': str(item['kills'])},
	'number_friends': {'N': str(item['number_friends'])},
	'weapon': {'S': item['weapon']},
	'money_spent': {'N': str(item['money_spent'])},
	'character': {'S': item['character']}
	}
    # Insert into DynamoDB
    dynamodb.put_item(TableName=table_name, Item=item_dict)

print("Table created and items inserted successfully!")

import pandas as pd
import sys
from pymongo import MongoClient

def load(profile_path):
	profiles = pd.read_csv(profile_path)

	client = MongoClient(host = '127.0.0.1', port = 27017)
	db = client['351Project']
	
	db['profiles'].insert_many(profiles.to_dict(orient = 'records'))


profile_filepath = sys.argv[1]
load(profile_filepath)

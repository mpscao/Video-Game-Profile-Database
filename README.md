# Video Game Profiles Database
The following application should allow users to upload video game profiles currently in CSV format into MongoDB and DynamoDB. 
After that, users should be able to View, Search, and Change(with sub-functions Insert, Delete and Modify) to use the database 
of Video Game profiles.

# How to run code.
1.  In Terminal, upload all of the profiles in profiles.csv into both MongoDB and DynamoDB using loadMongo.py and loadDDB.py, respectively.
    The csv and two Python scripts should be found in the "CSV/Python Scripts to Load Data into Databases" folder. The command in the terminal
    used for MongoDB will be “python3 loadMongo.py profiles.csv”, while for DynamoDB it will be “python3 loadDDB.py”. 

2. Open Jupyter Notebook through Terminal so you can access the databases of profiles that you have uploaded. Then using "VideoGameProfilesDB.ipynb"
   in Jupyter Notebook, you should be able to run all of the cells. The last cell with the "selection function" is where you will be able to
   choose which database you want to use and which functions you want to use. 

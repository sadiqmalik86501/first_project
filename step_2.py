import json 

def cleaned_data(data):
    data["users"]=[user for user in data["users"] if user["name"].strip()]
    
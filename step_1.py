import json
def load_data(filename):
    with open(filename,"r") as f:
        data=json.load(f)
        return data
data=load_data("data.json")
print(data)

def display_user(data):
    print("/n User Informatation/n")
    for user in data["users"]:
           print(
            f"Id.{user["id"]}:{user["name"]}: as with friends{user["friends"]} and like pages{user["liked_pages"]}"
            )
    print("\n Page Informatation \n")
    for page in data["pages"]:
        print(f"Id,{page["id"]}:{page["name"]}")

display_user(data)
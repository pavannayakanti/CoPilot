users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"}
]

usernames = [user['name'] for user in users]

def main():
#print each username
    for username in usernames:
        print(username)

# main funciton to run program 
if __name__ == "__main__":
    main()
    
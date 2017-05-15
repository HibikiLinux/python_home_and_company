import getpass
_username = 'yan'
_password = 'yan'
username = input("username:")
password = input("password:")
print(username,password)

if _username == username and _password == password:
    print("welcome user {name} login...".format(name=username))
else:
    print("invalid useranme or password")
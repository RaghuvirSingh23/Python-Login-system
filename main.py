import csv
credentials = {}
with open("newusers.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    next(csv_reader)
    for row in csv_reader:
        credentials[row[0]] = row[1]
def login():
    print("So you chose to login")
    def userlogin():
        username = input("Kindly enter the username: ")
        if username in credentials.keys():
            password = input("Kindly enter the password: ")
            if credentials.get(username) == password:
                print("Login Successful!")
                resp3 = input("Do you want to login(l)/signup(s) again?")
                if resp3 == "l":
                    login()
                elif resp3 == "s":
                    signup()
                else:
                    print("OK bye")
            else:
                print("wrong credentials, try again!")
                userlogin()
        else:
            print("No username found!, try again")
    userlogin()
def signup():
    print("So you chose to signup")
    def usersignup():
        username = input("Kindly enter your username: ")
        if username in credentials.keys():
            print("The username is already taken, try again: ")
            usersignup()
        else:
            password = input("Kindly enter a strong password: ")
            credentials[username] = password
            print("Signup successful!")
            resp2 = input("Do you want to login again? (y/n)")
            if resp2 == "y":
                login()
            else:
                print("OK bye")

    usersignup()


def page1():
    print("Would you like to Login(l) or SignUP(S)?")
    resp = input("Response: ")
    if resp == "l":
        login()
    elif resp == "s":
        signup()
    else:
        print("Invalid response")
        page1()
print("Welcome to the login portal!")
page1()
with open("users.csv", 'r') as infile, open("newusers.csv", 'w', newline= "") as outfile:
    r = csv.DictReader(infile)
    w = csv.DictWriter(outfile, r.fieldnames)
    w.writeheader()

    temp_dict = {row['Username']: row['Password'] for row in r}

    for k in credentials.keys():
        if k not in temp_dict:
            temp_dict[k] = credentials[k]

    for value in temp_dict:
        w.writerow({'Username': value, 'Password': temp_dict[value]})


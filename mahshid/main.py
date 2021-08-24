# This is a sample Python script.
import json

import redis

r = redis.Redis(host="localhost", port=6379, db=0)


# def print_hi(name):
# Use a breakpoint in the code line below to debug your script.
#  print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
def register():
    lcontact = []

    fname = input("Plz enter your name : ")
    lname = input("Plz enter your family : ")
    tel = int(input("Plz enter your phone : "))
    email = input("Plz enter your Email : ")
    passwd = input("Plz enter your password : ")

    info_user = {}
    info_user["fname"] = fname
    info_user["lname"] = lname
    info_user["tel"] = tel
    info_user["email"] = email
    info_user["passwd"] = passwd
    info_user["lcontact"] = lcontact
    vlu = json.dumps(info_user)
    r.set(tel, vlu)
    r.save()
    print("Tanks ")
    return


def add_contact(tel):
    r.keys()
    k = r.get(tel)
    value = json.loads(k)

    cname = input("Enter contact name  : ")
    ctel = int(input("Enter contact phone : "))
    cusername = input("Enter contact us_name : ")

    value["lcontact"].append({"cname": cname, "ctel": ctel, "cuser_name": cusername, "user_tel": tel, })
    vlue = json.dumps(value)

    r.set(tel, vlue)
    r.save()
    return


def send_msg(tel):
    txt = []
    print("🔻 list of cantact 🔻")
    key = r.keys(tel)
    for k in key:
        value = r.get(k)
        contacts = json.loads(value)["lcontact"]
        for c in contacts:
            print(c["cname"], ":", c["ctel"])
    print("------------------------------")
    number = int(input("enter phone number :"))
    print("enter text 🔻")
    while ("true"):

        text = input()
        if text == ".":
            break
        txt.append(text)
    print(txt)


def menu(phone):
    while ("true"):

        print("1. Add contat   ")
        print("2. Send message ")
        print("3. Read message ")
        print("4. Exit ")
        tel = phone
        n = int(input(" chosse of menu :"))
        if n == 1:
            add_contact(tel)
        elif n == 2:
            send_msg(tel)
        # elif n == 3 :
        #   read_msg()
        else:
            return


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#  print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/


while "true":
    print("1 ✈ Log In")
    print("2 ✈ Register")

    n = int(input("Wellcame  Please choose of menu : "))
    if n == 1:
        phone = int(input("Please enter phone : "))
        passwd = input("Please enter password :")
        key = r.keys(phone)

        for k in key:
            value = r.get(k)
            phne = json.loads(value)["tel"]
            if phne == phone:

                paswd = json.loads(value)["passwd"]
                if paswd == passwd:
                    print("Welcame")
                    menu(phone)
                else:
                    print("Sorry!! the username or password is incorrect ")
            else:
                print(" 😥 No username! Please register")
    if n == 2:
        register()



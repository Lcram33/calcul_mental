import random
import json
from timeit import default_timer as timer
from os import listdir, makedirs
from os.path import isfile, join, exists

user_data = {
    "scores": [],
    "faults_count": 0
}

def send_r():
    print("Entendu ! Répondez le plus vite possible sans vous tromper.\nTapez exit pour quitter.\n")

def cut_float(number: float, n: int):
    integer,decimal = str(number).split(".")
    cut_number = integer+"."
    for i in range(n):
        cut_number+="0" if i > len(decimal) else decimal[i]
    return float(cut_number)

def manage_time(time: float):
    formated = round(time, 1)
    global user_data
    user_data["scores"].append(formated)
    return str(formated)

def get_average_time():
    global user_data
    my_sum = 0
    for i in user_data["scores"]:
        my_sum+=i
    if len(user_data["scores"]) != 0:
        return str(round(my_sum/len(user_data["scores"]), 2))+"s"
    else:
        return "Pas de données."

def get_percent():
    global user_data
    if user_data["faults_count"] != 0:
        return str(round(100-100*user_data["faults_count"]/len(user_data["scores"]), 2))+"%"
    else:
        return "Pas de données."

user = input("Bonjour ! Veuillez entrer votre nom/pseudo : ")
path = "./users/"
if not exists(path):
    makedirs(path)
user_file = [f for f in listdir(path) if isfile(join(path, f)) and f == "{}.json".format(str(user))]
if len(user_file) > 0:
    with open("./users/{}.json".format(user), "r") as f:
        user_data = json.load(f)
    print("Bienvenue {} ! Vos données ont été chargées.".format(user))
else:
    print("Bienvenue {} !".format(user))

while 1:
    choice = input("Choix de l'opération (+|-|/|*|^|mod|exit|stats) : ")
    if choice == "+":
        send_r()
        while 1:
            n1 = random.randint(10, 1000)
            n2 = random.randint(10, 1000)
            rsum = n1 + n2
            start = timer()
            request = input("{}+{} ? ".format(str(n1), str(n2)))
            try:
                request = int(request)
            except Exception:
                break
            end = timer()
            timespent = manage_time(end - start)
            if request == rsum:
                print("Correct ! Calculé en {}s.\n".format(timespent))
            else:
                print("Incorrect ! Le résultat était {}. Calculé en {}s.\n".format(str(rsum), timespent))
                user_data["faults_count"]+=1
    elif choice == "-":
        send_r()
        while 1:
            n1 = random.randint(10, 1000)
            n2 = random.randint(10, 1000)
            rsubs = n1 - n2
            start = timer()
            request = input("{}-{} ? ".format(str(n1), str(n2)))
            end = timer()
            try:
                request = int(request)
            except Exception:
                break
            timespent = manage_time(end - start)
            if request == rsubs:
                print("Correct ! Calculé en {}s.\n".format(timespent))
            else:
                print("Incorrect ! Le résultat était {}. Calculé en {}s.\n".format(str(rsubs), timespent))
                user_data["faults_count"]+=1
    elif choice == "*":
        send_r()
        while 1:
            n1 = random.randint(10, 100)
            n2 = random.randint(10, 100)
            rmult = n1 * n2
            start = timer()
            request = input("{}*{} ? ".format(str(n1), str(n2)))
            end = timer()
            try:
                request = int(request)
            except Exception:
                break
            timespent = manage_time(end - start)
            if request == rmult:
                print("Correct ! Calculé en {}s.\n".format(timespent))
            else:
                print("Incorrect ! Le résultat était {}. Calculé en {}s.\n".format(str(rmult), timespent))
                user_data["faults_count"]+=1
    elif choice == "/":
        n_digits = int(input("Arrondir à : "))
        send_r()
        while 1:
            n1 = random.randint(1, 100)
            n2 = random.randint(1, 100)
            rdiv = cut_float(n1 / n2, n_digits)
            start = timer()
            request = input("{}/{} ? ".format(str(n1), str(n2)))
            end = timer()
            try:
                request = float(request)
            except Exception:
                break
            timespent = manage_time(end - start)
            if request == rdiv:
                print("Correct ! Calculé en {}s.\n".format(timespent))
            else:
                print("Incorrect ! Le résultat était {}. Calculé en {}s.\n".format(str(rdiv), timespent))
                user_data["faults_count"]+=1
    elif choice == "mod":
        send_r()
        while 1:
            n1 = random.randint(1, 1000)
            n2 = random.randint(1, 100)
            biggest = n1 if n1 > n2 else n2
            lowest = n1 if biggest == n2 else n2
            mod = biggest%lowest
            start = timer()
            request = input("{}mod{} ? ".format(str(biggest), str(lowest)))
            end = timer()
            try:
                request = int(request)
            except Exception:
                break
            timespent = manage_time(end - start)
            if request == mod:
                print("Correct ! Calculé en {}s.\n".format(timespent))
            else:
                print("Incorrect ! Le résultat était {}. Calculé en {}s.\n".format(str(mod), timespent))
                user_data["faults_count"]+=1
    elif choice == "^":
        send_r()
        while 1:
            n1 = random.randint(2, 15)
            n2 = random.randint(2, 5)
            rpow = n1**n2
            start = timer()
            request = input("{}^{} ? ".format(str(n1), str(n2)))
            end = timer()
            try:
                request = int(request)
            except Exception:
                break
            timespent = manage_time(end - start)
            if request == rpow:
                print("Correct ! Calculé en {}s.\n".format(timespent))
            else:
                print("Incorrect ! Le résultat était {}. Calculé en {}s.\n".format(str(rpow), timespent))
                user_data["faults_count"]+=1
    elif choice == "stats":
        print("Moyenne du temps de réponse : {}\nPourcentage de réussite : {}".format(get_average_time(), get_percent()))
    else:
        with open("./users/{}.json".format(user), "w+") as f:
            json.dump(user_data, f)
        print("Données enregistrées, à bientôt !")
        break
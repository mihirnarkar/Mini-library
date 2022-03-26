# Lets create an exercise app using python and mongoDB connection:-
import time
import pymongo

print("Hello welcome to out EXERCISE app, lets create your routine")
time.sleep(1)

def feed_data(collection,day,daily_food,daily_exercise,daily_water):
    data = [
        {
            "_id" : day,
            "Day" : day,
            "Food" : daily_food,
            "Exercise" : daily_exercise,
            "Water intake" : daily_water
        }
    ]
    print(f"Saving data for day-{day}...")
    time.sleep(2)
    collection.insert_many(data)
    print("All done")

def addData_5(day):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client['project']
    collection = db['5-Day']
    daily_food = input("Enter food to eat: ")
    daily_exercise = input("Enter exercise i.e shoulder/arms/legs/abbs: ")
    daily_water = input("Daily water glass: ")
    feed_data(collection,day,daily_food,daily_exercise,daily_water)

def addData_10(day):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client['project']
    collection = db['10-Day']
    daily_food = input("Enter food to eat: ")
    daily_exercise = input("Enter exercise i.e shoulder/arms/legs/abbs: ")
    daily_water = input("Daily water glass: ")
    feed_data(collection,day,daily_food,daily_exercise,daily_water)

def addData_15(day):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client['project']
    collection = db['15-Day']
    daily_food = input("Enter food to eat: ")
    daily_exercise = input("Enter exercise i.e shoulder/arms/legs/abbs: ")
    daily_water = input("Daily water glass: ")
    feed_data(collection,day,daily_food,daily_exercise,daily_water)

def addRoutine():
    print("Select Your routine for 5-Day, 10-Day, 15-Day")
    print('''
    Note: 
    5-Day --> press 5
    10-Day --> press 10
    15-Day --> press 15
    ''')
    choice = int(input("Enter choice: "))
    if choice == 5:
        print("Creating your 5-Day routine")
        print("")
        print("")
        for i in range(1,6):
            print(f"Lets add for Day-{i}:- ")
            addData_5(i)
            print("")
            print("")
        
    if choice == 10:
        print("Creating your 10-Day routine")
        print("")
        print("")
        for i in range(1,11):
            print(f"Lets add for Day-{i}:- ")
            addData_10(i)
            print("")
            print("")

    if choice == 15:
        print("Creating your 15-Day routine")
        print("")
        print("")
        for i in range(1,16):
            print(f"Lets add for Day-{i}:- ")
            addData_15(i)
            print("")
            print("")


def displayRoutine():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["project"]
    userChoice = input("Enter your routine schedule:- ")

    try:
        val_dict = db.validate_collection(userChoice)
        print("Checking for routine days...")
        time.sleep(2)
        print(f"Showing {userChoice} routine")
        collection = db[userChoice]
        for doc in collection.find():
            print(f"Day: {doc['Day']}")
            print(f"Food: {doc['Food']}")
            print(f"Exercise: {doc['Exercise']}")
            print(f"Water intake: {doc['Water intake']}")
            print()
    except Exception as e:
        print("Checking for collection...")
        time.sleep(2)
        print("Collection not found...Create a collection!")



def deleteRoutine():
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client['project']
    enter_routine = input("Enter your routine: ")
    collection = db[enter_routine]
    enter_day = int(input("Enter your day to delete: "))
    rec = {"Day":enter_day}
    a = collection.delete_one(rec)
    count = a.deleted_count
    if count == 1:
        print("Deleting...")
        time.sleep(2)
        print(f"Day - {enter_day} deleted successfull")
    elif count == 0:
        print("Wait some error occured...trying to resolve!")
        time.sleep(2)
        print("Error while deleting data")

while True:
    user = input("Press 'enter' to start the schedule and 'exit' to end the schedule: ")
    if user == "":
        print('''Select your choice:
        1. Add routine
        2. Display routine
        3. Delete your routine
        4. Exit''')
        choice = input("Enter choice: ")
        if choice == '1':
            addRoutine()

        if choice == '2':
            displayRoutine()

        if choice == '3':
            deleteRoutine()

        if choice == '4':
            print("Leaving you...")
            time.sleep(2)
            print('Bye')
            exit()

    elif user == 'exit':
        print("Leaving you hold back...")
        time.sleep(2)
        print("Visit again")
        break
    else:
        print("Please press enter to start the schedule!")


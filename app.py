#importing pandas as pd 

import pandas as pd ,json


#creating a simple  data set of items
#item ID, item name, quantity, price, and category. 

iteams = [
    {"id": "1", "name": "phones" ,"quantity": 12 , "price": 40000 , "category": "electronic"},
    {"id": "2", "name": "bat" ,"quantity": 5 , "price": 1500 , "category": "wood"},
    {"id": "3", "name": "chair" ,"quantity": 2 , "price": 200 , "category": "wood"},
    {"id": "4", "name": "laptop" ,"quantity": 12 , "price": 70000 , "category": "electronic"},
    {"id": "5", "name": "smart_watch" ,"quantity": 15 , "price": 3000 , "category": "electronic"},
    {"id": "6", "name": "register" ,"quantity": 33 , "price": 600 , "category": "paper"},
    {"id": "7", "name": "fans" ,"quantity": 20 , "price": 7000 , "category": "electronic and steel"},
    {"id": "8", "name": "toys" ,"quantity": 25 , "price": 300 , "category": "plastic"}

]



#df = pd.DataFrame(iteams)

# Explore the data and  different columns  -----  using pandas
  #print(df[["name", "price"]])


# creating the function for adding iteam in iteams ------------------with try and except ------data handling


def added_data():
    try:
        id = input("enter the id of iteam: ")
        name = input("enter the name of iteams: ")
        quantity = int(input("enter the quantity of iteam: "))
        price = int(input("enter the price of iteam: "))
        category = input("enter the category of iteam: ")
        if quantity < 0:
            print("please insert valid quantity")
            return
        if price < 0:
            print("price can not be in negative")
            return
        iteam = {"id": id, "name": name, "quantity": quantity, "price": price, "category": category}
        iteams.append(iteam)
        print("-----------data added------------")
    except :
        print("Invalid input. Please try again.")

#creating function which wil be update data from data -----------------

def updating_data():
    
    try: 
        
    
        id = int(input("enter the id of iteam which you want to update  = "))
        if id.is_integer :
          for  i in iteams:
           if i["id"] in id :
              i["id"] = input("enter the id of iteam: ")
              i["name"] = input("enter the name of iteams: ")
              i["quantity"] = int(input("enter the quantity of iteam: "))
              i["price"] = int(input("enter the price of iteam: "))
              i["category"] = input("enter the category of iteam: ")
             
        print("------------------iteam updated----------------")
        
    except :
        print("Invaild id. Please try again.")
        
#-------------------------creating a function for removing iteam from the iteams .......


def removing_data():
    try:
        n = int(input("enter the id of iteam = "))
        if n.is_integer:
           for i in iteams:
            if i["id"] == n:
                 iteams.remove(i)
                 print("----------------------iteam has been removed--------------")
    except :
        print("Invaild id . Please try again.")   
                                           
#-------------------creating a fuction in thsi function if user want to search any iteam so he can ----and data will be show of sepcific serch---by user

def serch_data():
    try :
        id = int(input("enter the id of iteam that you want to search ! = "))
        if id.is_integer :
             for i in iteams :
                if i["id"] == str(id):
                    print(i)
    except :
        print("invaild id _____try again")            
#-------------------file handling -#def savd_data(inventory.txt): -------------

def save_iteams_to_json(iteams, filename):
    """
    Save the iteams to a JSON file.

    :param iteams: List of dictionaries representing the iteams.
    :param filename: Name of the file to save the iteams.
    """
    with open(filename, 'w') as file:
        json.dump(iteams, file, indent=4)

#----------------------------loadibg iteams from jason-----------------

def load_iteams_from_jason(filename):
    with open(filename, 'r') as file:
        return json.load(file)
    
#----------------------------ASKING USER WHAT HE WABT TO DO -----------------
def menu():
    print("""
      press 1. for added iteams 
      press 2. for removing items
      press 3. for updating items
      press 4. for searching items 
      press 5. for showing data
      press 6. for sava iteams in jason
      press 7.  from  loading data from jason
      press 8. for Exit    
      """)
    
#--------------using while because we dont know how many times user want to do this task .....when user enter 5 so i will be exist fro the program------------


while True:
    menu()
    user_input  = int(input("ENTER THE NUMBER HERE : "))

    if user_input == 1:
        added_data()
    elif user_input == 2:
        removing_data()
    elif user_input == 3:
        updating_data()
    elif user_input == 4:
        serch_data()
    elif user_input == 5:
        print(pd.DataFrame(iteams))
    elif user_input == 6:
         save_iteams_to_json(iteams, 'iteams.json')
    elif user_input == 7:
        loaded_inventray = load_iteams_from_jason("iteams.json")
        print(loaded_inventray) 

    elif user_input == 8:
        break
    else:
        print("Invalid Number")
        

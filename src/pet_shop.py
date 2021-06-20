# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(storename):
    return storename['name']

def get_total_cash(total_cash):
    return total_cash["admin"]["total_cash"]
   

def add_or_remove_cash(pet_shop, cash_amount):
    pet_shop["admin"]["total_cash"] += cash_amount
    
    # Other way:
    # amount = pet_shop["admin"]["total_cash"]
    # add_amount = amount + cash_amount
    # pet_shop["admin"]["total_cash"]=add_amount


def get_pets_sold(pets_total_sold):
    return pets_total_sold["admin"]["pets_sold"]

def increase_pets_sold(pets_amount, sold):
    pets_amount["admin"]["pets_sold"] += sold

    # Other way:
    # amount = pets_amount["admin"]["pets_sold"]
    # add_pets = amount + sold
    # pets_amount["admin"]["pets_sold"]=add_pets


def get_stock_count(dict_pets):
    return len(dict_pets["pets"])


    # Other way:
    # count = 0
    # pet_number = dict_pets["pets"]
    # for pet in enumerate(pet_number):
    #     count += 1
    # return count

def get_pets_by_breed(pet_shop, pet_breed):
    dog_list = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == pet_breed:
            dog_list.append(pet)
    return dog_list


def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet

def remove_pet_by_name(pet_shop, remove_pet):
    pet = find_pet_by_name(pet_shop, remove_pet)
    if pet != None:
        pet_shop["pets"].remove(pet)

def add_pet_to_stock(pet_shop, add_pet):
    pet_shop["pets"].append(add_pet)

def get_customer_cash(customer_cash):
   return customer_cash["cash"]

def remove_customer_cash(customer_cash, amount):
    customer_cash["cash"] -= amount

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, pet):
    customer["pets"].append(pet) 
     


def customer_can_afford_pet(customer, pet):
    return customer["cash"]>= pet["price"]

def sell_pet_to_customer(pet_shop, pet, customer):
    if pet and customer_can_afford_pet(customer,pet):
        remove_customer_cash(customer,pet["price"])
        remove_pet_by_name(pet_shop,pet["name"])
        add_pet_to_customer(customer, pet)
        add_or_remove_cash(pet_shop,pet["price"])
        increase_pets_sold(pet_shop,1)
        




    


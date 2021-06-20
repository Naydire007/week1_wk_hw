# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(storename):
    return storename['name']

def get_total_cash(total_cash):
    return total_cash["admin"]["total_cash"]
   

def add_or_remove_cash(pet_shop, cash_amount):
    amount = pet_shop["admin"]["total_cash"]
    add_amount = amount + cash_amount
    pet_shop["admin"]["total_cash"]=add_amount

# def add_or_remove_cash(pet_shop,cash_amount):
# pet_shop["admin"]["total_cash"] += cash_amount

def get_pets_sold(pets_total_sold):
    return pets_total_sold["admin"]["pets_sold"]

def increase_pets_sold(pets_amount, pets_total):
    amount = pets_amount["admin"]["pets_sold"]
    add_pets = amount + pets_total
    pets_amount["admin"]["pets_sold"]=add_pets


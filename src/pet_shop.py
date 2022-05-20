# WRITE YOUR FUNCTIONS HERE

from unicodedata import name


def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop,cash_amount):
    pet_shop["admin"]["total_cash"] += cash_amount

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop,num_of_sold_pets):
    pet_shop["admin"]["pets_sold"] += num_of_sold_pets

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed_name):
    pets = []
    
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed_name:
            pets.append(pet["name"])
    
    return pets        

def find_pet_by_name(pet_shop, pet_name):
    for index in range(len(pet_shop["pets"])):
        pet = pet_shop["pets"][index]["name"]
        if pet == pet_name:
            return pet
    return None    

def remove_pet_by_name(pet_shop, pet_name):
    
    for index in range(len(pet_shop["pets"])):
        pet = pet_shop["pets"][index]["name"]
        if pet == pet_name:
            pet_shop["pets"].pop(index)
            break
    

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, cash_to_remove):
    customer["cash"] -= cash_to_remove

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer,new_pet):
    customer["pets"].append(new_pet)

def customer_can_afford_pet(customer, new_pet):
    if customer["cash"] >= new_pet["price"]:
        return True
    else:
        return False
    
def sell_pet_to_customer(pet_shop, pet_name, customer):

    for index in range(len(pet_shop["pets"])):
        pet_to_sell = pet_shop["pets"][index]
        pet_sold_price = pet_to_sell["price"]
        
        if customer_can_afford_pet(customer, pet_to_sell):
            
            if pet_to_sell["name"] == pet_name:
                add_pet_to_customer(customer, pet_name)
                remove_customer_cash(customer, pet_sold_price)
                remove_pet_by_name(pet_shop, pet_name)
                -abs(pet_sold_price)
                add_or_remove_cash(pet_shop, pet_sold_price)
                increase_pets_sold(pet_shop, 1)
                break

    

    


    



# check the test to find the correct function name
# some functions testing for both ways
# like add_or_remove_cash for add and remove


# get pets by breed can be example
# for list creating using for PDA

# cmd shift 4 takes screenhots for canvas

Cactus = {"Name": "Cactus",
          "Quantity": 800,
          "Unit": "pot",
          "Unite_price":2}
Lily = {"Name": "Lily",
          "Quantity": 550,
          "Unit": "piece",
          "Unite_price":4}
Orchid = {"Name": "Orchid",
          "Quantity": 330,
          "Unit": "pot",
          "Unite_price":18}
Rose =   {"Name": "Rose",
          "Quantity": 1200,
          "Unit": "piece",
          "Unite_price":4}
items=[Cactus, Lily, Orchid, Rose]
header=("Name\tQuantity\tUnit\tUnit_Price (PLN)")
sold_items=[]
def get_items():
     print(" ")
     print(header)
     print(" ")
     print("-"*50)
     print(" )")
     print(items)
def add_item():
    new_item={}
    new_item["Name"]=input("Item name: ")
    new_item["Quantity"]=int(input("Item quantity: "))
    new_item["Unit"]=input("Item unit: ")
    new_item["Unit_price"]=int(input("Item price: "))
    items.append(new_item)
def sell_item():
    sold_item = input("Item name: ")
    if any(d["Name"]==sold_item for d in items):
        sold_quantity = int(input("Quantity os sold items: "))
    if sold_item != items:
        print("Item not available")
def get_cost():
    cost=[]
    for d in items:
        cost.appnd(d["Quantity"] * d["Unit_price"])
        print(sum(cost))

welcome=input("What would you like to do??")
while welcome == "exit":
    print ("bye, bye...")
    exit(1)
if welcome == ("show"):
    get_items()
    welcome=input("What would you like to do??")
if welcome == ("add"):
    add_item()
    welcome=input("What would you like to do next??")
    if welcome==('nothing'or'escape'or'ok'):
        print('thank you for today and have a nice day' )
if welcome == "sell":
    sell_item()
    welcome==input("What would you like to do?")








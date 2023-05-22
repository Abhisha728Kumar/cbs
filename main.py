import mysql.connector as connector
from tabulate import tabulate
import time
# Connecting to MySQL server
connection=connector.connect(
    host="localhost",
    database="cbsdb",
    user="root",
    password="728@RishiKumar"
    
)
cursor=connection.cursor()
cursor.execute("select * from cbs")
results=cursor.fetchall() #cbs table results
food_purchased=[] # food items purchased
print("""
===========   WELCOME TO AROMA CANTEEN   =========== 
     WHAT WOULD YOU LIKE TO HAVE
 We have various CATEGORIES of FOOD --->
1. Fast Food
2. Beverages
3. Meal
4. Desert

*** Write your number for choice ***
""")
def filter_food(food_ctg):
    '''
    This is the filter_food function used to filter the food items on the basis of category and display all items when no category is prefered.
    '''
    if food_ctg !="":
        print(food_ctg)
        filtered_list=list(filter(lambda item:item[3]==food_ctg,results))
        print(tabulate(filtered_list,headers=["ID"," FOOD NAME", "PRICE", "CATEGORY"],tablefmt="pretty"))
    else:
        print(tabulate(results,headers=["ID"," FOOD NAME", "PRICE", "CATEGORY"],tablefmt="pretty"))
    
    
ask1=input("What's your mood to have now? :\t")

if ask1 !="":
    match (int(ask1)):
        case 1:filter_food("Fast Food")
        case 2:filter_food("Beverages")
        case 3:filter_food("Meal")
        case 4:filter_food("Desert")
        case _:print("Invalid choice")
else:
    filter_food("")
# Generate Bill for the customer
def bill_genartor():
    '''
    This is bill_generator function used to generate the bill for food items
    '''
    print(f"""
================   AROMA CANTEEN   ===================
    BILL GENERATED ON {time.strftime("%Y-%m-%d")}
          """)
    print(tabulate(food_purchased,headers=["ID","Food Name","Price","Quantity","Total Price"],tablefmt="pretty"))
    total_amount=0
    for item in food_purchased:
        total_amount=total_amount+item[4]
    print(f"TOTAL PAYABLE AMOUNT : ₹ {total_amount}")
    print("""
*** You can pay from different services provider :
        Paypal, Paytm, PhonePay, Google Pay, Amazon Pay
          """)
    print("""
     THANKS FOR PURCHASING FOOD ITEMS, VISIT AGAIN ... 
      """)
# Selecting the items for purchasing
end=True
while end:
    found=False
    food=input("Enter the NAME of food that you want to purchase:\t")
    qty=int(input("Enter the QUANTITY of food:\t"))
    for item in results:
        a=item[1].lower()
        b=food.lower()
        if a==b:
            print(item[1].lower(),"food",food.lower())
            lst=list(item)
            elem=item[2]*qty
            lst.pop(3)
            lst.insert(3,qty)
            lst.append(elem)
            modified_tuple=tuple(lst)
            food_purchased.append(modified_tuple)
            print("Added to your Billing cart")
            found=True
            break
    if not found:
        print("Your name does not match with Food name",food)
    finish=input("Do you want to purchase more items (y/n):\t")
    if finish=="y":
        continue
    else:
        end=False
        print("Generating Bill for your Food Items ...")
        bill_genartor()

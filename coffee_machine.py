MENU={
    "espresso":{
        "indregedents":{
            "water":50,
            "coffee":18,
            "milk":0
        },
        "cost":1.5
    },
    "latte":{
        "indregedents":{
            "water":200,
            "milk":150,
            "coffee":24
        },
        "cost":2.5
    },
    "cappacinno":{
        "indregedents":{
            "water":250,
            "milk":100,
            "coffee":24
        },
        "cost":3.0
    }

}
resources={
    "water":300,
    "milk":200,
    "coffee":100,
    "Money":0
}
ingredients={}
cost=0
def resouces_checker(ingredients, resources):
    if (resources["water"]-ingredients["water"] < 0 ) or (resources["milk"] - ingredients["milk"] < 0) or (resources["coffee"] - ingredients["coffee"] < 0) :
        print("resources are not sufficient")
        print("Please Wait Restocking ")
        resources["water"]=300
        resources["milk"]=200
        resources["coffee"]=100
        return 0
    else:
        return 1

def coffee_maker(ingredients, resources):
    resources["water"]=resources["water"]-ingredients["water"]
    resources["milk"] = resources["milk"] - ingredients["milk"]
    resources["coffee"] = resources["coffee"] - ingredients["coffee"]

def payement_maker(cost,resources):
    a=int(input("how many quarter? : "))
    b=int(input("how many dimes? : "))
    c=int(input("how many nickles? : "))
    d=int(input("how many pennies? : "))
    total=a*0.25+b*0.10+c*0.05+d*0.01
    change=total-cost
    resources["Money"]+=cost
    if change < 0:
        print("your money is not sufficient ")
        payement_maker(cost, resources )
    print(f"Here is your change ${change}")



while input("do you want something ?? (y/n)")=="y":
    response=input("what would like have ?  (espresso / latte / cappacinno)")
    if response=="report":
        print(resources)
    elif response=="off":
        break
    elif response=="espresso":
        ingredients=MENU["espresso"]["indregedents"]
        cost=MENU["espresso"]["cost"]
        if resouces_checker(ingredients, resources):
            print("Your coffee is being prepared  ")
        else:
            break
        coffee_maker(ingredients, resources)
        payement_maker(cost,resources)
        print("Here is your espresso ☕ ")
    elif response=="latte":
        ingredients = MENU["latte"]["indregedents"]
        cost = MENU["latte"]["cost"]
        if resouces_checker(ingredients, resources):
            print("Your coffee is being prepared  ")
        else:
            break
        coffee_maker(ingredients, resources)
        payement_maker(cost,resources)
        print("Here is your latte ☕ ")
    elif response=="cappacinno":
        ingredients = MENU["cappacinno"]["indregedents"]
        cost = MENU["cappacinno"]["cost"]
        if resouces_checker(ingredients, resources):
            print("Your coffee is being prepared  ")
        else:
            break
        coffee_maker(ingredients, resources)
        payement_maker(cost,resources)
        print("Here is your cappacinno ☕ ")



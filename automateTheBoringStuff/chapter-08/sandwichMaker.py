import pyinputplus as pyip

breadType = pyip.inputMenu(['wheat','white','sourdough'], prompt='Select the bread type :\n')
proteinType = pyip.inputMenu(['chicken' , 'turkey','ham','tofu'],prompt="Select protein type : \n")
ifCheese = pyip.inputYesNo(prompt="Add Cheese?")

if ifCheese:
    cheeseType = pyip.inputMenu(['cheddar','Swiss','mozzarella'],prompt="Select Cheese type: \n")

wantToppings = pyip.inputYesNo(prompt="Add Mayo, Mustard, Lettuce , Tomato? ")

orderCount = pyip.inputInt(min=1, prompt = "How many sandwiches do you want? ")

priceList ={
    'wheat': 10, 
    'white': 10, 
    'sourdough': 15,
    'chicken': 20, 
    'turkey': 20, 
    'ham': 15, 
    'tofu': 25,
    'cheddar': 5, 
    'Swiss': 7, 
    'mozzarella': 8,
    'topping': 2
}

totalCost = priceList[breadType] + priceList[proteinType] + (priceList[cheeseType] if ifCheese else 0) + (priceList['topping'] if wantToppings else 0)

print(totalCost)
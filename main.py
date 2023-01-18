#This chatbot is for an italian restaurant's online services
#This bot uses the keyword "PRICE" in order to tell a customer the price of a certain dish

menu = {
"spaghetti" : 14.25,
"fettucine" : 15.75,
"ravioli" : 11.95,
"burger" : 13.15,
"salad" : 9.50
}


def priceOfItems(menu):
  answer = (input("what item would you like to know the price of?")).lower()
  for food in menu:
    if food in answer:
      return("The price of " + food + " is " + str(menu[food]))
  return("That item is not on the menu")



initial = (input("Hi, what can I help you with today?\n")).lower()
if "price" in initial:
  print(priceOfItems(menu))

cart = []        # --- List to hold items to buy ---- #

def addItem(item):       # ---- Function to add items to cart ---- #
		cart.append(item)
		print("{} has been added to your cart".format(item))
	
def removeItem(item):     # --- Function to remove an item from the cart ---- #
	try:
		cart.remove(item)
		print("{} has been removed from your cart".format(item))
	except:
		print("Sorry, we could not remove that item")
	
def showCart():		# ---- Function to reveal items in cart to the user ---- #
	if cart:
		for item in cart:
			print("=> {}".format(item))
	else:
		print("Sorry, your cart is empty.")
	
def clearCart():     # ---- Measure to clear all items in the cart ---- #
	cart.clear()
	print("Your cart has been emptied")

def Main():
	done = False     # --- Loop switch ---- #
	
	while not done:
		print("What action would you like to perform?")
		ans = input("\n** Quit\n** Add\n** Remove\n** Show\n** Clear:\n ").title()
		if ans == "Quit":
			if not cart:
				print("Thanks for shopping with us")
			else:
				print("Thanks for shopping with us")
				print("\nHere are the items in your cart")
				showCart()
			done = True
		
		elif ans == "Add":
			item = input("What item would you like to add? ").title()
			addItem(item)
		
		elif ans == "Remove":
			showCart()
			item = input("What would you like to remove? ").title()
			removeItem(item)
		
		elif ans == "Show":
			print("Here is your cart:")
			showCart()
		
		elif ans == "Clear":
			print("Are you sure you want to clear your cart?")
			surety = input("Yes/No: ").upper()
			if surety == "YES":
				clearCart()
			else:
				continue


if __name__ == "__main__":
	Main()
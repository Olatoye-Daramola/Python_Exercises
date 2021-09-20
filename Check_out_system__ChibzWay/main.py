cart = Cart("default")

def set_up_cart():
	global cart
	cart_owner_name = input("What is the owner's name:\n")
	cart = Cart(cart_owner_name)

def __add_item_to_cart():
	item_name = input("What did " + cart.owner_name + " buy?\n")
	item_price = float(input("How much does " + item_name + " cost?\n"))
	item_quantity = int(input("How many " + item_name + " did " + cart_owner_name + " buy\n"))

	item = Item(item_name, item_price, item_quantity)
	cart.add(item)


def add_items_to_cart():
	add_more_items = "yes"

	while add_more_items == "yes":
		__add_item_to_cart()
		add_more_items = input("Anything else?\n").lower()

def display_invoice():
	print(cart)
	print("Your bill is " + str(cart.calculate_total()))
	print("Your VAT of 7.5% is:\n" + str(cart.calculate_vat_of()))


if __name__ == '__main__':
	set_up_cart()
	add_items_to_cart()
	display_invoice()

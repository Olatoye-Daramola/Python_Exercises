class Cart:
	def __init__(self, owner_name):
		self.owner_name = owner_name
		self.items = []

	def add(self, item):
		self.items.append(item)

	def calculate_total_price(self):
		total = 0
		for item in self.items:
			total += item.calculate_total()
		return total

	def calculate_vat_of(self, percentage):
		return self.calculate_total_price() * float(percentage / 100)

	def __str__(self):
		string_to_return = ""
		for item in self.items:
			string_to_return += item.__str__() + "\n"
		return string_to_return

class warehouse:

	def __init__(self, posX, posY):
		"""
		Create a warehouse
		"""
		self.posX = posX
		self.posy = posY
		self.products=[]

	def addProduct(self, prodId, prodCount, prodWeight):
		"""
		Record the product in the warehouse given 3 properties of storage
		"""
		#TODO Check if it already exists
		self.products.append({"id": prodId, "count": prodCount, "weight": prodWeight})

	def getById(self, id):
		for i in range(0, len(self.products)):

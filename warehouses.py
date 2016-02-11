def readWarehouse(inputFile):
    """
    Read the warehouse section of the file
    """
    numberOfWarehouses = int(inputFile.readline())
	warehouses = {}
	warehouseProducts = {}
	for w in numberOfWarehouses:
		warehouseCoordLine = inputFile.readLine()
		warehouseCoords = warehouseCoordLine.split(' ')
		x = int(warehouseCoords[0])
		y = int(warehouseCoords[1])
		warehouses[w] = (x, y)
	
		productLine = inputFile.readLine()
		products = productLine.split(' ')
		productsStored = []
		for i in range(0, len(products)):
			productsStored.append(int(products[i]))
	
		warehouseProducts[w] = (productsStored)
		return warehouses, warehouseProducts

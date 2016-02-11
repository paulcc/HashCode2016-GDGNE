def load(filename):
    inputFile = open(filename)
    header = readHeader(inputFile.readline())
    weights = readWeight(inputFile)
    warehouses = readWarehouse(inputFile)
    return header, weights, warehouses


def readHeader(line):
    """
    Read the header of the input file
    """
    line = line.split(' ')
    vals = {"rows": int(line[0]),
            "columns": int(line[1]),
            "drones": int(line[2]),
            "deadline": int(line[3]),
            "maxLoad": int(line[4])}
    return vals

def readWeight(inputFile):
    """
    Read the weight section of the file
    """
    numberOfProducts = int(inputFile.readline())
    productLine = inputFile.readline()
    products = productLine.split(' ')
    weights = []
    for i in range(0, len(products)):
        weights.append({'weight': int(products[i]), 'id': i})
    return weights

def readWarehouse(inputFile):
    """
    Read the warehouse section of the file
    """
    numberOfWarehouses = int(inputFile.readline())
    warehouses = []
    warehouseProducts = {}
    for w in range(0, numberOfWarehouses):
        warehouseCoordLine = inputFile.readline()
        warehouseCoords = warehouseCoordLine.split(' ')
        coords = {'x': int(warehouseCoords[0]), 'y': int(warehouseCoords[1])}
        productLine = inputFile.readline()
        products = productLine.split(' ')
        productsStored = []
        for i in range(0, len(products)):
            productsStored.append(int(products[i]))
        warehouses.append( {'pos': coords, 'prods': productsStored})
   
    return warehouses



if __name__ == "__main__":
    #print load("busy_day.in")
    print load("mother_of_all_warehouses.in")

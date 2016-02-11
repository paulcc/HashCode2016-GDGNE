class Drone:
    
    def __init__(self, maxWeight, coordX, coordY):
        """
        Create a drone with maxweight and position
        """
        self.weight = 0
        self.maxWeight = maxWeight
        self.coordX = coordX
        self.coordY = coordY
        self.action=None
        self.products={}
        self.targetX = coordX
        self.targetY = coordY


    def load(self, warX, warY, productType, productCount):
        """
        Tell the drone to go to warehouse (warX, warY)
        The drone checks if it can make that command and then stacks it
        The drone performs its action with execute
        """
        if self.action==None:
            self.action="load"
            self.targetX=warX
            self.targetY=warY
    
    def deliver(self, dstX, dstY, productIndex, productCount):
        """
        Tell the drone to go to the destination (dstX, dstY) and 
        """
        if self.action==None:
            self.action="deliver"
            self.targetX=dstX
            self.targetY=dstY


    def execute(self):
        """
        Perform the planned action
        """
        if self.action != None:
            if self.targetX != self.coordX:
                distanceX = self.targetX-self.coordX
                directionX = distanceX/abs(distanceX)
                self.coordX += directionX
            elif self.targetY != self.coordY:
                distanceY = self.targetY - self.coordY
                directionY = distanceY/abs(distanceY)
                self.coordY += directionY
            else:
                raise Exception("This condition should not happen")
            matchesX = self.coordX == self.targetX
            matchesY = self.coordY == self.targetY
            if (matchesX and matchesY):
                # Reached destination
                if self.action=="load":
                    #TODO load correct number of product

                elif self.action=="deliver":
                    #TODO drop off correct number of product
                else:

                self.action=None

    def coord(self):
        """
        Return the coordinates of the drone
        """
        return (self.coordX, self.coordY)

    def turns(self):
        """
        Calculate the number of turns remaining to complete action
        """
        distX = abs(self.targetX-self.coordX)
        distY = abs(self.targetY-self.coordY)
        return distX+distY

    def target(self):
        """
        Return the coordinates of the target
        """
        return (self.targetX, self.targetY)

    def __str__(self):
        return "Drone(action=%s, coord=(%d, %d), target=(%d, %d), distance=%d)" % (self.action, self.coordX, self.coordY, self.targetX, self.targetY, self.turns())


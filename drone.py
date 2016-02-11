class Drone:
    
    def __init__(self, maxWeight, coordX, coordY):
        """
        Create a drone with maxweight and position
        """
        self.weight = 0
        self.maxWeight = maxWeight
        self.coordX = coordX
        self.coordY = coordY
        self.action=False
        self.products={}
        self.targetX = coordX
        self.targetY = coordY


    def load(self, warX, warY, productType, productCount):
        """
        Tell the drone to go to warehouse (warX, warY)
        The drone checks if it can make that command and then stacks it
        The drone performs its action with execute
        """
        if self.action==False:
            self.action=True
            self.targetX=warX
            self.targetY=warY
    
    def deliver(self, dstX, dstY, productIndex, productCount):
        """
        Tell the drone to go to the destination (dstX, dstY) and 
        """
        if self.action==False:
            self.action=True
            self.targetX=dstX
            self.targetY=dstY


    def execute(self):
        """
        Perform the planned action
        """
        if self.action==True:
            if self.targetX != self.coordX:
                distanceX = self.targetX-self.coordX
                directionX = distanceX/abs(distanceX)
                self.coordX+=directionX
            elif self.targetY != self.coordY:
                distanceY = self.targetY - self.coordY
                directionY = distanceY/abs(distanceY)
                self.coordY+=directionY
            else:
                raise Exception("This condition should not happen")
            matchesX = self.coordX == self.targetX
            matchesY = self.coordY == self.targetY
            if (matchesX and matchesY):
                # Reached destination
                self.action=False

    def coord(self):
        return (self.coordX, self.coordY)

    def target(self):
        return (self.targetX, self.targetY)



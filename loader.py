def load(filename):
    """The first section of the file describes the ​
     parameters of the simulation​
      . This section contains a single line 
      containing the following natural numbers separated by single spaces: 
      ○ number of rows in the area of the simulation (1 ≤ number of rows ≤ 10000)  
      ○ number of columns in the area of the simulation (1 ≤ number of columns ≤ 10000)  
      ○ D​
       ­ number of drones available (1 ≤ D ≤ 1000)  
       ○ deadline of the simulation (1 ≤ deadline of the simulation ≤ 1000000)  
       ○ maximum load of a drone (1 ≤ maximum load of a drone ≤ 10000)  
       """
    inputFile = open(filename)


def readHeader(line):
    line = line.split(' ')
    vals = {"rows": int(line[0]),
            "columns": int(line[1]),
            "drones": int(line[2]),
            "deadline": int(line[3]),
            "maxLoad": int(line[4])}
    return vals




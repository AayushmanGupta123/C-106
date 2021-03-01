import plotly.express as px
import csv
import numpy as np

def getDataSource(DataPath):
    Coffee = []
    Sleep = []
    with open (DataPath) as csv_file:
        df = csv.DictReader(csv_file)
        for row in df:
            Coffee.append(float(row["Coffee in ml"]))
            Sleep.append(float(row["sleep in hours"]))        
        return{"x":Coffee,"y":Sleep}

def findCo_Relation(DataSource):
    corelation = np.corrcoef(DataSource["x"],DataSource["y"])
    print("Co-Relation Between Coffe vs Sleep: \n --->",corelation[0,1])

def Main():
    createDataPth = "Coffee.csv"
    DataSource = getDataSource(createDataPth)
    findCo_Relation(DataSource)

Main()

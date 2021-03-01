import plotly.express as px
import csv
import numpy as np

def getDataSource(DataPath):
    Temperature = []
    IceCreamSales = []
    SoftDrinkSales = []
    with open (DataPath) as csv_file:
        df = csv.DictReader(csv_file)
        for row in df:
            Temperature.append(float(row["Temperature"]))
            IceCreamSales.append(float(row["Ice-cream Sales"]))
            SoftDrinkSales.append(float(row["Cold drink sales"]))        
        return{"x":Temperature,"y":SoftDrinkSales}

def findCo_Relation(DataSource):
    corelation = np.corrcoef(DataSource["x"],DataSource["y"])
    print("Co-Relation Between Temperature vs SoftDrink: \n --->",corelation[0,1])

def Main():
    createDataPth = "Ice-Cream.csv"
    DataSource = getDataSource(createDataPth)
    findCo_Relation(DataSource)

Main()

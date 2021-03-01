import plotly.express as px
import csv
import numpy as np

def getDataSource(DataPath):
    Marks = []
    Days = []
    with open (DataPath) as csv_file:
        df = csv.DictReader(csv_file)
        for row in df:
            Marks.append(float(row["Marks In Percentage"]))
            Days.append(float(row["Days Present"]))        
        return{"x":Marks,"y":Days}

def findCo_Relation(DataSource):
    corelation = np.corrcoef(DataSource["x"],DataSource["y"])
    print("Co-Relation Between Marks vs DaysPresent: \n --->",corelation[0,1])

def Main():
    createDataPth = "Marks.csv"
    DataSource = getDataSource(createDataPth)
    findCo_Relation(DataSource)

Main()

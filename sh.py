import csv
import plotly.express as px
import numpy as np

def getDataSource(data_path):
    Marks = []
    Days = []
    
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        for row in df:
            Marks.append(float(row["Marks In Percentage"]))
            Days.append(float(row["Days Present"]))
    return {"x":Marks,"y":Days}
    
def find_Correlation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print("correlaton between Marks In Percentage vs Days Present " , correlation[0,1])

def setup():
    data_path = "sh.csv"
    datasource = getDataSource(data_path)
    find_Correlation(datasource)

setup()           
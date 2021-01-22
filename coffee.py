import csv
import plotly.express as px
import numpy as np

def getDataSource(data_path):
    Coffee = []
    Sleep = []
    
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        for row in df:
            Coffee.append(float(row["Coffee"]))
            Sleep.append(float(row["sleep"]))
    return {"x":Coffee,"y":Sleep}
    
def find_Correlation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print("correlaton between coffee vs sleep " , correlation[0,1])

def setup():
    data_path = "coffee.csv"
    datasource = getDataSource(data_path)
    find_Correlation(datasource)

setup()           

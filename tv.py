import csv
import plotly.express as px
import numpy as np

def getDataSource(data_path):
    tv = []
    time = []
    
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        for row in df:
            time.append(float(row["Average time spent watching TV in a week"]))
            tv.append(float(row["Size of TV"]))
    return {"x":tv,"y":time}
    
def find_Correlation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print("correlaton between Average time spent watching TV in a week vs Size of TV " , correlation[0,1])

def setup():
    data_path = "tv.csv"
    datasource = getDataSource(data_path)
    find_Correlation(datasource)

setup()           
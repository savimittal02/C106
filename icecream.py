import csv
import plotly.express as px
import numpy as np

def getDataSource(data_path):
    icecream = []
    temperature = []
    
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        for row in df:
            temperature.append(float(row["Temperature"]))
            icecream.append(float(row["Ice-cream Sales"]))
    return {"x":icecream,"y":temperature}
    
def find_Correlation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print("correlaton between temprature vs icecream Sales " , correlation[0,1])

def setup():
    data_path = "icecream.csv"
    datasource = getDataSource(data_path)
    find_Correlation(datasource)

setup()           


            

    

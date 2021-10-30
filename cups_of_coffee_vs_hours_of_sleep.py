import numpy as np
import plotly.express as px
import csv

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Coffee in ml", y="sleep in hours", color="week")
        fig.show()

def getDataSource(data_path):
    coffee = []
    sleep = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            coffee.append(float(row["Coffee in ml"]))
            sleep.append(float(row["sleep in hours"]))
        
        return {"x" : coffee, "y" : sleep}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Temperature vs Ice Cream Sales :-  \n--->",correlation[0,1])

def setup():
    data_path = "C:/Users/Meet Ankoliya/Python/project-10/data/cups of coffee vs hours of sleep.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)

setup()
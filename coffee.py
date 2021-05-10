import pandas as pd
import plotly.express as pe
import csv

#df=pd.read_csv("coffee.csv")
with open ('coffee.csv') as csv_file:
    df=csv.DictReader(csv_file)
    fig=pe.scatter(df,x="Coffee in ml",y="sleep in hours", color="week")
    fig.show()
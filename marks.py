import pandas as pd
import plotly.express as pe
import csv

#df=pd.read_csv("marks.csv")
with open ('marks.csv') as csv_file:
    df=csv.DictReader(csv_file)
    fig=pe.scatter(df,x="Marks In Percentage",y="Days Present", color="Roll No")
    fig.show()
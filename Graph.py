import pandas as pd
import plotly_express as pe 

df1 = pd.read_csv("data.csv")
fig1 = pe.scatter(df1,x="date",y="cases",color="country",size_max=60)
fig1.show()
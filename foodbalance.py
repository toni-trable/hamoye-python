import pandas as pd
import numpy as np
from matplotlib import pyplot

work = pd.read_excel(r'C:\Users\PC\Desktop\Projects\data\FoodBalanceSheets_E_Africa_NOFLAG.xlsx')

#Question 11
print(work.groupby('Item')['Y2014','Y2017'].sum())
#Question 12

#Question 13
print(work.isnull().sum())
#Question 14

#Question 15
print(work.groupby('Element')['Y2014','Y2015','Y2016','Y2017','Y2018'].sum())
#Question 16
x= work.groupby('Element')['Y2018','Y2017'].sum()    
print(x.sort_values('Y2018',ascending=False))
#Question 17  
y= work.groupby('Element')['Y2018','Y2017'].sum()
print(y.sort_values('Y2018',ascending=True))
#Question 18
print(work.groupby('Area')['Y2018'].sum())
#Question 19 
z= work.loc[work['Area']=='Algeria'] 
print(z.groupby('Element')['Y2018'].sum())
#Question 20
print(work['Area'].nunique())


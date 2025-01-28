import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import pickle

from termcolor import colored as cl

# pip install -U scikit-learn
from sklearn.model_selection import train_test_split


#Modeļi
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import BayesianRidge
from sklearn.linear_model import ElasticNet
from sklearn import ensemble #labāki algoritmi




#Modeļu analīze
from sklearn.metrics import explained_variance_score as evs
from sklearn.metrics import r2_score as r2

#Datu sagatavošana

def sagatavot_datus(fails, kolonna_x, kolonna_y):
    datu_fails = pd.read_csv(fails)
    datu_fails.dropna(inplace=True)
    X_var = datu_fails[kolonna_x]
    Y_var = datu_fails[kolonna_y]
    X_train, x_test, Y_train, y_test = train_test_split(X_var, Y_var, test_size=0.2, random_state=0)
    return (X_train, x_test, Y_train, y_test)

def modela_kvalitate(y_test , results):
    print(cl(f"Dispersija: {evs(y_test, results)}", 'red', attrs=['bold']))
    print(cl(f"Kvadrātiskā novirze: {r2(y_test, results)}", 'yellow', attrs=['bold']))
    return

def trenet_modeli(modelis, X_train, Y_train):
    modelis.fit(X_train, Y_train)
    return modelis

def parbaudit_modeli(modelis, x_test):
    results = modelis.predict(x_test)
    return results

datne1 = "masinmacisanas/auto_simple.csv"
kol_x1 = ['Volume','Weight']
kol_y1 = ['CO2']

datne2 = "masinmacisanas/auto_imports.csv"
kol_x2 = ['horsepower','highway-mpg', 'length']
kol_y2 = ['price']

#Sagatavot datus
X_train, x_test, Y_train, y_test = sagatavot_datus(datne1, kol_x1, kol_y1)
# X_train, x_test, Y_train, y_test = sagatavot_datus(datne2, kol_x2, kol_y2)

#Sagatavot_modeli
modelis = LinearRegression()

modelis = trenet_modeli(modelis, X_train, Y_train)
rezultats = parbaudit_modeli(modelis, x_test)

modela_kvalitate(y_test,rezultats)

dati1_x = [1000, 790]
dati1_rez = 99

rezultats_1 = parbaudit_modeli(modelis, [dati1_x])
print(cl(f"sagaidāmais rez:{dati1_rez}, MI rez:{rezultats_1}", 'magenta', attrs=['bold']))
import pandas as pd #Failu apstrāde
import matplotlib.pyplot as plt #grafiki
import seaborn as sb #vizualizācijas

sb.set_style('whitegrid')
plt.rcParams['figure.figsize']=(15,10)

fails2 = "masinmacisanas/auto_imports.csv"
fails1 = "masinmacisanas/auto_simple.csv"

def heat_map(datne):
    datu_fails = pd.read_csv(datne).select_dtypes('number')
    sb.heatmap(datu_fails.corr(), annot=True, cmap='magma')
    plt.show()
    return

def distribution(datne, kolonna):
    datu_fails = pd.read_csv(datne)
    sb.histplot(datu_fails[kolonna], color="r")
    plt.show()
   

heat_map(fails2)
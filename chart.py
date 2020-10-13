import matplotlib.pyplot as plt
import pandas as pd

from application import application


def chart():
    med_path = "/Users/Gabriela/Desktop/Warner Patch/Values.csv"
    med = pd.read_csv(med_path)
    sales = pd.DataFrame(med)

    ax = plt.gca()
    sales.plot(kind='line', y='Value1', ax=ax, color='red')
    ax.set_xlabel("Value2")
    ax.set_ylabel("Value1")
    plt.title("Values")
    plt.show()


application.add_url_rule('/chart', 'chart', chart)

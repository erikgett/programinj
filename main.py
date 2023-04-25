import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

df = pd.read_csv("data.csv")

def erik(df):
# Вывести имя, возраст, класс билета пассажиров, выбрав пол и спасен/нет.
    pass


def Vika(df):
# Вывести имя и возраст спасенных детей, указав пол и возраст (от 0 до 18).
    a = df.groupby('Name')['Age'].count()
    print(a)

if __name__ == "__main__":
    erik(df)
    Vika(df)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

df = pd.read_csv("data.csv")


def erik(df, sex, isAlived):
    # Вывести имя, возраст, класс билета пассажиров, выбрав пол и спасен/нет.
    if sex == 0:
        sex = 'male'
    else:
        sex = 'female'
    sex_df = df[df['Sex'] == sex]
    aliv_df = sex_df[df['Survived'] == isAlived]
    return aliv_df


def Vika(df, min_age, max_age, sex):
    # Вывести имя и возраст спасенных детей, указав пол и возраст (от 0 до 18).
    if sex == 0:
        sex = 'male'
    else:
        sex = 'female'
    young_survived = df[df['Age'] < max_age][df['Age'] >= min_age][df['Sex'] == sex]
    out_table = df.young_survived.Age
    print(young_survived.Age, young_survived.Sex, young_survived.Name)


if __name__ == "__main__":
    erik(df)
    Vika(df, 5, 10, 0)

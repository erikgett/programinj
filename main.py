import pandas as pd

df = pd.read_csv("data.csv")


def erik(df, sex, isAlived):
    # Вывести имя, возраст, класс билета пассажиров, выбрав пол и спасен/нет.
    if sex == 0:
        sex = 'male'
    else:
        sex = 'female'
    sex_df = df[df['Sex'] == sex]
    aliv_df = sex_df[df['Survived'] == isAlived]
    out = aliv_df[["Name", "Age", "Pclass"]]
    return out


def Vika(df, min_age, max_age, sex):
    # Вывести имя и возраст спасенных детей, указав пол и возраст (от 0 до 18).
    if sex == 0:
        sex = 'male'
    else:
        sex = 'female'
    young_survived = df[df['Age'] <= max_age]
    old_surv = young_survived[young_survived['Age'] >= min_age]
    sex = old_surv[old_surv['Sex'] == sex]
    return sex


if __name__ == "__main__":
    # erik(df)
    Vika(df, 5, 10, 0)

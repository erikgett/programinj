from main import erik
import pandas as pd

df = pd.DataFrame({
    'PassengerId': [1, 2, 3, 4],
    'Survived': [0, 1, 1, 1],
    'Pclass': [3, 1, 3, 2],
    'Name': ["Патрик", "Вика",
             "Эрик", "Вик"],
    'Sex': [0, 1, 0, 1],
    'Age': [14, 16, 12, 26],
    'SibSp': [0, 0, 0, 0],
    'Parch': [0, 0, 1, 1],
    'Ticket': [4, 6, 7, 8],
    'Fare': [4, 6, 7, 8],
    'Cabin': [4, 6, 7, 8],
    'Embarked': [4, 6, 7, 8]})
df2 = pd.DataFrame({
    'PassengerId': [1, 2, 3, 4],
    'Survived': [0, 1, 1, 1],
    'Pclass': [3, 1, 3, 2],
    'Name': ["Патрик", "Вика",
             "Эрик", "Вик"],
    'Sex': [0, 1, 0, 1],
    'Age': [10, 11, 12, 26],
    'SibSp': [0, 0, 0, 0],
    'Parch': [0, 0, 1, 1],
    'Ticket': [4, 6, 7, 8],
    'Fare': [4, 6, 7, 8],
    'Cabin': [4, 6, 7, 8],
    'Embarked': [4, 6, 7, 8]})


def test_erik_func():
    assert (erik(df, 1, 1).equals(erik(df, 1, 1)))

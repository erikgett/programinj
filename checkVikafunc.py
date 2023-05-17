from main import Vika
import pandas as pd

df = pd.DataFrame({
    'PassengerId': [1, 2, 3, 4],
    'Survived': [0, 1, 1, 1],
    'Pclass': [3, 1, 3, 2],
    'Name': ["Патрик", "Вика",
             "Эрик", "Вик"],
    'Sex': ["male", "female", "male", "female"],
    'Age': [18, 16, 12, 26],
    'SibSp': [0, 0, 0, 0],
    'Parch': [0, 0, 1, 1],
    'Ticket': ['4', '6', '7', '8'],
    'Fare': [4.0, 6.0, 7.0, 8.0],
    'Cabin': ['4', '6', '7', '8'],
    'Embarked': ['4', '6', '7', '8']})

df2 = pd.DataFrame({
    'PassengerId': [3, ],
    'Survived': [1, ],
    'Pclass': [3, ],
    'Name': ["Эрик", ],
    'Sex': ["male", ],
    'Age': [12, ],
    'SibSp': [0, ],
    'Parch': [1, ],
    'Ticket': ['7', ],
    'Fare': [7.0, ],
    'Cabin': ['7', ],
    'Embarked': ['7', ]})

print(Vika(df, 10, 12, 0))


def test_vika_func():
    assert (Vika(df, 10, 11, 1).equals(Vika(df, 10, 11, 1)))

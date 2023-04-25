import streamlit as st
import pandas as pd

from main import Vika, erik

# streamlit run C:\Users\erik_\PycharmProjects\programinj\interface.py - команда для локального запуска

df = pd.read_csv("data.csv")
st.write("# Решение задач:")

st.write("# Вывести имя и возраст спасенных детей, указав пол и возраст (от 0 до 18). Задача Виктории")

child_age_V = st.slider(label="Введите возраст ребенка >>: ", max_value=18, min_value=0, step=1, value=(10, 15))
sex_V = st.radio("Какой пол вам интересен", ('Женский', 'Мужской'))
if sex_V == 'Мужской':
    bool_Sex = 0
else:
    bool_Sex = 1

# Vika_table = Vika(df, child_age_V[0], child_age_V[1], bool_Sex)
# st.table(Vika_table)
st.table(df.head(5))
st.write("# Вывести имя, возраст, класс билета пассажиров, выбрав пол и спасен/нет. Задача Эрика")

is_suvrived_E = st.radio("Живых вам или мертвых", ('Живых', 'Мертвых'))
if is_suvrived_E == 'Мертвых':
    bool_Surv = 0
else:
    bool_Surv = 1
sex_E = st.radio("Какой пол вам интересен?", ('Женский', 'Мужской'))
if sex_E == 'Мужской':
    bool_Sex_E = 0
else:
    bool_Sex_E = 1
Erik_table = erik(df, bool_Sex_E, bool_Surv)

st.table(Erik_table)

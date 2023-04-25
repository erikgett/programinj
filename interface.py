import streamlit as st

# streamlit run C:\Users\erik_\PycharmProjects\programinj\interface.py - команда для локального запуска
st.write("# Решение задач:")

st.write("# Вывести имя и возраст спасенных детей, указав пол и возраст (от 0 до 18). Задача Виктории")

child_age_V = st.slider(label="Введите возраст ребенка >>: ", max_value=18, min_value=0, step=1, value=(10, 15))
sex_V = st.radio("Какой пол вам интересен", ('Женский', 'Мужской'))


st.write("# Вывести имя, возраст, класс билета пассажиров, выбрав пол и спасен/нет. Задача Эрика")

is_suvrived_E = st.radio("Живых вам или мертвых", ('Живых', 'Мертвых'))
sex_E = st.radio("Какой пол вам интересен?", ('Женский', 'Мужской'))

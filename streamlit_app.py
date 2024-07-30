import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

# Заголовок додатка
st.title('Ціни на продукти в Україні')

# Завантаження файлів
uploaded_file = st.file_uploader("Завантажте CSV файл з цінами на продукти", type="csv")

if uploaded_file is not None:
    # Завантаження даних
    data = pd.read_csv(uploaded_file)
    
    # Перевірка типів даних
    st.write("Типи даних у стовпцях:")
    st.write(data.dtypes)

    # Перетворення стовпця 'price' у рядковий тип та видалення ком
    data['price'] = data['price'].astype(str).str.replace(',', '', regex=False)
    
    # Перетворення рядків у числовий тип
    data['price'] = pd.to_numeric(data['price'], errors='coerce')

    # Перевірка пропущених значень
    st.write("Кількість пропущених значень у стовпці 'price':")
    st.write(data['price'].isna().sum())

    # Обробка пропущених значень
    data['price'].fillna(0, inplace=True)

    # Відображення даних
    st.header("Перегляд даних")
    st.dataframe(data)

    # Відображення таблиці
    st.header("Таблиця даних")
    st.table(data.head())

    # Графіки з Plotly
    st.header("Графіки з Plotly")
    fig = px.line(data, x='date', y='price', color='category')  # Замініть 'category' на правильний стовпець
    st.plotly_chart(fig)

    # Графіки з Matplotlib
    st.subheader("Графіки з Matplotlib")
    fig, ax = plt.subplots()
    data.groupby('date')['price'].mean().plot(kind='bar', ax=ax)  # Стовпчиковий графік
    st.pyplot(fig)

    # Інтерактивні елементи
    st.header("Інтерактивні елементи")
    product = st.selectbox('Оберіть продукт', data['category'].unique())  # Замініть 'category' на правильний стовпець
    filtered_data = data[data['category'] == product]  # Замініть 'category' на правильний стовпець
    st.write(filtered_data)

    # Прогрес-бар
    st.header("Прогрес-бар")
    with st.spinner('Завантаження...'):
        import time
        time.sleep(1)
    st.success('Завершено!')

    # Використання сторінок та закладок
    st.header("Навігація")
    with st.sidebar:
        st.title("Меню")
        page = st.selectbox("Виберіть сторінку", ["Головна", "Про нас", "Контакти"])
        if page == "Головна":
            st.write("Це головна сторінка.")
        elif page == "Про нас":
            st.write("Про нас.")
        elif page == "Контакти":
            st.write("Контакти.")

    # Користувацькі компоненти
    st.header("Користувацькі компоненти")
    st.components.v1.html("<div style='color: red;'>Це користувацький HTML компонент</div>")

else:
    st.write("Завантажте CSV файл для початку.")





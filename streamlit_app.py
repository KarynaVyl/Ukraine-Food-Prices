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
    
    # Перетворення стовпця 'price' у рядковий тип та видалення ком
    data['price'] = data['price'].astype(str).str.replace(',', '', regex=False)
    
    # Перетворення рядків у числовий тип
    data['price'] = pd.to_numeric(data['price'], errors='coerce')

    # Перевірка пропущених значень
    data['price'].fillna(0, inplace=True)

    # Видалення зайвих колонок з перевіркою наявності
    columns_to_drop = ['unit', 'currency', 'country', 'adnmane', 'mktname', 
                       'mktid', 'cmid', 'umid', 'catid', 'sn', 'default']
    columns_to_drop = [col for col in columns_to_drop if col in data.columns]
    data = data.drop(columns=columns_to_drop)

    # Відображення даних
    st.header("Перегляд даних")
    st.dataframe(data)

    # Відображення таблиці (без стовпця нумерації)
    st.header("Таблиця даних")
    st.table(data.reset_index(drop=True).head())

    # Графіки з Plotly (оптимізований графік)
    st.header("Графіки з Plotly")
    fig = px.line(data, x='date', y='price', color='category',  # Використання стовпця 'category'
                  title='Ціни на продукти по датах')
    fig.update_layout(xaxis_title='Дата', yaxis_title='Ціна', hovermode="x unified")
    st.plotly_chart(fig)

    # Графіки з Matplotlib (оптимізована дата)
    st.subheader("Графіки з Matplotlib")
    fig, ax = plt.subplots(figsize=(10, 5))
    data.groupby('date')['price'].mean().plot(kind='bar', ax=ax)  # Стовпчиковий графік
    ax.set_xlabel('Дата')
    ax.set_ylabel('Середня ціна')
    plt.xticks(rotation=45, ha='right')
    st.pyplot(fig)

    # Інтерактивні елементи
    st.header("Інтерактивні елементи")
    product = st.selectbox('Оберіть продукт', data['category'].unique())  # Використання стовпця 'category'
    filtered_data = data[data['category'] == product]  
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

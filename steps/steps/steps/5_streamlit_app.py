import streamlit as st
from steps.4_process_query import process_query

st.title("Текстовый поиск по индексу")

uploaded_file = st.file_uploader("Загрузите индексный файл", type="pkl")
query = st.text_input("Введите ваш запрос")
top_k = st.slider("Количество результатов", min_value=1, max_value=10, value=3)

if uploaded_file and query:
    with open(uploaded_file, 'rb') as f:
        index_data = f.read()
    
    results = process_query(query, uploaded_file, top_k=top_k)
    st.write("Результаты:")
    for i, result in enumerate(results, 1):
        st.write(f"**Результат {i}:**")
        st.write(result)

import streamlit as st
import pandas as pd
import requests

API_BASE = 'http://127.0.0.1:5000'

st.title("E-commerce dashboard")

tab1, tab2, tab3 = st.tabs(['Carts', 'Products', 'Users'])

with tab1:
    st.header('Carts with Product details')
    response = requests.get(f'{API_BASE}/carts')
    carts = response.json()
    if carts:
        df = pd.DataFrame(carts)
        st.dataframe(df)
    else:
        st.write('No carts found!')

with tab2:
    st.header("Products")
    response = requests.get(f"{API_BASE}/products")
    products = response.json()
    if products:
        df = pd.DataFrame(products)
        st.dataframe(df)
    else:
        st.write("No products found.")

with tab3:
    st.header("Users")
    response = requests.get(f"{API_BASE}/users")
    users = response.json()
    if users:
        df = pd.DataFrame(users)
        st.dataframe(df)
    else:
        st.write("No users found.")




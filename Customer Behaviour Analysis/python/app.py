import pandas as pd
import streamlit as st
import os

# Page config
st.set_page_config(page_title="Customer Behaviour Analysis", layout="wide")

# Title
st.title("📊 Customer Behaviour Analysis Dashboard")

# -------- LOAD DATA (PERMANENT FIX) --------
@st.cache_data
def load_data():
    BASE_DIR = os.path.dirname(__file__)
    file_path = os.path.join(BASE_DIR, "final_clean_data.csv")
    df = pd.read_csv(file_path)
    return df

df = load_data()

# -------- DATA PREVIEW --------
st.subheader("📌 Dataset Preview")
st.dataframe(df.head())

# Debug (safe)
st.subheader("📂 Dataset Columns")
st.write(df.columns)

# -------- AUTO COLUMN DETECTION --------
category_col = next((col for col in df.columns if "category" in col.lower()), None)

rating_col = next((col for col in df.columns if "rating" in col.lower() and "count" not in col.lower()), None)

rating_count_col = next((col for col in df.columns if "rating_count" in col.lower() or "review" in col.lower()), None)

price_col = next((col for col in df.columns if "price" in col.lower()), None)

discount_col = next((col for col in df.columns if "discount" in col.lower()), None)

# -------- CHARTS --------

# Top Categories by Reviews
if category_col and rating_count_col:
    st.subheader("🏆 Top Categories by Reviews")
    top_cat = df.groupby(category_col)[rating_count_col].sum().sort_values(ascending=False)
    st.bar_chart(top_cat)

# Average Rating by Category
if category_col and rating_col:
    st.subheader("⭐ Average Rating by Category")
    avg_rating = df.groupby(category_col)[rating_col].mean().sort_values(ascending=False)
    st.bar_chart(avg_rating)

# Average Price by Category
if category_col and price_col:
    st.subheader("💰 Average Price by Category")
    avg_price = df.groupby(category_col)[price_col].mean().sort_values(ascending=False)
    st.bar_chart(avg_price)

# Discount Distribution
if discount_col:
    st.subheader("🎯 Discount Distribution")
    st.bar_chart(df[discount_col].value_counts())

# Footer
st.markdown("---")
st.markdown("© Customer Behaviour Analysis Project")

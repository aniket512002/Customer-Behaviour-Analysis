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
    # Getting the absolute path of the current folder (python/)
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # Moving one level up to find the CSV in the root directory
    FILE_PATH = os.path.join(BASE_DIR, "..", "final_clean_data.csv")
    
    try:
        # Loading the data into the 'df' variable
        df = pd.read_csv(FILE_PATH)
        return df
    except FileNotFoundError:
        st.error(f"❌ File not found! Make sure 'final_clean_data.csv' is in the root folder.")
        return None

# Initialize Data
df = load_data()

# Only run the rest of the code if data is loaded successfully
if df is not None:
    # -------- DATA PREVIEW --------
    st.subheader("📌 Dataset Preview")
    st.dataframe(df.head())

    # Debug (safe)
    st.subheader("📂 Dataset Columns")
    st.write(list(df.columns))

    # -------- AUTO COLUMN DETECTION --------
    category_col = next((col for col in df.columns if "category" in col.lower()), None)
    rating_col = next((col for col in df.columns if "rating" in col.lower() and "count" not in col.lower()), None)
    rating_count_col = next((col for col in df.columns if "rating_count" in col.lower() or "review" in col.lower()), None)
    price_col = next((col for col in df.columns if "price" in col.lower()), None)
    discount_col = next((col for col in df.columns if "discount" in col.lower()), None)

    # -------- CHARTS --------
    col1, col2 = st.columns(2)

    with col1:
        # Top Categories by Reviews
        if category_col and rating_count_col:
            st.subheader("🏆 Top Categories by Reviews")
            top_cat = df.groupby(category_col)[rating_count_col].sum().sort_values(ascending=False).head(10)
            st.bar_chart(top_cat)

        # Average Price by Category
        if category_col and price_col:
            st.subheader("💰 Average Price by Category")
            avg_price = df.groupby(category_col)[price_col].mean().sort_values(ascending=False).head(10)
            st.bar_chart(avg_price)

    with col2:
        # Average Rating by Category
        if category_col and rating_col:
            st.subheader("⭐ Average Rating by Category")
            avg_rating = df.groupby(category_col)[rating_col].mean().sort_values(ascending=False).head(10)
            st.bar_chart(avg_rating)

        # Discount Distribution
        if discount_col:
            st.subheader("🎯 Discount Distribution")
            st.bar_chart(df[discount_col].value_counts().head(10))

# Footer
st.markdown("---")
st.markdown("© Customer Behaviour Analysis Project")

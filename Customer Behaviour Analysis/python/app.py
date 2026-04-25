import pandas as pd
import streamlit as st

# Page config
st.set_page_config(page_title="Customer Behaviour Analysis", layout="wide")

# Title
st.title("📊 Customer Behaviour Analysis Dashboard")

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("final_clean_data.csv")
    return df

df = load_data()

# Dataset Preview
st.subheader("📌 Dataset Preview")
st.dataframe(df.head())

# Show columns (debug safety)
st.subheader("📂 Dataset Columns")
st.write(df.columns)

# ---- CATEGORY COLUMN DETECT (auto safe) ----
category_col = None
for col in df.columns:
    if "category" in col.lower():
        category_col = col
        break

rating_col = None
for col in df.columns:
    if "rating" in col.lower() and "count" not in col.lower():
        rating_col = col
        break

rating_count_col = None
for col in df.columns:
    if "rating_count" in col.lower() or "review" in col.lower():
        rating_count_col = col
        break

price_col = None
for col in df.columns:
    if "price" in col.lower():
        price_col = col
        break

discount_col = None
for col in df.columns:
    if "discount" in col.lower():
        discount_col = col
        break


# ---- CHARTS ----

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

# Discount Analysis
if discount_col:
    st.subheader("🎯 Discount Distribution")
    st.bar_chart(df[discount_col].value_counts())

# Footer
st.markdown("---")
st.markdown("Customer Behaviour Analysis")
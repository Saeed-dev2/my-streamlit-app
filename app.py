import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# --- Page Config ---
st.set_page_config(page_title="Streamlit App", layout="wide")

# --- Title ---
st.title("📊 Streamlit + Altair Demo (No External Libraries)")

# --- Generate Sample Data ---
@st.cache_data
def create_data(rows: int = 100):
    np.random.seed(42)
    data = pd.DataFrame({
        "Category": np.random.choice(["A", "B", "C"], size=rows),
        "Value X": np.random.randn(rows) * 10 + 50,
        "Value Y": np.random.randn(rows) * 5 + 20,
    })
    return data

data = create_data()

# --- Sidebar Controls ---
st.sidebar.header("Options")
show_data = st.sidebar.checkbox("Show Raw Data", value=True)
chart_type = st.sidebar.radio("Select Chart Type", ["Scatter Plot", "Bar Chart"])

# --- Show Data ---
if show_data:
    st.subheader("🔍 Raw Data")
    st.dataframe(data)

# --- Scatter Plot ---
if chart_type == "Scatter Plot":
    x_col = st.selectbox("X-Axis", ["Value X", "Value Y"], index=0)
    y_col = st.selectbox("Y-Axis", ["Value Y", "Value X"], index=1)

    chart = alt.Chart(data).mark_circle(size=60).encode(
        x=alt.X(x_col),
        y=alt.Y(y_col),
        color='Category',
        tooltip=["Category", x_col, y_col]
    ).interactive()

    st.altair_chart(chart, use_container_width=True)

# --- Bar Chart ---
elif chart_type == "Bar Chart":
    feature = st.selectbox("Aggregate Feature", ["Value X", "Value Y"])
    bar_data = data.groupby("Category")[feature].mean().reset_index()

    chart = alt.Chart(bar_data).mark_bar().encode(
        x='Category',
        y=feature,
        color='Category',
        tooltip=['Category', feature]
    )

    st.altair_chart(chart, use_container_width=True)

# --- Footer ---
st.markdown("---")
st.markdown("✅ Built using only pre-installed libraries.")


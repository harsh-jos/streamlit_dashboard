import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


st.title("Data Visualization Dashboard")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    
    df = pd.read_csv(uploaded_file)

    st.write("Data Preview:")
    st.dataframe(df.head())

    # Sidebar
    st.sidebar.title("Visualization Options")
    chart_type = st.sidebar.selectbox(
        "Select Chart Type",
        ["Scatter Plot", "Line Chart", "Bar Chart", "Histogram", "Box Plot", "Heatmap"]
    )

    # Select columns for visualization
    columns = df.columns.tolist()
    x_axis = st.sidebar.selectbox("Select X-axis", columns)
    y_axis = st.sidebar.selectbox("Select Y-axis", columns)

    # Plotting based on user selection
    if chart_type == "Scatter Plot":
        fig = px.scatter(df, x=x_axis, y=y_axis)
        st.plotly_chart(fig)
    elif chart_type == "Line Chart":
        fig = px.line(df, x=x_axis, y=y_axis)
        st.plotly_chart(fig)
    elif chart_type == "Bar Chart":
        fig = px.bar(df, x=x_axis, y=y_axis)
        st.plotly_chart(fig)
    elif chart_type == "Histogram":
        fig = px.histogram(df, x=x_axis)
        st.plotly_chart(fig)
    elif chart_type == "Box Plot":
        fig = px.box(df, x=x_axis, y=y_axis)
        st.plotly_chart(fig)
    elif chart_type == "Heatmap":
        fig, ax = plt.subplots()
        sns.heatmap(df.corr(), ax=ax, annot=True, cmap="coolwarm")
        st.pyplot(fig)

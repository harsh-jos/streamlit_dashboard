import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Function to reset session state
def reset_state():
    st.session_state["step"] = "upload"
    st.session_state["file_uploaded"] = False
    st.session_state["df"] = None

# Initialize session state
if "step" not in st.session_state:
    reset_state()

# File upload step
if st.session_state["step"] == "upload":
    st.title("CSV Data Visualization Dashboard")
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.session_state["df"] = df
        st.session_state["file_uploaded"] = True
        st.write("Data Preview:")
        st.dataframe(df.head())

        if st.button("Next"):
            st.session_state["step"] = "visualize"

# Visualization configuration step
if st.session_state["step"] == "visualize" and st.session_state["file_uploaded"]:
    df = st.session_state["df"]
    st.sidebar.title("Visualization Options")
    chart_type = st.sidebar.selectbox(
        "Select Chart Type",
        ["Scatter Plot", "Line Chart", "Bar Chart", "Histogram", "Box Plot", "Heatmap"]
    )

    columns = df.columns.tolist()
    x_axis = st.sidebar.selectbox("Select X-axis", columns)
    y_axis = st.sidebar.selectbox("Select Y-axis", columns)

    unique_values_x = df[x_axis].unique().tolist()
    filter_x = st.sidebar.multiselect(f"Filter X-axis", unique_values_x, default=unique_values_x)

    unique_values_y = df[y_axis].unique().tolist()
    filter_y = st.sidebar.multiselect(f"Filter Y-axis", unique_values_y, default=unique_values_y)

    filtered_df = df[(df[x_axis].isin(filter_x)) & (df[y_axis].isin(filter_y))]

    if st.button("Visualize"):
        if chart_type == "Scatter Plot":
            fig = px.scatter(filtered_df, x=x_axis, y=y_axis)
            st.plotly_chart(fig)
        elif chart_type == "Line Chart":
            fig = px.line(filtered_df, x=x_axis, y=y_axis)
            st.plotly_chart(fig)
        elif chart_type == "Bar Chart":
            fig = px.bar(filtered_df, x=x_axis, y=y_axis)
            st.plotly_chart(fig)
        elif chart_type == "Histogram":
            fig = px.histogram(filtered_df, x=x_axis)
            st.plotly_chart(fig)
        elif chart_type == "Box Plot":
            fig = px.box(filtered_df, x=x_axis, y=y_axis)
            st.plotly_chart(fig)
        elif chart_type == "Heatmap":
            fig, ax = plt.subplots()
            sns.heatmap(filtered_df.corr(), ax=ax, annot=True, cmap="coolwarm")
            st.pyplot(fig)

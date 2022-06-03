import streamlit as st
import pandas as pd
import plotly.express as px

# set up the app with wide view preset and a title
st.set_page_config(layout = "wide")
st.title("Interact with Gapminder Data")

# read in the tidy gapminder data
df = pd.read_csv("Data/gapminder_tidy.csv")

# get list of options
continent_list = list(df["continent"].unique())
metric_list = list(df["metric"].unique())
year_list = list(df["year"].unique())
year_list.sort()

min_year = int(year_list[0])
max_year = int(year_list[len(year_list) - 1])

# filter the data to only Oceania gdpPercap values
with st.sidebar:
    st.subheader("Configure the plot")
    continent = st.selectbox(label = "Choose a continent", options = continent_list)
    metric = st.selectbox(label = "Choose a metric", options = metric_list)
    years = st.slider(label = "test", min_value = min_year, max_value = max_year, value = (min_year, max_year))
    show_data = st.checkbox(label = "Show the data used to generate this plot")

df_filtered = df.query(f"continent == '{continent}' & metric == '{metric}' & year >= {years[0]} & year <= {years[1]}")

title = f"{metric} for countries in {continent}"
fig = px.line(df_filtered, x = "year", y = "value", color = "country", title = title, labels={"value": f"{metric}"})
st.plotly_chart(fig)

st.markdown(f"This plot shows the {metric} for countries in {continent}.")

# Display the data table used to create the plot
if show_data:
    st.dataframe(df_filtered)

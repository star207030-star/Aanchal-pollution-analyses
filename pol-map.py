import plotly.express as px
import pandas as pd

# Sample country data
countries = ['USA', 'Canada', 'Brazil', 'UK', 'India', 'China', 'Australia']
pm25 = [12, 8, 18, 15, 45, 50, 10]

# Create DataFrame
df = pd.DataFrame({
    "Country": countries,
    "PM2.5": pm25
})

# Create Choropleth Map
fig = px.choropleth(
    df,
    locations="Country",
    locationmode="country names",
    color="PM2.5",
    color_continuous_scale="Reds",
    title="2024 Global PM2.5 Levels"
)

fig.show()

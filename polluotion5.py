import plotly.express as px
import pandas as pd

data = {
    "Country": ["China", "USA", "South Korea", "Iran", "Australia",
                "Spain", "UK", "Canada", "Brazil", "India",
                "South Africa", "Saudi Arabia", "Nigeria"],
    "Value": [18.5, 12.3, 11.1, 7.4, 7.4,
              6.2, 3.7, 3.7, 3.7, 1.2,
              2.4, 2.4, 1.2]
}

df = pd.DataFrame(data)

fig = px.choropleth(df,
                    locations="Country",
                    locationmode="country names",
                    color="Value",
                    title="World Map Highlighted Countries")

fig.show()
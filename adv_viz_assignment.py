import pandas as pd
import plotly.express as px
import pyarrow
import plotly.graph_objects as go
from plotly.offline import plot

# Load Gapminder 2007 Dataset
gapminder_df = pd.read_csv('gapminder2007.csv')

# PART 1 - Bubble Chart: GDP per Capita vs. Life Expectancy in 2007 Visualize the relationship between GDP per capita
# and life expectancy, with bubble sizes representing population sizes.
fig_bubble = px.scatter(gapminder_df,
                        x="gdpPercap",
                        y="lifeExp",
                        size="pop",
                        color="continent",
                        hover_name="country",
                        log_x=True,
                        size_max=60,
                        title="GDP per Capita vs. Life Expectancy in 2007")
fig_bubble.update_layout(xaxis_title="GDP per Capita (log scale)",
                         yaxis_title="Life Expectancy",
                         legend_title="Continent")

# Part 2 - Funnel Chart: Distribution of Jobs Across Categories in 2023

# Load Jobs in Data Dataset
jobs_in_data_df = pd.read_csv('jobs_in_data.csv')

# Preparing data for the Funnel Chart
jobs_category_counts = jobs_in_data_df['job_category'].value_counts().reset_index()
jobs_category_counts.columns = ['job_category', 'count']
jobs_category_counts = jobs_category_counts.sort_values('count', ascending=False)

# Create a Funnel Chart
fig_funnel = px.funnel(jobs_category_counts,
                       x='count',
                       y='job_category',
                       title='Distribution of Jobs Across Categories in 2023')

# Load AMZN Stock Data for Candlestick Chart
amzn_df = pd.read_csv('AMZN.csv')

# Candlestick Chart: AMZN Stock Price Movement
fig_candlestick = go.Figure(data=[go.Candlestick(x=amzn_df['Date'],
                                                 open=amzn_df['Open'],
                                                 high=amzn_df['High'],
                                                 low=amzn_df['Low'],
                                                 close=amzn_df['Close'])])
fig_candlestick.update_layout(xaxis_title="Date",
                              yaxis_title="Price",
                              title="Amazon Stock Price Movement")

# Display Charts
plot(fig_bubble, filename='bubble_chart.html')
plot(fig_funnel, filename='funnel_chart.html')
plot(fig_candlestick, filename='candle_chart.html')

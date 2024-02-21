import pandas as pd
import plotly.express as px
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

# Exploration - Create a Stacked Funnel Chart
# Preparing data for the Stacked Funnel Chart
# Counting the number of jobs within each job category and experience level
jobs_region_experience = jobs_in_data_df.groupby(['job_category', 'experience_level'])['job_title'].count().reset_index()
jobs_region_experience.columns = ['job_category', 'experience_level', 'count']

# Sorting the job categories in descending order by count to have the largest segment at the top of the funnel
jobs_region_experience_sorted = jobs_region_experience.sort_values('count', ascending=False)

# Create a Stacked Funnel Chart
# The data should be sorted by 'count' in descending order to maintain the correct funnel shape
fig_stacked_funnel = px.funnel(jobs_region_experience_sorted,
                               x='count',
                               y='job_category',
                               color='experience_level',
                               title='Stacked Funnel Chart: Distribution of Jobs Across Categories by Experience '
                                     'Level in 2023')


# Part 3 - Candlestick Chart: AMZN Stock Price Movement
# Load AMZN Stock Data for Candlestick Chart
amzn_df = pd.read_csv('AMZN.csv')

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
plot(fig_stacked_funnel, filename='stacked_funnel_chart')
plot(fig_candlestick, filename='candle_chart.html')

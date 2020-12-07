# load modules
import pandas as pd

# load the csv file into a df
cities_df = pd.read_csv('Resources/cities.csv')

# export the data to html
cities_df.to_html('Resources/cities.html', index=False)



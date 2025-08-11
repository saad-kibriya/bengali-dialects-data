import pkg_resources
import pandas as pd

# This is how you access the data file inside your package
data_path = pkg_resources.resource_filename('data_collection', 'raw_data/bengali_dialects.csv')

# Load the data into a pandas DataFrame
df = pd.read_csv(data_path)

# Print the first 5 rows to see your data
print(df.head())
import pandas as pd

# Load the Excel file into a DataFrame
df = pd.read_excel('questions.xlsx')

# Find name od of column where we want change values
column_name = df['Name of column where is answer']

# Change the 'No' values in the 'Are you employed?' column to 'Not employed' in the 'Employment dimension' column
df.loc[column_name == 'What value active this fragment', 'Column where you want change value'] = 'What will be inputed'

# Save the changes to the Excel file
df.to_excel('updated_questions.xlsx', index=False)

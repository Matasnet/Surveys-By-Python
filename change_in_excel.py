import pandas as pd

# Load the Excel file into a DataFrame
df = pd.read_excel('questions.xlsx')

# Find name od of column where we want change values
column_name = df['Name of column where you want change']

# Change the 'No' values in the 'Are you employed?' column to 'Not employed' in the 'Employment dimension' column
df.loc[column_name == 'What we want change'] = 'What will be inputed'

# Save the changes to the Excel file
df.to_excel('updated_questions.xlsx', index=False)

# Komunikat o aktualizacji
print("Was created file with updates values'.")

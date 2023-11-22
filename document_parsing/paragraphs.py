import pandas as pd

# Reading the text file
file_path = 'aipg/aipg_alltext.txt'  # Replace with your file path
with open(file_path, 'r') as file:
    text = file.read()

# Splitting the text into paragraphs
paragraphs = text.split('\n\n')

# Creating a DataFrame from the paragraphs
df = pd.DataFrame(paragraphs, columns=['Paragraph'])

# Saving the DataFrame to a CSV file
csv_path = 'path_to_your_csv_file.csv'  # Replace with your desired CSV file path
df.to_csv(csv_path, index=False)
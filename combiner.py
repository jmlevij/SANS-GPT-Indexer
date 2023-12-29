import pandas as pd

# List to store each entry
data = []

# Iterating through all 5 files
for i in range(1, 6):
    # Loading CSV file
    df = pd.read_csv(f'SEC588{i}.csv')

    # Iterating through each row
    for index, row in df.iterrows():
        term = row['Term']
        pages = row['Pages']
        definition = str(row['Definition'])  # Convert definition to string

        # Append each term with its book number, page number, and definition
        data.append({"Term": term, "Book": f"B{i}", "Page": pages, "Definition": definition})

# Transforming list to dataframe
final_df = pd.DataFrame(data)

# Saving to composite CSV
final_df.to_csv('GPCS_Composite.csv', index=False)

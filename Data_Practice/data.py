import pandas as pd
import numpy as np

# disc= {"Name": ["Alice", "Bob", "Charlie"], "Age": [25, 30, 35], "City": ["New York", "Los Angeles", "Chicago"]}
# list=[1, 2, 3, 4, 5]

# disc_a=pd.DataFrame(disc)   
# list_b= pd.DataFrame(list, columns=['Values'],copy=False)

# def test():
#     print(disc_a)
#     print(list_b)

# if __name__ == "__main__":
#     print("This is a test script for working with Pandas DataFrame.")
#     test()



data = [
    {'name': 'Mike', 'degree': 'MBA', 'score': 90},
    {'name': 'Dan', 'degree': 'BCA', 'score': 50},
    {'name': 'Mike', 'degree': 'M.Tech', 'score': 40},
]

# Sorts by score (highest first), then by name (alphabetically) if scores are tied
df_sorted = pd.DataFrame(data).sort_values(by='score', ascending=False).reset_index(drop=True)
print(df_sorted)


# data = { 'A': np.array([1, 4, 7]),
#          'B': np.array([2, 5, 8]),
#          'C': np.array([3, 6, 9]) }
# df = pd.DataFrame(data)
# print(df)

df_unique = df_sorted.drop_duplicates(subset='name', keep='first')
print(df_unique)








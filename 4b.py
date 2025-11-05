import pandas as pd
import numpy as np
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael',
             'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}
labels =['a', 'b', 'c', 'd', 'e', 'f ','g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data, index=labels)
print("\nDataFrame:")
print(df)
df.loc[df['name'] == 'James', 'name'] = 'Suresh'
print("\nDataFrame after changing 'James' to 'Suresh':")
print(df)
df['age'] = [23, 21, 22, 20, 21, 22, 20, 23, 21, 22]
print("\nDataFrame after inserting new column 'age':")
print(df)
columns_list = list(df.columns)
print("\nList of DataFrame column headers:", columns_list)
print("\nList of DataFrame column headers (again):", list(df.columns))

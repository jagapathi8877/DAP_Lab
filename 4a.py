import pandas as pd
data = [10, 20, 30, 40, 50]
series = pd.Series(data)
print("Pandas Series:")
print(series)
py_list = series.tolist()
print("\nConverted to Python list:")
print(py_list)
print("Type of the list:", type(py_list))

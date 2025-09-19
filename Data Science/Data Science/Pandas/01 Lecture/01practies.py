import pandas as pd

data = {
    'name' : ['Chirag', 'Ved', 'Kashyap', 'Jay', 'Kunal'], 
    'age' : [20, 21, 22, 23, 24],
    'city': ['Dhrangadhra', 'Kutch', 'Kutch', 'Rajkot', 'Amdavad'],
    'Marks': [85, 90, 78, 88, 92]   
}

students = pd.DataFrame(data)

print("Original DataFrame:")
print(students)

avg_marks = students["Marks"].mean()
print("\nAverage Marks:", avg_marks)

sorted_students = students.sort_values(by="age")
print("\nDataFrame sorted by Age:")
print(sorted_students)

df_no_marks = students.drop(columns=["Marks"])
print("\nDataFrame after dropping 'Marks' column:")
print(df_no_marks)

df_drop_first = students.drop(index=0)
print("\nDataFrame after dropping the first row:")
print(df_drop_first)

missing_check = students.isnull().any()
print("\nMissing values in columns:")
print(missing_check)

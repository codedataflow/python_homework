import pandas as pd
import numpy as np

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

task1_data_frame = df

task1_with_salary = df.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]

print("\nUpdated DataFrame with new column 'Salary':")
print(task1_with_salary)

task1_older = task1_with_salary.copy()
task1_older['Age'] = task1_older['Age'] + 1

print("\nUpdated DataFrame with column 'Age' incremented by 1:")
print(task1_older)

csv_file_path = 'employees.csv'
task1_older.to_csv(csv_file_path, index=False)
task2_employees = pd.read_csv(csv_file_path)

print(f"\nOriginal DataFrame from '{csv_file_path}':")
print(task2_employees)

# created the original JSON
# task2_employees.to_json('additional_employees.json')

json_file_path = 'additional_employees.json'
json_employees = pd.read_json(json_file_path)

print(f"\nOriginal DataFrame from '{json_file_path}':")
print(json_employees)

more_employees = pd.concat([pd.read_csv(csv_file_path), pd.read_json(json_file_path)], ignore_index=True)

print(f"\nOriginalCombined DataFrame from '{csv_file_path}' '{json_file_path}':")
print(more_employees)

first_three = more_employees.head(3)
print("\nUpdated DataFrame withfor first three employees':")
print(first_three)

last_two = more_employees.tail(2)
print("\nUpdated DataFrame for last two employees':")
print(last_two)

employee_shape = more_employees.shape
print("\nUpdated DataFrame with employee_shape':")
print(employee_shape)

df.info()
task1_older.info()
more_employees.info()

dirty_data = pd.read_csv('dirty_data.csv')
print("\nDataFrame with dirty_data':")
print(dirty_data.head())

clean_data = dirty_data.copy()
clean_data = clean_data.drop_duplicates()

print("\nUpdated clean data without dublicates':")
print(clean_data)

clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors='coerce')

age_median = clean_data['Age'].median()
# it causes pandas warning
# clean_data['Age'].fillna(age_median, inplace=True)
# version with fixed warning
clean_data.fillna({'Age': age_median}, inplace=True)

print("\nCleanData after converting Age to numeric and handling missing values:")
print(clean_data)

clean_data['Salary'] = clean_data['Salary'].replace(["unknown", "n/a", "Unknown"], np.nan)
clean_data['Salary'] = pd.to_numeric(clean_data['Salary'], errors='coerce')

print("\nCleanData after converting Salary to numeric and handling missing values:")
print(clean_data)

age_mean = clean_data['Age'].mean()
# it causes pandas warning
# clean_data['Age'].fillna(age_mean, inplace=True)
# version with fixed warning
clean_data.fillna({'Age': age_mean}, inplace=True)

salary_median = clean_data['Salary'].median()
# it causes pandas warning
# clean_data['Salary'].fillna(salary_median, inplace=True)
# version with fixed warning
clean_data.fillna({'Salary': salary_median}, inplace=True)

print(f"\nMean Age used for fillna: {age_mean}")
print(f"Median Salary used for fillna: {salary_median}")
print("\nData after filling missing numeric values:")
print(clean_data)

# potentially needed for cleaning date before datetime, but not in the case of the present data and task
# keeping it as example
# clean_data["Hire Date"] = clean_data["Hire Date"].str.strip().str.replace('-', '/')

print("\nBefore converting to datetime:")
print(clean_data)

# "format='mixed'" is important to parse different data parts delimenters and order 
clean_data["Hire Date"] = pd.to_datetime(clean_data["Hire Date"], format='mixed', errors="coerce")

print("\nAfter converting to datetime:")
print(clean_data)

hire_date_1 = clean_data["Hire Date"][1]

print(f"Validate conversion result for '{hire_date_1}'")
print(type(hire_date_1))

clean_data["Name"] = clean_data["Name"].str.strip().str.upper()
clean_data["Department"] = clean_data["Department"].str.strip().str.upper()

print("\nAfter strip extra whitespace and standardize Name and Department as uppercase:")
print(clean_data)

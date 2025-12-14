import csv
import traceback

"""
from ..assignment2 import assignment2

employees = assignment2.read_employees()
print(employees)
"""

def read_csv(path_to_csv):
    my_list = []
    try:
        with open(path_to_csv, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                my_list.append(row)

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
    return my_list

employees = read_csv('../csv/employees.csv')
#print(employees)
    
employee_names = [f"{employee[1]} {employee[2]}" for employee in employees][1:]
print(employee_names)

# include only those names that contain the letter "e"
employee_names_with_e = [name for name in employee_names if 'e' in name]
# single line print
#print(employee_names_with_e)
# multi line print with list join to string with separator
#print('\n'.join(employee_names_with_e))
# multi line print with list unpack and separator function argument
print(*employee_names_with_e, sep='\n')

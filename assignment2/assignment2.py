import csv
from datetime import datetime
import os
import traceback
import custom_module

def write_csv(path_to_csv, rows):
    try:
        with open(path_to_csv, 'w', newline='') as file:
            writer = csv.writer(file)
            for row in rows:
                writer.writerow(row)

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

def read_csv(path_to_csv, rows_as_tuple = False):
    fields = ""
    my_list = []

    try:
        with open(path_to_csv, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if fields == "":
                    fields = row
                    continue
                my_list.append(tuple(row) if rows_as_tuple else row)

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
    
    my_dict = {}
    my_dict["fields"] = fields #my_list[0]
    my_dict["rows"] = my_list #my_list[1:]
    return my_dict

def read_employees():
    return read_csv('../csv/employees.csv')

employees = read_employees()

def column_index(column_name):
    try:
        return employees["fields"].index(column_name)
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
    return -1 # TBD, -1 or None

employee_id_column = column_index("employee_id")

def first_name(row_number):
    try:
        first_name_idx = column_index("first_name")
        return employees["rows"][row_number][first_name_idx]
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

def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    return list(filter(employee_match, employees["rows"]))

def employee_find_2(employee_id):
   return list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))

def sort_by_last_name():
    employees["rows"].sort(key=lambda row: row[column_index("last_name")])
    return employees["rows"]

def employee_dict(employee):
    dict = {}
    for field in employees["fields"]:
        if field != "employee_id":
            dict[field] = employee[column_index(field)]
    return dict

print(employee_dict(employees["rows"][0]))

def all_employees_dict():
    dict = {}
    for employee in employees["rows"]:
        dict[employee[employee_id_column]] = employee_dict(employee)
    return dict

def get_this_value():
    return os.getenv("THISVALUE")

def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

def read_minutes():
    return read_csv('../csv/minutes1.csv', True), read_csv('../csv/minutes2.csv', True)

minutes1, minutes2 = read_minutes()

def create_minutes_set():
    return set(minutes1["rows"] + minutes2["rows"])

minutes_set = create_minutes_set()

def create_minutes_list():
    return list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_set))

minutes_list = create_minutes_list()

def write_sorted_list():
    minutes_list.sort(key=lambda dt: dt[1])
    result = list(map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")), minutes_list))
    result_to_write = list(result)
    result_to_write.insert(0, tuple(minutes1["fields"]))
    write_csv('./minutes.csv', result_to_write)
    return result

write_sorted_list()

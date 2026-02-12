import sqlite3
import pandas as pd
from datetime import date

# Get current date in YYYY-MM-DD format
def get_date_now():
    return date.today().isoformat()

# Generic function to execute any SQL SELECT statement with/wihout pandas
def execute_sql_statement(sql_statement, use_pandas = False):
    conn = sqlite3.connect("../db/lesson.db")
    return pd.read_sql_query(sql_statement, conn).to_string(index=False) if use_pandas else \
           conn.cursor().execute(sql_statement).fetchall()

# Task 1: Complex JOINs with Aggregation
def get_total_price_for_first_5_orders(use_pandas = False):
    sql_statement = """
        SELECT
            o.order_id,
            ROUND(SUM(i.quantity * p.price), 2) total_price
        FROM orders o
            JOIN line_items i ON i.order_id = o.order_id
            JOIN products p ON p.product_id = i.product_id
        GROUP BY o.order_id
        ORDER BY o.order_id
        LIMIT 5"""

    return execute_sql_statement(sql_statement, use_pandas)

# Task 2: Understanding Subqueries
def get_average_order_price_per_customer(use_pandas = False):
    sql_statement = """
        SELECT
            customer_id,
            ROUND(AVG(total_price), 2) average_price
        FROM customers
            JOIN 
                (SELECT o.customer_id customer_id_b, o.order_id, SUM(i.quantity * p.price) total_price FROM orders o
                    JOIN line_items i ON i.order_id = o.order_id
                    JOIN products p ON p.product_id = i.product_id
                    GROUP BY o.order_id, o.customer_id
                    ORDER BY o.customer_id, o.order_id) ON customer_id_b = customer_id
        GROUP BY customer_id"""

    return execute_sql_statement(sql_statement, use_pandas)

# Task 3: An Insert Transaction Based on Data
def insert_transaction(use_pandas = False):
    conn = sqlite3.connect("../db/lesson.db")
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()

    try:
        # customer
        customer_name = "Perez and Sons"
        cursor.execute("""
                        SELECT customer_id
                        FROM customers
                        WHERE customer_name = ?""", (customer_name,))
        
        results = cursor.fetchall()
        if len(results) == 0:
            raise Exception(f"Customer '{customer_name}' not found.")
        
        customer_id = results[0][0]

        # employee
        first_name = "Miranda"
        last_name = "Harris"
        cursor.execute("""
                        SELECT employee_id
                        FROM employees
                        WHERE first_name = ? AND last_name = ?""",
                        (first_name, last_name))
        
        results = cursor.fetchall()
        if len(results) == 0:
            raise Exception(f"Employee '{first_name} {last_name}' not found.")

        employee_id = results[0][0]

        # 5 least expensive products
        min_products_count = 5
        cursor.execute("""
                        SELECT product_id
                        FROM products
                        ORDER BY price ASC
                        LIMIT ?""",
                        (min_products_count,))
        
        results = cursor.fetchall()
        if len(results) != min_products_count:
            raise Exception(f"""Can't get {min_products_count} least expensive products,
                                max avaialble is {len(results)}""")
        
        product_ids = [row[0] for row in results]

        # prints
        #print(f"Employee ID: {employee_id}, {type(employee_id)}")
        #print(f"Customer ID: {customer_id}, {type(customer_id)}")
        #print(f"Product IDs: {product_ids}, {type(product_ids)}")

        # insert new order
        cursor.execute("""
                INSERT INTO orders   (customer_id, employee_id, date)
                VALUES (?, ?, ?)""", (customer_id, employee_id, get_date_now()))
        
        order_id = cursor.lastrowid
        #print(f"Order: {order_id}, {type(order_id)}")

        # insert order line items
        for product_id in product_ids:
            cursor.execute("""
                INSERT INTO line_items (order_id, product_id, quantity)
                VALUES (?, ?, ?)""",   (order_id, product_id, 10))

        conn.commit()  # Commit transaction

        # final result
        print(f"New order {order_id} is created with: ")
        sql_statement = """
                SELECT
                    o.order_id,
                    o.customer_id,
                    o.employee_id,
                    o.date,
                    i.line_item_id,
                    i.product_id,
                    i.quantity
                FROM orders o
                JOIN line_items i ON o.order_id = i.order_id
                WHERE o.order_id = ?"""
        
        sql_statement_param_typle = (order_id,)

        print(
            pd.read_sql_query(sql_statement, conn, params=sql_statement_param_typle).to_string(index=False) if use_pandas else \
            cursor.execute(sql_statement, sql_statement_param_typle).fetchall())

    except Exception as e:
        conn.rollback()  # Rollback transaction if there's an error
        print("Exception:", e)

# Task 4: Aggregation with HAVING
def aggregation_with_having(use_pandas = False):
    sql_statement = """
        SELECT
            e.first_name EmployeeFirstName,
            e.last_name EmployeeLastName,
            COUNT(o.order_id) OrderCount
        FROM employees e
        JOIN orders o ON e.employee_id = o.employee_id
        GROUP BY e.first_name, e.last_name
        HAVING COUNT(order_id) > 5"""

    return execute_sql_statement(sql_statement, use_pandas)

##############################################################
#### Task 1: Complex JOINs with Aggregation
print("Find the total price of each of the first 5 orders")
print(get_total_price_for_first_5_orders(True))

##############################################################
#### Task 2: Understanding Subqueries
print("For each customer, find the average price of their orders")
print(get_average_order_price_per_customer(True))

##############################################################
#### Task 3: An Insert Transaction Based on Data
print("Create new order")
insert_transaction(True)

##############################################################
#### Task 4: Aggregation with HAVING
print("Aggregation with HAVING")
print(aggregation_with_having(True))

import mysql.connector
from mysql.connector import Error
from sql import create_connection
from sql import execute_query
from sql import execute_read_query

#create connection to mysql database
conn = create_connection('test1.cb2xgxcjhdsv.us-east-2.rds.amazonaws.com', 'admin'
                         ,'admin111', 'test1db')

query = "INSERT INTO users (firstname, lastname) VALUES ('Thomas', Edison')"
# execute_query(conn, query)

select_users = "SELECT * FROM users"
users = execute_read_query(conn, select_users)

for user in users:
    print(user["firstname"] + "has the last name: " + user["lastname"])
    
    
# add a table for invoices
create_invoice_table = """
CREATE TABLE IF NOT EXISTS invoices(
    id INT AUTO_INCREMENT,
    amount INT,
    description VARCHAR(255) NOT NULL,
    user_id INTEGER UNSIGNED NOT NULL,
    FOREIGN KEY fk_user_id(user_id) REFERENCES users(id),
    PRIMARY KEY (id)
)
"""

# execute_query(conn, create_invoice_table)

invoice_from_user = 1
invoice_amount = 50
invoice_description = "Harry Potter Books"

query = "INSERT INTO invoices (amount, descriptionm user_id) VALUES (%s, '%s', %s)" % (invoice_amount, invoice_description, invoice_from_user)
execute_query(conn, query)


#updating invoice record
new_amount = 30
update_invoice_query = """
UPDATE invoices
SET amount = %s
WHERE id = 1
"""
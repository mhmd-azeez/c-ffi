import ctypes
import os

OK = 0

sqlite3 = ctypes.CDLL("../sqlite/sqlite3")

def exec(connection, sql):
    errMsgPtr = ctypes.c_char_p()
    result = sqlite3.sqlite3_exec(connection, sql.encode('utf-8'), None, None, ctypes.byref(errMsgPtr))
    if result != OK:
        errMsg = errMsgPtr.value.decode('utf-8')
        raise Exception(f"Error Code: {result}. Message: {errMsg}")

def open_database(path):
    connection = ctypes.c_void_p()
    result = sqlite3.sqlite3_open(path.encode('utf-8'), ctypes.byref(connection))
    
    if result != OK:
        message = sqlite3.sqlite3_errmsg(connection).decode('utf-8')
        raise Exception(f"Failed to open DB: {message}")
    
    return connection

# Define the path to the database and schema file
db_path = "../sample.db"
schema_path = "../schema.sql"

# Open the database
connection = open_database(db_path)

# Execute the schema
schema = open(schema_path, "r").read()
exec(connection, schema)
exec(connection, "INSERT INTO logs (text) VALUES ('hello from Python!');")

print("Done.")

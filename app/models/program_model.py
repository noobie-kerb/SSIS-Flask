from app.models.database_connect import database_connect

def get_total_programs():
    db, cursor = database_connect()
    try:
        cursor.execute("SELECT COUNT(*) FROM Program")
        return cursor.fetchone()[0]
    finally:
        cursor.close()
        db.close()


def get_programs(per_page, offset):
    db, cursor = database_connect()
    try:
        cursor.execute("SELECT * FROM Program LIMIT %s OFFSET %s", (per_page, offset))
        return cursor.fetchall()
    
    finally:
        cursor.close()
        db.close()

def get_colleges():
    db, cursor = database_connect()
    try:
        cursor.execute("SELECT college_code, college_name FROM college")
        return cursor.fetchall()
    finally:
        cursor.close()
        db.close()

def add_programdb(program_code, program_name, college_code):
    db, cursor = database_connect()
    try:
        sql = "INSERT INTO Program (program_code, program_name, college) VALUES (%s, %s, %s)"
        cursor.execute(sql, (program_code, program_name, college_code))
        db.commit()
    finally:
        cursor.close()
        db.close()

def get_program_by_code(program_code):
    db, cursor = database_connect()
    cursor = db.cursor(dictionary = True)
    try:
        cursor.execute("SELECT * FROM Program WHERE program_code = %s", (program_code,))
        program = cursor.fetchone()
        return program
    finally:
        cursor.close()
        db.close()

def update_program(program_data, program_code):
    db, cursor = database_connect()
    try:
        sql = "UPDATE Program SET program_code = %s, program_name = %s, college = %s WHERE program_code = %s"
        cursor.execute(sql, (*program_data, program_code))
        db.commit()
    finally:
        cursor.close()
        db.close()

def delete_programdb(program_code):
    db, cursor = database_connect()
    try:
        sql = "DELETE FROM Program WHERE program_code = %s"
        cursor.execute(sql, (program_code,))
        db.commit()
    finally:
        cursor.close()
        db.close()
    
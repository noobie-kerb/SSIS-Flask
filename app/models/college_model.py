from app.models.database_connect import database_connect

def get_total_colleges():
    db, cursor = database_connect()
    try:
        cursor.execute("SELECT COUNT(*) FROM College")
        return cursor.fetchone()[0]
    finally:
        cursor.close()
        db.close()

def get_colleges_page(per_page, offset):
    db, cursor = database_connect()
    try:
        cursor.execute("SELECT * FROM College LIMIT %s OFFSET %s", (per_page, offset))
        return cursor.fetchall()
    finally:
        cursor.close()
        db.close()

def get_colleges():
    db, cursor = database_connect()
    try:
        cursor.execute("SELECT * FROM College")
        return cursor.fetchall()
    finally:
        cursor.close()
        db.close()

def add_collegedb(college_code, college_name):
    db, cursor = database_connect()
    try:
        sql = "INSERT INTO College (college_code, college_name) VALUES (%s, %s)"
        cursor.execute(sql, (college_code, college_name))
        db.commit()
    finally:
        cursor.close()
        db.close()

def get_college_by_code(college_code):
    db, cursor = database_connect()
    try:
        cursor.execute("SELECT * FROM College WHERE college_code = %s", (college_code,))
        return cursor.fetchone()
    finally:
        cursor.close()
        db.close()

def update_college(college_data, college_code):
    db, cursor = database_connect()
    try:
        sql = "UPDATE College SET college_code = %s, college_name = %s WHERE college_code = %s"
        cursor.execute(sql, (*college_data, college_code))
        db.commit()
    finally:
        cursor.close()
        db.close()

def delete_collegedb(college_code):
    db, cursor = database_connect()
    try:
        sql = "DELETE FROM College WHERE college_code = %s"
        cursor.execute(sql, (college_code,))
        db.commit()
    finally:
        cursor.close()
        db.close()
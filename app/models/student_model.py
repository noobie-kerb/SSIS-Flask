from app.models.database_connect import database_connect
import math

def get_total_students():
    db, cursor = database_connect()
    try:
        cursor.execute("SELECT COUNT(*) FROM Student")
        return cursor.fetchone()[0]
    finally:
        cursor.close()
        db.close()
    

def get_students(per_page, offset):
    db, cursor = database_connect()
    try:
        cursor.execute( "SELECT student_id, first_name, last_name, program, year, gender, photo_url FROM Student LIMIT %s OFFSET %s",
            (per_page, offset)
        )
        return cursor.fetchall()
    finally:
        cursor.close()
        db.close()

def get_student_by_id(student_id):
    db, cursor = database_connect()
    cursor = db.cursor(dictionary = True)
    try:
        cursor.execute("SELECT * FROM Student WHERE student_id = %s", (student_id,))
        student = cursor.fetchone()
        return student
    finally:
        cursor.close()
        db.close()

def update_student(student_id, student_data):
    db,cursor = database_connect()
    try:
        sql = """UPDATE Student 
                        SET student_id = %s, first_name = %s, last_name = %s, 
                            program = %s, year = %s, gender = %s, photo_url = %s 
                        WHERE student_id = %s"""
        cursor.execute(sql, (*student_data, student_id))
        db.commit()
    finally:
        cursor.close()
        db.close()

def get_programs():
    db, cursor = database_connect()
    try:
        cursor.execute("SELECT program_code, program_name FROM program")
        return cursor.fetchall()
    
    finally:
        cursor.close()
        db.close()

def add_studentdb(student_data):
    db, cursor = database_connect()
    try:
        sql = """
        INSERT INTO Student 
        (student_id, first_name, last_name, program, year, gender, photo_url) 
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, student_data)
        db.commit()
    finally:
        cursor.close()
        db.close()

def delete_studentdb(student_id):
    db, cursor = database_connect()
    try:
        cursor.execute("DELETE FROM Student WHERE student_id = %s", (student_id,))
        db.commit()
    finally:
        cursor.close()
        db.close()
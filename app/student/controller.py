from flask import  render_template, redirect, request,url_for, flash
from .forms import addStudentForm, editStudentForm, deleteStudentForm
from ..student import student_bp
from app.models import database_connect
from mysql.connector import connect, Error
import mysql.connector
from ..program import program_bp

@student_bp.route("/")
@student_bp.route("/student", methods = ['POST', 'GET'])
def student():
   db,cursor = database_connect()
   add_form = addStudentForm()
   edit_form = editStudentForm()
   if not db or not cursor:
      flash("Unable to connect to the database", "error")
      return render_template("student.html", add_form = add_form, edit_form = edit_form)
   try:
      cursor.execute("SELECT * FROM student")
      students = cursor.fetchall()
      
      cursor.execute("SELECT program_code, program_name FROM program")
      programs = cursor.fetchall()

      add_form.course.choices = [(program[0], program[1]) for program in programs]
      edit_form.course.choices = [(program[0], program[1]) for program in programs]
   
      return render_template("student.html", add_form = add_form, edit_form = edit_form, student = students)
   except Exception as e:
      flash(f"An Error Occurred", "Error")
      return render_template("student.html", add_form = add_form, edit_form = edit_form, student = [])
   finally:
      cursor.close()
      db.close()

@student_bp.route("/add_student", methods =["POST"])
def add_student():
   add_form = addStudentForm()
   db, cursor = database_connect()

   cursor.execute("SELECT program_code, program_name FROM program")
   programs = cursor.fetchall()
   add_form.course.choices = [(program[0], program[1]) for program in programs]
   try:

      if add_form.validate_on_submit():
         student_id = add_form.student_id.data
         first_name = add_form.first_name.data.title()
         last_name = add_form.last_name.data.title()
         course = add_form.course.data.upper()
         year = add_form.year.data
         gender = add_form.gender.data.title()

         sql = "INSERT INTO Student (student_id, first_name,last_name, program, year, gender) VALUES (%s, %s, %s, %s, %s, %s)"
         cursor.execute(sql, (student_id, first_name, last_name, course, year, gender))
         db.commit()

         return redirect(url_for("student.student"))
      
      else:
         print(add_form.errors)

   except Exception as e:
         flash(f"An Error Occurred: {e}", "Error")

   finally:
      cursor.close()
      db.close()

   edit_form = editStudentForm()
   return render_template("student.html", add_form = add_form, edit_form = edit_form)

@student_bp.route("/edit_student/<student_id>", methods=["POST", "GET"])
def edit_student(student_id):
    db, cursor = database_connect()
    cursor.execute("SELECT program_code, program_name FROM program")
    programs = cursor.fetchall()
    edit_form = editStudentForm()
    edit_form.course.choices = [(program[0], program[1]) for program in programs]

    try:
        if request.method == "GET":
            cursor.execute("SELECT * FROM Student WHERE student_id = %s", (student_id,))
            student = cursor.fetchone()
            
            if not student:
                return redirect(url_for("student.student"))
            
            edit_form = editStudentForm()
            edit_form.edit_student_id.data = student['student_id']
            edit_form.edit_first_name.data = student['first_name']
            edit_form.edit_last_name.data = student['last_name']
            edit_form.course.data = student['course']
            edit_form.edit_year.data = student['year']
            edit_form.edit_gender.data = student['gender']

            return render_template("student.html", edit_form = edit_form, edit_student = student)
        
        elif request.method == "POST":
        
            if edit_form.validate_on_submit():
                new_student_id = edit_form.edit_student_id.data
                new_first_name = edit_form.edit_first_name.data.title()
                new_last_name = edit_form.edit_last_name.data.title()
                new_course = edit_form.course.data
                new_year = edit_form.edit_year.data
                new_gender = edit_form.edit_gender.data

                sql = """UPDATE Student 
                        SET student_id = %s, first_name = %s, last_name = %s, 
                            program = %s, year = %s, gender = %s 
                        WHERE student_id = %s"""
                cursor.execute(sql, (new_student_id, new_first_name, new_last_name, 
                                    new_course, new_year, new_gender, student_id))
                db.commit()
                flash("Student edited successfully", "success")

                return redirect(url_for("student.student"))
            else:
                print(edit_form.errors)
    except Exception as e:
        flash(f"An error occurred: {str(e)}", "error")

    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()

    return render_template("student.html", edit_form = edit_form)
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
   form = addStudentForm()
   if not db or not cursor:
      flash("Unable to connect to the database", "error")
      return render_template("student.html")
   try:
      cursor.execute("SELECT * FROM student")
      students = cursor.fetchall()
      
      cursor.execute("SELECT program_code, program_name FROM program")
      programs = cursor.fetchall()

      form.course.choices = [(program[0], program[1]) for program in programs]
   
      return render_template("student.html", form = form, student = students)
   except Exception as e:
      flash(f"An Error Occurred", "Error")
      return render_template("student.html", form = form, student = [])
   finally:
      cursor.close()
      db.close()

@student_bp.route("/add_student", methods =["POST"])
def add_student():
   form = addStudentForm(request.form)
   db, cursor = database_connect()

   cursor.execute("SELECT program_code, program_name FROM program")
   programs = cursor.fetchall()

   form.course.choices = [(program[0], program[1]) for program in programs]
   try:

      if form.validate_on_submit():
         student_id = form.student_id.data
         first_name = form.first_name.data.title()
         last_name = form.last_name.data.title()
         course = form.course.data.upper()
         year = form.year.data
         gender = form.gender.data.title()

         sql = "INSERT INTO Student (student_id, first_name,last_name, program, year, gender) VALUES (%s, %s, %s, %s, %s, %s)"
         cursor.execute(sql, (student_id, first_name, last_name, course, year, gender))
         db.commit()

         return redirect(url_for("student.student"))
      
      else:
         print(form.errors)

   except Exception as e:
         flash(f"An Error Occurred: {e}", "Error")

   finally:
      cursor.close()
      db.close()

         
   return render_template("student.html", form = form)

@program_bp.route("/edit_student/<student_id>", methods =["POST", "GET"])
def edit_student(program_code):
   db, cursor= database_connect()

   cursor.execute("SELECT college_code, college_name FROM college")
   colleges = cursor.fetchall()

   try:

      if request.method == "GET":
         cursor.execute("SELECT * FROM Program WHERE program_code = %s", (program_code,))
         program = cursor.fetchone()
      
         if not program:
            return redirect(url_for("program.program"))
         
         form = editProgramForm()
         form.edit_program_code.data = program['program_code']
         form.edit_program_name.data = program['program_name']
         form.college_code.data = program['college_code']

         cursor.execute("SELECT * FROM Program")
         programs = cursor.fetchall()
         return render_template("program.html", program_code = program['program_code'], program_name = program['program_name'], college_code = program['college_code'], program = programs)
      
      form = editProgramForm(request.form)
      form.college_code.choices = [(college[0], college[1]) for college in colleges]

      if form.validate_on_submit():
         new_program_code = form.edit_program_code.data.upper()
         new_program_name = form.edit_program_name.data.title()
         new_college = form.college_code.data.upper()

         sql = "UPDATE Program SET program_code = %s, program_name = %s, college = %s WHERE program_code = %s"
         cursor.execute(sql, (new_program_code, new_program_name, new_college, program_code))
         db.commit()
         flash(f"Edited Successfully","success")

         return redirect(url_for("program.program"))
      else:
         print(form.errors)
   except Exception as e:
      flash(f"An Error Occured:{e}", "error")

   finally:
      if cursor:
         cursor.close()
      if db:
         db.close()

   return redirect(url_for("program.program"))



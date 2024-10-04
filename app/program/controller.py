from flask import render_template, request, redirect, url_for, flash
from .forms import addProgramForm, editProgramForm, deleteProgramForm
from app.models import database_connect
from mysql.connector import connect, Error
import mysql.connector
from ..program import program_bp

@program_bp.route("/program", methods = ["POST", "GET"])
def program():
   db, cursor= database_connect()
   form = addProgramForm()
   if not db or not cursor:
      flash("Unable to connect to the database", "error")
      return render_template("program.html")
   try:
      cursor.execute("SELECT * FROM Program")
      programs = cursor.fetchall()

      cursor.execute("SELECT college_code, college_name FROM college")
      colleges = cursor.fetchall()

      form.college_code.choices = [(college[0], college[1]) for college in colleges]


      return render_template("program.html", form = form, program = programs)
   
   except Error as e:
      flash(f"An Error Occured:{e}", "Error")
      return render_template("program.html", form = form, program = [])
   
   finally:
      cursor.close()
      db.close()


@program_bp.route('/add_program', methods=['POST'])
def add_program():
   form = addProgramForm(request.form)
   db, cursor = database_connect()

   cursor.execute("SELECT college_code, college_name FROM college")
   colleges = cursor.fetchall()

   form.college_code.choices = [(college[0], college[1]) for college in colleges]

   try:
      if form.validate_on_submit():
         program_code = form.program_code.data.upper()
         program_name = form.program_name.data.title()
         college_code = form.college_code.data.upper()

         sql = "INSERT INTO Program (program_code, program_name, college) VALUES (%s, %s, %s)"
         cursor.execute(sql, (program_code, program_name, college_code))
         db.commit()
         
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
   
   return render_template("program.html", form = form)

@program_bp.route("/edit_program/<program_code>", methods =["POST", "GET"])
def edit_program(program_code):
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

@program_bp.route("/delete_program/<program_code>", methods = ["POST", "GET"])
def delete_program(program_code):
   form = deleteProgramForm()
   db,cursor = database_connect()

   if form.validate_on_submit():
      sql = "DELETE FROM Program WHERE program_code = %s"
      cursor.execute(sql, (program_code,))
      db.commit()
      cursor.close()
      db.close()
      return redirect(url_for("program.program"))
   
   return redirect(url_for("program.program"))
from flask import render_template, request, redirect, url_for, flash
from .forms import addProgramForm, editProgramForm, deleteProgramForm
from app.models import database_connect
from mysql.connector import connect, Error
import mysql.connector
from ..program import program_bp

@program_bp.route("/program", methods = ["POST", "GET"])
def program():
   db, cursor= database_connect()
   add_form = addProgramForm()
   edit_form = editProgramForm()
   if not db or not cursor:
      flash("Unable to connect to the database", "error")
      return render_template("program.html")
   try:
      cursor.execute("SELECT * FROM Program")
      programs = cursor.fetchall()

      cursor.execute("SELECT college_code, college_name FROM college")
      colleges = cursor.fetchall()

      add_form.college_code.choices = [(college[0], college[1]) for college in colleges]
      edit_form.college_code.choices = [(college[0], college[1]) for college in colleges]

      return render_template("program.html", add_form = add_form, edit_form = edit_form, program = programs)
   
   except Error as e:
      flash(f"An Error Occured:{e}", "Error")
      return render_template("program.html", add_form = add_form, edit_form = edit_form, program = [])
   
   finally:
      cursor.close()
      db.close()


@program_bp.route('/add_program', methods=['POST'])
def add_program():
   form = addProgramForm()
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

   edit_form = editProgramForm()
   edit_form.college_code.choices = [(college[0], college[1]) for college in colleges]

   try:

      if request.method == "GET":
         cursor.execute("SELECT * FROM Program WHERE program_code = %s", (program_code,))
         program = cursor.fetchone()
      
         if not program:
            return redirect(url_for("program.program"))
         
         edit_form.edit_program_code.data = program['program_code']
         edit_form.edit_program_name.data = program['program_name']
         edit_form.college_code.data = program['college_code']

         return render_template("program.html", edit_form = edit_form)
      
      elif request.method == "POST":
         if edit_form.validate_on_submit():
            new_program_code = edit_form.edit_program_code.data.upper()
            new_program_name = edit_form.edit_program_name.data.title()
            new_college = edit_form.college_code.data.upper()

            sql = "UPDATE Program SET program_code = %s, program_name = %s, college = %s WHERE program_code = %s"
            cursor.execute(sql, (new_program_code, new_program_name, new_college, program_code))
            db.commit()
            flash(f"Edited Successfully","success")

            return redirect(url_for("program.program"))
         else:
            print(edit_form.errors)
   except Exception as e:
      flash(f"An Error Occured:{e}", "error")

   finally:
      if cursor:
         cursor.close()
      if db:
         db.close()

   return render_template("program.html", edit_form = edit_form)

@program_bp.route("/delete_program/<program_code>", methods = ["POST", "GET"])

def delete_program(program_code):
   delete_form = deleteProgramForm()
   db,cursor = database_connect()

   if delete_form.validate_on_submit():
      sql = "DELETE FROM Program WHERE program_code = %s"
      cursor.execute(sql, (program_code,))
      db.commit()
      cursor.close()
      db.close()
      return redirect(url_for("program.program"))
   
   return redirect(url_for("program.program"))
from flask import render_template, request, redirect, url_for, flash
import math
from .forms import addProgramForm, editProgramForm, deleteProgramForm
from app.models import database_connect
from mysql.connector import connect, Error, IntegrityError
import mysql.connector
from ..program import program_bp
from app.models.program_model import *

@program_bp.route("/program", methods = ["POST", "GET"])
def program():
   page = request.args.get('page', 1, type=int)
   per_page = 13
   offset = (page - 1) * per_page
   total_pages = 0

   add_form = addProgramForm()
   edit_form = editProgramForm()
   
   try:
      total_programs = get_total_programs()

      programs = get_programs(per_page, offset)

      
      colleges = get_colleges()

      total_pages = math.ceil(total_programs / per_page)

      add_form.college_code.choices = [(college[0], college[1]) for college in colleges]
      edit_form.college_code.choices = [(college[0], college[1]) for college in colleges]

      return render_template("program.html", add_form = add_form, edit_form = edit_form, program = programs, current_page = page, total_pages = total_pages)
   
   except Error as e:
      flash(f"An Error Occured:{e}", "Error")
      return render_template("program.html", add_form = add_form, edit_form = edit_form, program = [], current_page = page, total_pages = total_pages)
   

@program_bp.route('/add_program', methods=['POST'])
def add_program():
   form = addProgramForm()

   colleges = get_colleges()

   form.college_code.choices = [(college[0], college[1]) for college in colleges]

   try:
      if form.validate_on_submit():
         program_code = form.program_code.data.upper()
         program_name = form.program_name.data.title()
         college_code = form.college_code.data.upper()

         add_programdb(program_code, program_name, college_code)
         
         flash("Program added successfully!", "success")
         return redirect(url_for("program.program"))
      
      else:
         flash("Program Code cannot contain spaces.", "danger")

   except IntegrityError as e:
            if e.errno == 1062:
                flash("College code already exists. Please use a different code.", "danger")      

   except Exception as e:
      flash(f"An Error Occured:{e}", "danger")
   
   return redirect(url_for("program.program"))

@program_bp.route("/edit_program/<program_code>", methods =["POST", "GET"])
def edit_program(program_code):
   
   colleges = get_colleges()

   add_form = addProgramForm()
   edit_form = editProgramForm()
   edit_form.college_code.choices = [(college[0], college[1]) for college in colleges]

   try:

      if request.method == "GET":
         program = get_program_by_code(program_code)
      
         if not program:
            return redirect(url_for("program.program"))
         
         edit_form.edit_program_code.data = program['program_code']
         edit_form.edit_program_name.data = program['program_name']
         edit_form.college_code.data = program['college_code']

         return redirect(url_for("program.program"))
      
      elif request.method == "POST":
         if edit_form.validate_on_submit():
            new_program_code = edit_form.edit_program_code.data.upper()
            new_program_name = edit_form.edit_program_name.data.title()
            new_college = edit_form.college_code.data.upper()

            program_data = (new_program_code, new_program_name, new_college)
            update_program(program_data, program_code)

            flash(f"Program edited successfully!","success")
            return redirect(url_for("program.program"))
         else:
            flash("Program Code cannot contain spaces.", "danger")

      return redirect(url_for("program.program"))
   except IntegrityError as e:
            if e.errno == 1062:
                flash("Program code already exists. Please use a different code.", "danger")  
                return redirect(url_for("program.program"))  

   except Exception as e:
      flash(f"An Error Occured:{e}", "danger")

   return redirect(url_for("program.program"))

@program_bp.route("/delete_program/<program_code>", methods = ["POST", "GET"])

def delete_program(program_code):
   delete_form = deleteProgramForm()

   if delete_form.validate_on_submit():
      
      delete_programdb(program_code)
      flash("Program deleted successfully!", "success")
      return redirect(url_for("program.program"))
   
   return redirect(url_for("program.program"))
from ..college import college_bp
from flask import render_template, request, redirect, url_for, flash
import math
from .forms import addCollegeForm, editCollegeForm, deleteCollegeForm
from app.models import database_connect
from app.models.college_model import *
from mysql.connector import connect, Error, IntegrityError
import mysql.connector


@college_bp.route("/college")
def college():
   page = request.args.get('page', 1, type=int)
   per_page = 13
   offset = (page - 1) * per_page
   total_pages = 0

   add_form = addCollegeForm()
   edit_form = editCollegeForm()

   try:
      total_colleges = get_total_colleges()

      colleges = get_colleges_page(per_page, offset)

      total_pages = math.ceil(total_colleges / per_page)

      return render_template("college.html", add_form = add_form, edit_form = edit_form, college = colleges, current_page = page, total_pages = total_pages)
   except Error as e:
      flash(f"An Error Occured:{e}", Error)
      return render_template("college.html", college= [], edit_form = edit_form, add_form = add_form, current_page = page, total_pages = total_pages)

@college_bp.route("/add_college", methods =["POST"])
def add_college():

   add_form = addCollegeForm()

   if add_form.validate_on_submit():
      try:
        college_code = add_form.college_code.data.upper()
        college_name = add_form.college_name.data.title()

        add_collegedb(college_code, college_name)

        flash("College added successfully!", "success")
      except IntegrityError as e:
        if e.errno == 1062: 
            flash("College code already exists. Please use a different code.", "danger")

      except Error as e:
         flash(f"An error occurred: {e}", "danger")

   else:
      flash(f"Failed to add college: College Code should contain no spaces", "danger")


   return redirect(url_for("college.college"))

@college_bp.route("/edit_college/<college_code>", methods=["POST", "GET"])
def edit_college(college_code):
    edit_form = editCollegeForm()

    try:
        if request.method == "GET":
            college = get_college_by_code(college_code)

            if not college:
                return redirect(url_for("college.college"))

            edit_form.edit_college_code.data = college['college_code']
            edit_form.edit_college_name.data = college['college_name']

            
            colleges = get_colleges()
            return render_template("college.html", edit_form=edit_form, colleges=colleges)

        if request.method == "POST" and edit_form.validate_on_submit():
            new_college_code = edit_form.edit_college_code.data.upper()
            new_college_name = edit_form.edit_college_name.data.title()

            college_data = (new_college_code, new_college_name)
            update_college(college_data, college_code)
            
            flash("College edited successfully", "success")

            return redirect(url_for("college.college"))
        else:
           flash(f"Failed to edit college: College Code should contain no spaces", "danger")
    except IntegrityError as e:
            if e.errno == 1062: 
                flash("College code already exists. Please use a different code.", "danger")

    except Exception as e:
        flash(f"An Error Occurred: {e}", "danger")


    return redirect(url_for("college.college"))


@college_bp.route("/delete_college/<college_code>", methods = ["POST"])
def delete_college(college_code):
   form = deleteCollegeForm()

   if form.validate_on_submit():
      
      delete_collegedb(college_code)
      
      flash("College deleted successfully!", "success")
      return redirect(url_for("college.college"))
   
   return redirect(url_for("college.college"))
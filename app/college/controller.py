from ..college import college_bp
from flask import render_template, request, redirect, url_for, flash
from .forms import addCollegeForm, editCollegeForm, deleteCollegeForm
from app.models import database_connect
from mysql.connector import connect, Error
import mysql.connector

@college_bp.route("/college")
def college():
   db, cursor= database_connect()
   add_form = addCollegeForm()
   edit_form = editCollegeForm()
   if not db or not cursor:
      flash("Unable to connect to the database", "error")
      return render_template("college.html")
   try:
      cursor.execute("SELECT * FROM College")
      colleges = cursor.fetchall()
      return render_template("college.html", add_form = add_form, edit_form = edit_form, college = colleges)
   except Error as e:
      flash(f"An Error Occured:{e}", Error)
      return render_template("college.html", college= [], edit_form = edit_form, add_form = add_form)
   finally:
      cursor.close()
      db.close()

@college_bp.route("/add_college", methods =["POST"])
def add_college():
   db, cursor = database_connect()
   cursor = db.cursor(dictionary=True)
   add_form = addCollegeForm()
   edit_form = editCollegeForm()
   if add_form.validate_on_submit():
      college_code = add_form.college_code.data.upper()
      college_name = add_form.college_name.data.title()
      sql = "INSERT INTO College (college_code, college_name) VALUES (%s, %s)"
      cursor.execute(sql, (college_code, college_name))
      db.commit()
      cursor.close()
      db.close()
      return redirect(url_for("college.college"))
   return render_template("college.html", add_form = add_form, edit_form = edit_form)

@college_bp.route("/edit_college/<college_code>", methods=["POST", "GET"])
def edit_college(college_code):
    db, cursor = database_connect()
    edit_form = editCollegeForm()

    try:
        if request.method == "GET":
            cursor.execute("SELECT * FROM College WHERE college_code = %s", (college_code,))
            college = cursor.fetchone()

            if not college:
                return redirect(url_for("college.college"))

            # Pre-fill the form with the college data
            edit_form.edit_college_code.data = college['college_code']
            edit_form.edit_college_name.data = college['college_name']

            cursor.execute("SELECT * FROM College")
            colleges = cursor.fetchall()
            return render_template("college.html", edit_form=edit_form, colleges=colleges)

        if request.method == "POST" and edit_form.validate_on_submit():
            new_college_code = edit_form.edit_college_code.data.upper()
            new_college_name = edit_form.edit_college_name.data.title()

            sql = "UPDATE College SET college_code = %s, college_name = %s WHERE college_code = %s"
            cursor.execute(sql, (new_college_code, new_college_name, college_code))
            db.commit()
            flash("Edited Successfully", "success")

            return redirect(url_for("college.college"))
        else:
            # Handle invalid form submission
            print(edit_form.errors)
            flash("Failed to edit college. Please check the form.", "error")

    except Exception as e:
        flash(f"An Error Occurred: {e}", "error")

    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()

    return redirect(url_for("college.college"))


@college_bp.route("/delete_college/<college_code>", methods = ["POST"])
def delete_college(college_code):
   form = deleteCollegeForm()
   db,cursor = database_connect()

   if form.validate_on_submit():
      sql = "DELETE FROM College WHERE college_code = %s"
      cursor.execute(sql, (college_code,))
      db.commit()
      cursor.close()
      db.close()
      return redirect(url_for("college.college"))
   
   return redirect(url_for("college.college"))
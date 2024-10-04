from ..college import college_bp
from flask import render_template, request, redirect, url_for, flash
from .forms import addCollegeForm, editCollegeForm, deleteCollegeForm
from app.models import database_connect
from mysql.connector import connect, Error
import mysql.connector

@college_bp.route("/college")
def college():
   db, cursor= database_connect()
   form = addCollegeForm
   if not db or not cursor:
      flash("Unable to connect to the database", "error")
      return render_template("college.html")
   try:
      cursor.execute("SELECT * FROM College")
      colleges = cursor.fetchall()
      return render_template("college.html", form = form, college = colleges)
   except Error as e:
      flash(f"An Error Occured:{e}", Error)
      return render_template("college.html", college= [])
   finally:
      cursor.close()
      db.close()

@college_bp.route("/add_college", methods =["POST"])
def add_college():
   db, cursor = database_connect()
   cursor = db.cursor(dictionary=True)
   form = addCollegeForm(request.form)
   if form.validate_on_submit():
      college_code = form.college_code.data.upper()
      college_name = form.college_name.data.title()
      sql = "INSERT INTO College (college_code, college_name) VALUES (%s, %s)"
      cursor.execute(sql, (college_code, college_name))
      db.commit()
      cursor.close()
      db.close()
      return redirect(url_for("college.college"))
   return render_template("college.html", form = form)

@college_bp.route("/edit_college/<college_code>", methods =["POST", "GET"])
def edit_college(college_code):
   db, cursor= database_connect()

   try:

      if request.method == "GET":
         cursor.execute("SELECT * FROM College WHERE college_code = %s", (college_code,))
         college = cursor.fetchone()
      
         if not college:
            return redirect(url_for("college.college"))
         
         form = editCollegeForm()
         form.edit_college_code.data = college['college_code']
         form.edit_college_name.data = college['college_name']

         cursor.execute("SELECT * FROM College")
         colleges = cursor.fetchall()
         return render_template("college.html", college_code = college['college_code'], college_name = college['college_name'], college = colleges)
      
      form = editCollegeForm(request.form)

      if form.validate_on_submit():
         new_college_code = form.edit_college_code.data.upper()
         new_college_name = form.edit_college_name.data.title()

         sql = "UPDATE College SET college_code = %s, college_name = %s WHERE college_code = %s"
         cursor.execute(sql, (new_college_code, new_college_name, college_code))
         db.commit()
         flash(f"Edited Successfully",)

         return redirect(url_for("college.college"))
      else:
         print(form.errors)
   except Exception as e:
      flash(f"An Error Occured:{e}", "error")

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
from flask import  render_template, redirect, request,url_for, flash
import math
from math import ceil
from .forms import addStudentForm, editStudentForm, deleteStudentForm
from ..student import student_bp
from app.models import database_connect
from mysql.connector import connect, Error, IntegrityError
import mysql.connector
from ..program import program_bp
import cloudinary
import cloudinary.uploader
from cloudinary.uploader import upload
import re
from app.models.student_model import *

@student_bp.route("/")
@student_bp.route("/student", methods = ['POST', 'GET'])
def student():
   page = request.args.get('page', 1, type=int)
   per_page = 13
   offset = (page - 1) * per_page
   total_pages = 0

   add_form = addStudentForm()
   edit_form = editStudentForm()
   try:
      total_students = get_total_students()

      students = get_students(per_page, offset)
      total_pages = math.ceil(total_students / per_page)

      programs = get_programs()

      add_form.course.choices = [(program[0], program[1]) for program in programs]
      edit_form.course.choices = [(program[0], program[1]) for program in programs]
   
      return render_template("student.html", add_form = add_form, edit_form = edit_form, student = students, current_page = page, total_pages = total_pages)
   except Exception as e:
      flash(f"An Error Occurred", "danger")
      return render_template("student.html", add_form = add_form, edit_form = edit_form, student = [], current_page = page, total_pages = total_pages)


@student_bp.route("/add_student", methods=["POST"])
def add_student():
    page = request.args.get('page', 1, type = int)
    total_pages = 0
    add_form = addStudentForm()
    programs = get_programs()
    add_form.course.choices = [(program[0], program[1]) for program in programs]
    
    try:
        if add_form.validate_on_submit():
            student_id = add_form.student_id.data
            first_name = add_form.first_name.data.title()
            last_name = add_form.last_name.data.title()
            course = add_form.course.data.upper()
            year = add_form.year.data
            gender = add_form.gender.data.title()
            
            photo_url = None
            if add_form.photo.data:
                file = add_form.photo.data
                try:
                    upload_result = cloudinary.uploader.upload(
                        file,
                        folder="images",
                        public_id=f"{student_id}",
                        overwrite=True,
                        resource_type="image"
                    )
                    photo_url = upload_result.get('secure_url')
                    print(f"Upload successful: {photo_url}")
                except Exception as e:
                    print(f"Cloudinary upload error: {str(e)}")
                    flash(f"Error uploading photo: {str(e)}", "error")

            student_data = (student_id, first_name, last_name, course, year, gender, photo_url)
            add_studentdb(student_data)

            flash("Student added successfully!", "success")
            return redirect(url_for("student.student"))
        else:
            print(add_form.errors)

            flash(f"Error adding student: {add_form.errors}", "danger")  
            return redirect(url_for("student.student"))
            
    except IntegrityError as e:
        if e.errno == 1062:
            flash("Student_ID already exists. Please use your own ID.", "danger")  
            return redirect(url_for("student.student"))   

    except Exception as e:
        print(f"General error: {str(e)}")
        flash(f"An Error Occurred: {e}", "error")

    edit_form = editStudentForm()
    return render_template("student.html", add_form=add_form, edit_form=edit_form, current_page = page, total_pages = total_pages)


@student_bp.route("/edit_student/<student_id>", methods=["POST", "GET"])
def edit_student(student_id):
    programs = get_programs()
    edit_form = editStudentForm()
    edit_form.course.choices = [(program[0], program[1]) for program in programs]
    student = get_student_by_id(student_id)
    if not student:
        flash("Student not found", "danger")
        return redirect(url_for("student.student"))

    try:
        if request.method == "GET":
            
            edit_form.edit_student_id.data = student['student_id']
            edit_form.edit_first_name.data = student['first_name']
            edit_form.edit_last_name.data = student['last_name']
            edit_form.course.data = student['program']
            edit_form.edit_year.data = student['year']
            edit_form.edit_gender.data = student['gender']
            current_photo_url = student['photo_url']

            return render_template("student.html", edit_form=edit_form, edit_student=student, current_photo_url=current_photo_url)

        elif request.method == "POST":
            if edit_form.validate_on_submit():
                new_student_id = edit_form.edit_student_id.data
                new_first_name = edit_form.edit_first_name.data.title()
                new_last_name = edit_form.edit_last_name.data.title()
                new_course = edit_form.course.data
                new_year = edit_form.edit_year.data
                new_gender = edit_form.edit_gender.data

                public_id = f"images/{new_student_id}"  

                if edit_form.edit_photo.data:
                    file = edit_form.edit_photo.data
                    upload_result = cloudinary.uploader.upload(file, public_id=public_id)
                    new_photo_url = upload_result['secure_url']
                else:
                    new_photo_url = student['photo_url']

                student_data = (new_student_id, new_first_name, new_last_name, new_course, new_year, new_gender, new_photo_url)
                update_student(student_id, student_data)
                flash("Student edited successfully", "success")
                return redirect(url_for("student.student"))

    except IntegrityError as e:
        if e.errno == 1062:
            flash("Student_ID already exists. Please use your own ID.", "danger")  
            return redirect(url_for("student.student"))
        
    except Exception as e:
        flash(f"An error occurred: {str(e)}", "danger")

    return redirect(url_for("student.student"))




@student_bp.route("/delete_student/<student_id>", methods=['POST'])
def delete_student(student_id): 

    try:
        student = get_student_by_id(student_id)
        
        if student:
            photo_url = student['photo_url']
            public_id = f"images/{student_id}"
            
            cloudinary.api.delete_resources(public_id)

        delete_studentdb(student_id)
        flash("Student deleted successfully", "success")
    except Exception as e:
        flash(f"Error deleting student: {str(e)}", "danger")

    return redirect(url_for("student.student"))
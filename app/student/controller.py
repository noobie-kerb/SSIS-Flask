from flask import render_template
from ..student import student_bp

@student_bp.route("/")
@student_bp.route("/student")
def student():
   return render_template("student.html")

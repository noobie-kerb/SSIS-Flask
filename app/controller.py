from flask import render_template, redirect
from .student import student_bp
from .college import college_bp
from .program import program_bp

def register_routes(app):
    app.register_blueprint(student_bp)
    app.register_blueprint(college_bp)
    app.register_blueprint(program_bp)
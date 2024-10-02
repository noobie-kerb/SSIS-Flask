from flask import render_template
from ..program import program_bp

@program_bp.route('/program')
def program():
   return render_template("program.html")
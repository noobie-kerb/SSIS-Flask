from flask import render_template
from ..college import college_bp


@college_bp.route("/college")
def college():
   return render_template("college.html")

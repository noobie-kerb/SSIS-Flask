from flask import render_template, redirect, request, jsonify
from . import user_bp

@user_bp.route('/user')
@user_bp.route('/')
def index():
    return render_template('index.html')
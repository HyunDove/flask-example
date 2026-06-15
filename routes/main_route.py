from flask import Flask, render_template, request, redirect, url_for

main_route = Flask("main", __name__)

@main_route.route('/', methods=['GET'])
def index():
    return render_template('index.html')
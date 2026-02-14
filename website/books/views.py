from pickle import GET
from . import bp
from flask import render_template, request
#from flask_login import login_required, current_user


books_bp = bp


@books_bp.route('/')
def index():
    return render_template('books/index.html')

@books_bp.route('/books/new', methods=['GET', 'POST'])
def add_books():
     # if request.method == 'POST':
        # search_query = request.form.get('search_query')
    #query = request.args.get(f'https://www.googleapis.com/books/v1/volumes?q={search_query}')


    return render_template('books/new.html', query='')

import flask
import sqlite3
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# books = [
#     {'id': 0,
#      'title': 'A Fire Upon the Deep',
#      'author': 'Vernor Vinge',
#      'first_sentence': 'The coldsleep itself was dreamless.',
#      'year_published': '1992'},
#     {'id': 1,
#      'title': 'The Ones Who Walk Away From Omelas',
#      'author': 'Ursula K. Le Guin',
#      'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
#      'published': '1973'},
#     {'id': 2,
#      'title': 'Dhalgren',
#      'author': 'Samuel R. Delany',
#      'first_sentence': 'to wound the autumnal city.',
#      'published': '1975'}
# ]

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

#Entry route
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''

#GetAllBooks route
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    connection = sqlite3.connect('books.db')
    connection.row_factory = dict_factory
    cursor = connection.cursor()
    all_books = cursor.execute('SELECT * FROM books;').fetchall()

    return jsonify(all_books)

#Status 404
@app.errorhandler(404)
def page_not_found(e):
    return '<h1>404</h1><p>The resource could not be found.</p>', 404

#GetBookById route
@app.route('/api/v1/resources/books', methods=['GET'])
def api_filter():
    query_parameters = request.args
    id = query_parameters.get('id')
    published = query_parameters.get('published')
    author = query_parameters.get('author')

    query = 'SELECT * FROM books WHERE'
    to_filter = []

    if id:
        query += ' id=? AND'
        to_filter.append(id)
    if published:
        query += ' published=? AND'
        to_filter.append(published)
    if author:
        query += ' author=? AND'
        to_filter.append(author)
    if not (id or published or author):
        return page_not_found(404)

    query = query[:-4] + ';'

    connection = sqlite3.connect('books.db')
    connection.row_factory = dict_factory
    cursor = connection.cursor()

    results = cursor.execute(query, to_filter).fetchall()

    return jsonify(results)

app.run()
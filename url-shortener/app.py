from flask import Flask, request, redirect
from flask_sqlalchemy import SQLAlchemy
import validators
import random
import string

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.before_first_request
def create_tables():
    db.create_all()

class Urls(db.Model):    # database table
    id_ = db.Column("id_", db.Integer, primary_key=True)
    long = db.Column("long", db.String())
    short = db.Column("short", db.String(10))
    count_visited = db.Column("count_visited", db.Integer, default=0)

    def __init__(self, long, short):
        self.long = long
        self.short = short

def gen_random_short_id():  # getting random short id 
    string_length = 9
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(string_length))


@app.route('/', methods=['POST'])
def shorten():
    url_received = request.json["url"]
    short_url = gen_random_short_id()
    validate = validators.url(url_received)
    print(validate)
    if not validate:  # check if the url is valid
        return 'Validate URL!'
    new_url = Urls(url_received, short_url)
    db.session.add(new_url)
    db.session.commit()
    return request.base_url + short_url

@app.route('/custom', methods=['POST'])
def shorten_custom():
    url_received = request.json["url"]
    short_url = request.json["short_id"]
    validate = validators.url(url_received)
    if not validate:
        return 'Validate URL!'
    if len(short_url) != 9:  # make sure that custom short id is valid
        return 'Invalid short id'
    found_url = db.session.query(Urls).filter(Urls.short == short_url).first()
    if (found_url is None):
        print(short_url)
        new_url = Urls(url_received, short_url)
        db.session.add(new_url)
        db.session.commit()
        return request.url_root + short_url
    return 'URL is already used'

@app.route('/<short_id>', methods=['GET'])
def get_short(short_id):  # redirect to long url
    got_short = db.session.query(Urls).filter(Urls.short==short_id).first()
    got_short.count_visited += 1
    db.session.commit()
    return redirect(got_short.long)



if __name__ == '__main__':
    app.run(port=5000, debug=True)


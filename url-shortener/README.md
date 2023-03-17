# REST URL Shortener API

This is a simple API application made with flask that allows us to shorten the given URL.

## Usage

```python

# create virtual env
python -m venv venv

# activate virtual env (Linux/Mac)
source venv/bin/activate

# activate virtual env (Windows)
venv\Scripts\activate.bat or venv\Scripts\Activate.ps1

# install packages
pip install -r requirements.txt

# run the application
python app.py

# open application in you browser with next address
http://localhost:5000
```

## API Endpoints

http://127.0.0.1:5000/ - POST - body: json(url): gives shortened version of provided url


example:
{
    "url": "https://www.youtube.com/watch?v=Zv1645UtH9w"
}

http://127.0.0.1:5000/custom - POST - body: json(url, short_id): gives shortened version of provided url with custom short id


example:
{
    "url": "https://www.youtube.com/watch?v=Zv1645UtH9w",
    "short_id": "customidd"
}



http://127.0.0.1:5000/<short_id> - GET: redirects to long version of url



from flask import Flask, request, jsonify, render_template, url_for
import requests

app = Flask(__name__)


url = "http://20.244.56.144/test/"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiZXhwIjoxNzE4NzkyNTE5LCJpYXQiOjE3MTg3OTIyMTksImlzcyI6IkFmZm9yZG1lZCIsImp0aSI6IjFiZTIxNWQ5LTA4ODYtNGU4OS1hZmQwLTIzNTAwYjNjMThjOSIsInN1YiI6ImthcmFuMTAwNzIwMDJAZ21haWwuY29tIn0sImNvbXBhbnlOYW1lIjoiQUJDSV9ORElBIiwiY2xpZW50SUQiOiIxYmUyMTVkOS0wODg2LTRlODktYWZkMC0yMzUwMGIzYzE4YzkiLCJjbGllbnRTZWNyZXQiOiJMZk9Hb3RPbmVCYmtGVVJMIiwib3duZXJOYW1lIjoiQUJDMTIzIiwib3duZXJFbWFpbCI6ImthcmFuMTAwNzIwMDJAZ21haWwuY29tIiwicm9sbE5vIjoiQTYwMjA1MjIxMjU5In0.7jy89jhKd67P-AvlvWcmI3HSyIZKvESHkZ_tPmJMmsY"

headers = {
    'Authorization': f"Bearer: {token}"
}

@app.route('/')
def home():
    return "Welcome to the Flask App!"

prev_numbers = []
@app.route('/numbers/e')
def even():
    global prev_numbers, url
    response = requests.get(url+"/even", headers=headers)
    even_numbers = response.json()["numbers"]

    response = {
        "numbers": even_numbers,
        "windowPrevState": prev_numbers,
        "windowCurrState": even_numbers,
        "avg": sum(even_numbers)/len(even_numbers)
    }

    prev_numbers = even_numbers

    return jsonify(response),201


@app.route('/numbers/p')
def primes():
    global prev_numbers, url
    response = requests.get(url+"/primes", headers=headers)
    prime_numbers = response.json()["numbers"]

    response = {
        "numbers": prime_numbers,
        "windowPrevState": prev_numbers,
        "windowCurrState": prime_numbers,
        "avg": sum(prime_numbers)/len(prime_numbers)
    }

    prev_numbers = prime_numbers

    return jsonify(response),201


@app.route('/numbers/f')
def fibbo():
    global prev_numbers, url
    response = requests.get(url+"/fibo", headers=headers)
    fibbo_numbers = response.json()["numbers"]

    response = {
        "numbers": fibbo_numbers,
        "windowPrevState": prev_numbers,
        "windowCurrState": fibbo_numbers,
        "avg": sum(fibbo_numbers)/len(fibbo_numbers)
    }

    prev_numbers = fibbo_numbers

    return jsonify(response),201


@app.route('/numbers/r')
def random():
    global prev_numbers, url
    response = requests.get(url+"/rand", headers=headers)
    rand_numbers = response.json()["numbers"]

    response = {
        "numbers": rand_numbers,
        "windowPrevState": prev_numbers,
        "windowCurrState": rand_numbers,
        "avg": sum(rand_numbers)/len(rand_numbers)
    }

    prev_numbers = rand_numbers

    return jsonify(response),201
if __name__ == '__main__':
    app.run(port=5000)

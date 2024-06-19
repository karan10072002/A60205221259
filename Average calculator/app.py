from flask import Flask, request, jsonify, render_template, url_for
import requests

app = Flask(__name__)


url = "http://20.244.56.144/test/primes"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiZXhwIjoxNzE4NzkxNzkxLCJpYXQiOjE3MTg3OTE0OTEsImlzcyI6IkFmZm9yZG1lZCIsImp0aSI6IjFiZTIxNWQ5LTA4ODYtNGU4OS1hZmQwLTIzNTAwYjNjMThjOSIsInN1YiI6ImthcmFuMTAwNzIwMDJAZ21haWwuY29tIn0sImNvbXBhbnlOYW1lIjoiQUJDSV9ORElBIiwiY2xpZW50SUQiOiIxYmUyMTVkOS0wODg2LTRlODktYWZkMC0yMzUwMGIzYzE4YzkiLCJjbGllbnRTZWNyZXQiOiJMZk9Hb3RPbmVCYmtGVVJMIiwib3duZXJOYW1lIjoiQUJDMTIzIiwib3duZXJFbWFpbCI6ImthcmFuMTAwNzIwMDJAZ21haWwuY29tIiwicm9sbE5vIjoiQTYwMjA1MjIxMjU5In0.bvJ9xMMKyNuuNu5czNF_LYZ7Qrys1LkIcdTYroGZTJk"

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
    response = requests.get(url, headers=headers)
    even_numbers = response.json()["numbers"]

    response = {
        "numbers": even_numbers,
        "windowPrevState": prev_numbers,
        "windowCurrState": even_numbers,
        "avg": sum(even_numbers)/len(even_numbers)
    }

    return jsonify(response),201


if __name__ == '__main__':
    app.run(port=5000)

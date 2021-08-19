from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home_page():
    #return render_template('home.html') first example
    return render_template('index.html')

#@app.route('/about/<username>')
#def about_page(username):
    
   # return f'<h1>This is the Page of {username}</h1>'
   

@app.route("/market")
def market_page():
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '12456123789', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '25879143984', 'price': 1500},
        {'id': 3, 'name': 'Mouse', 'barcode': '70145767292', 'price': 100}
    ]
    return render_template('market.html', items = items)

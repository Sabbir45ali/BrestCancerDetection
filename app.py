from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("signup.html")
  
@app.route('/products')
def products():
    return "This is product pages"

if __name__ == "__main__":
    app.run(debug=True, port=3000)
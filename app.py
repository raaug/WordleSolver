from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


# Create a Flask instance:
app = Flask(__name__)
app.config['SECRET_KEY'] = "My super secret key that no one is supposed to know"



# Create a route decorator
@app.route('/')
def index():
    first_name = "Ray"
    stuff = "This is not bold text"

    favorite_pizza = ['pepperoni', 'cheese', 'sausage', 41]
    return render_template('index.html', first_name=first_name,
                           stuff=stuff,
                           favorite_pizza=favorite_pizza)

# Create custom error pages
# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

# Internal serger error
@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html")

# Create Guess Page
@app.route('/guess', methods=['GET', 'POST'])
def guess():
    guess = None
    form = GuesserForm()
    # Validate Form
    if form.validate_on_submit():
        guess = form.guess.data
        form.guess.data = ''
    return render_template("guess.html", guess = guess, form = form)



if __name__ == "__main__":
    app.run(debug=True)
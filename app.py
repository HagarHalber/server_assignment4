import json

from flask import Flask, redirect
from flask import url_for
from flask import render_template
from datetime import timedelta
from flask import request, session, jsonify
import requests

from DB import interact_db

app = Flask(__name__)

app.secret_key = '123'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=20)

list_pizza = [{'pizza type': 'Margherita', 'sauce': 'tomato',
               'topping': 'mozzarella cheese, fresh basil, salt, and extra-virgin olive oil.'},
              {'pizza type': 'White', 'sauce': 'cream', 'topping': 'olive oil, garlic, cheese, salt'},
              {'pizza type': 'Hawaiian', 'sauce': 'tomato',
               'topping': 'pineapple, tomato sauce, cheese, and either ham or bacon.'},
              {'pizza type': 'Fungi', 'sauce': 'tomato',
               'topping': 'Pomodoro, mozzarella cheese, fresh champignon mushrooms, fried onions and chopped parsley.'},
              {'pizza type': 'Spicy Pizza', 'sauce': 'tomato',
               'topping': 'Green base, mozzarella cheese, roasted eggplant, zucchini, halafinio, garlic confit, and hot chili sauce.'}]

user_dict = {
    'Revital': '1919',
    'Hagar': '1234',
    'Itamar': '123456',
    'Eden': '2204',
    'Avishag': '2689'
}


@app.route('/')
def HomePage():  # put application's code here
    return render_template('HomePage.html')


@app.route('/home')
def Home():
    return redirect('/')


@app.route('/about')
def About():  # put application's code here
    return render_template('AboutUsPage.html')


@app.route('/contact')
def Contact():  # put application's code here
    return render_template('ContactUsPage.html')


@app.route('/assignment3_1')
def assignment3():  # put application's code here
    Pizza = {'#1': 'Margarita', '#2': 'Hawaiian', '#3': 'White '}
    Topping = ['Olives', 'Onion', 'Corn']
    Dessert = ('Teramusu', 'Chess Cake', 'Mascarpone', 'Chocolate Cake')
    return render_template('assignment3_1.html',
                           Pizza=Pizza,
                           Topping=Topping,
                           Dessert=Dessert)


@app.route('/assignment3_2', methods=['GET', 'POST'])
def assigment3_2():
    if 'product_type' in request.args:
        product_type = request.args['product_type']
        if product_type == '':
            return render_template('assignment3_2.html',
                                   pizza=list_pizza)

        my_item = next((item for item in list_pizza if item['pizza type'] == product_type), None)
        if my_item is None:
            return render_template('assignment3_2.html',
                                   message='Pizza Not Found.')
        else:
            return render_template('assignment3_2.html',
                                   product_type=product_type,
                                   ingredients=my_item['sauce'],
                                   topping=my_item['topping'])

    elif request.method == 'POST':
        username = request.form['email']
        password = request.form['password']
        if username in user_dict:
            real_pas = user_dict[username]
            if real_pas == password:
                session['email'] = username
                session['logedin'] = True
                return render_template('assignment3_2.html',
                                       message_log='Success',
                                       username=username)
            else:
                return render_template('assignment3_2.html',
                                       message_log='Wrong password!')
        else:
            return render_template('assignment3_2.html',
                                   message_log='User not exists, please sign in!')
    return render_template('assignment3_2.html')


@app.route('/log_out')
def logout_func():
    session['logedin'] = False
    session.clear()
    return redirect(url_for('assigment3_2'))


@app.route('/session')
def session_func():
    # print(session['CHECK'])
    return jsonify(dict(session))


from assignment_4.assignment_4 import assignment_4

app.register_blueprint(assignment_4)

if __name__ == '__main__':
    app.run(debug=True)

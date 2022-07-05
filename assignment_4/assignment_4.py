import requests
from flask import Blueprint, render_template
from flask import Flask, redirect
from flask import url_for
from flask import request, session, jsonify
from DB import interact_db

assignment_4 = Blueprint('assignment_4', __name__,
                         template_folder='templates')


@assignment_4.route('/assignment4', methods=['GET', 'POST'])
def assignment_4_func():
    query = 'select * from users'
    users_list = interact_db(query, query_type='fetch')
    if 'message_update' in request.args:
        return render_template('assignment4.html', users_list=users_list, message_update=request.args['message_update'])
    if 'message_insert' in request.args:
        return render_template('assignment4.html', users_list=users_list, message_insert=request.args['message_insert'])
    return render_template('assignment4.html', users_list=users_list)


@assignment_4.route('/Update_users', methods=['POST'])
def update_func():
    if 'id' in request.form and 'name' in request.form and 'password' in request.form and 'email' in request.form:
        name = request.form['name']
        id = request.form['id']
        password = request.form['password']
        email = request.form['email']
        query = f"UPDATE users set name='%s', password='%s', email='%s' where id=%s" % (name, password, email, id)
        query_id = "select * from users where id=%s" % (id)
        if len(interact_db(query=query_id, query_type='fetch')) == 0:
            return redirect(url_for('assignment_4.assignment_4_func', message_update='User not exists'))
        interact_db(query=query, query_type='commit')
        return redirect(url_for('assignment_4.assignment_4_func', message_update='User not exists'))
    return redirect('/assignment4')


@assignment_4.route('/Insert_users', methods=['POST'])
def insert_func():
    if 'id' in request.form and 'name' in request.form and 'password' in request.form and 'email' in request.form:
        name = request.form['name']
        id = request.form['id']
        password = request.form['password']
        email = request.form['email']
        query_id = "select * from users where id=%s" % (id)
        if len(interact_db(query=query_id, query_type='fetch')) != 0:
            return redirect(
                url_for('assignment_4.assignment_4_func', message_insert='User already exists, enter your personal id'))
        query = "INSERT INTO users(name, id, password, email) VALUES ('%s', '%s', '%s','%s')" % (
            name, id, password, email)
        interact_db(query=query, query_type='commit')
        return redirect('/assignment4')
    return redirect('/assignment4')


@assignment_4.route('/Delete_user', methods=['POST'])
def delete_user_func():
    user_id = request.form['id']
    query = "DELETE FROM users WHERE id='%s';" % user_id
    interact_db(query, query_type='commit')
    return redirect('/assignment4')


@assignment_4.route('/assignment_4/outer_source', methods=['GET', 'POST'])
def outer_source():
    return render_template('outer_source_assignment4.html')


@assignment_4.route('/assignment_4/source', methods=['GET', 'POST'])
def source():
    if request.method == 'GET':
        if 'id' in request.args:
            id = request.args['id']
            response = requests.get(f"https://reqres.in/api/users/{id}")
            print(response)
            img = response.json()['data']['avatar']
            first_name = response.json()['data']['first_name']
            last_name = response.json()['data']['last_name']
            return render_template('outer_source_assignment4.html', url=img, name=first_name, last_name=last_name)
        return render_template('outer_source_assignment4.html')
    return render_template('outer_source_assignment4.html')


@assignment_4.route('/assignment_4/users')
def Jason_users():
    query_id = "select * from users"
    query_res = interact_db(query=query_id, query_type='fetch')
    return jsonify(query_res)


@assignment_4.route('/assignment_4/restapi_users')
def get_default_user():
    query = 'select * from users'
    query_res = interact_db(query, query_type='fetch')
    if len(query_res) != 0:
        return jsonify(query_res[0])
    else:
        return jsonify({
            "error": "Data base empty"
        })


@assignment_4.route('/assignment_4/restapi_users/')
def get_empty_user():
    return redirect('/assignment_4/restapi_users')


@assignment_4.route('/assignment_4/restapi_users/<USER_ID>')
def get_user(USER_ID):
    if len(USER_ID) == 0:
        return redirect('/assignment_4/restapi_users')
    if not USER_ID.isnumeric():
        return jsonify({
            "error": "No such user exists"
        })

    id = int(USER_ID)
    query_id = "select * from users where id=%s" % (id)
    query_res = interact_db(query_id, query_type='fetch')
    if len(query_res) != 0:
        return jsonify(query_res)
    else:
        return jsonify({"error": "No such user exists"})

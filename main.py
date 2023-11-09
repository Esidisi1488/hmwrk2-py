from flask import Flask, request
from utils import generate_users, get_astronauts_num, read_requirements, commit_sql
from create_table import create_table

app = Flask(__name__)


@app.route("/requirements")
def requirements():
    return read_requirements()


@app.route("/generate-users")
def users():
    quantity = request.args.get('quantity', '100')

    if quantity.isdigit():
        quantity = int(quantity)
        max_quantity = 100

        if quantity > max_quantity:
            return f'Quantity should be less then {max_quantity}'

        return generate_users(quantity)

    return f'Invalid quantity value: {quantity}'


@app.route("/phones/create_table")
def table():
    return create_table()


@app.route("/space")
def astronauts():
    res = get_astronauts_num()
    return str(res)


@app.route('/phones/create')
def emails_create():
    name_value = request.args['name']
    phone_value = request.args['phone']

    sql = f"""
    INSERT INTO Phones (contactName, phoneValue)
    VALUES ({name_value}, {phone_value});
    """
    commit_sql(sql)

    return 'phones_create'


@app.route('/phones/read')
def emails_read():
    import sqlite3
    con = sqlite3.connect('example.db')
    cur = con.cursor()

    sql = """
    SELECT * FROM Phones;
    """
    cur.execute(sql)

    result = cur.fetchall()
    con.close()

    return result


@app.route('/phones/update')
def emails_update():
    name_value = request.args['name']
    phone_value = request.args['phone']
    phone_id = request.args['id']

    sql = f"""
    UPDATE Phones
    SET contactName = '{name_value}', phoneValue = '{phone_value}'
    WHERE phoneId = {phone_id};
    """
    commit_sql(sql)

    return 'phones_update'


@app.route('/phones/delete')
def emails_delete():
    phone_id = request.args['id']

    sql = f"""
    DELETE FROM Phones
    WHERE phoneId = {phone_id};
    """
    commit_sql(sql)

    return 'phones_delete'


if __name__ == '__main__':
    app.run(host='0.0.0.0')

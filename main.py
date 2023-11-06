from flask import Flask, request
from utils import generate_users, get_astronauts_num, read_requirements

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


@app.route("/space")
def astronauts():
    res = get_astronauts_num()
    return str(res)


if __name__ == '__main__':
    app.run(host='0.0.0.0')

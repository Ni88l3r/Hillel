from flask import Flask, request
import utils

app = Flask(__name__)


@app.route('/requirements/')
def requirements_page():
    return utils.get_file_content('requirements.txt')


@app.route('/generate-users/')
def generate_users_page():
    quantity = request.args.get('quantity', '100')
    if not quantity.isdigit() or not int(quantity):
        return "<b>ERROR!</b> Quantity (" + quantity + ") must be integer more than 0!"
    return utils.generate_users(int(quantity))


@app.route('/mean/')
def mean_page():
    return "<b>Average Height (Inches):</b> " + str(utils.get_csv_row_average("hw.csv", 1)) + '<br/>' +\
           "<b>Average Weight (Pounds):</b> " + str(utils.get_csv_row_average("hw.csv", 2))


@app.route('/space/')
def space_page():
    return "There are currently <b>" +\
           str(utils.get_json_value("http://api.open-notify.org/astros.json", "number")) +\
           "</b> humans in space."


if __name__ == '__main__':
    app.run()

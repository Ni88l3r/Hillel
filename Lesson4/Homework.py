from flask import Flask, request
import utils

app = Flask(__name__)


@app.route('/names/')
def names_page():
    return str(utils.sql_request('./chinook.db', "SELECT COUNT(DISTINCT FirstName) FROM Customers;"))


@app.route('/customers/')
def customers_page():
    if not request.args.get('filter'):
        return utils.paginate(utils.sql_request('./chinook.db', "SELECT * FROM Customers;"))
    else:
        sql_statement = utils.filter_and(request.args.get('filter'))
        return utils.paginate(utils.sql_request('./chinook.db', "SELECT * FROM Customers WHERE " + sql_statement + ";"))


@app.route('/tracks/')
def tracks_page():
    return str(utils.sql_request('./chinook.db', "SELECT COUNT(*) FROM Tracks;"))


@app.route('/tracks-sec/')
def tracks_sec_page():
    return utils.paginate(utils.sql_request('./chinook.db', "SELECT *, Milliseconds/1000 FROM Tracks;"))


if __name__ == '__main__':
    app.run()

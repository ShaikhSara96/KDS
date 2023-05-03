from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__, static_folder="static")

orders = [
    {
        'order_id': 221,
        'items': [{'name': 'Noodle', 'quantity': 3}, {'name': 'coke', 'quantity': 2}],
        'table_num': 1,
    },
    {
        'order_id': 222,
        'items': [{'name': 'Bingsu', 'quantity': 10}, {'name': 'Cola', 'quantity': 6}],
        'table_num': 1,
    },
    {
        'order_id': 121,
        'items': [{'name': 'Noodle', 'quantity': 0}, {'name': 'coke', 'quantity': 1}],
        'table_num': 2,
    },
    {
        'order_id': 234,
        'items': [{'name': 'Noodle', 'quantity': 10}, {'name': 'coke', 'quantity': 5}],
        'table_num': 3,
    },
    {
        'order_id': 984,
        'items': [{'name': 'Noodle', 'quantity': 10}, {'name': 'coke', 'quantity': 5}],
        'table_num': 4,
    },
    {
        'order_id': 701,
        'items': [{'name': 'Noodle', 'quantity': 10}, {'name': 'coke', 'quantity': 5}],
        'table_num': 5,
    },
    {
        'order_id': 701,
        'items': [{'name': 'Maza', 'quantity': 10}, {'name': 'pepsi', 'quantity': 5}],
        'table_num': 6,
    }
]

@app.route("/")
def kds():
    tables = {}
    for order in orders:
        if order["table_num"] not in tables:
            tables[order["table_num"]] = {
                "orders": [order],
            }
        else:
            tables[order["table_num"]]["orders"].append(order)
            
    return render_template('kds.html', tables=tables)

@app.route('/hist2.html')
def history():
    return render_template('hist2.html')

@app.route("/process_date", methods=["POST"])
def process_date():
    # get the selected date from the form submission
    selected_date = request.form["datepicker"]

    # convert the selected date to a datetime object
    dt_object = datetime.strptime(selected_date, "%Y-%m-%d")

    # get the current time
    current_time = datetime.now().strftime("%H:%M:%S")

    # combine the date and time into a single datetime object
    dt_object = datetime.combine(dt_object, datetime.strptime(current_time, "%H:%M:%S").time())

    # print the datetime object
    print("Selected date and time:", dt_object)

    # return a response to the user
    return "Selected date and time: {}".format(dt_object)

if __name__ == "__main__":
     app.run(debug=True)
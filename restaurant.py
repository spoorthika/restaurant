from flask import Flask, jsonify, send_file
import mysql.connector

app = Flask(__name__)
password = input("Enter MySQL password: ")


def get_data(query):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password=password,
        database="restaurant"
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data


@app.route('/')
def home():
    return send_file('index.html')


@app.route('/orders')
def orders():
    query = """
        SELECT
            order_id,
            DATE_FORMAT(order_date, '%Y-%m-%d') AS order_date,
            GROUP_CONCAT(item_id SEPARATOR ', ') AS items,
            GROUP_CONCAT(qty SEPARATOR ', ') AS quantity,
            IFNULL(CAST(SUM(total) AS CHAR), '') AS order_total
        FROM orders_history
        GROUP BY order_id, order_date
        ORDER BY order_id
    """
    return jsonify(get_data(query))


@app.route('/payments')
def payments():
    query = """
        SELECT
            payment_id,
            order_id,
            DATE_FORMAT(payment_date, '%Y-%m-%d') AS payment_date,
            payment_type,
            IFNULL(CAST(amount_due AS CHAR), '') AS amount_due,
            IFNULL(CAST(tips AS CHAR), '') AS tips,
            IFNULL(CAST(discount AS CHAR), '') AS discount,
            IFNULL(CAST(total_paid AS CHAR), '') AS total_paid,
            payment_status
        FROM payments
    """
    return jsonify(get_data(query))


@app.route('/menu')
def menu():
    query = """
        SELECT
            menu.item_id,
            menu.item_name,
            categories.category_name,
            menus.menu_name,
            IFNULL(menu.size, '') AS size,
            IFNULL(CAST(menu.price AS CHAR), '') AS price
        FROM menu
        JOIN categories ON menu.cat_id = categories.cat_id
        JOIN menus ON menu.menu_id = menus.menu_id
        ORDER BY menu.item_id
    """
    return jsonify(get_data(query))


if __name__ == '__main__':
    app.run(debug=False)

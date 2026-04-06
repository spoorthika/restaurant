from flask import Flask, jsonify, send_file
import mysql.connector

app = Flask(__name__)
password = input("Enter MySQL password: ")

queries = {
    "orders": """
        SELECT
            order_id,
            DATE_FORMAT(order_date, '%Y-%m-%d') AS order_date,
            GROUP_CONCAT(item_id SEPARATOR ', ') AS items,
            GROUP_CONCAT(qty SEPARATOR ', ') AS quantity,
            SUM(total) AS order_total
        FROM orders_history
        GROUP BY order_id, order_date
        ORDER BY order_id
    """,
    "payments": """
        SELECT
            payment_id,
            order_id,
            DATE_FORMAT(payment_date, '%Y-%m-%d') AS payment_date,
            payment_type,
            amount_due,
            tips,
            discount,
            total_paid,
            payment_status
        FROM payments
    """,
    "menu": """
        SELECT
            menu.item_id,
            menu.item_name,
            categories.category_name,
            menus.menu_name,
            menu.size,
            menu.price
        FROM menu
        JOIN categories ON menu.cat_id = categories.cat_id
        JOIN menus ON menu.menu_id = menus.menu_id
        ORDER BY menu.item_id
    """
}


def get_data(name):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password=password,
        database="restaurant"
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute(queries[name])
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    for row in data:
        for key, value in row.items():
            row[key] = "" if value is None else str(value)

    return data


@app.route('/')
def home():
    return send_file('index.html')


@app.route('/<name>')
def show_data(name):
    if name not in queries:
        return jsonify({"error": "Page not found"}), 404

    try:
        return jsonify(get_data(name))
    except Exception as error:
        return jsonify({"error": str(error)}), 500


if __name__ == '__main__':
    app.run(debug=False)

from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)


# Connection DB
def Connection_DB():
    connection = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='',
        database='ArtGallery',
        cursorclass=pymysql.cursors.DictCursor
    )

    return connection


@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS, POST'
    return response


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/select-category', methods=['POST'])
def handle_post_request_1():
    try:
        data = request.get_json()


        try:
            Connection_DB()
            print('Conection')
            try:
                cursor = Connection_DB().cursor()
                select_category = f"select * from category;"
                cursor.execute(select_category)
                rows = cursor.fetchall()
            finally:
                Connection_DB().close()
        except Exception as ex:
            print('No Conection')
            print(ex)

        return jsonify({"message": "Данные успешно приняты на бэкенде!", "category": rows})

    except Exception as e:
        print("Ошибка обработки запроса:", str(e))
        return jsonify({"error": "Произошла ошибка обработки запроса"}), 500


@app.route('/search-paintings', methods=['POST'])
def handle_post_request_2():
    try:
        data = request.get_json()

        value = data.get('value')

        try:
            Connection_DB()
            print('Conection')
            try:
                cursor = Connection_DB().cursor()
                select_category = f"CALL SearchPaintings2('{value}');"
                cursor.execute(select_category)
                rows = cursor.fetchall()
            finally:
                Connection_DB().close()
        except Exception as ex:
            print('No Conection')
            print(ex)

        return jsonify({"message": "Данные успешно приняты на бэкенде!", "paintings": rows})

    except Exception as e:
        print("Ошибка обработки запроса:", str(e))
        return jsonify({"error": "Произошла ошибка обработки запроса"}), 500


@app.route('/select6', methods=['POST'])
def handle_post_request_3():
    try:
        data = request.get_json()

        value = data.get('value')

        try:
            Connection_DB()
            print('Conection')
            try:
                cursor = Connection_DB().cursor()
                select_category = f"CALL select6();"
                cursor.execute(select_category)
                rows = cursor.fetchall()
            finally:
                Connection_DB().close()
        except Exception as ex:
            print('No Conection')
            print(ex)

        return jsonify({"message": "Данные успешно приняты на бэкенде!", "paintings": rows})

    except Exception as e:
        print("Ошибка обработки запроса:", str(e))
        return jsonify({"error": "Произошла ошибка обработки запроса"}), 500


@app.route('/SelectOfCategory', methods=['POST'])
def handle_post_request_4():
    try:
        data = request.get_json()

        categoryName = data.get('CategoryName')

        try:
            Connection_DB()
            print('Conection')
            try:
                cursor = Connection_DB().cursor()
                select_category = f"CALL SearchPaintingsByCategory('{categoryName}')"
                cursor.execute(select_category)
                rows = cursor.fetchall()
            finally:
                Connection_DB().close()
        except Exception as ex:
            print('No Conection')
            print(ex)

        return jsonify({"message": "Данные успешно приняты на бэкенде!", "paintings": rows})

    except Exception as e:
        print("Ошибка обработки запроса:", str(e))
        return jsonify({"error": "Произошла ошибка обработки запроса"}), 500


if __name__ == '__main__':
    app.run(debug=True)

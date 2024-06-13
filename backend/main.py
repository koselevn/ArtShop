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
                select_category = f"CALL SearchPaintingsByCategory1('{categoryName}')"
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


@app.route('/select-popup', methods=['POST'])
def handle_post_request_5():
    try:
        data = request.get_json()

        id = data.get('id')

        try:
            Connection_DB()
            print('Conection')
            try:
                cursor = Connection_DB().cursor()
                select_category = f"select * from paintings JOIN authors ON paintings.autor_id = authors.autor_id where p_id = {id}"
                cursor.execute(select_category)
                rows = cursor.fetchall()
            finally:
                Connection_DB().close()
        except Exception as ex:
            print('No Conection')
            print(ex)

        return jsonify({"message": "Данные успешно приняты на бэкенде!", "painting": rows})

    except Exception as e:
        print("Ошибка обработки запроса:", str(e))
        return jsonify({"error": "Произошла ошибка обработки запроса"}), 500


@app.route('/insertOrder', methods=['POST'])
def handle_post_request6():
    try:
        data = request.get_json()

        p_id = data.get('p_id')
        client_full_name = data.get('client_full_name')
        client_phone_number = data.get('client_phone_number')
        client_country = data.get('client_country')
        client_city = data.get('client_city')
        client_area = data.get('client_area')
        client_address = data.get('client_address')
        client_apartment = data.get('client_apartment')
        client_index = data.get('client_index')

        print(data)
        try:
            connection = Connection_DB()
            print('Connection')
            try:
                cursor = connection.cursor()
                select_prod = f"CALL AddClient( '{client_full_name}', '{client_phone_number}', '{client_country}', '{client_city}', '{client_area}', '{client_address}', '{client_apartment}', '{client_index}' );"
                cursor.execute(select_prod)
                connection.commit()
            finally:
                print('And1')
            try:
                cursor = connection.cursor()
                select_prod = f"CALL AddOrder({p_id});"
                cursor.execute(select_prod)
                connection.commit()
            finally:
                print('And2')
        except Exception as ex:
            print('No Connection')
            print(ex)

            return jsonify({"message": "Данные успешно приняты на бэкенде!", "Result": "Good"})
    except Exception as e:
        print("Ошибка обработки запроса:", str(e))
        return jsonify({"error": "Произошла ошибка обработки запроса"}), 500

    return jsonify(message='Order inserted')  # Возвращаем JSON


if __name__ == '__main__':
    app.run(debug=True)

import pymysql

# MySQL bağlantısı kurun
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='2508',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

try:
    # Veritabanı oluşturun
    with connection.cursor() as cursor:
        cursor.execute('CREATE DATABASE IF NOT EXISTS elderco')

    # Değişiklikleri kaydedin
    connection.commit()

    print('Success')

finally:
    # Bağlantıyı kapatın
    connection.close()

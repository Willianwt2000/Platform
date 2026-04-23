import psycopg2

try:
    connection = psycopg2.connect(
        database="analysis",
        user="student",
        password="123456",
        host="127.0.0.1",
        port="5432"
    )

    cursor = connection.cursor()

    cursor.execute("""
        SELECT 
            varchar_column,
            LENGTH(varchar_column) AS varchar_length,

            char_column,
            LENGTH(char_column) AS char_length,

            text_column,
            LENGTH(text_column) AS text_length
        FROM char_data_types;
    """)

    records = cursor.fetchall()

    for row in records:
        print(row)

except Exception as e:
    print("Error:", e)

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals():
        connection.close()
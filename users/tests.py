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







# -- * Using the interval Data Type in Calculations

# SELECT
#     timestamp_column
#     interval_column,
# timestamp_column - interval_column AS new_date
# FROM date_time_types;



# CREATE TABLE  test_numbers (
#     number_one INT,
#     number_two INT
# )


# INSERT INTO test_numbers (
#     VALUES
#     (6,4)
# )

# SELECT number_one,number_two , number_one + number_two AS number_result FROM test_numbers


# SELECT timestamp_column, CAST(timestamp_column AS varchar(10))
# FROM date_time_types;


# SELECT numeric_column,
#     CAST(numeric_column AS integer),
#     CAST(numeric_column AS varchar(6))
# FROM number_data_types;


# SELECT CAST(char_column AS integer) FROM char_data_types;



# SELECT timestamp_column, CAST(timestamp_column AS varchar(10))
# FROM date_time_types;

# SELECT timestamp_column::varchar(10)
# FROM date_time_types;




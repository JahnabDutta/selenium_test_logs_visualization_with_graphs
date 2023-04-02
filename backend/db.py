import mysql.connector

def connect(host, user, password, database):
    return mysql.connector.connect(host=host, user=user, password=password, database=database)


def create_table(conn):
    cursor = conn.cursor()
    create_table_query = '''
       CREATE TABLE IF NOT EXISTS network_logs (
        id INT AUTO_INCREMENT PRIMARY KEY,
        timestamp DATETIME,
        url VARCHAR(500),
        method VARCHAR(10),
        status_code INT,
        content_type VARCHAR(50),
        request_headers TEXT,
        response_headers TEXT,
        request_body TEXT,
        response_body TEXT
    )
    '''
    cursor.execute(create_table_query)
    conn.commit()


def insert(conn, timestamp, url, method, status_code, content_type, request_headers, response_headers, request_body, response_body):
    cursor = conn.cursor()
    insert_query = '''
        INSERT INTO network_logs (timestamp, url, method, status_code, content_type, request_headers, response_headers, request_body, response_body)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    '''
    values = (
        timestamp,
        url,
        method,
        status_code,
        content_type,
        request_headers,
        response_headers,
        request_body,
        response_body
    )
    cursor.execute(insert_query, values)
    conn.commit()



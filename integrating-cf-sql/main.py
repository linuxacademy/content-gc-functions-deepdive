import sqlalchemy

connection_name = "[SQL_CONNECTION_NAME]"
table_name = "books"
table_field = "title"
table_field_value = "Rafe Rebelius and the Clash of the Genres"
db_name = "content"
db_user = "root"
db_password = "root"

driver_name = 'mysql+pymysql'
query_string = dict({"unix_socket": "/cloudsql/{}".format(connection_name)})

# If the type of your table_field value is a string, surround it with double quotes.

def insert(request):
    request_json = request.get_json()
    stmt = sqlalchemy.text('insert into {} ({}) values ("{}")'.format(table_name, table_field, table_field_value))
    
    db = sqlalchemy.create_engine(
      sqlalchemy.engine.url.URL(
        drivername=driver_name,
        username=db_user,
        password=db_password,
        database=db_name,
        query=query_string,
      ),
      pool_size=5,
      max_overflow=2,
      pool_timeout=30,
      pool_recycle=1800
    )
    try:
        with db.connect() as conn:
            conn.execute(stmt)
    except Exception as e:
        return 'Error: {}'.format(str(e))
    return 'ok'

import sqlite3


def sql_request(db: str, request: str) -> list:
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(request)
        response = cur.fetchall()
        conn.close()
        return response
    except sqlite3.Error as error:
        print(error)
        return None
    finally:
        conn.close()


def paginate(response: list) -> str:
    response = str(response)
    response = response.replace("), ", "), <br/>")
    return response


def filter_and(query_param: str) -> str:
    sql_statement = ''
    query_param = query_param.replace(":", " ")
    query_param = query_param.replace(";", " ")
    query_param = query_param.split()
    for i in range(0, len(query_param), 2):
        sql_statement += str(query_param[i].capitalize() + " = '" + query_param[i + 1] + "'")
        if i != len(query_param) - 2:
            sql_statement += str(' AND ')
    return sql_statement

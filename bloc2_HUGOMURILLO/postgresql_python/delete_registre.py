import connect

def delete_reg(nombre_cliente):
    conn = connect.connection_db()
    cursor = conn.cursor()

    sql_delete = '''
    DELETE FROM clientes
    WHERE nombre_cliente=%s
    '''

    cursor.execute(sql_delete, (nombre_cliente,))
    conn.commit()

    cursor.close()
    conn.close()

    return {"Delete successfully"}

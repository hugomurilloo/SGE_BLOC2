import connect

def update_reg(nombre_cliente, nuevo_telefono):
    conn = connect.connection_db()
    cursor = conn.cursor()

    sql_update ='''
    UPDATE clientes
    SET teléfono_cliente=%s
    WHERE nombre_cliente=%s
    '''

    cursor.execute(sql_update, (nuevo_telefono, nombre_cliente))
    conn.commit()

    cursor.close()
    conn.close()

    return {"Update successfully"}

# SGE_BLOC2
![alt text](image-1.png)

### Passos seguits:

1. **Configuració de la connexió**: El codi de la connexió es troba a `connect.py`. Allà es defineixen els detalls de la base de dades (usuari, contrasenya, nom de la base de dades, etc.).
2. **Crida a la funció de connexió**: A `main.py`, es crida a la funció `connection_db()` que establirà la connexió.
3. **Comprovació de l'èxit**: Si la connexió és exitosa, es mostra el missatge "Connexió establerta amb èxit!". Si no, el sistema mostrarà un error per indicar el problema.

## Com executar

1. Assegura't que tens PostgreSQL instal·lat i en funcionament.
2. Instal·la la llibreria `psycopg2` amb la comanda:
   ```bash
   pip install psycopg2
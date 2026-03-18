import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()
cursor.execute(
  """
  CREATE TABLE IF NOT EXISTS empleados(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre TEXT,
  cargo TEXT,
  salario REAL
  )
  """
)
conn.commit()
conn.close()
print("Base de datos creada correctamente")
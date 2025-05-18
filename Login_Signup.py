"""
Schema design for login
id primary key not null
email string
password string
"""




def AddUser( Email:str|None , Password:str|None )->bool:
  try:
    conn =sqlite3.connect("UserLogin.db")
    csr = conn.cursor()

    csr.execute('''
      CREATE TABLE IF NOT EXISTS  Users(
              Id INTEGER PRIMARY KEY AUTOINCREMENT,
              Email TEXT NOT NULL,
              Password TEXT NOT NULL
        )
    ''')
    csr.execute('''
            INSERT INTO  Users(Email,Password )
            VALUES (?, ?)
        ''', (Email, Password))
    conn.commit()

    conn.close()
    return True
  except Exception as e:
    print("Database error:", e)
    return False



import sqlite3

def Check_user(email: str | None, password: str | None) -> bool:
    try:
        conn = sqlite3.connect("UserLogin.db")
        csr = conn.cursor()


        csr.execute('''
            SELECT * FROM Users WHERE Email = ? AND Password = ?
        ''', (email, password))

        result = csr.fetchone()

        conn.close()

        # If a match is found, return True
        return result is not None

    except Exception as e:
        print("Database error:", e)
        return False

def Get_user_id(email: str) -> int | None:
  try:
    conn = sqlite3.connect("UserLogin.db")
    csr = conn.cursor()

    csr.execute("SELECT Id FROM Users WHERE email = ?", (email,))
    result = csr.fetchone()

    conn.close()

    return result[0] if result else None

  except Exception as e:
    print("DB error:", e)
    return None

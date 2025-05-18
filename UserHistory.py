"""

store history of chats mainly used on I_ver model

Send them to AI as a context of conversation

  for perfomance reasons i will only give it the last 10 conversation messages
  this will contain 5 last user quetions and last 5 ai response

"""


import sqlite3





def StoreConvo(user_id:int|None , User_messg:str|None , Ai_response:str|None):
  try:

    conn =sqlite3.connect("Convos.db")
    csr = conn.cursor()

    csr.execute('''
      CREATE TABLE IF NOT EXISTS  Convo(
              Id INTEGER PRIMARY KEY AUTOINCREMENT,
              User_id INTEGER NOT NULL,
              U_Messg TEXT NOT NULL,
              AI_res TEXT NOT NULL
        )
    ''')
    csr.execute('''
            INSERT INTO  Convo(User_id,U_Messg,AI_res )
            VALUES (?, ?, ?)
        ''', (user_id, User_messg,Ai_response))
    conn.commit()

    conn.close()
    return True
  except Exception as e:
    print("Database error:", e)
    return False


def GiveContext(userId:int|None,ContextLen:int= 10 )->list:
  """
  context len means the ammount of messge you want to give to ai as
  a context this will contain both ai and user response and queries
  """
  try:
    conn = sqlite3.connect("Convos.db")
    csr = conn.cursor()

    csr.execute("SELECT U_Messg, AI_res FROM Convo WHERE User_id = ?", (userId,))
    conversations = csr.fetchall()

    conn.close()

    return conversations[-ContextLen:]

  except Exception as e:
    print("Database fetch error:", e)
    return []

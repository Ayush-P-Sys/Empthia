import ollama
import sqlite3

def Store(UserM:str , AiRes:str , UserId:int)-> bool:
    try:
        conn = sqlite3.connect("Convos.db")
        csr = conn.cursor()
        csr.execute('''
      CREATE TABLE IF NOT EXISTS  Convo(
              Id INTEGER PRIMARY KEY AUTOINCREMENT,
              User TEXT NOT NULL,
              Aires TEXT NOT NULL,
              userId INTEGER
        )
    ''')
        csr.execute('''
            INSERT INTO  Convo(User, Aires, UserId )
            VALUES (?, ? , ?)
        ''', (UserM, AiRes, UserId))
        conn.commit()

        conn.close()
        return True

    except Exception as e:
        print("Db error ",e)
        return False


def Retrieve(UserId: int, limit: int = 5):
    try:
        conn = sqlite3.connect("Convos.db")
        csr = conn.cursor()
        csr.execute('''
            SELECT User, Aires FROM Convo
            WHERE UserId = ?
            ORDER BY Id DESC
            LIMIT ?
        ''', (UserId, limit))
        rows = csr.fetchall()
        conn.close()
        # Reverse to keep chronological order
        return rows[::-1]
    except Exception as e:
        print("Db error (retrieve):", e)
        return []


def BuildPrompt(memory: list, new_user_message: str) -> str:
    prompt = "### Conversation History:\n"
    for user, ai in memory:
        prompt += f"User: {user}\nAI: {ai}\n"
    prompt += "\n### New Message:\n"
    prompt += f"User: {new_user_message}\nAI:"
    return prompt

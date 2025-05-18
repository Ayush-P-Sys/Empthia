import ollama
from UserHistory import *


def Model_Reply(userId: int | None , ConLen:int , Model_Name: str = "caspian:latest", UserM: str = "") -> str:
  messages = []

  if Model_Name == "I_ver_1:latest" and userId is not None:

      history = GiveContext(userId, ConLen)

      for user_msg, ai_msg in history:
          messages.append({"role": "user", "content": user_msg})
          messages.append({"role": "assistant", "content": ai_msg})


  messages.append({"role": "user", "content": UserM})

  # testing
  print("\n\n\n\n\n")
  print(messages[:])

  # 4. Get AI response from Ollama
  try:
      response = ollama.chat(model=Model_Name, messages=messages)
      print(response)
      ai_reply = response['message']['content']  # assuming ollama gives a dict response
  except Exception as e:
      print("Ollama Error:", e)
      return "Error getting response from model."

  # 5. Save conversation if it's "I_ver_1"
  if Model_Name == "I_ver_1:latest" and userId is not None:
      StoreConvo(userId, UserM, ai_reply)

  # 6. Return AI reply
  return ai_reply

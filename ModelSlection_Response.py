import ollama
from UserHistory import *



def AIRes(Mssg , Mname):

  response = ollama.chat(model= Mname, messages=[{
      "role": "user",
      "content": Mssg
  }])

  return response['message']['content']


def ModelSel(userId:int|None , Umssg:str ,Clen:int , Mname:str = "caspian:latest"):

  if Mname == "I_ver_1:latest" and userId is not None:
    history = Retrieve(userId, Clen)
    FinalPrompt = BuildPrompt(history , Umssg)
    res = AIRes(FinalPrompt,Mname)
    Store(Umssg,res,userId)
    return res
  else:
    res = AIRes(Umssg,Mname)
    return res

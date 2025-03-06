from flask import Flask ,request, url_for, render_template


import ollama

app = Flask(__name__ ,template_folder = 'template/')

@app.route("/")
def Home():
    return render_template("Home.html")




@app.route("/ask" , methods = ["Post"])
def GetQuery():

    q = request.form.get("query")

    response = ollama.chat(model="caspian:latest", stream=False, messages=[{"role": "user", "content": q}])
    ai_replay = response["message"]["content"]
    return f' AI reply  {ai_replay}'

if __name__ == "__main__":
    app.run(debug = True)

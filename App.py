from flask import Flask, render_template, request, jsonify,Response, session ,redirect,url_for
import ollama
from Login_Signup import *

app = Flask(__name__, template_folder="template/")
app.secret_key = "1140a4ffefc25f141377c9f38aac8483"

@app.route("/")
def index():
    return render_template("Main.html")


#Signup Route

@app.route('/SignUp.html')
def SignUp():
   return render_template('SignUp.html')


@app.route("/SignUp", methods=["POST"])
def Add_User():
  try:
    data = request.get_json()
    Uemail = data.get("email")
    Upass = data.get("pass")

    # Simulated AddUser function
    Uadd = AddUser(Uemail, Upass)

    if Uadd:
      return { "success": True, "redirect": "/Login.html", "message": "Account created Sucessfully   Welcome!" }
    else:
        return jsonify({"error": "Failed to upload to database."}), 500
  except Exception as e:
    return jsonify({"error": str(e)}), 500



#Login Route

@app.route('/Login.html')
def LogIn():
  if 'user' in session:
    return redirect(url_for('index'))
  return render_template('Login.html')


@app.route("/logout")
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))


@app.route("/Login", methods=["POST"])
def Check():
  try:
    data = request.get_json()
    Uemail = data.get("email")
    Upass = data.get("pass")

    # Simulated AddUser function
    IsUser = Check_user(Uemail, Upass)

    if IsUser:
        session['user'] = Uemail
        return { "success": True, "redirect": "/", "message": "Welcome!" }

    else:
        return jsonify({"error": "Email or password incorrect."}), 500
  except Exception as e:
    return jsonify({"error": str(e)}), 500



@app.route("/ask2")
def ask_page():
  if 'user' not in session:
    return redirect(url_for('LogIn'))

  return render_template("ask2.html")


@app.route("/ask2", methods=["POST"])
def ask():
    try:
        data = request.get_json()  # Receive JSON data
        user_input = data.get("message", "")
        model_name = data.get("model", "caspian:latest")  # Default model if not provided

        if not user_input.strip():
            return jsonify({"error": "Message cannot be empty"}), 400

        response = ollama.chat(model=model_name, messages=[{"role": "user", "content": user_input}])
        return jsonify({"response": response["message"]["content"]})  # Send JSON response

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=5000)

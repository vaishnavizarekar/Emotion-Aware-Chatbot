from flask import Flask, render_template, request
from chatbot import get_bot_response, update_q_table

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  # make sure index.html exists in /templates folder

@app.route("/get")
def get_response():
    user_input = request.args.get('msg')
    if "update_q_table" in user_input:
        feedback = user_input.replace("update_q_table(", "").replace(")", "")
        update_q_table(feedback)
        return "Thanks for the feedback!"
    return get_bot_response(user_input)

@app.route("/admin")
def admin_dashboard():
    try:
        with open("q_table_log.txt", "r") as file:
            logs = file.readlines()
        return "<h3>Recent Feedback Logs:</h3><br>" + "<br>".join(logs[-50:])
    except FileNotFoundError:
        return "No logs found yet."
    
if __name__ == "__main__":
    app.run(debug=True)

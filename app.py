from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

def get_top_output():
    """Returns the output of the 'top' command"""
    try:
        top_output = subprocess.check_output("top -b -n 1 | head -10", shell=True).decode("utf-8")
    except Exception as e:
        top_output = str(e)
    return top_output

@app.route('/htop')
def htop():
    name = "Shubham Srivastava"
    username = os.getenv("USER", "unknown")  # ✅ Fixed username retrieval
    ist_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S IST')
    top_output = get_top_output().replace("\n", "<br>")

    return f"""
    <h1>System Info</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {ist_time}</p>
    <p><strong>Top Output:</strong></p>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

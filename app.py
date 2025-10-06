from flask import Flask, render_template_string
import subprocess

app = Flask(__name__)

# Giao diện web đơn giản (HTML)
HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>🐍 Snake Game Online</title>
    <style>
        body { text-align: center; font-family: Arial; background: #222; color: #fff; }
        h1 { margin-top: 50px; }
        button {
            background-color: #4CAF50;
            color: white;
            padding: 15px 30px;
            margin-top: 20px;
            border: none;
            border-radius: 5px;
            font-size: 18px;
            cursor: pointer;
        }
        button:hover { background-color: #45a049; }
    </style>
</head>
<body>
    <h1>🐍 Snake Game Online (Flask + Docker + AWS)</h1>
    <p>Click to run the game inside the server (for demo)</p>
    <form action="/run" method="post">
        <button type="submit">🎮 Run Game</button>
    </form>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML)

@app.route('/run', methods=['POST'])
def run_game():
    # Chạy game trên server (chỉ hiển thị log)
    subprocess.Popen(["python3", "snake_game.py"])
    return "<h2>Game is running on the server! Check Docker logs for output.</h2>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

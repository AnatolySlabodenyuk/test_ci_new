from flask import Flask, jsonify
import random

app = Flask(__name__)

FUNNY_NICKNAMES = [
    "Котлета Убийца",
    "Мозгоклюй 3000",
    "Бульбозавр",
    "Гроза Принтеров",
    "Властелин Пельменей",
    "Байт Сбежавший",
    "Фрилансер в Панике",
    "Капитан Очевидность",
    "Программист на Скольких Языках?",
    "Шаман Багов"
]

@app.route("/nicknames")
def get_nickname():
    nickname = random.choice(FUNNY_NICKNAMES)
    return jsonify({"nickname": nickname})

if __name__ == '__main__':
    app.run(host='0.0.0.0')

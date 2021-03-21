from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/armstrong/<int:num>')
def armstrong(num):
    # num = int(input("Enter a number: "))
    sum = 0
    order = len(str(num))
    temp = num
    while (num>0):
        digit = num % 10
        sum += digit ** 3
        num //= 10

    if (sum == temp) :
        print(f"{num} is an Armstrong number")
        result = {
            "Number": num,
            "Armstrong": True,
            "Server Ip": "125:522:253:121"
        }
    else:
        print("is not an Armstrong number")
        result = {
            "Number": num,
            "Armstrong": False,
            "Server Ip": "125:522:253:121"
        }

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)

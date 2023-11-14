from flask import Flask, request

app = Flask(__name__)
@app.route('/alkuluku/<number>')
def prime(number):
    isprime = True
    num = int(number)
    for j in range(2, num):
        if num % j == 0 and (j != 1 or j != num):
            isprime = False
            break
    return {"Number" : number, "isPrime": isprime}

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
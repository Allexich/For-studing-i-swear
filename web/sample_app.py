#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# A very simple Flask Hello World app for you to get started with...

import flask
from flask import Flask, request
import copy  # to copy list of lists

app = Flask(__name__, static_folder="static", static_url_path="", template_folder="templates")

def gauss(a, b):
    a = copy.deepcopy(a)  # to copy internal lists too
    b = b.copy()
    N = len(a)
    
    def forward():
        for i in range(N):
            for j in range(i+1, N):
                t = (a[j][i] / a[i][i])
                for k in range(N):
                    a[j][k] -= a[i][k] * t
                b[j] -= b[i] * t


    def backward():
        x = [0] * len(b)
        for i in range(N, 0, -1):
            x[i-1] = b[i-1]
            for j in range(i, N):
                x[i-1] -= a[i-1][j] * x[j]
            x[i-1] /= a[i-1][i-1]
        return x

    forward()
    return backward()


@app.route('/', methods = ['GET'])
def hello_name():
    if request.method == 'GET':
        A= [[request.args.get('a11'), request.args.get('a12'), request.args.get('a13')],
                [request.args.get('a21'), request.args.get('a22'), request.args.get('a23')],
                [request.args.get('a31'), request.args.get('a32'), request.args.get('a33')]]
        B=[request.args.get('b1'), request.args.get('b2'), request.args.get('b3')]

    
    if None in B or True in [None in i for i in A] :
        res = "Не введены параметры"
    else:
        A = [list(map(float, i)) for i in A]
        B = list(map(float, B))
        C = gauss(A, B)
        C = list(map(str, C))
        res = "x = " + C[0] + ", y = " + C[1] + ", z = " + C[2]

    return flask.render_template(
        'gauss.html',
        name=res,
    )

if __name__ == '__main__':
   app.run(debug = True)

#!/usr/bin/env python3
from sanic import Sanic
from sanic.response import json
import numpy as np
np.set_printoptions(precision=15)

from sanic.log import logger
app = Sanic(log_config=None)

import matplotlib.pyplot as plt

def plot_data(data):
    data = ([*zip(*data)])
    x_plot = data[0]
    a_plot = data[1]
    b_plot = data[2]
    e_plot = data[3]
    e0_plot = data[4]
    plt.subplot(221)
    plt.plot(x_plot, a_plot)
    plt.subplot(222)
    plt.plot(x_plot, b_plot)
    plt.subplot(223)
    plt.plot(x_plot, e_plot)
    plt.subplot(224)
    plt.plot(x_plot, e0_plot)
    plt.savefig('/app/static/prolog.png')

def calc_prolog(x):
    a = np.float64(0.0)
    b = np.float64(0.0)
    e = np.float64(0.0)
    e0 = np.finfo(np.float64).max
    x = np.float64(x)
    a = (x + 1.0) * 0.5
    b = np.sqrt(x)
    e = np.abs(a - b)
    i = 0
    data = []
    while e < e0:
        data.append([i, a, b, e, e0])
        i = i + 1
        a = 0.5 * (a + b)
        b = np.sqrt(a * b)
        e0 = e
        e = np.abs(a - b)
    plot_data(data)
    return (x - 1.0) / a

@app.route('/prolog')
async def prolog(request):
    x = float(request.args["x"][0])
    y = calc_prolog(x)
    return json({"args": request.args, "answer": np.float64(y)})

@app.route('/delete')
async def prolog(request):
    plt.subplot(111)
    plt.plot([1],[1])
    plt.savefig('/app/static/prolog.png')
    return json({"success": "True"})

# Serves files from the static folder to the URL /static
app.static('/static', './static')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)






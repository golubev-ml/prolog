#!/usr/bin/env python3
from sanic import Sanic
from sanic.response import json
import numpy as np
np.set_printoptions(precision=15)

from sanic.log import logger
app = Sanic(log_config=None)

import matplotlib.pyplot as plt

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
    logger.info(data)
    logger.info([*zip(*data)])
    plt.plot([*zip(*data)])
    plt.savefig('/app/static/prolog.png')
    return (x - 1.0) / a


@app.route('/prolog')
async def prolog(request):
    x = float(request.args["x"][0])
    y = calc_prolog(x)
    return json({"args": request.args, "answer": np.float64(y)})

# Serves files from the static folder to the URL /static
app.static('/static', './static')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)






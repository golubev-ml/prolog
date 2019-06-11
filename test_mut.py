import requests
import math
import random
import pytest

@pytest.mark.parametrize('x_param', [random.uniform(15, 20) for i in range(13)])
def test_prolog(x_param):
   resp = requests.get("http://prolog:8000/prolog?x={}".format(x_param))
   assert resp.status_code == 200
   assert float(resp.json()["answer"]) - math.log(x_param) < 1e-7

import requests
import random

def heartrate(d):
    hrs = [random.randrange(80, d) + d/100 for d in range(81, 120, 2)]
    time = [d for d in range(len(hrs))]
    return hrs, time


def insulin_val(d):
    insulin_val = [random.randrange(d) + d/100 for d in range(2, 30, 2)]
    time = [d for d in range(len(insulin_val))]
    return insulin_val, time


def carbs_taken(d):
    carb_val = s = [random.randrange(10+d) + d/100 for d in range(2, 30, 2)]
    time = [d for d in range(len(carb_val))]
    return carb_val, time

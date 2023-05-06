#!/usr/bin/python3

def weight_average(my_list=[]):
    return (sum([i[0] * i[1] for i in my_list]) / sum([j[1] for j in my_list]))

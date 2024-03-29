#!/usr/bin/python3

def add(x, y):
    """Add function"""
    return x + y

def subtract(x, y):
    """Subtract function"""
    return x - y

def multiply(x, y):
    """Multiply function"""
    return x * y

def divide(x, y):
    """Multiply function"""
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

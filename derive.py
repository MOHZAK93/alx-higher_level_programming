#!/usr/bin/python3

import base
class Emp(base.Person):
    def Print(self):
        print("Emp class called")

Emp_details = Emp("Mark", 104)

Emp_details.Display()

Emp_details.Print()

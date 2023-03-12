"""
In an attempt to make it easily portable to other GUI modules, like PyQt.
"""


from calcFunctions import *



calc = Calculator(lang="PT")

def addingNumber(number, targetUI):
    calc.addNumber(number)
    targetUI.calcscreen.setText(calc.showDisplay())

def addingOperation(operation, targetUI):
    calc.addOperation(operation)
    targetUI.calcscreen.setText(calc.showDisplay())

def inverting(targetUI):
    calc.addInversor()
    targetUI.calcscreen.setText(calc.showDisplay())

def erasing(targetUI):
    calc.erase()
    targetUI.calcscreen.setText(calc.showDisplay())

def clearing(targetUI):
    calc.clearAll()
    targetUI.calcscreen.setText(calc.showDisplay())

def calculate(targetUI):

    calc.calculate()
    targetUI.calcscreen.setText(calc.showDisplay())

def addingComma(targetUI):
    calc.addComma()
    targetUI.calcscreen.setText(calc.showDisplay())
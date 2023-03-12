from typing import Literal
from utils import isnumber, popString


class Calculator():

    possibleOperators = "+-Xx÷/"

    def __init__(self, lang="ENG"):
        self.display = []
        self.multidivTracker = {}

        self.errorMessageZero = "ERROR: Division by zero"

        if lang.upper() == "PT":
            self.errorMessageZero = "ERRO: Divisão por zero"


    def addNumber(self, number):
        number = str(number)

        if isnumber(number):
            if not self.display:
                self.display.append(number)

            else:
                lastItem = self.display[-1]

                if lastItem in self.possibleOperators:
                    self.display.append(number)

                elif isnumber(lastItem):
                    self.display[-1] += number

                else:
                    raise Exception("Fallback error")

        else:
            raise Exception("addNumber: Provided parameter doesn't seem to be a valid number")


    def addOperation(self, operator: Literal["+", "-", "x","÷", "/"]):
        operator = str(operator).lower()

        if operator == "/":
            operator = "÷"
        if self.display:
            lastItem = self.display[-1]

            if lastItem in self.possibleOperators:
                self.display[-1] = operator

                if lastItem in "x÷": self.multidivTracker.popitem()
                if operator in "x÷": self.multidivTracker[len(self.display) - 1] = operator

            else:
                self.display.append(operator)
                if operator in "x÷": self.multidivTracker[len(self.display) - 1] = operator


    def addInversor(self):
        "Technically the inverse of a number is not the negative one, but ok."

        if self.display:
            lastItem = self.display[-1]

            if isnumber(lastItem) and not lastItem == "0":
                inversed = str(float(lastItem) * -1)
                if inversed[-2:] == ".0": inversed = inversed.replace(".0", "")
                self.display[-1] = inversed


    def addParentheses(self):
        pass


    def addComma(self):
        if self.display:
            lastItem = self.display[-1]

            if isnumber(lastItem) and "." not in lastItem:
                self.display[-1] += "."


    def erase(self):
        if self.display:
            lastItem = self.display[-1]

            if len(lastItem) == 1:
                self.display.pop()
                if lastItem in "x÷":
                    self.multidivTracker.popitem()

            else:
                if lastItem.isnumeric():
                    self.display[-1] = popString(self.display[-1])

                else:
                    self.display[-1] = popString(self.display[-1])
                    if self.display[-1] == "-":
                        self.display.pop()


    def clearAll(self):
        self.display.clear()


    def showDisplay(self):
        finalDisplay = ("".join(self.display)).replace(".", ",")

        if self.errorMessageZero in self.display:
            self.display.clear()
        return finalDisplay


    def calculate(self):
        # I decided to start commenting.
        # Here it checks if the equation is incomplete.
        # If so, it removes the operator from the end.
        if self.display[-1] in self.possibleOperators:
            if self.display[-1] in "x÷":
                # and removes it from the tracker.
                self.multidivTracker.popitem()
            self.display.pop()

        # This tracker fixes the position of the other tracker.
        # As 2 items are removed from the display every "round"
        # the tracker becomes useless if the positions are not fixed.
        trackerRemoved = 0
        for k, v in self.multidivTracker.items():
            k -= trackerRemoved

            previousNumber = float(self.display[k - 1])
            nextNumber = float(self.display[k + 1])


            if v == "x":
                self.display[k] = str(previousNumber * nextNumber)

            elif v == "÷":
                if previousNumber == 0 or nextNumber == 0:
                    self.display.clear()
                    self.display.append(self.errorMessageZero)
                    break
                else:
                    self.display[k] = str(previousNumber / nextNumber )

            else:
                # Just in case...
                raise Exception("Fallback error. Something happened. Good luck!")

            del self.display[k - 1]
            del self.display[k]
            trackerRemoved += 2
        self.multidivTracker.clear()

        # Now it sums and subtracts, just like above.
        plusMinusTrackerRemoved = 0
        for operatorPos in range(1, len(self.display), 2):
            operatorPos -= plusMinusTrackerRemoved

            previousNumber = float(self.display[operatorPos - 1])
            nextNumber = float(self.display[operatorPos + 1])

            if self.display[operatorPos] == "+":
                self.display[operatorPos] = str(
                    previousNumber + nextNumber)

            elif self.display[operatorPos] == "-":
                self.display[operatorPos] = str(
                    previousNumber - nextNumber)

            else:
                # Just in case...
                raise Exception("Fallback error. Something happened. Good luck!")

            del self.display[operatorPos - 1]
            del self.display[operatorPos]
            plusMinusTrackerRemoved += 2

        if self.display[-1][-2:] == ".0": self.display[-1] = self.display[-1].replace(".0", "")


    def mathAccordingCalculation(self, expression: list) -> str:
        # Big name yes, uhum.
        # It's not been used, I know.
        # This one should replace the calculate method, being more maintainable
        # and support parentheses. I'm not planning to add parentheses support for
        # the moment, so it will stay in here just in case.

        if expression[-1] in self.possibleOperators:
            expression.pop()

        trackerMulDiv = {}
        for position, value in enumerate(expression):
            if value in "÷x":
                trackerMulDiv[position] = value

        removedTrackers = 0
        for key, value in trackerMulDiv.items():
            key -= removedTrackers

            if value == "x":
                expression[key] = (float(expression[key - 1]) * float(expression[key + 1]))
            elif value == "÷":
                expression[key] = (float(expression[key - 1]) / float(expression[key + 1]))
            else:
                raise Exception("Fallback Error. Something went wrong. Good luck!")

            del expression[key - 1]
            del expression[key]
            removedTrackers += 1
        trackerMulDiv.clear()

        removedTrackers = 0
        for operatorPos in range(1, len(expression), 2):
            operatorPos -= removedTrackers
            if expression[operatorPos] == "+":
                expression[operatorPos] = str(float(expression[operatorPos - 1]) + float(expression[operatorPos + 1]))

            elif expression[operatorPos] == "-":
                expression[operatorPos] = str(float(expression[operatorPos - 1]) - float(expression[operatorPos + 1]))

            else:
                # Just in case...
                raise Exception("Fallback error. Something happened. Good luck!")

            del expression[operatorPos - 1]
            del expression[operatorPos]
            removedTrackers += 2

        return str(expression)

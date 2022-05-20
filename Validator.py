from Formatter import Formatter


class Validator:
    def __init__(self):
        self.operations = ['+', '-', '*', '/', '^']
        self.empty_cell = "Please Fill the Empty Cells."
        self.max_less_min = "The Maximum Value of X must Be Greater than The Minimum Value of X"
        self.equation_format = "The Equation Must be in X format"
        self.must_digit = "The Values of X Must be an Integer"

    @staticmethod
    def __validate_ranges(self, min_value, max_value):
        temp_min = Formatter.reformat_min_max(min_value)
        temp_max = Formatter.reformat_min_max(max_value)
        if len(min_value) == 0 or len(max_value) == 0:
            return self.empty_cell
        if not (temp_min.isdigit()) or not (temp_max.isdigit()):
            return self.must_digit
        if int(min_value) >= int(max_value):
            return self.max_less_min
        return True

    @staticmethod
    def __validate_equation(self, equation):
        if len(equation) == 0:
            return self.empty_cell
        else:
            for i in range(len(equation)):
                if not (str(equation[i]).isdigit()) and equation[i] not in self.operations and equation[i] != 'x':
                    return self.equation_format
        return True

    def validate(self, equation, min_value, max_value):
        status = self.__validate_ranges(self, min_value, max_value)
        if type(status) == bool:
            return self.__validate_equation(self, equation)
        return status

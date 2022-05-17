class Formatter:

    @staticmethod
    def reformat_equation(equation):
        equation = equation.replace(' ', '')
        equation = equation.replace('^', "**")
        equation = equation.replace('X', 'x')
        return equation

    @staticmethod
    def reformat_min_max(value):
        temp_value = value.lstrip(' ')
        temp_value = temp_value.lstrip('-')
        return temp_value

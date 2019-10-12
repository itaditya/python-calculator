import argparse
from Calculator import Calculator

method_list = [func for func in dir(Calculator) if callable(getattr(Calculator, func)) and not func.startswith("__")]
allowed_methods_help = '*' + '* or *'.join(method_list) + '*'

parser = argparse.ArgumentParser(description='Calculate ' + allowed_methods_help + ' of the numbers you provide')

parser.add_argument('operation', type=str, help='One of the following operations: ' + allowed_methods_help)
parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')

args = parser.parse_args()
calc = Calculator()

def calculate(operation, integers):
  if (operation == 'sum'):
    return calc.sum(integers)
  if (operation == 'multiply'):
    return calc.multiply(integers)
  if (operation == 'average'):
    return calc.average(integers)
  if (operation == 'meter_to cm'):
    return calc.mettocm(integers)
  if (operation == 'cm to meter'):
    return calc.cmtomet(integers)
  return 0

result = calculate(args.operation, args.integers)
print('------')
print(result)
print('------')

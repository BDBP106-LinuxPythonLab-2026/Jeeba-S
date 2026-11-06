from utils import math_utils
from utils import string_utils

print("addition",math_utils.add(34,45))
print("subtraction",math_utils.sub(34,45))
print("multiplication",math_utils.mul(34,45))
print("division",math_utils.div(34,45))
print("remainder",math_utils.rem(34,45))

print("convert to upper",string_utils.lower_to_upper("bdbh"))
print("convert to lower",string_utils.upper_to_lower("BDBH"))
print("concatenate",string_utils.concatenate("BDBH",str(101)))
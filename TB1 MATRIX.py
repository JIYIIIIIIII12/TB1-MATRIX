import math
import os
import random
import re
import sys 

import re

with open('matrix.txt', 'r') as file:
     lines = file.readlines()

first_multiple_input = lines[0].rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

matrix = lines[1:]
encoded_list = list(zip(*matrix))
encoded_string = "".join([''.join(item) for item in encoded_list])
decoded = r'\b[^a-zA-Z0-9]+\b'
print(re.sub(decoded,r' ',encoded_string))
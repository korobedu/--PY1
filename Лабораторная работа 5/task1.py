# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint

list_nums = [{'bin': bin(num), 'dec': num, 'oct': oct(num), 'hex': hex(num)}
             for num in range(16)]
pprint(list_nums)

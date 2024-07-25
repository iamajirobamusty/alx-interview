#!/usr/bin/python3

"""
Method to check if a data utf-8 validated
"""

def def validUTF8(data):
 """_summary_

    Args:
            data (list[int]): a list of integers
  """

  #loop through the data to be validated
  for i in data:
    check = bin(i).lstrip('0b')
    if check[1:] == "00000000":
      return False
    return True

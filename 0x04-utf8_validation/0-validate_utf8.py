#!/usr/bin/python3

"""
Method to check if a data utf-8 validated
"""

def def validUTF8(data):
  """
  function to receive data as parameter
  """
  for i in data:
    """
    loop through the data to be validated
    """
    check = bin(i).lstrip('0b')
    if check[1:] == "00000000":
      return False
    return True

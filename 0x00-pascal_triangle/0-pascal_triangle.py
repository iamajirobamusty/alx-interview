#!/usr/bin/python3
""" A script to create A Pascal Triangle """


def create_list(no, prev, const):
  """ return a list integers 
    
  
  """
  my_list = []
  if const > 2:
    my_list = [1] + [0] * (no -2 ) + [1]
    itr = 1
    my_no = 1
    while itr < (len(my_list) - 1 ):
      time = prev[no-2]
      my_list[itr] = time[itr-1] + time[itr]
      my_no += 1
      itr += 1
    return my_list
  elif const == 1:
    my_list.append(1)
    return my_list
  elif const == 2:
    my_list = [1,1]
    return my_list

def pascal_triangle(n):
  """ retrun a list of lists """
  itr = 1
  const = 1
  comp = []
  while n:
    result = create_list(itr, comp, cosnt)
    comp.append(result)
    const += 1
    itr += 1
    n -= 1
  return comp

def solution(array):
  print(array[-1])
  if array == []:
    return 1
  else:
    if len(array) < 3:
      return  array[0] - 1
    else:
      array.sort() 
      for i in range(0, len(array) - 1):
        if array[0] > 1:
          return 1
        elif array[-1] != len(array) + 1:
          return len(array) + 1
        else:
          if (array[i] + 1 != array[i+1]):
            return array[i] + 1

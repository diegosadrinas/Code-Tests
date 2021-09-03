def partition(array, number):
  return (sum(array[:number]))


def solution(array):
  minimum = abs(sum(array))
  for i in range(1, len(array)):
    absolute_diff = abs(partition(array, i) - sum(array[i:]))
    if absolute_diff < minimum:
      minimum = absolute_diff
  return abs(minimum)

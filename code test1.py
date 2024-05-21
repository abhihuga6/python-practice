from typing import *

def longestsuccessiveElements(a : list[int]):
  a_set=set(s)
  higest_sequence=0
  for i in a_set:
      if i-1 not in a_set:
          count=0
          num=i
          while num in a_set:
              count+=1
              num+=1
          if higest_sequence<count:
              higest_sequence+count
  return higest_sequence

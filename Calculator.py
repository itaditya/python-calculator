import math
class Calculator:
  
  def sum(self, nums):
    val = 0
    for n in nums:
      val += n
    result = val
    return result
  def multiply(self, nums):
    val = 1
    for n in nums:
      val *= n
    result = val
    return result
  def average(self, nums):
    val = 0
    l = len(nums)
    nums_sum = self.sum(nums)
    result = nums_sum / l
    return result
  def tangent(self,nums):
    result = []
    for i in nums:
        result.append(math.tan(i))
    return result
 def cosine(self,nums):
    result = []
    for i in nums:
        result.append(math.cos(i))
    return result


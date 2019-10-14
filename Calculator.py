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

  def sin(self,nums):
    result = list(map(math.sin,nums))
    return result

  def m_to_cm(self, nums):
  	m_to_cm_unit = 100
  	result = list(map(lambda x:m_to_cm_unit*x, nums))
  	return result


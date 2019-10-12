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
  def mettocm(self, nums):
    conv = 100
    result = nums*conv
    return result
  def mettocm(self, nums):
    conv = 1/100
    result = nums*conv
    return result

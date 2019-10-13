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
  def cm_to_metres(self, nums):
    results_list = []
    for i in nums:
      metres = i/100
      results_list.append(str(i) + "cm = " + str(metres) + "m")

    return(results_list)

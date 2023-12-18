def convert_to_indian_currency(num):
  """
  Converts an integer to Indian currency notation without using currency libraries.

  Args:
    num: An integer representing the amount.

  Returns:
    A string representing the amount in Indian currency notation.
  """
  num_str = str(num)
  num_len = len(num_str)
  if num_len <= 3:
    return num_str
  else:
    groups = []
    while num_len > 0:
      groups.append(num_str[-3:])
      num_str = num_str[:-3]
      num_len -= 3
    groups.reverse()
    return ",".join(groups)

# Example usage
amount = 504678
indian_currency_format = convert_to_indian_currency(amount)
print(f"Input: {amount}")
print(f"Output: {indian_currency_format}")

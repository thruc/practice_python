import re


def reg_check(target: str, pattern: str) -> bool:
  result = re.match(pattern, target)

  if result:
    return True

  return False


if __name__ == "__main__":
  import sys
  args = sys.argv
  target = args[1]
  pattern = args[2]
  
  print(reg_check(target, pattern))







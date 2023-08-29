def st(str):
  if len(str) < 2:
    return ''

  return str[0:2] + str[-2:]

print(st('SRIMAN'))
print(st('SR'))
print(st('S'))

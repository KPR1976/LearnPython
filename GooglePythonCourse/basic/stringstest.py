def front_back(a, b):
  # +++your code here+++
  alen = len(a)
  blen = len(b)

  if alen % 2 == 0:
      c = a[:alen / 2]
      d = a[alen / 2:]
  else:
      c = a[:alen / 2 + 1]
      d = a[alen / 2 + 1:]

  if blen % 2 == 0:
      c = c + b[:blen / 2]
      d = d + b[blen / 2:]
  else:
      c = c + b[:blen / 2 + 1]
      d = d + b[blen / 2 + 1:]


  return c, d


print(front_back('abcde', 'xy'))

def hype(n):
    lst=n.split('-')
    lst.sort()
    return '-'.join(lst)
print(hype("Here-is-the-Great-Wall-of-China"))

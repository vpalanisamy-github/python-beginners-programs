def interleave(s1, s2):
    return "".join(["".join(i) for i in (zip(s1,s2))])


print(interleave("hi", 'ls'))
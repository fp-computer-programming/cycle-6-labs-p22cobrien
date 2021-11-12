# Author: CMOB 11/12/2021

subject = ["math", "history", "science"]
print(subject)

subject.append("french")
print(subject)

print(subject.index("science"))

subject.sort()
print(subject)

c_subject = subject.copy()

c_subject.sort(reverse=True)
print(c_subject)

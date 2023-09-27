s = []
a = "mango_tREE"
b = list(a.split("_"))
print(b)
for i in range(len(b)):
    if b[i].islower():
        s.append(b[i])
if len(s)==len(b):
    print("True",+len(b))
else:
    print(False)
    
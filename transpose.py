def transpose(listofstrings):
    return [" ".join(t) for t in (zip(*[s.split() for s in listofstrings]))]



print(transpose(['abc def ghi', 'jkl mno pqr', 'stu vw xyz']))

array = ['abc def ghi', 'jkl mno pqr', 'stu vw xyz']
output = []
for i in range(min(len(x.split()) for x in array)):
    temp = []
    for eachstring in array:

        temp.append(eachstring.split(" ")[i])
    output.append(" ".join(temp))
print(output)

transposed_array = []
modified_array = [x.split() for x in array]
print(modified_array)
while modified_array:
    temp = []
    for x in modified_array:
        if x:
            print(x[0])
            temp.append(x[0])
            x.remove(x[0])
        else:
            modified_array.remove(x)
    if temp:
        transposed_array.append(" ".join(temp))
print(transposed_array)


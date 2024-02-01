def neg_or_pos(number):
    if number < 0:
        negatives.append(number)
    elif number > 0:
        positives.append(number)

negatives = []
positives = []
numbers = [int(x) for x in input().split()]
for number in numbers:
    neg_or_pos(number)

print(sum(negatives))
print(sum(positives))

if sum(positives) > abs(sum(negatives)):
    print('The positives are stronger than the negatives')
else:
    print('The negatives are stronger than the positives')
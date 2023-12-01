electrons = int(input())
final_list = []
for i in range(1, electrons):
    shell = i ** 2 * 2
    if electrons < shell:
        final_list.append(electrons)
        break
    electrons -= shell
    final_list.append(shell)
    if electrons == 0:
        break
print(final_list)





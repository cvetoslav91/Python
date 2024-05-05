from collections import deque

tools = deque([int(x) for x in input().split()])
substances = [int(x) for x in input().split()]
challenges = [int(x) for x in input().split()]

while tools and substances:
    current_tool = tools.popleft()
    current_substance = substances.pop()

    result = current_tool * current_substance

    if result in challenges:
        challenges.remove(result)
        if not challenges:
            print("Harry found an ostracon, which is dated to the 6th century BCE.")
            break

    else:
        tools.append(current_tool + 1)
        substances.append(current_substance - 1)
        if substances[-1] == 0:
            substances.pop()

if challenges:
    print("Harry is lost in the temple. Oblivion awaits him.")

if tools:
    print('Tools: ' + ', '.join([str(t) for t in tools]))

if substances:
    print('Substances: ' + ', '.join([str(t) for t in substances]))

if challenges:
    print('Challenges: ' + ', '.join([str(t) for t in challenges]))
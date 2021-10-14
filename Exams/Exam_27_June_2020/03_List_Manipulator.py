# 03. List Manipulator

from collections import deque


def list_manipulator(list_int, add_remove, command, *args):
    list_int = deque(list_int)

    if add_remove == "add" and command == "end":
        numbers = [*args]
        for el in numbers:
            list_int.append(el)
        return list(list_int)
        # return f"[{', '.join([str(x) for x in list_int])}]"

    if add_remove == "add" and command == "beginning":
        numbers = [*args]
        for el in numbers[::-1]:
            list_int.appendleft(el)
        return list(list_int)
        # return f"[{', '.join([str(x) for x in list_int])}]"

    if add_remove == "remove" and command == "beginning":
        if args:
            n = args[0]
            for _ in range(n):
                list_int.popleft()
        else:
            list_int.popleft()
        return list(list_int)
        # return f"[{', '.join([str(x) for x in list_int])}]"

    if add_remove == "remove" and command == "end":
        if args:
            n = args[0]
            for _ in range(n):
                list_int.pop()
        else:
            list_int.pop()
        return list(list_int)
        # return f"[{', '.join([str(x) for x in list_int])}]"


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
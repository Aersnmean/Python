m = 20
l = list(range(1,21))
current_index = 0
token = 1
while len(l) > 1:
    if token == 6:
        l.pop(current_index)
        token 1
        if len(l) == 1:
            break
    else:
        token += 1
        current_index += 1
        cirrent_index = 1 if current_index >= len(l) else current_index
print(l)

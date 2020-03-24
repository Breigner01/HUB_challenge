def is_pangram(s):
    alpha_min = [chr(ord('a') + i) for i in range(26)]
    alpha_maj = [chr(ord('A') + i) for i in range(26)]
    presence = [0 for i in range(26)]
    count = 0

    for i in range(len(s)):
        for j in range(26):
            if s[i] == alpha_min[j] or alpha_maj[j]:
                presence[j] = 1
    for i in range(26):
        if presence[i] == 1:
            count += 1
    if count == 26:
        return True
    else:
        return False

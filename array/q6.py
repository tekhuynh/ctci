def compress(s):
    compressed_chars = []
    curr_char = ''
    curr_char_count = 1
    for c in s:
        if curr_char == '':
            curr_char = c
        elif curr_char != c:
            compressed_chars.append('%s%d' % (curr_char, curr_char_count))
            curr_char = c
            curr_char_count = 1
        elif curr_char == c:
            curr_char_count += 1
    compressed_chars.append('%s%d' % (curr_char, curr_char_count))
    return ''.join(compressed_chars)

s = input()
c = compress(s)
if len(s) <= len(c):
    print(s)
else:
    print(c)
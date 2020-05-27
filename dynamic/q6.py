def towers(n, orig, dest, buff, steps):
    if n <= 0:
        return
    towers(n-1, orig, buff, dest, steps)
    steps.append("%d: %d -> %d" % (n, orig, dest))
    towers(n-1, buff, dest, orig, steps)

steps = []
towers(4, 1, 3, 2, steps)
print("\n".join(steps))
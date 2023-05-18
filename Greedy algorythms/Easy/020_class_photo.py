from timeit import timeit


def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
    redShirtHeights.sort()
    blueShirtHeights.sort()

    if redShirtHeights[-1] > blueShirtHeights[-1]:
        big = redShirtHeights
        small = blueShirtHeights
    else:
        small = redShirtHeights
        big = blueShirtHeights

    for a, b in zip(small, big):
        if a >= b:
            return False
    return True


def classPhotos_all(redShirtHeights, blueShirtHeights):
    # Write your code here.
    redShirtHeights.sort()
    blueShirtHeights.sort()

    if redShirtHeights[-1] > blueShirtHeights[-1]:
        big = redShirtHeights
        small = blueShirtHeights
    else:
        small = redShirtHeights
        big = blueShirtHeights

    return all(s < b for s, b in zip(small, big))


a = [19, 2, 4, 6, 2, 3, 1, 1, 4]
b = [21, 5, 4, 4, 4, 4, 4, 4, 4]
itr = 1_000_000

for foo in [classPhotos, classPhotos_all]:
    t = timeit(stmt="foo(a, b)", number=itr, globals=globals())
    print(f"{foo.__name__} {itr:,} runs took {t:.6f} seconds")

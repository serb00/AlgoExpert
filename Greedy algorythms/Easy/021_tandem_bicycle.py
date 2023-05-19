def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # Write your code here.
    redShirtSpeeds.sort(reverse=fastest)
    blueShirtSpeeds.sort()
    return sum(max(r, b) for r, b in zip(redShirtSpeeds, blueShirtSpeeds))

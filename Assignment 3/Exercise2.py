def generateCombinations(chars, n, current=""):
    if n == 0:
        print(current)
        return
    for char in chars:
        generateCombinations(chars, n - 1, current + char)

characters = ["a", "b", "c"]
n = 2
generateCombinations(characters, n)

def solve(strings: list[str]) -> list[int]:
    def count_symmetry(word):
        return sum(1 for i, c in enumerate(word.lower()) if i == ord(c) - ord('a'))

    return [count_symmetry(word) for word in strings]
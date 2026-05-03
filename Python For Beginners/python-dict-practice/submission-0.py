def count_characters(word: str) -> dict[str, int]:
    characters: list[str] = list(word)
    return {
        character: characters.count(character)
        for character in characters
    }


# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))

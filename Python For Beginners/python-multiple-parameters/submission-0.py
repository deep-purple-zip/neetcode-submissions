def two_sum(operand_a, operand_b, /) -> None:
    print(f"{operand_a + operand_b}")


def three_sum(operand_a, operand_b, operand_c, /) -> None:
    print(f"{operand_a + operand_b + operand_c}")


two_sum(7, 10)
three_sum(3, 5, 8)

# do not modify below this line
two_sum(10, 9)
three_sum(5, 14, 6)

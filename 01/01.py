import time

# def simulate(inputs: list[str]) -> int:
#     curr = 50
#     count = 0
#     for input in inputs:
#         input = input.strip()
#         direction = input[0]
#         steps = int(input[1:])
#         print(f"Current: {curr}, Input: {input}, ", end="")

#         if direction == "L":
#             new_curr = curr - steps
#             print(new_curr, end=" ")
#             if new_curr < 0:
#                 # shift remaining
#                 remaining = abs(new_curr) % 100
#                 new_curr = 100 - remaining - 1
#                 print(new_curr, end=" ")
#             curr = new_curr
#         if direction == "R":
#             curr = (curr + steps) % 100
#         print(f"New Current: {curr}")

#         # count if curr is pointing to 0
#         count += 1 if curr == 0 else 0
#     return count


# TODO: this is a brute force solution. Try to get the above working with modulo arithmetic.
def simulate_part1(inputs: list[str]) -> int:
    curr = 50
    count = 0
    for input in inputs:
        input = input.strip()
        direction = input[0]
        steps = int(input[1:])
        while steps > 0:
            if direction == "L":
                curr -= 1
                if curr < 0:
                    curr = 99
            else:
                curr += 1
                if curr > 99:
                    curr = 0
            steps -= 1
        count += 1 if curr == 0 else 0
    return count


def simulate_part2(inputs: list[str]) -> int:
    curr = 50
    count = 0
    for input in inputs:
        input = input.strip()
        direction = input[0]
        steps = int(input[1:])
        while steps > 0:
            if direction == "L":
                curr -= 1
                if curr < 0:
                    curr = 99
            else:
                curr += 1
                if curr > 99:
                    curr = 0
            steps -= 1
            count += 1 if curr == 0 else 0
    return count


def main():
    with open("01.txt", "r") as f:
        inputs = f.readlines()

    # solve by simluating
    start_time = time.time()
    print(f"Count Part 1: {simulate_part1(inputs)}", end=" | ")
    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds", end="\n")

    start_time = time.time()
    print(f"Count Part 2: {simulate_part2(inputs)}", end=" | ")
    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds", end="\n")


if __name__ == "__main__":
    main()

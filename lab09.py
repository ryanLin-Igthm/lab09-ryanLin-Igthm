# Problem-solving practice (LeetCode / ICPC style).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def two_sum(nums, target):
    # Restate:
    # return true if within the list i < j and the sum of it is equal to the total
    # Outline (write your plan here first):
    # I would go through each number and compare all the other numbers to it, if the other numbers are greater than
    # and adds up to the target, then I will return the i and j. As well as only checking numbers after the i.
    #   ...
    # TODO: return the indices [i, j] (i < j) of the two numbers in `nums` that add up
    #   to `target`. Assume there is exactly one answer.
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    


def max_profit(prices):
    # Restate:
    # Find what number will result in the highest possible profit with another number that comes after it
    # Outline:
    #   ...
    # I would go through each number where I will save the numbers which will lead to the current highest profit 
    # then compare it to each other number and save the new numbers that will lead to a higher profit and repeat. 
    # Also only checking the numbers after the i to not go backwards. If not found just return 0
    # TODO: `prices[i]` is a stock price on day i. Return the most profit obtainable by
    #   buying on one day and selling on a LATER day. If no profit is possible, return 0.
    firstNum=prices[0]
    secondNum=prices[0]
    found=False
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[j] - prices[i] > secondNum - firstNum:
                firstNum = prices[i]
                secondNum = prices[j]
                found=True

    # print(f"(buy at {firstIndex}, sell at {secondIndex})")
    if found:
        return (f"{secondNum - firstNum}")
    return 0
    pass


def max_subarray(nums):
    # Restate:
    # Find which contiguous (in-a-row) would result in the highest sum
    # Outline:
    #   ...
    # I would go each different combination by starting at the first number and moving through the list 
    # and adding each of the numbers after that number to overtime finding the largest contiguous sum.
    # As well as saving the combination that returns the largest sum into a different list and replacing the old
    # list each time. 
    # TODO: return the largest sum of any contiguous (in-a-row) block of numbers in
    #   `nums`. The list has at least one number.
    largest_sum = nums[0]
    # largest_subarray = [nums[0]] # saves the highest sum contiguous subarray
    for i in range(len(nums)): 
        current_sum = 0
        for j in range(i, len(nums)):
            current_sum += nums[j]
            if current_sum > largest_sum:
                largest_sum = current_sum
                # largest_subarray = nums[i:j+1] # saves the highest sum contiguous subarray

    return (f"{largest_sum}")


def is_balanced(s):   # Part 4 - stretch (optional)
    # Restate:
    # Check if a open bracket comes after a closing bracket and if a pair of open and closing bracket exist
    # Outline:
    #   ...
    # I would take the first part of 's' such as '(' then I would pop it and move through the list 
    # looking for the other end and pop it off the list. Then I would return back to the start 
    # and get the next bracket and repeat it. I would return false if the closing brack is not found 
    # or if the first brack is a closing bracket.
    # TODO: return True if every bracket in `s` is closed correctly and in the right
    #   order. The brackets are ( ) [ ] { }. (Hint: a list used as a stack works well.)
    s = list(s)
    while len(s) > 0:
        first = s.pop(0)

        # First bracket cannot be a closing bracket
        if first in ")]}":
            return False

        match = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        found = False

        for i in range(len(s)):
            if s[i] == match[first]:
                s.pop(i)
                found = True
                break

        if not found:
            return False

    return True
    pass


def main():
    # Optional scratch space - try your functions here, then run: python lab09.py
    print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
    print(two_sum([3, 2, 4], 6))
    print(max_profit([7, 1, 5, 3, 6, 4]))   # returns 5   (buy at 1, sell at 6)
    print(max_profit([7, 6, 4, 3, 1]))
    print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) )# returns 6   (4 + -1 + 2 + 1)
    print(max_subarray([5, 4, -1, 7, 8]) )
    print(is_balanced("{[]}"))     # returns True

    pass


if __name__ == "__main__":
    main()

#!/usr/bin/python3
# coding=utf-8


def insertion_sort(A):
    sumW = 0
    sumF = 0
    for j in range(1,len(A)):
        sumF = sumF + 1
        key = A[j]
        i = j-1
        while (i >= 0 and A[i] > key):
            A[i+1] = A[i]
            i = i-1
            sumW = sumW + 1
        A[i+1] = key

    print("while_loop ran " + str(sumW) + " times")
    print("for_loop ran " + str(sumF) + " times")
    return A


if __name__ == "__main__":
    tests = [
        ([], []),
        ([1, 2, 3], [1, 2, 3]),
        ([3, 2, 1], [1, 2, 3]),
        ([9, 7, 3, 5, 2, 6], [2, 3, 5, 6, 7, 9]),
        ([-1, 1, -1, 2], [-1, -1, 1, 2]),
    ]

    for test, solution in tests:
        answer = insertion_sort(test)
        if answer != solution:
            print(
                "`insertion_sort` feilet for listen {:}. ".format(test)
                + "Svaret skulle vært {:}, men var {:}.".format(
                    solution, answer
                )
            )

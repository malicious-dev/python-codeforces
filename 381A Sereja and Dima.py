def solve(n, arr):

    is_serajas_turn = True

    s = 0
    e = n - 1
    seraja = 0
    dima = 0

    while s <= e:

        if arr[s] < arr[e]:
            this_round_point = arr[e]
            e -= 1
        else:
            this_round_point = arr[s]
            s += 1

        if is_serajas_turn:
            seraja += this_round_point
        else:
            dima += this_round_point

        is_serajas_turn = not is_serajas_turn

    return str(seraja) + " " + str(dima)


if __name__ == "__main__":

    n = int(input())
    arr = map(int, input().split())
    print(solve(n, arr))

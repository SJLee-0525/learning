for test_case in range(1, 11):
    dump = int(input())
    box_arr = list(map(int, input().split()))

    for _ in range(dump):
        high_box, low_box = 0, 101
        high_box_i, low_box_i = 0, 0
        for i, box in enumerate(box_arr):
            if high_box < box:
                high_box = box
                high_box_i = i
            if low_box > box:
                low_box = box
                low_box_i = i
        if high_box == low_box or high_box == low_box + 1:
            break
        else:
            box_arr[low_box_i] += 1
            box_arr[high_box_i] -= 1

    final_max, final_min = 0, 101
    for arr in box_arr:
        if final_max < arr:
            final_max = arr
        if final_min > arr:
            final_min = arr

    print(f'#{test_case} {final_max - final_min}')

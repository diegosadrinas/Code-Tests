def solution(N):
    bin_n = str(format(N, "b"))
    binary_gap = 0
    binary_gaps_list = []
    for i in range(1, len(bin_n)-1):
        if bin_n[i] == "0" and bin_n[i-1] == "1":
          binary_gap += 1
        if bin_n[i] == "1":
          binary_gap = 0
        elif bin_n[i + 1] == "0":
            binary_gap += 1
        elif bin_n[i+1] == "1":
          binary_gaps_list.append(binary_gap)
          binary_gap = 0
    if N == 0 or binary_gaps_list == []:
        return 0
    return max(binary_gaps_list)

def total_rank_count(rank):
    count = 0
    for i in range(len(rank)):
        if rank[i] == "A":
           count += 1
        elif rank[i] == "C":
            count -= 1
    total_rank_count = ""
    if count == 2:
        total_rank_count = "A"
    elif -1 <= count <= 1 :
        total_rank_count = "B"
    else:
        total_rank_count = "C"
    return total_rank_count
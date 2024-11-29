# 腕立てのランク判定
def rank_0(angle0, angle1):
    rank = []
    # 腕の角度
    if 0 <= angle0 and angle0 <= 110:
        rank.append("A")
    elif 110 < angle0 and angle0 <= 170:
        rank.append("B")
    else:
        rank.append("C")
    # 腰の角度
    if 165 <= angle1 and angle1 <= 180:
        rank.append("A")
    elif (180 < angle1 and angle1 < 190) or (150 < angle1 and angle1 < 165):
        rank.append("B")
    else:
        rank.append("C")
    return rank

# スクワットのランク判定
def rank_1(angle0, angle1):
    rank = []
    # 体軸の角度
    if 80 <= angle0 <= 100:
        rank.append("A")
    elif (100 < angle0 and angle0 <= 115) or (65 <= angle0 and angle0 < 80):
        rank.append("B")
    else:
        rank.append("C")
    # 膝の角度
    if 80 <= angle1 <= 100:
        rank.append("A")
    elif (60 <= angle1 < 80) or (100 < angle1 < 120):
        rank.append("B")
    else:
        rank.append("C")
    return rank
        
# 腹筋のランク判定
def rank_2(angle0, angle1):
    rank = []
    # 体を上げた時の上半身の角度
    if 0 <= angle0 <= 85:
        rank.append("A")
    elif 85 < angle0 <= 100:
        rank.append("B")
    else:
        rank.append("C")
    # 体を下げた時の上半身の角度
    # if 150 <= angle1 <= 170:
    #     rank.append("A")
    # elif 120 <= angle1 < 150:
    #     rank.append("B")
    # else:
    #     rank.append("C")
    # 首の角度
    if 0 <= angle1 <= 130:
        rank.append("A")
    elif 130 < angle1 <= 160:
        rank.append("B")
    else:
        rank.append("C")
    # # 足が地についているか
    # if 0 <= angle3 <= 10:
    #     rank.append("A")
    # else:
    #     rank.append("C")
    return rank
    
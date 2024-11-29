# 考え方

# 点の定義
# 点X(Xx,Xy)、点Y(Yx,Yy)、点Z(Zx,Zy)

# ベクトルXYおよびZYを計算
# XY = {(Yx-Xx),(Yy-Xy)} = (XYx,XYy)
# ZY = {(Yx-Zx),(Yy-Zy)} = (ZYx,ZYy)

# ベクトルXYおよびXZの内積を計算
# XY * ZY = (XYx*ZYx) + (XYy*ZYy)  代数的定義の定義

# ベクトルXYおよびZYの大きさを計算 
# |XY| = √{(XYx)**2 + (XYy)**2}  
# |ZY| = √{(ZYx)**2 + (ZYy)**2}
# XY * ZY = (|XY|*|ZY|)*cosθ       幾何的定義の内積

# 代数的定義の内積と幾何的定義の内積を連立
# (XYx*ZYx) + (XYy*ZYy) = (|XY|*|ZY|)*cosθ
# cosθ = {(XYx*ZYx) + (XYy*ZYy)} / (|XY|*|ZY|)


import math

def angle_between_points(a, b, c, d, e, f):
    # ベクトルXYおよびZYを計算
    vector_XY = (c - a, d - b)
    vector_ZY = (c - e, d - f)

    # ベクトルXYおよびZYの内積を計算 
    # 式 XY * ZY = (XYx*ZYx) + (XYy*ZYy)
    dot_product = vector_XY[0] * vector_ZY[0] + vector_XY[1] * vector_ZY[1]
    if dot_product == 0:
        dot_product = 1


    # ベクトルXYおよびZYの大きさを計算 
    # 式 |XY| = √{(XYx)**2 + (XYy)**2}  
    # 　 |ZY| = √{(ZYx)**2 + (ZYy)**2}
    #   　XY * ZY = (|XY|*|ZY|)*cosθ
    magnitude_XY = math.sqrt((c - a)**2 + (d - b)**2)
    magnitude_ZY = math.sqrt((c - e)**2 + (d - f)**2)

    # アークコサイン関数を用いて角度を計算
    # 式 
    angle_rad = math.acos(dot_product / (magnitude_XY * magnitude_ZY))
    # 弧度法から度数法に変換
    angle_deg = int(math.degrees(angle_rad))

    return angle_deg

# 例として、点X(810, )、点Y(445, 312)、点Z(0, 810)の角度を求める
# result_angle = angle_between_points(810, 0, 445, 312, 0, 810)
# print(f"∠XYZ の角度は {result_angle} 度です。")

from flask import render_template, request, redirect, url_for
from app import app
# from models import db, Memo
from vector import angle_between_points
from rank import rank_0, rank_1, rank_2
import csv # csvファイルを扱うためにcsvモジュールをインポート
import os
from total_rank import total_rank_count
from video_move import video_move, file_move_0
from frame_cut import frame_cut
from VP import VP

# ==================================================
# ルーティング
# =============
@app.route("/")
def top():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/video?exercisetype_id=<int:exercisetype_id>")
def video(exercisetype_id):
    return render_template("video.html", exercisetype_id=exercisetype_id)


@app.route("/camera?exercisetype_id=<int:exercisetype_id>")
def camera(exercisetype_id):
    return render_template("camera.html", exercisetype_id=exercisetype_id)

@app.route("/camera_check?exercisetype_id=<int:exercisetype_id>")
def camera_check(exercisetype_id):
    video_move('C:/Users/VisionPose2/Downloads/video.webm', 'C:/HEW/hew/training_video')
    # 動画を画像に変換
    if exercisetype_id == 2:
        sec = 31
    else:
        sec = 29
    if frame_cut("video", "C:/HEW/hew/training_video", "C:/HEW/hew_vp_analysis/images",sec):
        return render_template("error.html", exercisetype_id=exercisetype_id)
    # VisionPoseにかける
    VP()
    return render_template("camera_check.html", exercisetype_id=exercisetype_id)

@app.route("/result?exercisetype_id=<int:exercisetype_id>")
def result(exercisetype_id):
    try:
        # 種目名
        trainingname = ["腕立て伏せ", "スクワット", "腹筋"]
        # 評価項目
        Analysispoint = [{0: "腕の角度", 1: "腰の角度"}, {0: "体軸の角度", 1: "膝の角度"}, {0: "体を起こした時の角度", 1: "首の角度"}]
        # 角度算出
        # 結果csvから各点の座標を取り出しリストに格納。（角度は最大3つ）仮で数字入れてます（90度になるはず）
        result_point = []

        # Skeleton_Logsフォルダ内の画像の名前一覧取得
        path = "C:/HEW\hew_vp_analysis/tools/Skeleton_Logs"
        # files = 画像の名前一覧
        files = os.listdir(path)
        csv_list = []
        with open(f'C:/HEW/hew_vp_analysis/tools/Skeleton_Logs/{files[0]}') as f:
            # csvの要素をすべてcsv_listに格納
            csv_list = list(csv.reader(f))

        def zahyou_kakunou(exercisetype_id, csv_list, csv_number_a,csv_number_b,csv_number_c,csv_number_d,csv_number_e,csv_number_f):
            # csv_listから、使う要素をcsv_zahyouに格納
            csv_zahyou = []
            # スクワットの時だけ体軸の関係でcsvにない値を入れるので条件分岐に
            if exercisetype_id == 1:
                csv_zahyou = [[csv_list[1][csv_number_a],csv_list[1][csv_number_a+1],csv_list[1][csv_number_b],csv_list[1][csv_number_b+1],int(csv_list[1][csv_number_a]) + 500,csv_list[1][csv_number_b+1]],[csv_list[1][csv_number_c],csv_list[1][csv_number_c+1],csv_list[1][csv_number_d],csv_list[1][csv_number_d+1],csv_list[1][csv_number_e],csv_list[1][csv_number_e+1]]]
            else:
                csv_zahyou = [[csv_list[1][csv_number_a],csv_list[1][csv_number_a+1],csv_list[1][csv_number_b],csv_list[1][csv_number_b+1],csv_list[1][csv_number_c],csv_list[1][csv_number_c+1]],[csv_list[1][csv_number_d],csv_list[1][csv_number_d+1],csv_list[1][csv_number_e],csv_list[1][csv_number_e+1],csv_list[1][csv_number_f],csv_list[1][csv_number_f+1]]]
            
            csv_zahyou_change_int = []

            # csv_zahyouの要素をすべてint型に変えてcsv_zahyou_change_intに格納
            for row in csv_zahyou:
                row_int = []
                for data in row:
                    row_int.append(int(data))
                csv_zahyou_change_int.append(row_int)  

            # グローバル変数のresult_listにcsv_zahyou_change_intを格納
            return csv_zahyou_change_int
        
        # トレーニング毎にif文で分岐
        if exercisetype_id == 0:
            result_point = zahyou_kakunou(exercisetype_id, csv_list, 21,25,29,15,49,53)
        elif exercisetype_id == 1:
            result_point = zahyou_kakunou(exercisetype_id, csv_list, 3,61,49,53,57,0)
        else:
            result_point = zahyou_kakunou(exercisetype_id, csv_list, 43,49,53,5,15,17)

        # print(result_point)
        # 角度をAnalysispointに対応するようにリストに格納
        angle = [angle_between_points(result_point[0][0], result_point[0][1], result_point[0][2], result_point[0][3], result_point[0][4], result_point[0][5]), angle_between_points(result_point[1][0], result_point[1][1], result_point[1][2], result_point[1][3], result_point[1][4], result_point[1][5])]

        # ランク評価
        rank = []
        if exercisetype_id == 0:
            rank = rank_0(angle[0], angle[1])
        elif exercisetype_id == 1:
            rank = rank_1(angle[0], angle[1])
        elif exercisetype_id == 2:
            rank = rank_2(angle[0], angle[1])
        # 総合評価
        total_rank = total_rank_count(rank)
        # コメント
        comment = []
        if exercisetype_id == 0:
            if rank[0] == "A":
                comment.append("その調子です。頑張って維持しましょう。")
            elif rank[0] == "B":
                comment.append("惜しいです。もう少し曲げましょう。")
            else:
                comment.append("まだまだです。もっと意識して曲げてみましょう。")
            if rank[1] == "A":
                comment.append("その調子です。頑張って維持しましょう。")
            elif rank[1] == "B":
                comment.append("惜しいです。もう少し意識して真っすぐにしましょう。")
            else:
                comment.append("まだまだです。もっと意識して真っすぐにしましょう。")
        elif exercisetype_id == 1:
            if rank[0] == "A":
                comment.append("その調子です。頑張って維持しましょう。")
            elif rank[0] == "B":
                comment.append("惜しいです。もう少し意識して重心を真ん中にしましょう。")
            else:
                comment.append("まだまだです。もっと意識して重心を真ん中にしましょう。")
            if rank[1] == "A":
                comment.append("その調子です。頑張って維持しましょう。")
            elif rank[1] == "B":
                comment.append("惜しいです。出来るだけ直角になるよう、もう少しだけ意識してみましょう。")
            else:
                comment.append("まだまだです。出来るだけ直角になるよう、もっと意識してみましょう。")
        elif exercisetype_id == 2:
            if rank[0] == "A":
                comment.append("その調子です。頑張って維持しましょう。")
            elif rank[0] == "B":
                comment.append("惜しいです。もう少し意識して上体を起こしてみましょう。")
            else:
                comment.append("まだまだです。もっと意識して上体を起こしましょう。")
            if rank[1] == "A":
                comment.append("その調子です。頑張って維持しましょう。")
            elif rank[1] == "B":
                comment.append("惜しいです。もう少し意識して首を前に曲げてみましょう。")
            else:
                comment.append("まだまだです。もっと意識して首を前に曲げてみましょう。")

        goal_angle = []
        if exercisetype_id == 0:
            goal_angle = [90, 170]
        elif exercisetype_id == 1:
            goal_angle = [90, 90]
        else:
            goal_angle = [60, 110]

        goal_angle_sa = []
        for index, val in enumerate(goal_angle):
            goal_angle_sa.append(abs(val - angle[index]))

        # # 結果画像をstaticフォルダに移動
        # # result_imgフォルダ内の画像の名前一覧取得
        # path = "C:/HEW/hew_vp_analysis/result_img"
        # # files = 画像の名前一覧
        # files = os.listdir(path)
        # file_move_0(f"C:/HEW/hew_vp_analysis/result_img/{files[0]}", "C:/HEW/hew/static/img/training_images", "0.jpg")
    except:
        return render_template("error.html", exercisetype_id=exercisetype_id)
    else:
        return render_template("result.html", exercisetype_id=exercisetype_id, trainingname=trainingname[exercisetype_id], Analysispoint=Analysispoint[exercisetype_id], angle=angle, rank=rank, total_rank= total_rank, comment=comment, goal_angle=goal_angle, goal_angle_sa=goal_angle_sa)
    
@app.route("/error?exercisetype_id=<int:exercisetype_id>")
def error(exercisetype_id):
    return render_template("error.html", exercisetype_id=exercisetype_id)


# @app.route("/history")
# def history():
#     return render_template("history.html")


# @app.route("/history-item")
# def history_item():
#     return render_template("history-item.html")

# モジュールのインポート
# from werkzeug.exceptions import NotFound

# # エラーハンドリング
# @app.errorhandler(NotFound)
# def show_404_page(error):
#     msg = error.description
#     print('エラー内容：',msg)
#     return render_template('errors/404.html', msg=msg) , 404
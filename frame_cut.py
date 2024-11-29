# ライブラリのインポート
import cv2
import os
from pathlib import Path
import shutil
import subprocess

def frame_cut(movie_name, movie_path, result_folder_path,sec):    
    # movie_name = 動画のファイル名
    # movie_path = 動画の保存されているフォルダのパス
    # 動画を保存しているファイルパスを入力
    # sec = 切り取りたい秒数

    # 画像を入れるfolderを空に
    shutil.rmtree(result_folder_path)
    os.mkdir(result_folder_path)

    # 動画をmp4に変換
    subprocess.call(f'ffmpeg -i {movie_path}/{movie_name}.webm -c:v copy -c:a copy -an {movie_path}/{movie_name}.mp4')
    # webm形式の動画を削除
    os.remove(f'{movie_path}/{movie_name}.webm')

    path = Path(f"{movie_path}/{movie_name}.mp4")

    # 動画の読み込み
    movie = str(path)
    # 動画の読み込み
    cap = cv2.VideoCapture(movie)
    
    # フレーム総数
    fps =cap.get(cv2.CAP_PROP_FPS)
    totalFrames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # for i in sec:
    # for i in range(sec):
    cut_fream = fps * sec
    if cut_fream <=  totalFrames:
        #動画を切り取って画像にする
        cap.set(cv2.CAP_PROP_POS_FRAMES, cut_fream )
        ret, image = cap.read()
        cv2.imwrite(f"{result_folder_path}/user_photo.jpg", image)
        return False
    else:
        # 動画の秒数がキャプチャの秒数が超えている時
        return True


# if __name__ == "__main__":
#     frame_cut("video", "C:/HEW/hew/training_video", "C:/HEW/hew_vp_analysis/images",16)




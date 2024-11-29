import os
import glob
import shutil

def VP():
    # training_imagesフォルダを空にする
    shutil.rmtree("C:/HEW/hew/static/img/training_images")
    os.mkdir("C:/HEW/hew/static/img/training_images")
    # Skeleton_Logsフォルダを空にする
    shutil.rmtree("C:/HEW/hew_vp_analysis/tools/Skeleton_Logs")
    os.mkdir("C:/HEW/hew_vp_analysis/tools/Skeleton_Logs")
    
    # imageフォルダの数をカウント
    # imageフォルダの入っているディレクトリのパス
    DIR = "C:/HEW/hew_vp_analysis/images"
    # file_list = os.listdir(DIR)
    # sum_images = imagesフォルダ内の画像の枚数
    # sum_images = len(file_list)

    # imageフォルダ内の画像の名前一覧取得
    # files = 画像の名前一覧
    files = os.listdir(DIR)

    # batファイルに処理を書き込み
    # imagefile_name_before = ""
    # imagefile_name_after = ""
    try:
        with open('C:/HEW/VPcmd.bat', mode='x', encoding='utf-8') as f:
            f.write(f'cd C:/HEW/hew_vp_analysis/tools\n')
    except FileExistsError:
        with open('C:/HEW/VPcmd.bat', mode='w', encoding='utf-8') as f:
            f.write(f'cd C:/HEW/hew_vp_analysis/tools\n')
    # for i in range(sum_images):
    imagefile_name_before = files[0]
        # imagefile_name_after = files[i]
        # バッチファイルにコマンドを記入
    with open('C:/HEW/VPcmd.bat', mode='a', encoding='utf-8') as f:
        f.write(f'VPAnalyzer.exe 23G9LR3XJZZFYRZBFU44 -im "C:/HEW/hew_vp_analysis/images/{imagefile_name_before}" -o "C:/HEW/hew/static/img/training_images/result.jpg" -s\n')

    # デバッグ用。VPcmd.batを実行時にコマンドラインが消えずに残る
    # with open('VPcmd.bat', mode='a', encoding='utf-8') as f:
    #         f.write(f'pause')

    # batファイルの場所
    cmd_file = "C:/HEW/VPcmd.bat"
    # batファイルの実行
    os.system(cmd_file)

# if __name__ == '__main__':
#     VP()
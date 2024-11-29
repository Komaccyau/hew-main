import shutil
import os

def video_move(before_pass, after_pass):
    # afterフォルダを空にする
    shutil.rmtree(after_pass)
    os.mkdir(after_pass)
    
    shutil.move(before_pass, after_pass)

def file_move_0(before_pass, after_pass, filename):
    # afterフォルダを空にする
    shutil.rmtree(after_pass)
    os.mkdir(after_pass)
    
    shutil.move(before_pass, f"{after_pass}/{filename}")

# フォルダを空にしない（2フォルダ目）パターン
# def file_move_1(before_pass, after_pass, filename):    
#     shutil.move(before_pass, f"{after_pass}/{filename}")
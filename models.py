from flask_sqlalchemy import SQLAlchemy

# Flask-SQLAlchemyの生成
db = SQLAlchemy()

# ==================================================
# モデル
# ==================================================
# 会員情報テーブル
# class T_Member_Information(db.Model):
#     # テーブル名
#     __tablename__ = 'T_Member_Information'
#     # ユーザーID（PK）
#     F_UserID= db.Column(db.Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
#     # ユーザー名
#     F_UserName = db.Column(db.String(20), nullable=False)
#     # パスワード
#     F_Password = db.Column(db.String(20), unique=True, nullable=False)
#     # メールアドレス
#     F_Email= db.Column(db.String(319), unique=True, nullable=False)

# # 履歴情報テーブル
# class T_Background_Information(db.Model):
#     # テーブル名
#     __tablename__ = 'T_Background_Information'
#     # データID（PK）
#     F_DataID = db.Column(db.Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
#     # ユーザーID（FK）
#     F_UserID = db.Column(db.Integer, db.ForeignKey('T_Member_Information.F_UserID'), unique=True, nullable=False, autoincrement=True)
#     # トレーニング種目ID（FK）
#     F_Exercise_TypeID = db.Column(db.Integer, db.ForeignKey('T_Training_Master.F_Exercise_TypeID'), nullable=False)
#     # トレーニング日付時間
#     F_Exercise_Time = db.Column(db.DateTime, nullable=False)

# トレーニング情報テーブル
# class T_Training_Master(db.Model):
#     # テーブル名
#     __tablename__ = 'T_Training_Master'
#     # トレーニング種目ID（PK）
#     F_Exercise_TypeID = db.Column(db.Integer, unique=True, nullable=False, autoincrement=True)
#     # 見本映像ID
#     F_Sample_ImageID = db.Column(db.Integer, nullable=False)
#     # ピクトグラムID
#     F_PictogramID = db.Column(db.Integer, nullable=False)
    
# # 撮影情報テーブル
# class T_Photography_Information(db.Model):
#     # テーブル名
#     __tablename__ = 'T_Photography_Information'
#     # データID（FK）
#     F_DataID = db.Column(db.Integer, db.ForeignKey('T_Background_Information.F_DataID'), unique=True, nullable=False, autoincrement=True)
#     # 画像データID（PK）
#     F_Image_DataID = db.Column(db.Integer, nullable=False, unique=True)
#     # CSVデータID
#     F_CSV_DataID = db.Column(db.Integer, nullable=False, unique=True)
    
# # 分析項目テーブル
# class T_Analysis_Data(db.Model):
#     # テーブル名
#     __tablename__ = 'T_Analysis_Data'
# pybo 프로젝트에 있는 db를 임포트
from pybo import db

# Question 클래스는 SQLAlchemy에 있는 Model을 상속 받아 사용한다.
class Question(db.Model):
    # primary key
    # SQL쿼리를 모르더라도 각 디비 테이블을 생성할 수 있다.
    # 기존에 형을 맞추어 생성해야했던 과정을 이렇게 파일 하나로 처리가 가능
    id = db.Column(db.Integer, primary_key=True)
    #column NOT NULL
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    question = db.relationship('Question', backref=db.backref('answer_set', cascade='all, delete-orphan'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

# 위 과정을 mysql에 쿼리로 처리할 경우 이런 쿼리를 주어야함.
# CREATE TABLE Question (
#     id INT PRIMARY KEY,
#     subject VARCHAR(50) NOT NULL,
#     content VARCHAR(100) NOT NULL, ~~
#);
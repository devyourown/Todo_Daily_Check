from QnA import QnA
import datetime

if __name__ == "__main__":
    while True:
        current_time = str(datetime.datetime.now())
        if "12:00" == current_time[11:16]:
            qna = QnA()
            qna.execute()
    
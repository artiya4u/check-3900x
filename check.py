from datetime import datetime

from check_advice_3900x import check_advice
from check_jib_3900x import check_jib

if __name__ == '__main__':
    print(str(datetime.now()))
    check_jib()
    check_advice()

import os
import datetime


class Counter:

    filename = '.data/counter.txt'
    today = datetime.date.today()

    def check_counter(self) -> None:

        if not os.path.exists(".data"):
            os.mkdir(".data")
        try:
            with open(Counter.filename, 'r') as f:
                savedDateStr, countStr = f.read().strip().split(',')
                savedDate = datetime.datetime.strptime(savedDateStr, '%Y-%m-%d').date()
                self.count = int(countStr)
                if savedDate != Counter.today:
                    self.count = 0
        except FileNotFoundError:
            self.count = 0
        self.count += 1

        with open(Counter.filename, 'w') as f:
            f.write(f'{Counter.today},{self.count}')
    
    def get_counter(self) -> int:
        return self.count
    


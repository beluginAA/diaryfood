import os
import sys
import shutil
import locale

from loguru import logger
from datetime import date, datetime
from counter import Counter

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

class Notebook:
    
    logger.remove()
    prpLogger = logger.bind(name = 'preprocessingLogger').opt(colors = True)
    prpLogger.add(sink = sys.stdout, format = '<green> {time:HH:MM:SS} </green> {message}', level = 'INFO')

    notebookName = 'DiaryFoodNotebook.txt'
    headers = ['Наименование продукта', 'Количество продукта', 'Калорийность', 'Белки', 'Жиры', 'Углеводы']

    @staticmethod
    def check_the_date(filePath: str) -> None :
        currentDate = date.today().isoweekday()
        if currentDate == 1:
            with open(filePath, mode = 'w') as notebook:
                notebook.truncate()
                notebook.write(f"{' | '.join(Notebook.headers)}\n")

    def get_notebook(self) -> None:
        Notebook.prpLogger.info('Поиск документа.')

        findSuccess = False
        desktopPath = os.path.expanduser('~/Desktop')
        for root, dirs, files in os.walk(desktopPath):
            for file in files:
                if file.endswith(Notebook.notebookName):
                    Notebook.prpLogger.info('Документ найден.')
                    findSuccess = True
                    filePath = os.path.join(root, file)
                    if not filePath.endswith(f'Desktop\{Notebook.notebookName}'):
                        Notebook.prpLogger.info('Документ находится не на рабочем столе. Переношу его на рабочий стол.')
                        destinationFolder = os.path.expanduser("~/Desktop")
                        shutil.move(filePath, destinationFolder)
                    else:
                        Notebook.prpLogger.info('Документ находится на рабочем столе.')
        
        if not findSuccess:
            Notebook.prpLogger.info('Кажется, такого документа нет. Создаю файл на рабочем столе.')
            with open(Notebook.notebookName, 'w') as f:
                pass
    
    def open_notebook(self, filePath: str) -> bool:
        Notebook.prpLogger.info('Проводится проверка файла...')
        try:
            with open(filePath, 'r') as file:
                self.check_the_date(file)
        except:
            Notebook.prpLogger.info('Файл не готов для работы!')
            return False
        else:
            Notebook.prpLogger.info('Файл полностью готов для работы.')
            return True
    
    def write_to_notebook(self, filePath:str, text:str, foodLen:int) -> None:
        maxLenRow = [foodLen, 5, 5, 3, 3, 3]
        maxLenName = [len(name) for name in Notebook.headers]
        maxLen = [colLen if colLen > rowLen else rowLen for colLen, rowLen in zip(maxLenName, maxLenRow)]
        with open(filePath, 'a') as file:
            count = Counter()
            count.check_counter()
            counter = count.get_counter()
            if counter == 1:
                file.write(f'{datetime.today().strftime("%Y-%m-%d %H:%M - %A")}')
                file.write('\n')
            else:
                file.write(f'{datetime.today().strftime("%H:%M - %A")}')
                file.write('\n')
            fileWrite = ''
            for column, colLen in zip(Notebook.headers, maxLen):
                fileWrite += f"{column:<{colLen}}|"
            file.write(fileWrite)
            file.write('\n')
            for row in text:
                columnValue = ''
                for i in range(len(row)):
                    columnValue += f"{str(row[i]) if row[i] else '-':<{maxLen[i]}}|"
                file.write(f"{columnValue}\n")
            file.write('\n')

        
                

class String:

    food = []
    foodLenMax = 0
    
    def check_len_string(self, currentString:str) -> bool:
        self.summaryStr = [part.strip() for part in currentString.strip('\n').split(',')]
        if len(self.summaryStr) == 6:
            self.summaryStr = [self.summaryStr[i].capitalize() if i == 0 else self.summaryStr[i].lower() for i in range(len(self.summaryStr))]
            String.food.append(self.summaryStr)
            return True
        else:
            return False

    def return_max_value(self) -> None:
        if len(self.summaryStr[0]) > String.foodLenMax:
            String.foodLenMax = len(self.summaryStr[0])

    def get_values(self) -> list:
        return String.food, String.foodLenMax


import os
import sys
import shutil

from loguru import logger
from datetime import date

class Notebook:
    
    logger.remove()
    prpLogger = logger.bind(name = 'preprocessingLogger').opt(colors = True)
    prpLogger.add(sink = sys.stdout, format = '<green> {time:HH:MM:SS} </green> {message}', level = 'INFO')

    @staticmethod
    def check_the_date(filePath: str) -> None :
        currentDate = date.today().isoweekday()
        if currentDate == 1:
            with open(filePath, mode = 'w') as notebook:
                notebook.truncate()

    def get_notebook(self) -> None:
        Notebook.prpLogger.info('Поиск документа.')

        findSuccess = False
        desktopPath = os.path.expanduser('~/Desktop')
        for root, dirs, files in os.walk(desktopPath):
            for file in files:
                if file.endswith('DiaryFoodNotebook.txt'):
                    Notebook.prpLogger.info('Документ найден.')
                    findSuccess = True
                    filePath = os.path.join(root, file)
                    if not filePath.endswith('Desktop\DiaryFoodNotebook.txt'):
                        Notebook.prpLogger.info('Документ находится не на рабочем столе. Переношу его на рабочий стол.')
                        destinationFolder = os.path.expanduser("~/Desktop")
                        shutil.move(filePath, destinationFolder)
                    else:
                        Notebook.prpLogger.info('Документ находится на рабочем столе.')
        
        if not findSuccess:
            Notebook.prpLogger.info('Кажется, такого документа нет. Создаю файл на рабочем столе.')
            desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
            with open(os.path.join(desktop, 'DiaryFoodNotebook.txt'), 'w') as f:
                f.write('--')
    
    def open_notebook(self, filePath: str) -> bool:
        try:
            with open(filePath, 'r') as file:
                self.check_the_date(file)
        except:
            return False
        else:
            return True


class String:

    def __init__(self, currentString:str):
        self.currentString = currentString
    
    def check_the_string(self) -> bool:
        summaryString = [part.strip() for part in self.currentString.strip().split(',')]
        return len(summaryString) == 6


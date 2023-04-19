import sys

from loguru import logger
from preprocessing import Notebook, String


logger.remove()
mainLogger = logger.bind(name = 'mainLogger').opt(colors = True)
mainLogger.add(sink = sys.stdout, format = '<green> {time:HH:MM:SS} </green> {message}', level = 'INFO')

attempt = Notebook()
attempt.get_notebook()

try:
    if attempt.open_notebook(Notebook.notebookName):
        content = String()
        for string in sys.stdin:
            if string.strip('\n') == '':
                sys.stdin.close()
            elif not content.check_len_string(string):
                mainLogger.info('Введите значение еще раз!')
            else:
                content.return_max_value()
except Exception:
    food, foodLenMax = content.get_values()
    attempt.write_to_notebook(Notebook.notebookName, food, foodLenMax)
    mainLogger.info('Все значения сохранены, до свидания!')


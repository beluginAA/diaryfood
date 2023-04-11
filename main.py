import sys

from loguru import logger


logger.remove()
mainLogger = logger.bind(name = 'mainLogger').opt(colors = True)
mainLogger.add(sink = sys.stdout, format = '<green> {time:HH:MM:SS} </green> {message}', level = 'INFO')

try:
    for string in sys.stdin:
        if string.strip('\n') == '':
            sys.stdin.close()
        else:
            pass
except Exception:
    mainLogger.info('До встречи!')

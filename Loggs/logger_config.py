from loguru import logger

# Логгеры для дебага и эррора, файлы отправляются по команде /loggs
LOGGS = logger.add("Loggs/loggs.log", format="--------\n{time:DD-MM HH-MM} --> {level}\n\n{message}", level='INFO', rotation='1 week')


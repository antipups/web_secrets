import functools
from enum import Enum

from loguru import logger
from config import levels_config_to_file


class LogType(Enum):
    info = logger.info
    error = logger.error
    exception = logger.exception
    debug = logger.debug
    success = logger.success


def _log_filter(record) -> bool:
    return record['level'].name in levels_config_to_file


logger.add('logs.txt',
           compression='zip',
           rotation='5MB',
           filter=_log_filter)


def logging(function=None, entry: bool = True,
            exit: bool = False,
            level: str = "DEBUG",
            error: bool = False):
    """
        Реализация собственного декоратора для логирования
    :param function: декорируемая функция
    :param entry: логировать входные данные
    :param exit: логировать выходные данные
    :param level: уровень логирования входа и выхода
    :return:
    """
    if function is None:
        return functools.partial(logging,
                                 entry=entry,
                                 exit=exit,
                                 level=level,
                                 error=error)

    @functools.wraps(function)
    def wrapper(*args, **kwargs):

        function_name = function.__name__
        logger_ = logger.opt(depth=1)

        if entry:
            logger_.log(level, "Entering '{}' (args={}, kwargs={})", function_name, args, kwargs)

        try:
            result = function(*args, **kwargs)

        except Exception as e:
            if error:
                logger.exception(e)
            return

        if exit:
            logger_.log(level, "Exiting '{}' (result={})", function_name, result)

        return result

    return wrapper

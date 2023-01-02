import os
import time


class Logger:
    INFO = "INFO"
    DEBUG = "DEBUG"
    WARNING = "WARN"
    FATAL = "FATAL"

    LOG_OUTPUT = "file"

    def __init__(self) -> None:
        pass

    @classmethod
    def log(cls, log_level: str, messages) -> None:

        output = f"[{time.ctime()}] {log_level}: { ' | '.join([str(msg) for msg in messages])}\n"
        if cls.LOG_OUTPUT == "file":
            with open(os.path.join(os.path.dirname(__file__), "output.log"), "a+") as logfile:
                logfile.write(output)

        print(output)

    @classmethod
    def info(cls, *messages) -> None:
        cls.log(cls.INFO, messages)

    @classmethod
    def debug(cls, *messages) -> None:

        cls.log(cls.DEBUG, messages)

    @classmethod
    def warn(cls, *messages) -> None:
        cls.log(cls.WARNING, messages)

    @classmethod
    def fatal(cls, *messages) -> None:
        cls.log(cls.FATAL, messages)

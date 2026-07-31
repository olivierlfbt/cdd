from datetime import datetime


class Logger:

    @staticmethod
    def info(message):

        print(

            f"[{datetime.now():%H:%M:%S}] "

            f"INFO  {message}"

        )

    @staticmethod
    def warning(message):

        print(

            f"[{datetime.now():%H:%M:%S}] "

            f"WARN  {message}"

        )

    @staticmethod
    def error(message):

        print(

            f"[{datetime.now():%H:%M:%S}] "

            f"ERROR {message}"

        )

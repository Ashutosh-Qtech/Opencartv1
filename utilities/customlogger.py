import logging


class Loggen:

    @staticmethod
    def loggen():
        path = "G:\My Drive\QA Automation\Log file for Opencart\automation.log"

        logging.basicConfig(filename=path,
                            format='%(asctime)s:%(levelname)s:%(message)s',datefmt='%m/%d/%y %I:%M:%S %p'
                            )

        logger=logging.getLogger()
        logger.setLevel(logging.ERROR)

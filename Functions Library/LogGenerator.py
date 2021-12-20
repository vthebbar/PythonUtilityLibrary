import logging

class LogGen:

    @staticmethod     # static method, no need to create object, can be directly called using class name
    def log_gen():
        logging.basicConfig(filename="..\\Logs\\Logfile.log",
                            format='%(asctime)s : %(levelname)s : %(message)s',
                            datefmt='%d-%m-%Y  %H:%M:%S',
                            force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger


#  Below commented statements are used for testing above function to ensure it is working fine
'''
log = LogGen.log_gen()
log.info("***Info Log***")
log.error("****Error Log***")
log.warning("***Warning Log***")
log.debug("***Debug Log****")
log.critical("***Critical Log***")
'''


import logging
import requests

logging.basicConfig(level="DEBUG", filename="mylog.log")

logger = logging.getLogger()
print(logger.level)
print(logger.handlers)

logging.getLogger('urllib3').setLevel('CRITICAL')

def main(name):
    logger.debug(f'Enter in the main function: name = {name} ')
    r = requests.get('https://google.com')

if __name__ == '__main__':
    main('pavel')
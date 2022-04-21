
import logging
import random
import sys
import time

import cv2


def main():
    counter = 0
    """
    Normally all the logs in python directs to stderror.
    To change the log to stdout, we need to set it explicitly
    """
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

    while counter < 5:
        time.sleep(2)
        counter += 1
        _text = "Hello Cat {:03d}".format(counter)
        image = cv2.imread("dog.png")
        cv2.putText(image, _text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow("Display1", image)
        cv2.waitKey(1000)
        cv2.destroyWindow("Display1")

        logging.info(_text)

    logging.warning("Exiting the program - Bye Bye")
    if random.random() > 0.5:
        raise AssertionError("This is a Random Exception generated by python program")


if __name__ == '__main__':
    main()

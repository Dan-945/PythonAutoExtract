import os
import sched, time,logging
logger = logging.getLogger('autoExtracter')

fh = logging.FileHandler('/LogFolder/log.txt')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s, - %(levelname)s %(message)s')
logger.addHandler(fh)
fh.setFormatter(formatter)


def do_something(scheduler):
    scheduler.enter(5,1, do_something, (scheduler,))
    logger.warning("doing stuff")

    with open(os.path.join("/Watch", 'unrared'), "a"):
        logger.warning("file created " + "unrared " + "at " + "/Watch")
    os.popen('cp ' + "/Watch/unrared" + ' ' + "/ExtractFolder/" + "unrared")

my_scheduler = sched.scheduler(time.time, time.sleep)
my_scheduler.enter(1, 1, do_something, (my_scheduler,))
my_scheduler.run()
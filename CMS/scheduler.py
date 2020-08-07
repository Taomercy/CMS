import os
import shutil
import time

from apscheduler.schedulers.background import BackgroundScheduler
import logging
import git
from git import Actor

from CMS.settings import BACKUP_PATH


def get_time_format():
    now = time.strftime('%Y-%m-%d-%H%M%S', time.localtime(time.time()))
    return now


def database_backup():
    repo = git.Repo(BACKUP_PATH)
    origin = repo.remote('origin')
    origin.pull()
    try:
        now = get_time_format()
        json_name = 'data_{}.json'.format(now)
        try:
            cmd = 'python manage.py dumpdata > %s ' % json_name
            os.system(cmd)
        except:
            cmd = 'python3 manage.py dumpdata > %s ' % json_name
            os.system(cmd)

        if not os.path.isfile(json_name):
            return 1

        shutil.move(json_name, BACKUP_PATH) 

        author = Actor("taomercy", "taomercy@qq.com")
        committer = Actor("taomercy", "taomercy@qq.com")

        repo.git.add(os.path.join(BACKUP_PATH, json_name))
        commit_msg = 'data backup %s' % now
        repo.index.commit(commit_msg, author=author, committer=committer)
        origin.push()

        logging.info('backup end')
        return 0
    except Exception as err:
        print(repo.git.status())
        logging.info(err)
        return 1


class SchedulerMain(object):
    scheduler = None

    def __init__(self):
        logging.basicConfig()
        logging.getLogger('apscheduler').setLevel(logging.DEBUG)
        self.scheduler = BackgroundScheduler()

    def job_scheduler_add(self, job):
        pass

    def scheduler_shutdown(self, wait=True):
        self.scheduler.shutdown(wait=wait)

    def get_scheduler(self):
        return self.scheduler


class BackupScheduler(SchedulerMain):
    scheduler = None

    def job_scheduler_add(self, job):
        pass

    def scheduler_start(self):
        self.scheduler.start()
        # self.scheduler.add_job(database_backup, 'interval', days=1)
        self.scheduler.add_job(database_backup, 'cron', day_of_week='mon-fri', hour=18)

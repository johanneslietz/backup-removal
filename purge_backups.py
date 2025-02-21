#!/usr/bin/env python3

import shutil
import sys
from datetime import date, timedelta
from os import listdir
from os.path import isdir, join, exists


def purge_daily_backups(path: str, pattern: str) -> None:
    if not exists(path):
        print("Backup directory '{0}' does not exist, exiting.".format(path))
        return
    print("Purging daily backups...")
    today = date.today()
    the_day_before = today - timedelta(days=1)
    backup_dirs = [f for f in listdir(path) if isdir(join(path, f))]
    all_files_deleted = False
    while not all_files_deleted:
        date_string = the_day_before.strftime(pattern)
        all_files_deleted = True
        for dir in backup_dirs:
            if date_string in dir:
                dir_to_delete = join(path, dir)
                print("Purging '{0}'...".format(dir_to_delete))
                shutil.rmtree(dir_to_delete)
                all_files_deleted = False
        the_day_before = the_day_before - timedelta(days=1)
    print("Done purging daily backups.")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 purge_daily_backups.py <backupFolder> [<pattern>]")
        exit(1)
    backup_folder = sys.argv[1]
    if len(sys.argv) > 2:
        pattern = sys.argv[2]
    else:
        pattern = '%Y-%m-%d'
    purge_daily_backups(backup_folder, pattern)

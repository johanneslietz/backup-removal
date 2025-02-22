#!/usr/bin/env python3

import json
import subprocess
from datetime import date

from purge_backups import main


def verify_last_virtualmin_backup_successful() -> bool:
    today = date.today()
    command = "/usr/sbin/virtualmin list-backup-logs --start {0} --json".format(today.strftime('%Y-%m-%d'))
    output = subprocess.check_output(command, shell=True, text=True)
    backup_log = json.loads(output)
    last_backup_successful = True
    for backup in backup_log['data']:
        for final_status in backup['values']['final_status']:
            if final_status != 'OK':
                last_backup_successful = False
    return last_backup_successful


if __name__ == '__main__':
    if not verify_last_virtualmin_backup_successful():
        print("Last Virtualmin backup was not successful, exiting.")
        exit(1)
    else:
        main()

# backup-removal
## Deletes old backup directories via a Python script
Expects a directory of daily backup directories, with a %Y-%m-%d pattern in the folder names.

- /var/backups/2025-02-01-daily
- /var/backups/2025-02-02-daily
- /var/backups/2025-02-03-daily
- ...

It will delete delete all backup directories under /var/backups except the one for the current date.

## Usage
> python3 purge_backups.py /path/to/backups

Optionally add the date pattern, default is <code>%Y-%m-%d</code>.
> python3 purge_backups.py /path/to/backups %Y-%m-%d
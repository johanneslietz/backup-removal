# backup-removal
## Deletes old backup directories via a Python script
Expects a directory of daily backup directories, with a %Y-%m-%d pattern in the folder names.

- /path/to/backups/2025-01-31-daily
- /path/to/backups/2025-02-01-daily
- /path/to/backups/2025-02-02-daily
- /path/to/backups/2025-02-03-daily
- ...

It will delete all old backup directories under /path/to/backups except the one for the current date.

## Usage
### Verify last Virtualmin backup was successful
> purge_virtualmin_backups.py /path/to/backups

### General
> purge_backups.py /path/to/backups

Optionally add the date pattern, default is <code>%Y-%m-%d</code>.
> purge_backups.py /path/to/backups %Y-%m-%d
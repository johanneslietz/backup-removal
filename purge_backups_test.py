import os
import shutil
import tempfile
import unittest
from datetime import date, timedelta

from purge_backups import purge_daily_backups

backup_folder = tempfile.mkdtemp()
print("Using backup folder: {}".format(backup_folder))

class PurgeBackupTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        today = date.today()
        shutil.rmtree(backup_folder, ignore_errors=True)
        print('Creating backup folders...')
        for n in range(30):
            dt = today - timedelta(days=n)
            folder_name = dt.strftime('%Y-%m-%d-daily')
            os.makedirs(os.path.join(backup_folder, folder_name), exist_ok=True)
            file = open(os.path.join(backup_folder, folder_name, 'dummyfile.txt'), 'x')
            file.write('dummy content')
            file.close()
        print('Done...')

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(backup_folder)

    def test_purge_old_backups(self):
        # Act
        purge_daily_backups(backup_folder, '%Y-%m-%d')
        # Assert
        remaining_files = os.listdir(backup_folder)
        self.assertEqual(1, len(remaining_files))
        self.assertEqual(remaining_files[0], date.today().strftime('%Y-%m-%d-daily'))

if __name__ == '__main__':
    unittest.main()

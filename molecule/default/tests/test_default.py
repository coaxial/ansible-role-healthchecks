import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hc_presence(host):
    repo = host.file('/opt/docker-healthchecks')

    repo.exists


def test_files(host):
    files = [
        'ssh/id_rsa',
        'ssh/id_rsa.pub',
        'ssh/known_hosts',
        'backups/passphrase',
        'app/config/local_settings.py',
        'db/db.env',
        'app/app.env',
        'nginx/config/app.conf'
    ]

    for file in files:
        file.exists

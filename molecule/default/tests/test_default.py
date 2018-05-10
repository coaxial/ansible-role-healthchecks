import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hc_presence(host):
    repo = host.file('/opt/docker-healthchecks')

    assert repo.exists


def test_files(host):
    files = [
        'backups/ssh/id_rsa',
        'backups/ssh/id_rsa.pub',
        'backups/ssh/known_hosts',
        'backups/passphrase',
        'backups/config.yaml',
        'app/config/local_settings.py',
        'db/db.env',
        'app/app.env',
        'nginx/config/app.conf'
    ]

    for f in files:
        assert host.file("/opt/docker-healthchecks/" + f).exists

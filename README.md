Healthchecks role
=========

This role will deploy a Dockerized [healthchecks](https://github.com/healthchecks/healthchecks) instance. Optionally backs up to a borg repo hourly.

Requirements
------------

- Ubuntu host
- borg backup repo (optional)
- Docker and Docker Compose (and their pip modules `docker`, `docker-py`, `docker-compose`)

Role Variables
--------------

name | default value | possible values | purpose | notes
---|---|---|---|---
`hc__db_name` | `hc` | any valid database name | database name in the RDBMS
`hc__db_user` | `postgres` | any valid RDBMS username | username for accessing the database
`hc__db_password` | none, must be set if using mysql or postgres | any string | set database password |
`hc__email_host` | none, must be set | any valid hostname, fqdn, or IP | mail server used to send notifications
`hc__email_port` | `587` | any valid port number | port to connect to the `hc__email_host` server
`hc__email_user` | `healthchecks` | any username supported by the mail server at `hc__email_host`
`hc__email_password` | none, must be set | password for `hc__email_user`@`hc__email_host`
`hc__email_from` | none, must be set | any valid email address | used as the default from address for emails
`hc__site_name` | `Healthchecks monitoring` | any string | used throughout the app to refer to itself
`hc__hostname` | none, must be set | sets the root for thisapplication (i.e. `https://example.com/`)
`hc__su_email` | none, must be set | any valid email address | used to create the first admin user
`hc__su_password` | none, must be set | any string | used to create the first admin user
`hc__su_username` | none, must be set | any string of `[a-zA-Z0-9]` characters | used to create the first admin user
`hc__enable_backups` | `true` | `true` or `false` | enable or disable hourly backups to a borg repo
`hc__backup_passphrase` | none, must be set | any string | password to the borg repo (if backups are enabled)
`hc__borg_repo_url` | none, must be set | any valid borg repo string (cf. https://borgbackup.readthedocs.io/en/stable/usage/general.html#repository-urls)


Notes
------------

If you want https, you will need to set it up on the host (with nginx as a reverse proxy and let's encrypt for instance)

Example Playbook
----------------

    - hosts: servers
      roles:
         - coaxial.healthchecks

License
-------

BSD

Author Information
------------------

Coaxial, https://64b.it

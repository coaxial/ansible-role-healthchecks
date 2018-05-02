Healthchecks role
=========

This role will deploy a Dockerized [healthchecks](https://github.com/healthchecks/healthchecks) instance.

Requirements
------------

- Ubuntu host

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
`hc__site_root` | none, must be set | sets the root for thisapplication (i.e. `https://example.com/`)


Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in
regards to parameters that may need to be set for other roles, or variables that
are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - coaxial.healthchecks

License
-------

BSD

Author Information
------------------

Coaxial, https://64b.it

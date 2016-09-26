pyharmony
=======

Python library for programmatically using a Logitech Harmony Link or Ultimate Hub.

A fork of [bkanuka/pyharmony](https://github.com/bkanuka/pyharmony) with the intent to:
- Make pip/setup.py installable.
- Unify improvments made in other forks.
- Configurable for Harmony Link/Hub differences.
- Better practices for project layout.
- Better error handling!
- Inclusion into Home Assistant (https://home-assistant.io)

Protocol
--------

As the harmony protocol is being worked out, notes are in PROTOCOL.md.

Status
------

* Authentication to Logitech's web service working.
* Authentication to harmony device working.
* Querying for entire device information
* Querying for activity information only
* Querying for current activity
* Starting Activity
* Sending Command

Usage
-----

!!

TODO
----

* Figure out how to detect when the session token expires so we can get a new
  one.
* Figure out a good way of sending commands based on sync state.
* Is it possible to update device configuration?

#!/usr/bin/env python

"""Command line utility for querying the Logitech Harmony."""

from __future__ import print_function
import json
import sys
from pyharmony import auth
from pyharmony import client as harmony_client



def login_to_logitech(email, password, harmony_ip, harmony_port):
    """Logs in to the Logitech service.

    Args:
      args: argparse arguments needed to login.

    Returns:
      Session token that can be used to log in to the Harmony device.
    """
    token = auth.login(email, password)
    if not token:
        sys.exit('Could not get token from Logitech server.')

    session_token = auth.swap_auth_token(
        harmony_ip, harmony_port, token)
    if not session_token:
        sys.exit('Could not swap login token for session token.')

    return session_token



def get_client(email, password, harmony_ip, harmony_port):
    """Connect to the Harmony and return a Client instance."""
    token = login_to_logitech(email, password, harmony_ip, harmony_port)
    client = harmony_client.create_and_connect_client(harmony_ip, harmony_port, token)
    return client


def show_config(email, password, harmony_ip, harmony_port):
    """Connects to the Harmony and prints its configuration."""
    client = get_client(email, password, harmony_ip, harmony_port)
    pprint(client.get_config())
    client.disconnect(send_close=True)
    return 0


def show_current_activity(email, password, harmony_ip, harmony_port):
    """Connects to the Harmony and prints the current activity block
    from the config."""
    client = get_client(email, password, harmony_ip, harmony_port)
    config = client.get_config()
    current_activity_id = client.get_current_activity()

    activity = [x for x in config['activity'] if int(x['id']) == current_activity_id][0]

    client.disconnect(send_close=True)
    return activity['label']



def start_activity(email, password, harmony_ip, harmony_port, new_activity):
    """Connects to the Harmony and starts an activity"""
    client = get_client(email, password, harmony_ip, harmony_port)
    config = client.get_config()
    activities = config['activity']
    labels_and_ids = dict([(a['label'], a['id']) for a in activities])
    matching = [label for label in list(labels_and_ids.keys())
                if new_activity.lower() in label.lower()]
    if len(matching) == 1:
        activity = matching[0]
        print("Found activity named %s (id %s)" % (activity,
                                                   labels_and_ids[activity]))
        client.start_activity(labels_and_ids[activity])
    else:
        print("found too many! %s" % (" ".join(matching)))
    client.disconnect(send_close=True)
    return 0



def power_off(email, password, harmony_ip, harmony_port):
    """Connects to the Harmony and syncs it.
    """
    client = get_client(email, password, harmony_ip, harmony_port)
    client.power_off()
    client.disconnect(send_close=True)
    return 0



def send_command(email, password, harmony_ip, harmony_port, device_id, new_command):
    """Connects to the Harmony and send a simple command."""
    client = get_client(email, password, harmony_ip, harmony_port)
    client.send_command(device_id, command)
    client.disconnect(send_close=True)
    return 0


def sync(email, password, harmony_ip, harmony_port):
    """Connects to the Harmony and syncs it.
    """
    client = get_client(email, password, harmony_ip, harmony_port)
    client.sync()
    client.disconnect(send_close=True)
    return 0


def pprint(obj):
    """Pretty JSON dump of an object."""
    print(json.dumps(obj, sort_keys=True, indent=4, separators=(',', ': ')))

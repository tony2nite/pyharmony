#!/usr/bin/env python

"""Command line utility for querying the Logitech Harmony."""

from __future__ import print_function
import argparse
import logging
import json
import sys

from pyharmony import auth
from pyharmony import client as harmony_client

import code

class EmbeddedConsole(code.InteractiveConsole):
  def start(self):
    try:
      self.interact("Debug console starting...")
    except:
      print("Debug console closing...")

LOGGER = logging.getLogger(__name__)
#WORKING
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


#WORKING
def get_client(email, password, harmony_ip, harmony_port):
    """Connect to the Harmony and return a Client instance."""
    token = login_to_logitech(email, password, harmony_ip, harmony_port)
    client = harmony_client.create_and_connect_client(harmony_ip, harmony_port, token)
    return client

#WORKING
def show_config(email, password, harmony_ip, harmony_port):
    """Connects to the Harmony and prints its configuration."""
    client = get_client(email, password, harmony_ip, harmony_port)
    pprint(client.get_config())
    client.disconnect(send_close=True)
    return 0

#WORKING
def show_current_activity(email, password, harmony_ip, harmony_port):
    """Connects to the Harmony and prints the current activity block
    from the config."""
    client = get_client(email, password, harmony_ip, harmony_port)
    config = client.get_config()
    current_activity_id = client.get_current_activity()

    activity = [x for x in config['activity'] if int(x['id']) == current_activity_id][0]

    client.disconnect(send_close=True)
    return activity['label']


#WORKING
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


#WORKING
def power_off(email, password, harmony_ip, harmony_port):
    """Connects to the Harmony and syncs it.
    """
    client = get_client(email, password, harmony_ip, harmony_port)
    client.power_off()
    client.disconnect(send_close=True)
    return 0


#WORKING
def send_command(email, password, harmony_ip, harmony_port, device_id, new_command):
    """Connects to the Harmony and send a simple command."""
    client = get_client(email, password, harmony_ip, harmony_port)
    client.send_command(device_id, command)
    client.disconnect(send_close=True)
    return 0

#WORKING
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

def repl(args):
    """Connects to the Harmony and start ipython with client"""
    client = get_client(args)
    console = EmbeddedConsole(locals())
    console.start()










def main():
    """Main method for the script."""
    # parser = argparse.ArgumentParser(
        # description='pyharmony utility script',
        # formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # # Required flags go here.
    # required_flags = parser.add_argument_group('required arguments')
    # required_flags.add_argument('--email', required=True, help=(
        # 'Logitech username in the form of an email address.'))
    # required_flags.add_argument(
        # '--password', required=True, help='Logitech password.')
    # required_flags.add_argument(
        # '--harmony_ip', required=True, help='IP Address of the Harmony device.')

    # # Flags with defaults go here.
    # parser.add_argument('--harmony_port', default=5222, type=int, help=(
        # 'Network port that the Harmony is listening on.'))
    # # loglevels = dict((logging.getLevelName(level), level)
                     # # for level in [10, 20, 30, 40, 50])
    # # parser.add_argument('--loglevel', default='INFO', choices=list(loglevels.keys()),
        # # help='Logging level to print to the console.')

    # subparsers = parser.add_subparsers()

    # show_config_parser = subparsers.add_parser(
        # 'show_config', help='Print the Harmony device configuration.')

    # show_config_parser.set_defaults(func=show_config)

    # show_activity_parser = subparsers.add_parser(
        # 'show_current_activity', help='Print the current activity config.')
    # show_activity_parser.set_defaults(func=show_current_activity)

    # start_activity_parser = subparsers.add_parser(
        # 'start_activity', help='Switch to a different activity.')

    # start_activity_parser.add_argument(
        # 'activity', help='Activity to switch to, id or label.')

    # start_activity_parser.set_defaults(func=start_activity)

    # repl_parser = subparsers.add_parser(
        # 'repl', help='Start a client repl')
    # repl_parser.set_defaults(func=repl)

    # power_off_parser = subparsers.add_parser(
        # 'power_off', help='Stop the activity.')
    # power_off_parser.set_defaults(func=power_off)

    # sync_parser = subparsers.add_parser(
        # 'sync', help='Sync the harmony.')
    # sync_parser.set_defaults(func=sync)

    # command_parser = subparsers.add_parser(
        # 'send_command', help='Send a simple command.')
    # command_parser.add_argument('--device_id',
        # help='Specify the device id to which we will send the command.')
    # command_parser.add_argument('--command',
        # help='IR Command to send to the device.')
    # command_parser.set_defaults(func=send_command)

    # args = parser.parse_args()

    # # logging.basicConfig(
        # # level=loglevels[args.loglevel],
        # # format='%(levelname)s:\t%(name)s\t%(message)s')

    # sys.exit(args.func(args))

# if __name__ == '__main__':
    # main()

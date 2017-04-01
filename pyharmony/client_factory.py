#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sleekxmpp


def get_xmpp_client_with_timeout(clazz, *args, timeout=None, retries=None):
    # All these overrides need to happen before the object is instantiated
    sleekxmpp.xmlstream.xmlstream.RESPONSE_TIMEOUT = timeout
    sleekxmpp.xmlstream.xmlstream.RECONNECT_MAX_ATTEMPTS = retries
    print('timeout', timeout)
    if timeout:
        # Override/Patch sleekxmpp's configure_socket method with our timeout
        def _configure_xmpp_socket(self):
            self.socket.settimeout(timeout)
        sleekxmpp.xmlstream.XMLStream.configure_socket = _configure_xmpp_socket
    return clazz(*args)

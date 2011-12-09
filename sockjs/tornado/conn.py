# -*- coding: utf-8 -*-
"""
    sockjs.tornado.conn
    ~~~~~~~~~~~~~~~~~~~

    SockJS connection interface
"""


class SockJSConnection(object):
    def __init__(self, session):
        """Connection constructor.

        `session`
            Associated session
        """
        self.session = session

    # Public API
    def on_open(self, request):
        """Default on_open() handler.

        Override when you need to do some initialization or request validation.
        If you return False, connection will be rejected.

        You can also throw Tornado HTTPError to close connection.

        `request`
            ``ConnectionInfo`` object which contains caller IP address, query string
            parameters and cookies associated with this request.

        For example::

            class MyConnection(SocketConnection):
                def on_open(self, request):
                    self.user_id = request.get_argument('id', None)

                    if not self.user_id:
                        return False

        """
        pass

    def on_message(self, message):
        """Default on_message handler. Must be overridden in your application"""
        raise NotImplementedError()

    def on_close(self):
        """Default on_close handler."""
        pass

    def send(self, message):
        """Send message to the client.

        `message`
            Message to send.
        """
        if self.is_closed:
            return

        if not isinstance(message, basestring):
            message = unicode(message)

        self.session.send_message(message)

    def close(self):
        self.session.close()

    @property
    def is_closed(self):
        """Check if session was closed"""
        return self.session.is_closed

import sys
import unittest
from unittest.mock import patch, Mock

from thermostat.relays.relay import Relay, PIN


class TestRelayMethods(unittest.TestCase):

    def setUp(self):
        gpio = Mock()
        self.relay = Relay(gpio)

    def test_relay_init_state(self):
        self.assertEqual(self.relay.state, None)

    def test_relay_open_conn(self):
        self.relay.open_conn()
        self.assertEqual(self.relay.state, 'open')
        self.assertEqual(self.relay._gpio.output.called, True)
        self.relay._gpio.output.assert_called_once_with(PIN, False)

    def test_relay_close_conn(self):
        self.relay.close_conn()
        self.assertEqual(self.relay.state, 'closed')
        self.assertEqual(self.relay._gpio.output.called, True)
        self.relay._gpio.output.assert_called_once_with(PIN, True)


if __name__ == '__main__':
    unittest.main()

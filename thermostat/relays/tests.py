import sys
import unittest
from unittest.mock import patch, Mock, MagicMock

try:
    from relay import Relay
except ModuleNotFoundError:
    # mocking RPi module as it can be run only on a Raspberry Pi
    sys.modules['RPi'] = MagicMock()
    sys.modules['RPi.GPIO'] = MagicMock()
    from relay import Relay, PIN



class TestRelayMethods(unittest.TestCase):

    def setUp(self):
        self.relay = Relay()

    def test_relay_init_state(self):
        self.assertEqual(self.relay.state, None)

    @patch('relay.GPIO')
    def test_relay_open_conn(self, mock_gpio):
        self.relay.open_conn()
        self.assertEqual(self.relay.state, 'open')
        mock_gpio.output.assert_called()
        mock_gpio.output.assert_called_once_with(PIN, False)

    @patch('relay.GPIO')
    def test_relay_close_conn(self, mock_gpio):
        self.relay.close_conn()
        self.assertEqual(self.relay.state, 'closed')
        mock_gpio.output.assert_called()
        mock_gpio.output.assert_called_once_with(PIN, True)


if __name__ == '__main__':
    unittest.main()

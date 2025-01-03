import unittest
from unittest.mock import MagicMock

from rxconf import AsyncRxConf, RxConf


class TestRxConf(unittest.TestCase):

    def test_repr(self):
        mock_config = MagicMock()
        mock_config.__repr__ = MagicMock(return_value="MockConfigRepresentation")

        rx_conf_instance = RxConf(config=mock_config)

        self.assertEqual(repr(rx_conf_instance), "MockConfigRepresentation")


class TestAsyncRxConf(unittest.TestCase):

    def test_repr(self):
        mock_config = MagicMock()
        mock_config.__repr__ = MagicMock(return_value="MockConfigRepresentation")

        rx_conf_instance = AsyncRxConf(config=mock_config)

        self.assertEqual(repr(rx_conf_instance), "MockConfigRepresentation")

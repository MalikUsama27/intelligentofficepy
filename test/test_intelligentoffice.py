import unittest
from datetime import datetime
from unittest.mock import patch, Mock, PropertyMock

import logging
import mock.GPIO as GPIO
from mock.SDL_DS3231 import SDL_DS3231
from mock.adafruit_veml7700 import VEML7700
from src.intelligentoffice import IntelligentOffice, IntelligentOfficeError

class TestIntelligentOffice(unittest.TestCase):

    @patch.object(GPIO, "input")
    def test_something(self, mock_object: Mock):
        # This is an example of test where I want to mock the GPIO.input() function
        mock_object.return_value = GPIO.HIGH

        # Act
        value = GPIO.input(11)

        # Assert
        mock_object.assert_called_once_with(11)
        self.assertEqual(value, GPIO.HIGH)

        # smart bulb
        def __in_it__(self, pin):
            self.pin = pin
            pin=15
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)

        def turn_on(self):
            GPIO.output(self.pin, GPIO.HIGH)

        def turn_off(self):
            GPIO.output(self.pin, GPIO.LOW)
        #temprature
        def __init__(self, pin):
            self.pin = pin
            pin=20
            GPIO.setup(pin, GPIO.OUT)
            GPIO.setup(pin, GPIO.IN)
        def red_temp(pin):
            GPIO.output(pin, GPIO.HIGH)
        def green_temp(pin):
            GPIO.output(pin, GPIO.LOW)

        pass


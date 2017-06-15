import pendulum
from pendulum import Time
from .. import AbstractTestCase


class StringsTest(AbstractTestCase):

    def test_to_string(self):
        d = Time(1, 2, 3)
        self.assertEqual('01:02:03', str(d))
        d = Time(1, 2, 3, 123456)
        self.assertEqual('01:02:03.123456', str(d))

    def test_set_to_string_format(self):
        Time.set_to_string_format('HH mm ss')
        d = Time(1, 2, 3)
        self.assertEqual('01 02 03', str(d))

    def test_reset_to_string_format(self):
        d = Time(1, 2, 3)
        Time.set_to_string_format('123')
        Time.reset_to_string_format()
        self.assertEqual('01:02:03', str(d))

    def test_repr(self):
        d = Time(1, 2, 3)
        self.assertEqual('Time(1, 2, 3)', repr(d))

        d = Time(1, 2, 3, 123456)
        self.assertEqual('Time(1, 2, 3, 123456)', repr(d))

    def test_format_with_locale(self):
        d = Time(14, 15, 16)
        self.assertEqual('02:15:16 PM',
                         d.format('hh:mm:ss A', locale='fr'))

    def test_strftime(self):
        d = Time(14, 15, 16)
        self.assertEqual('14', d.strftime('%H'))

    def test_for_json(self):
        d = Time(14, 15, 16)
        self.assertEqual('14:15:16', d.for_json())

    def test_format(self):
        d = Time(14, 15, 16)
        self.assertEqual('14:15:16', '{}'.format(d))
        self.assertEqual('15', '{:mm}'.format(d))

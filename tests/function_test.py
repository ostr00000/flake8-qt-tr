import pytest


@pytest.mark.parametrize(
    "code",
    [
        """translate('context', 'Original')""",
        """translate('context', 'Original', 'disambiguation')""",
        """translate('context', 'Original', 'disambiguation', 2)""",
    ],
)
def test_translate_valid(plugin_wrapper, code):
    pl = plugin_wrapper(code)
    assert pl.run() == set()


@pytest.mark.parametrize(
    "code",
    [
        """translate('context', f'Original')""",
        """translate('context', f'Original', 'disambiguation')""",
        """translate('context', f'Original', 'disambiguation', 2)""",
    ],
)
def test_translate_fstring_formatted(plugin_wrapper, code):
    pl = plugin_wrapper(code)
    assert pl.run() == {"1:21 TR011 f-string is resolved before translation call"}


@pytest.mark.parametrize(
    "code",
    [
        """translate('context', 'Original %d' % 1)""",
        """translate('context', 'Original %d' % 1, 'disambiguation')""",
        """translate('context', 'Original %d' % 1, 'disambiguation', 2)""",
    ],
)
def test_translate_printf(plugin_wrapper, code):
    pl = plugin_wrapper(code)
    assert pl.run() == {
        "1:21 TR013 printf-style format is resolved before translation call",
    }

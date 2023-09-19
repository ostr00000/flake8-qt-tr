import pytest


@pytest.mark.parametrize(
    "code",
    [
        """Context.tr('Original')""",
        """Context.tr('Original', 'disambiguation')""",
        """Context.tr('Original', 'disambiguation', 2)""",
    ],
)
def test_tr_valid(plugin_wrapper, code):
    pl = plugin_wrapper(code)
    assert pl.run() == set()


@pytest.mark.parametrize(
    "code",
    [
        """Context.tr(f'Original')""",
        """Context.tr(f'Original', 'disambiguation')""",
        """Context.tr(f'Original', 'disambiguation', 2)""",
    ],
)
def test_tr_fstring_formatted(plugin_wrapper, code):
    pl = plugin_wrapper(code)
    assert pl.run() == {"1:11 TR011 f-string is resolved before translation call"}


@pytest.mark.parametrize(
    "code",
    [
        """Context.tr('Original{}'.format(1))""",
        """Context.tr('Original{}'.format(1), 'disambiguation')""",
        """Context.tr('Original{}'.format(1), 'disambiguation', 2)""",
    ],
)
def test_tr_format_method(plugin_wrapper, code):
    pl = plugin_wrapper(code)
    assert pl.run() == {
        "1:11 TR012 `format` method argument is resolved before translation call",
    }


@pytest.mark.parametrize(
    "code",
    [
        """Context.tr('Original %d' % 1)""",
        """Context.tr('Original %d' % 1, 'disambiguation')""",
        """Context.tr('Original %d' % 1, 'disambiguation', 2)""",
    ],
)
def test_tr_printf(plugin_wrapper, code):
    pl = plugin_wrapper(code)
    assert pl.run() == {
        "1:11 TR013 printf-style format is resolved before translation call",
    }

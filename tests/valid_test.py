import pytest


@pytest.mark.parametrize(
    "code",
    [
        "{fun}({bracket}Original text{bracket})",
        "{fun}({bracket}Original text{bracket}, 'disambiguation')",
        "{fun}({bracket}Original text{bracket}, 'disambiguation', 1)",
    ],
)
@pytest.mark.parametrize("fun", ["Context.tr", "translate"])
@pytest.mark.parametrize("bracket", ["'", '"', "'''", '"""'])
def test_tr_valid(plugin_wrapper, code: str, bracket: str, fun: str):
    pl = plugin_wrapper(code.format(fun=fun, bracket=bracket))
    assert pl.run() == set()


@pytest.mark.parametrize(
    "code",
    [
        "",
        "call()",
        "tr()",
        "_tr()",
        "x.translate()",
        "x._tr()",
    ],
)
def test_valid_empty(plugin_wrapper, code):
    pl = plugin_wrapper(code)
    assert pl.run() == set()

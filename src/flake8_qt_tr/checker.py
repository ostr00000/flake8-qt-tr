from __future__ import annotations

import ast
import importlib.metadata
from importlib.metadata import version
from typing import TYPE_CHECKING, Generic, TypeAlias, TypeVar

if TYPE_CHECKING:
    from collections.abc import Iterator

try:
    __version__ = version("flake8-qt-tr")
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.0.0-dev"

FlakeErrorTuple: TypeAlias = tuple[int, int, str, type]
T = TypeVar("T")


class Contain(Generic[T]):
    def __init__(self, data: list[T]) -> None:
        self.data = data

    def __eq__(self, other: T) -> bool:
        return other in self.data


class TrChecker:
    name = "flake8-qt-tr"
    version = __version__

    TR011_fstring = "TR011 f-string is resolved before translation call"
    TR012_format = "TR012 `format` method argument is resolved before translation call"
    TR013_bin_op = "TR013 printf-style format is resolved before translation call"

    def __init__(self, tree: ast.AST) -> None:
        self._tree = tree

    def run(self) -> Iterator[FlakeErrorTuple]:
        for node in ast.walk(self._tree):
            if not isinstance(node, ast.Call):
                continue

            match node:
                case ast.Call(
                    func=ast.Attribute(attr="tr"),
                    args=[text_node, _, _] | [text_node, _] | [text_node],
                ):
                    # method call (sourceText, disambiguation=None, n=-1)
                    # https://doc.qt.io/qt-6/qobject.html#tr
                    yield from self._gen_error(text_node)

                case ast.Call(
                    func=ast.Name(id="translate"),
                    args=[_, text_node, _, _] | [_, text_node, _] | [_, text_node],
                ):
                    # function call (context, sourceText, disambiguation=None, n=-1)
                    # https://doc.qt.io/qt-6/qcoreapplication.html#translate
                    yield from self._gen_error(text_node)

                case ast.Call(
                    func=ast.Name(id="QT_TR_NOOP"),
                    args=[text_node],
                ):
                    # function call (sourceText)
                    # https://doc.qt.io/qt-6/qttranslation-proxy.html#QT_TR_NOOP
                    yield from self._gen_error(text_node)

                case ast.Call(
                    func=ast.Name(id="QT_TRANSLATE_NOOP"),
                    args=[_, text_node],
                ):
                    # function call (context, sourceText)
                    # https://doc.qt.io/qt-6/qttranslation-proxy.html#QT_TRANSLATE_NOOP
                    yield from self._gen_error(text_node)

    def _gen_error(self, error_node: ast.AST) -> Iterator[FlakeErrorTuple]:
        match error_node:
            case ast.JoinedStr():
                yield self._create_error(error_node, self.TR011_fstring)
            case ast.Call(func=ast.Attribute(attr="format")):
                yield self._create_error(error_node, self.TR012_format)
            case ast.BinOp(op=ast.Mod(), left=ast.Str()):
                yield self._create_error(error_node, self.TR013_bin_op)

    def _create_error(self, node: ast.AST, msg: str) -> FlakeErrorTuple:
        return node.lineno, node.col_offset, msg, type(self)

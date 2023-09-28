#!/usr/bin/env python

from panflute import *


def action(elem, _):
    if not isinstance(elem, CodeBlock):
        return
    path = elem.attributes.get("include", None)

    if path is None:
        return

    snippet = elem.attributes.get("snippet", None)

    with open(path, "r") as f:
        lines = f.readlines()

    if snippet is not None:
        code_lines = ""
        read = False
        for line in lines:
            line = line.strip()

            if read is False and line == f"// start snippet {snippet}":
                read = True
                continue

            if read is True and line == f"// end snippet {snippet}":
                break

            if read:
                code_lines += f"{line}\n"

    else:
        code_lines = "".join(lines)

    return CodeBlock(code_lines, elem.identifier, elem.classes, {})


def main(doc=None):
    return run_filter(action, doc=doc)


if __name__ == '__main__':
    main()

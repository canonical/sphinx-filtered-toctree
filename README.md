# filtered-toctree

filtered-toctree allows you to filter pages out of your documentation's navigation
by prefixing ToC entries with configurable tags.

## Basic usage

First, list the tags you wish to exclude with `toc_filter_exclude` in your `conf.py`
file:

```
toc_filter_exclude = ["exclude", "hidden"]
```

To filter entries out of your documentation's navigation, prefix either the document's
label or target with one of the tags defined in `toc_filter_exclude`:

```
.. filtered-toctree::

    :exclude:how-to-code
    Unit testing <:hidden:unit-testing>

```

Aside from this added functionality, `filtered-toctree` behaves exactly the same as
the `toctree` directive.

## Project setup

filtered-toctree is published on PyPI and can be installed with:

```bash
pip install filtered-toctree
```

After adding filtered-toctree to your Python project, update your Sphinx's conf.py file
to include filtered-toctree as one of its extensions:

```python
extensions = [
    "filtered_toctree"
]
```

## Community and support

You can report any issues or bugs on the project's [GitHub
repository](https://github.com/canonical/filtered-toctree).

filtered-toctree is covered by the [Ubuntu Code of
Conduct](https://ubuntu.com/community/ethos/code-of-conduct).

## License and copyright

filtered-toctree is released under the [GPL-3.0 license](LICENSE).

© 2025 Canonical Ltd.

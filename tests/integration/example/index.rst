
Test doc
========

.. filtered-toctree::
    :caption: With filters

    visible
    :exclude:not visible <hidden>
    not visible <:exclude:hidden>

.. filtered-toctree::
    :caption: Without filters

    :include:visible
    hidden

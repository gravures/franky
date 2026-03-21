# Ipython-franky

An Ipython dark theme extension.

## Installing

Install the python module inside the virtual environment of your `Ipython`.
If for example, you have installed `Ipython` with the `uv` tool command, you could do:

```bash
uv pip install --inexact --prefix="$(uv tool dir)"/ipython franky-ipython
```

Add the module to the extensions list in your `ipython_config.py` file.

```python
c = get_config()
c.InteractiveShellApp.extensions.append("franky_ipython")
```

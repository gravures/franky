# Franky

![Python Version from PEP 621 TOML](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2Fgravures%2Ffranky%2Fmain%2Fpyproject.toml) ![GitHub License](https://img.shields.io/github/license/gravures/standard-deluxe) ![OS support](https://img.shields.io/badge/OS-macOS%20Linux%20Windows-red) ![downloads](assets/downloads.svg)

**Franky** is a color scheme designed for coding, it start as **github-dark** inspired theme frankensteined with **catppuccin-mocha**. So, **Franky** works well along **catppuccin** dark themes when not available for an application.

## Preview

![Franky](assets/franky.png)

## Installation

**Franky** comes with a python installer. The preferred way to install the *cli* is using [UV](https://docs.astral.sh/uv/):

```bash
uv tool install franky-theme
```

or you could also use [PIPX](https://pipx.pypa.io/stable/):

```bash
pipx install franky-theme
```

## Usage

Most of the themes are simple config file generated on demand by the *cli* and installed on preconfigured location (some themes — like *ipython* — have specific instalation procedure).

```bash
$ franky install ghostty
```

![Terminal](assets/term.gif)

## Road Map

- [x] Helix editor
- [x] Ipython shell
- [x] Ghostty
- [x] Qman
- [ ] shell: LS_COLORS + man colors + ncurse colors
- [ ] Yazi
- [ ] Delta
- [ ] Tmux
- [ ] Zellij
- [ ] Glow
- [ ] CSS
- [ ] Gtk.SourceView
- [ ] Gnome Shell

## Contributing

Contributors are always welcome. Feel free to grab an [issue](https://github.com/gravures/standard-deluxe/issues) to work on or make a suggested improvement. If you wish to contribute, please read the [Contribution Guide](https://github.com/gravures/standard-deluxe/contributing.md) and [Code of Conduct](https://github.com/gravures/standard-deluxe/code_of_conduct.md). <!-- rumdl-disable-line MD013 -->

## License

Use of this repository is authorized under the [GPL-3.0](https://github.com/gravures/standard-deluxe/LICENSE).

# Lume

**Lume** is a minimalist brightness control utility built in Python, GTK4, and Libadwaita for Linux. Designed around the philosophy of "open, adjust the slider, and close", it aims for extreme simplicity without sacrificing power.

Lume features universal support: it fluidly controls both built-in displays (laptop screens) via `sysfs`, and multiple external monitors connected via HDMI/DisplayPort through the DDC/CI protocol (using `ddcutil`).

## Installation

The easiest and recommended way to install Lume is by using the native installers. They automatically download and configure everything (Python, GTK4, dependencies) so you don't have to worry.

### Ubuntu, Linux Mint, Debian (.deb)
Download the latest `.deb` file from the GitHub **Releases** tab and install it with a double click. Alternatively, via terminal:
```bash
sudo apt install ./lume_1.0.0-1_all.deb
```

### Fedora, CentOS, openSUSE (.rpm)
Download the latest `.rpm` file from the GitHub **Releases** tab and install it with a double click. Alternatively, via terminal:
```bash
sudo dnf install ./lume-1.0.0-1.noarch.rpm
```

---

## Uninstallation

Since Lume uses native installers, it can be easily removed through your system's package manager.

**To uninstall on Ubuntu/Debian:**
```bash
sudo apt remove lume
```

**To uninstall on Fedora/openSUSE:**
```bash
sudo dnf remove lume
```

If you want to completely clean up local configuration files and user routines:
```bash
rm -rf ~/.config/lume
rm -f ~/.config/autostart/lume-daemon.desktop
rm -f ~/.cache/lume.json
```

---

## Key Features
- **Minimalist Design:** Native integration with the GNOME ecosystem (GTK4 + Libadwaita).
- **Simultaneous Control:** Adjust the brightness of multiple screens at the same time asynchronously, without the app freezing or stuttering.
- **Smart Detection:** The application caches external monitors and syncs hardware status instantly upon opening.
- **Automated Routines:** A built-in invisible background *Daemon* allows you to schedule independent brightness adjustments for each monitor at specific times.

## FAQ (Permissions)
To control external monitors, Linux requires special permissions on the i2c bus. The `.deb` and `.rpm` packages provided above automatically install the correct *udev* rules. If your external monitors don't show up the first time, **restart your computer** to apply the video group permissions to your user account.

## Packaging from Source (For Developers)

If you have cloned this repository and want to compile your own installer locally:

**Build .deb package (Ubuntu/Debian):**
```bash
sudo apt install devscripts debhelper
dpkg-buildpackage -us -uc -b
```

**Build .rpm package (Fedora/RedHat):**
```bash
rpmbuild -ba lume.spec
```

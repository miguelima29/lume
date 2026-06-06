Name:           lume
Version:        1.0.0
Release:        1%{?dist}
Summary:        Minimalist brightness control utility
License:        GPLv3+
URL:            https://github.com/lume/lume
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch

Requires:       python3-gobject
Requires:       gtk4
Requires:       libadwaita
Requires:       ddcutil

%description
Lume is a minimalist brightness control utility focused on the 
"open, adjust the slider, and close" philosophy. Compatible with external 
monitors via DDC/CI and laptop screens via sysfs.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
# Instala o executável Python
install -d -m 0755 $RPM_BUILD_ROOT%{_bindir}
install -m 0755 lume $RPM_BUILD_ROOT%{_bindir}/lume

# Instala o .desktop
install -d -m 0755 $RPM_BUILD_ROOT%{_datadir}/applications
install -m 0644 lume.desktop $RPM_BUILD_ROOT%{_datadir}/applications/lume.desktop

# Instala o ícone SVG
install -d -m 0755 $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps
install -m 0644 lume.svg $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps/lume.svg

# Instala as regras udev
install -d -m 0755 $RPM_BUILD_ROOT%{_udevrulesdir}
install -m 0644 99-lume.rules $RPM_BUILD_ROOT%{_udevrulesdir}/99-lume.rules

%post
# Recarrega o udev para aplicar permissões de brilho
udevadm control --reload-rules && udevadm trigger || true
# Atualiza os caches da interface
update-desktop-database -q || true
gtk-update-icon-cache -q %{_datadir}/icons/hicolor || true

%files
%{_bindir}/lume
%{_datadir}/applications/lume.desktop
%{_datadir}/icons/hicolor/scalable/apps/lume.svg
%{_udevrulesdir}/99-lume.rules

%changelog
* Fri Jun 05 2026 Desenvolvedor <dev@lume.local> - 1.0.0-1
- Release inicial do Lume.

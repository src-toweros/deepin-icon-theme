Name:           deepin-icon-theme
Version:        2020.06.28
Release:        1
Summary:        Icons for the Deepin Desktop Environment
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-icon-theme
Source0:        %{name}-%{version}.orig.tar.xz
BuildArch:      noarch
BuildRequires:  gtk-update-icon-cache
BuildRequires:  xorg-x11-apps
Requires:       papirus-icon-theme
Conflicts:      deepin-cursor-theme

%description
%{summary}.

%package      -n sea-icon-theme
Summary:      Deepin Sea Icons
Conflicts:    deepin-icon-theme < 15.12.65

%description -n sea-icon-theme
 Deepin Sea Icons 
 This package is DeepinIconTheme Sea

%prep
%setup -q -n %{name}-%{version}

%build
make

%install
sed -i -E '/bloom-v20/d' Makefile
mkdir -p %{buildroot}/usr/share/icons/bloom-classic
cp -r bloom-classic/* %{buildroot}/usr/share/icons/bloom-classic
mkdir -p %{buildroot}/usr/share/icons/bloom-classic-dark
cp -r bloom-classic-dark/* %{buildroot}/usr/share/icons/bloom-classic-dark
mkdir -p %{buildroot}/usr/share/icons/Sea
cp -r Sea/* %{buildroot}/usr/share/icons/Sea/

%{__make} install-icons DESTDIR=%{?buildroot} INSTALL="%{__install} -p" PREFIX=%{_prefix}
%{__make} install-cursors DESTDIR=%{?buildroot} INSTALL="%{__install} -p" PREFIX=%{_prefix}
%{__make} hicolor-links

%post
touch --no-create %{_datadir}/icons/deepin &>/dev/null || :
touch --no-create %{_datadir}/icons/deepin-dark &>/dev/null || :
touch --no-create %{_datadir}/icons/Sea &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
  touch --no-create %{_datadir}/icons/deepin &>/dev/null
  /usr/bin/gtk-update-icon-cache %{_datadir}/icons/deepin &>/dev/null || :
  touch --no-create %{_datadir}/icons/deepin-dark &>/dev/null
  /usr/bin/gtk-update-icon-cache %{_datadir}/icons/deepin-dark &>/dev/null || :
  touch --no-create %{_datadir}/icons/Sea &>/dev/null
  /usr/bin/gtk-update-icon-cache %{_datadir}/icons/Sea &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/deepin &>/dev/null || :
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/deepin-dark &>/dev/null || :
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/Sea &>/dev/null || :

%files
%license LICENSE
%{_datadir}/icons/bloom/
%{_datadir}/icons/bloom-classic/
%{_datadir}/icons/bloom-classic-dark/
%{_datadir}/icons/bloom-dark


%files -n sea-icon-theme
%license LICENSE
%{_datadir}/icons/Sea/


%changelog
* Thu Jun 11 2020 uoser <uoser@uniontech.com> - 2020.05.25
- Update to 2020.05.25 

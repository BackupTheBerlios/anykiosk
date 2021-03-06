#spec for building rpm for alt-linux with gear

%define ver 0.0.3
%define reldate 20101216

Name: anykiosk
Version: %ver.%reldate
Release: alt0.M50P.1

Summary: Easy kiosk mode tuning for various programs
License: GPL
Group: System/Configuration/Other

Vendor: UnixForum.org (Denjs, Minoru-kun, Skull)
Url: http://anykiosk.berlios.de
#Packager: Denjs <denjs@users.berlios.de>
Packager: Andrey Cherepanov <cas@altlinux.org>

Source: anykiosk-0.0.3.20101216.tar.gz
Source1: %name.pamd
Source2: %name.security

BuildArch: noarch

BuildPreReq: python >= 2.5
BuildPreReq: python-module-PyQt4 >= 4.5
BuildPreReq: perl 
BuildPreReq: perl-Encode >= 2.37 
BuildPreReq: perl-PerlIO >= 1:5.8

# Support ALT Linux consolehelper
Requires:    consolehelper
BuildPreReq: libpam-devel

#Requires: python >= 2.5
#Requires: python-module-PyQt4 >= 4.5
#Requires: perl 
#Requires: perl-Encode >= 2.37 
#Requires: perl-PerlIO >= 1:5.8

#Requires:
#python-module-setuptools

%description
AnyKiosk - a Point-and-Click tool for system administrators 
to enable KIOSK features for various software.
0.0.2beta release includes only FireFox 3.6 plugin.

%description -l ru_RU.UTF-8
AnyKiosk - утилита настройки различных программ в режим киоска -
режим с заблокированными от изменения настройками и ограниченной 
функциональностью. Просто отметье галочками нужные программы и
нажмите "применить".
Версия 0.0.2 поставляется с плагином для FireFox 3.6.

%prep
%setup -q
cp %SOURCE1 .
cp %SOURCE2 .

%build

%install
#python_install
%make_install DESTDIR=%buildroot install

# Adapt for consolehelper
mkdir -p %buildroot%_sbindir/
mv %buildroot%_bindir/%name %buildroot%_sbindir
ln -s %_libexecdir/consolehelper/helper %buildroot%_bindir/%name
install -pD -m640 %name.pamd %buildroot%_sysconfdir/pam.d/%name
install -pD -m640 %name.security %buildroot%_sysconfdir/security/console.apps/%name

%files
%_bindir/%name
%_sbindir/%name
%dir %_datadir/%name
%dir %_datadir/%name/tmp
%_datadir/%name/*.py
%_datadir/%name/moz-byteshift.pl
%config(noreplace) %_sysconfdir/pam.d/%name
%config(noreplace) %_sysconfdir/security/console.apps/%name

%changelog
* Tue Dec 14 2010 Andrey Cherepanov <cas@altlinux.org> 0.0.2.20101210-alt0.M50P.1
- backport to p5

* Sun Dec 12 2010 Denjs <denjs@users.berlios.de> 0.0.2.20101210-alt1
[ Denjs ]
- Initial build for Sisyphus
  + firefox 3.6  plugin

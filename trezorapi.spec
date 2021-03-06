Name:           trezorapi
Version:        1.1.6
Release:        1%{?dist}
Summary:        Trezor-K2 application

License:        Proprietary
URL:            http://trezorrussia.ru/
Source0:        https://panov.email/%{name}-%{version}.tar.xz

BuildArch:      x86_64

BuildRequires:  systemd-rpm-macros 
Requires:       postgresql-server

%description
This package contains Trezor-K2 application. 
Application for setup and basic monitoring of Trezor secuity devices.

%prep
%autosetup

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/opt/trezor
mkdir -p $RPM_BUILD_ROOT/opt/trezor/frontend
mkdir -p $RPM_BUILD_ROOT/opt/trezor/docs
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
cp -r  %{_builddir}/%{name}-%{version}/frontend $RPM_BUILD_ROOT/opt/trezor/
cp -r  %{_builddir}/%{name}-%{version}/docs $RPM_BUILD_ROOT/opt/trezor/
ln -sf /opt/trezor/%{name}-%{version} $RPM_BUILD_ROOT/opt/trezor/%{name}
install -D -m 0755 %{_builddir}/%{name}-%{version}/trezorapi-%{version} $RPM_BUILD_ROOT/opt/trezor/trezorapi-%{version}
install -D -m 0644 %{_builddir}/%{name}-%{version}/ActivatorPublicKey.key $RPM_BUILD_ROOT/opt/trezor/ActivatorPublicKey.key
install -D -m 0644 %{_builddir}/%{name}-%{version}/trezorapi.toml $RPM_BUILD_ROOT/opt/trezor/trezorapi.toml
install -D -m 0644 %{_builddir}/%{name}-%{version}/trezorapi.service $RPM_BUILD_ROOT%{_unitdir}/trezorapi.service

%files
/opt/trezor/frontend/*
/opt/trezor/docs/*
/opt/trezor/%{name}-%{version}
/opt/trezor/%{name}
/opt/trezor/%{name}.toml
/opt/trezor//ActivatorPublicKey.key
%{_unitdir}/trezorapi.service

%preun
%systemd_preun trezorapi.service
exit 0

%postun
%systemd_postun_with_restart trezorapi.service

%changelog
* Fri Jul 29 2022 Alexei Panov <alexei@panov.email> - 1.1.6-1
- new release

* Thu Jul 28 2022 Alexei Panov <alexei@panov.email> - 1.1.4-1
- new release

* Mon Jul 25 2022 Alexei Panov <alexei@panov.email> - 1.1.3-1
- new release

* Thu Jul  7 2022 Alexei Panov <alexei@panov.email> - 1.1.2-2
- fixed name collisions

* Thu Jul  7 2022 Alexei Panov <alexei@panov.email> - 1.1.2-1
- new release

* Thu Jun 30 2022 Alexei Panov <alexei@panov.email> - 1.1.1-1
- new release

* Fri Apr  8 2022 Alexei Panov <alexei@panov.email> - 1.1.0-1
- new release

* Wed Mar 16 2022 Alexei Panov <alexei@panov.email> - 1.0.9-3
- wrong install instructions

* Wed Mar 16 2022 Alexei Panov <alexei@panov.email> - 1.0.9-2
- changes in spec-file, requires changed to postgresql-server

* Tue Mar 15 2022 Alexei Panov <alexei@panov.email> - 1.0.9-1
- Initial build


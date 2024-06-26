Name:           trezorapi
Version:        1.2.26
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
install -D -m 0755 %{_builddir}/%{name}-%{version}/trezor-start.sh $RPM_BUILD_ROOT/opt/trezor/trezor-start.sh
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
/opt/trezor/trezor-start.sh
%{_unitdir}/trezorapi.service

%preun
%systemd_preun trezorapi.service
exit 0

%postun
%systemd_postun_with_restart trezorapi.service

%changelog
* Wed Jun 26 2024 Alexei Panov <alexei@panov.email> - 1.2.26-1
- new release

* Mon May  6 2024 Alexei Panov <alexei@panov.email> - 1.2.25-1
- new release

* Fri Mar 15 2024 Alexei Panov <alexei@panov.email> - 1.2.24-1
- new release

* Fri Mar  1 2024 Alexei Panov <alexei@panov.email> - 1.2.19-1
- new release

* Wed Jan 31 2024 Alexei Panov <alexei@panov.email> - 1.2.18-1
- new release

* Fri Dec 29 2023 Alexei Panov <alexei@panov.email> - 1.2.17-1
- new release

* Thu Dec 28 2023 Alexei Panov <alexei@panov.email> - 1.2.16-1
- new release

* Fri Nov 17 2023 Alexei Panov <alexei@panov.email> - 1.2.13-1
- new release

* Wed Oct 25 2023 Alexei Panov <alexei@panov.email> - 1.2.12-1
- new release

* Wed Jun 28 2023 Alexei Panov <alexei@panov.email> - 1.2.11-1
- new release

* Sun Jun 25 2023 Alexei Panov <alexei@panov.email> - 1.2.10-1
- new release

* Thu Apr 20 2023 Alexei Panov <alexei@panov.email> - 1.2.8-1
- new release

* Fri Apr  7 2023 Alexei Panov <alexei@panov.email> - 1.2.4-1
- new release

* Fri Mar 31 2023 Alexei Panov <alexei@panov.email> - 1.2.3-1
- new release

* Thu Mar 30 2023 Alexei Panov <alexei@panov.email> - 1.2.2-1
- new release

* Mon Mar 27 2023 Alexei Panov <alexei@panov.email> - 1.2.1-1
- new release

* Thu Dec  8 2022 Alexei Panov <alexei@panov.email> - 1.1.9-1
- new release

* Mon Dec  5 2022 Alexei Panov <alexei@panov.email> - 1.1.8-1
- new release

* Mon Oct 31 2022 Alexei Panov <alexei@panov.email> - 1.1.7-1
- new release

* Thu Oct  6 2022 Alexei Panov <alexei@panov.email> - 1.1.6-2
- added shell-script for start service

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


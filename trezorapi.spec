Name:           trezorapi
Version:        1.0.9
Release:        2%{?dist}
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
cp -r  %{_builddir}/%{name}-%{version}/frontend $RPM_BUILD_ROOT/opt/trezor/frontend
cp -r  %{_builddir}/%{name}-%{version}/docs $RPM_BUILD_ROOT/opt/trezor/docs
# install -D -m 0644 %{_builddir}/%{name}-%{version}/trezorapi $RPM_BUILD_ROOT/opt/trezor/trezorapi
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
* Wed Mar 16 2022 Alexei Panov <alexei@panov.email> - 2
- changes in spec-file, requires changed to postgresql-server

* Tue Mar 15 2022 Alexei Panov <alexei@panov.email> - 1
- Initial build


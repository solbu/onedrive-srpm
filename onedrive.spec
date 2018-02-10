%define name onedrive
%define debug_package %{nil}
%define version 1.1.1
%define release 1

Summary: A complete tool to interact with OneDrive on Linux. Built following the UNIX philosophy.
Name: %{name}
Version: %{version}
Release: %{release}
Vendor: Patrick Pichon <patrick@pichon.me>
Source: https://github.com/skilion/onedrive.tar
Patch0: onedrive-copr.patch
License: GPL
Group: System Environment/Daemons
Buildroot: /var/tmp/%{name}-%{version}-%{release}-root
BuildRequires: ldc sqlite-devel libcurl-devel
Requires: libcurl sqlite
Requires(post): systemd
Requires(preun): systemd 

%description
A complete tool to interact with OneDrive on Linux. Built following the UNIX philosophy.

%prep
%setup -q
%patch0 -p0

%build
make DC=ldc2 PREFIX=/usr/ DESTDIR=$RPM_BUILD_ROOT all

%install
mkdir -p %{buildroot}/usr/bin
install -D onedrive %{buildroot}/usr/bin/onedrive
install -D -m 644 onedrive.service %{buildroot}/usr/lib/systemd/user/onedrive.service


%files
%doc CHANGELOG.md LICENSE README.md config
%license LICENSE
%defattr(-,root,root)
%attr(555,bin,bin) /usr/bin/onedrive
%attr(555,bin,bin) /usr/lib/systemd/user/onedrive.service

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sat Feb 10 2018 Patrick Pichon <patrick@pichon.me>
add config file, and few addition prerequisites

* Fri Feb 9 2018 Patrick Pichon <patrick@pichon.me>
ready for Copr

* Thu Feb 8 2018 Patrick Pichon <patrick@pichon.me>
initial version


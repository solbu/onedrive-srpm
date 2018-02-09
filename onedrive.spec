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
Requires: libcurl sqlite
BuildRequires: ldc sqlite-devel libcurl-devel

%description
A complete tool to interact with OneDrive on Linux. Built following the UNIX philosophy.
Features:

    State caching
    Real-Time file monitoring with Inotify
    Resumable uploads
    Support OneDrive for Business (part of Office 365)
    Shared folders (not Business)

What's missing:

    While local changes are uploaded right away, remote changes are delayed
    No GUI



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
%doc CHANGELOG.md LICENSE README.md
%defattr(-,root,root)
%attr(555,bin,bin) /usr/bin/onedrive
%attr(555,bin,bin) /usr/lib/systemd/user/onedrive.service

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Fri Feb 9 2018 Patrick Pichon <patrick@pichon.me>
ready for Copr

* Thu Feb 8 2018 Patrick Pichon <patrick@pichon.me>
initial version


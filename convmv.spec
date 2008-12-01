%define name convmv
%define version 1.13
%define release %mkrel 1

Summary: Converts filenames from one encoding to another
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.j3e.de/linux/convmv/%{name}-%{version}.tar.gz
Source1: testsuite2.tar.bz2
License: GPLv2+
Group: File tools
Url: http://j3e.de/linux/convmv/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch

%description
This is a script for renaming files from one file name encoding to another,
e.g. from ISO-LATIN-1 to UTF-8.

%prep
%setup -q -a 1

%build
make 
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall PREFIX=%buildroot%_prefix

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes CREDITS TODO
%_bindir/%name
%_mandir/man1/%name.1*

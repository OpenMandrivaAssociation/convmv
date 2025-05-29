%define name convmv
%define version 1.15
%define release 2

Summary: Converts filenames from one encoding to another
Name: %{name}
Version: 2.06
Release: 1%{release}1
Source0: http://www.j3e.de/linux/convmv/%{name}-%{version}.tar.gz
Source1: testsuite2.tar.bz2
License: GPLv2+
Group: File tools
Url: https://j3e.de/linux/convmv/
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


%changelog
* Mon Aug 22 2011 GÃ¶tz Waschk <waschk@mandriva.org> 1.15-1mdv2012.0
+ Revision: 696080
- update to new version 1.15

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 1.14-2mdv2011.0
+ Revision: 437105
- rebuild

* Fri Dec 19 2008 GÃ¶tz Waschk <waschk@mandriva.org> 1.14-1mdv2009.1
+ Revision: 315999
- update to new version 1.14

* Mon Dec 01 2008 GÃ¶tz Waschk <waschk@mandriva.org> 1.13-1mdv2009.1
+ Revision: 308708
- update to new version 1.13

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.12-3mdv2009.0
+ Revision: 243629
- rebuild

* Thu Jan 24 2008 Funda Wang <fwang@mandriva.org> 1.12-1mdv2008.1
+ Revision: 157322
- New version 1.12

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Jul 01 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.10-1mdv2008.0
+ Revision: 46425
- Import convmv




* Wed Jun 28 2006 Götz Waschk <waschk@mandriva.org> 1.10-1mdv2007.0
- update test suite
- New release 1.10

* Sun Dec 11 2005 Götz Waschk <waschk@mandriva.org> 1.09-1mdk
- drop patch
- New release 1.09
- use mkrel

* Wed May 11 2005 Götz Waschk <waschk@mandriva.org> 1.08-1mdk
- initial package

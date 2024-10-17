%define name webgrep
%define version 2.12
%define release 6


Summary: Web page search utilities
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: Development/Other
Source: %{name}-%{version}.tar.bz2
Patch: %{name}-makefile.patch.bz2
URL: https://www.linuxfocus.org/~guido/
Buildroot: %{_tmppath}/%{name}-buildroot

%description
webgrep is a set of search utilities for web-masters. This package includes
7 utilities:

srcgrep is a utility to search for the IMG/SRC-tag or the BODY/BACKGROUND-tag 
in web-pages and display the path to the referenced images in a nice readable 
way.

hrefgrep is a search utility for the <... href=...> tag.

webfgrep is a poor man's web search engine. A script (e.g perl) must still
be written to do the cgi-bin. webfgrep is good for website up to 1 Mb of 
html. A small cgi-bin called websearch comes with this package. It is written
in perl and you can adapt it to your web-site.
webfgrep is basically just an exteremly fast fgrep program that leaves out
the html tags.

blnkcheck is a program to check for broken links on the server.
This is probably the most powerful program in this toolkit.

httpcheck is a post processor for blnkcheck and is written in perl. It can
be used to check also absolute http links in web-pages.

lshtmlref is a program to build tar archives from a given list of web-pages.
It helps you to include all GIFs, text files, etc.. in the archives.

taggrep is a program to grep for html tags. E.g search for meta tags or
list the title of a number of web pages.

%prep
rm -rf $RPM_BUILD_ROOT

%setup

%patch 

%build
%make  CFLAGS="$RPM_OPT_FLAGS"

%install
make DESTDIR=$RPM_BUILD_ROOT install


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root)
%doc README cgi-bin
%{_bindir}/*
%{_mandir}/man1/*



%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 2.12-5mdv2010.0
+ Revision: 434735
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.12-4mdv2009.0
+ Revision: 261924
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.12-3mdv2009.0
+ Revision: 255844
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 2.12-1mdv2008.1
+ Revision: 129299
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import webgrep


* Sat Aug 28 2004 Franck Villaume <fvill@freesurf.fr> 2.12-1mdk
- 2.12

* Mon Mar 17 2003 Lenny Cartier <lenny@mandrakesoft.com> 2.11-1mdk
- regenerate patch0

* Thu Jan 02 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.9-3mdk
- build release
- fix no-clean-section

* Fri Aug 31 2001 Etienne Faure <etienne@mandrakesoft.com> 2.9-2mdk
- rebuild

* Wed Dec 27 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 2.9-1mdk
- new and shiny source.
- use our own optimizations.

* Thu Oct 19 2000 Lenny Cartier <lenny@mandrakesoft.com> 2.7-1mdk
- new in contribs
- makefile patch

Summary:	Improved color IRC client with built-in scripts
Summary(pl):	Ulepszony, kolorowy klient IRC z wbudowanymi skryptami
Name:		BitchX
Version:	75p3
Release:	1
Source0:	ftp://ftp.bitchx.com/pub/BitchX/source/ircii-pana-%{version}.tar.gz
Source1:	ircII.servers
Source2:	ftp://ftp.acronet.net/pub/ircii/epic3.004-help.tar.gz
Source3:	bitchx.1
Copyright:	GPL
Group:		Applications/Communications
Group(pl):	Aplikacje/Komunikacja
Patch0:		%{name}-75.patch
Patch1:		%{name}-pld.patch
Patch2:		%{name}-75.iso2.patch
Patch3:         %{name}-tcl.patch
Patch4:         %{name}-script.patch
Patch5:		BitchX-config.patch
URL:            ftp://ftp.bitchx.com/pub/BitchX/source/
BuildRoot:	/tmp/%{name}-%{version}-root
 
%description 
BitchX is a popular ANSI color ircII client by panasync. It
incorporates various features that would normally require a
script. It's interface is more colorful and cleaner than ircII.

%description -l pl 
BitchX jest popularnym klientem ircII. Jego interfejs jest bardziej 
kolorowy i przej¿ysty ni¿ interfejs standardowego kilienta ircII.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p0

%build
gzip -dc %{SOURCE2} | tar -xf -

CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -w" LDFLAGS="-s" \
./configure %{_target_platform} \
	--prefix=%{_prefix}
make all 

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/usr/{bin,share/BitchX/{script,translation,help}}
install -d $RPM_BUILD_ROOT/{%{_mandir}/man1,etc/irc}

strip source/BitchX
strip source/wserv
strip source/scr-bx

install %{SOURCE1} $RPM_BUILD_ROOT/etc/irc
install %{SOURCE3} $RPM_BUILD_ROOT%{_mandir}/man1
echo .so bitchx.1 > $RPM_BUILD_ROOT%{_mandir}/man1/BitchX.1

install source/BitchX $RPM_BUILD_ROOT%{_bindir}
install source/wserv $RPM_BUILD_ROOT%{_bindir}/wserv-bx
install source/scr-bx $RPM_BUILD_ROOT%{_bindir}
install install-bitchx $RPM_BUILD_ROOT%{_bindir}

install BitchX.help $RPM_BUILD_ROOT%{_datadir}/BitchX
cp -a help $RPM_BUILD_ROOT%{_datadir}/BitchX

gzip -9nf Changes doc/* BitchX.quit BitchX.reasons \
	$RPM_BUILD_ROOT%{_mandir}/man1/* || :

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755) 
%doc Changes.gz doc/* BitchX* 

%attr(755,root,root) %{_bindir}/*

%{_datadir}/BitchX

%config(noreplace) %verify(not md5 size mtime) /etc/irc/*
%{_mandir}/man1/*

%changelog
* Thu Oct 01 1998 Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>
- wserv is now as wserv-bx (modifiet to avoid conflicts with others
  irc clients)
- irclib is now ${prefix}/lib/BitchX
- added /usr/lib/BitchX with subdirectories
- modified pl translations
- added configuration /etc/irc/ircII.servers
- added help (from EPIC3 but should be from EPIC4!)
- added pl message in %post
- now BitchX uses /usr/lib/BitchX/BitchX.help instead ~/.BitchX/BitchX.help
- added Polish IRCNet servers to DEFAULT

* Thu Aug 13 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
- build against glibc-2.1,
- translation modified for pl,
- changed build root to /tmp/bitchx (oj Andrzej, Andrzej... fonetyka ;)
- changed permissions of ELF binaries to 711.

* Thu Jul 02 1998 Rod Cordova <rcordova@ethernet.org>
- Applied the dcc.c fix to the source code

* Wed Jul 01 1998 Rod Cordova <rcordova@ethernet.org>
- Upgraded to version 75
- incorporated the tcl-1.5-linux.o object into the binary for tcl support

* Thu Apr 02 1998 Rod Cordova <rcordova@ethernet.org>
- fixed the post install since it was not echo'ing properly after install
- applied the fixpack74p4.tgz to the source code
- incorporated the tcl.o object into the binary for tcl support
- stripped the BitchX binary and the wserv binary to reduce the size of
  the package

* Sat Mar 28 1998 Rod Cordova <rcordova@ethernet.org>
- upgraded to version 74p4

* Fri Feb 27 1998 Andrzej K. Brandt <andy@monk.cs.net.pl>
- upgraded to patchlevel 2

* Sun Feb 15 1998 Andrzej K. Brandt <andy@monk.cs.net.pl>
- backported from an SRPM made for RH 5.0 distribution (glibc)

Summary:     Improved color IRC client with built-in scripts
Summary(pl): Ulepszony, kolorowy klient IRC z wbudowanymi skryptami
Name:        BitchX
Version:     75p1
Release:     2
Copyright:   GPL
Group:       Applications/Communications
Group(pl):   Aplikacje/Komunikacja
Source:      ftp://ftp.bitchx.com/pub/BitchX/source/ircii-pana-%{version}.tar.gz
Source2:     ftp://ftp.acronet.net/pub/ircii/epic3.004-help.tar.gz
Source3:     BitchX.wmconfig
Patch:       BitchX.patch
BuildRoot:   /tmp/%{name}-%{version}-root
 
%description 
BitchX is a popular ANSI color ircII client by panasync. It
incorporates various features that would normally require a
script. It's interface is more colorful and cleaner than ircII.

%description -l pl 
BitchX jest popularnym klientem ircII. Jego interfejs jest bardziej 
kolorowy i przej¿ysty ni¿ interfejs standardowego kilienta ircII.

%prep
%setup -q -n %{name} -b 2
%patch  -p1
%patch1 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr
make all

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{bin,lib/BitchX/{script,translation,help}} \
	$RPM_BUILD_ROOT/etc/{X11/wmconfig,irc}

install $RPM_SOURCE_DIR/ircII.servers $RPM_BUILD_ROOT/etc/irc
install -s source/BitchX $RPM_BUILD_ROOT/usr/bin
install -s source/wserv $RPM_BUILD_ROOT/usr/bin/wserv-bx
install -s source/scr-bx $RPM_BUILD_ROOT/usr/bin
install install-bitchx $RPM_BUILD_ROOT/usr/bin
install BitchX.help $RPM_BUILD_ROOT/usr/lib/BitchX
cp -r help $RPM_BUILD_ROOT/usr/lib/BitchX

install %{SOURCE3} $RPM_BUILD_ROOT/etc/X11/wmconfig/BitchX

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755) 
%doc Changes  doc/* BitchX.quit BitchX.reasons
%config(noreplace) %verify(not md5 size mtime) /etc/irc/*
/etc/X11/wmconfig/Bitch
%attr(755, root, root) /usr/bin/*
%attr(644, root, root) /usr/lib/BitchX

%changelog
* Thu Oct 13 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [75-2]
- removed /etc/ircII.servers,
- added wmconfig file,
- fixed: removed %attr(644, root, root) from /usr/lib/BitchX.

* Thu Oct 01 1998 Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>
- wserv is now as wserv-bx (modifiet to avoid conflicts with others
  irc clients),
- irclib is now ${prefix}/lib/BitchX
- added /usr/lib/BitchX with subdirectories,
- added Group(pl),
- added configuration /etc/irc/ircII.servers,
- added help (from EPIC3 but should be from EPIC4!),
- now BitchX uses /usr/lib/BitchX/BitchX.help instead ~/.BitchX/BitchX.help.

* Thu Aug 13 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
- added pl translation.

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

Summary:	Improved color IRC client with built-in scripts
Summary(pl):	Ulepszony, kolorowy klient IRC z wbudowanymi skryptami
Name:		BitchX
Version:	1.0c15
Release:	2	
License:	GPL
Group:		Applications/Networking
Group(pl):	Aplikacje/Sieciowe
Source0:	ftp://ftp.bitchx.com/pub/BitchX/source/%{name}-%{version}.tar.gz
Source1:	BitchX-config.h
Source2:	ircII.servers
Source3:	BitchX.desktop
Patch0:		BitchX-configure.patch
Patch1:		BitchX-pld.patch
Icon:		BitchX.xpm
URL:		http://www.bitchx.com/
BuildRequires:	ncurses-devel >= 5.0
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_applnkdir	/usr/X11R6/share/applnk
 
%description 
BitchX is a popular ANSI color ircII client by panasync. It incorporates
various features that would normally require a script. It's interface is
more colorful and cleaner than ircII.

%description -l pl 
BitchX jest popularnym klientem ircII. Jego interfejs jest bardziej
kolorowy i przejrzysty ni¿ interfejs standardowego kilienta ircII.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

%build
cp -f %{SOURCE1} include/config.h

autoconf

CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -w -I%{_includedir}/ncurses" LDFLAGS="-s"
export CFLAGS LDFLAGS
%configure \
	--enable-ipv6

make all 

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/BitchX/{script,translation,help} \
	$RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,/etc/irc} \
	$RPM_BUILD_ROOT{%{_applnkdir}/Networking/IRC,/usr/X11R6/share/pixmaps}

install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/irc
gzip -d doc/BitchX.1.gz
install doc/BitchX.1 $RPM_BUILD_ROOT%{_mandir}/man1
rm -f doc/{bitchx.1.gz,BitchX{.1,-macros.tar.gz}}

install source/BitchX $RPM_BUILD_ROOT%{_bindir}
install source/wserv $RPM_BUILD_ROOT%{_bindir}/wserv-bx
install source/scr-bx $RPM_BUILD_ROOT%{_bindir}

install BitchX.help $RPM_BUILD_ROOT%{_datadir}/BitchX

install %{SOURCE3} $RPM_BUILD_ROOT%{_applnkdir}/Networking/IRC
install doc/BitchX.png $RPM_BUILD_ROOT/usr/X11R6/share/pixmaps

cp -a bitchx-docs/* $RPM_BUILD_ROOT%{_datadir}/BitchX/help
cp -a translation $RPM_BUILD_ROOT%{_datadir}/BitchX
rm -rf $RPM_BUILD_ROOT%{_datadir}/BitchX/help/CVS

gzip -9nf doc/{functions,README.hooks,BitchX{-format,.faq,.doc,.bot}} \
	BitchX.quit BitchX.reasons \
	$RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.gz BitchX* 
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/irc/*
%{_datadir}/BitchX
%{_applnkdir}/Networking/IRC/*
/usr/X11R6/share/pixmaps/*
%{_mandir}/man1/*

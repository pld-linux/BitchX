Summary:	Improved color IRC client with built-in scripts
Summary(es):	Cliente IRC para la consola Linux
Summary(pl):	Ulepszony, kolorowy klient IRC z wbudowanymi skryptami
Summary(pt_BR):	Cliente IRC para o console do Linux
Name:		BitchX
Version:	1.0c19
Release:	7
License:	GPL
Group:		Applications/Networking
Source0:	ftp://ftp.bitchx.com/pub/BitchX/source/ircii-pana-%{version}.tar.gz
# Source0-md5:	79431ff0880e7317049045981fac8adc
Source1:	ircII.servers
Source2:	%{name}.desktop
Source3:	%{name}-bxglobal.script
Source4:	%{name}.1.pl
Patch0:		%{name}-config.h.patch
Patch1:		%{name}-numver.patch
Patch2:		%{name}-dcc-force-port.patch
Patch3:		%{name}-doc.patch
Patch4:		%{name}-emacs.patch
Patch5:		%{name}-versioned-tcl.patch
Patch6:		%{name}-353fix.patch
Patch7:		%{name}-security.patch
Patch8:		%{name}-names.patch
Patch9:		%{name}-gcc33.patch
Icon:		BitchX.xpm
URL:		http://www.bitchx.com/
BuildRequires:	mysql-devel
BuildRequires:	ncurses-devel >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_datadir	%{_libdir}

%description
BitchX is a popular ANSI color ircII client by panasync. It
incorporates various features that would normally require a script.
It's interface is more colorful and cleaner than ircII.

%description -l es
Cliente IRC para la consola Linux.

%description -l pl
BitchX jest popularnym klientem ircII. Jego interfejs jest bardziej
kolorowy i przejrzysty ni¿ interfejs standardowego klienta ircII.

%description -l pt_BR
O BitchX é um cliente de IRC com suporte a cores para o console do
Linux. Ele incorpora várias características que normalmente
requereriam um script, e a sua interface é mais colorida, e simples de
trabalhar que a do ircII :)

%package europa
Summary:	Europa Plugin
Summary(pl):	Wtyczka Europa
Group:		Applications/Networking
Requires:	BitchX = %{version}

%description europa
Europa is a BitchX plugin to provide easy access to an SQL
knowledgebase. This is helpful for use in help channels where common
questions repeatedly come up.

%description europa -l pl
Europa jest wtyczk± do BitchX zapewniaj±c± ³atwy dostêp do SQL-owej
bazy wiedzy. Jest przydatny na kana³ach pomocy, gdzie czêsto
powtarzaj± siê te same pytania.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1

%build
CFLAGS="%{rpmcflags} -I%{_includedir}/ncurses"
%configure2_13 \
	--enable-ipv6 \
	--with-plugins=all

%{__make} \
	IRCLIB="%{_datadir}/%{name}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_pixmapsdir},%{_desktopdir}} \
	$RPM_BUILD_ROOT{%{_sysconfdir}/irc,%{_mandir}/{man1,pl/man1}} \
	$RPM_BUILD_ROOT%{_datadir}/%{name}/{script,translation,help,plugins}

install source/{BitchX,scr-bx} \
			$RPM_BUILD_ROOT%{_bindir}
install dll/*/*.so	$RPM_BUILD_ROOT%{_datadir}/%{name}/plugins

install source/wserv	$RPM_BUILD_ROOT%{_datadir}/%{name}

install script/*	$RPM_BUILD_ROOT%{_datadir}/%{name}/script
install translation/*	$RPM_BUILD_ROOT%{_datadir}/%{name}/translation
cp -pfr bitchx-docs/*	$RPM_BUILD_ROOT%{_datadir}/%{name}/help

install doc/BitchX.png	$RPM_BUILD_ROOT%{_pixmapsdir}

install doc/BitchX.1	$RPM_BUILD_ROOT%{_mandir}/man1

install %{SOURCE1}	$RPM_BUILD_ROOT%{_sysconfdir}/irc/ircII.servers
install %{SOURCE2}	$RPM_BUILD_ROOT%{_desktopdir}/BitchX.desktop
install %{SOURCE3}	$RPM_BUILD_ROOT%{_datadir}/%{name}/script/bxglobal
install %{SOURCE4}	$RPM_BUILD_ROOT%{_mandir}/pl/man1/BitchX.1


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog doc/BitchX{-format,-idea,.bot,.doc,.faq,.tcl} IPv6-support dll/europa/{README,knowledgebase.sql}
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/irc/*
%dir %{_datadir}/BitchX
%dir %{_datadir}/BitchX/plugins
%attr(755,root,root) %{_datadir}/BitchX/plugins/acro.so
%attr(755,root,root) %{_datadir}/BitchX/plugins/aim.so
%attr(755,root,root) %{_datadir}/BitchX/plugins/arcfour.so
%attr(755,root,root) %{_datadir}/BitchX/plugins/autobot.so
%attr(755,root,root) %{_datadir}/BitchX/plugins/autocycle.so
%attr(755,root,root) %{_datadir}/BitchX/plugins/blowfish.so
%attr(755,root,root) %{_datadir}/BitchX/plugins/cavlink.so
%attr(755,root,root) %{_datadir}/BitchX/plugins/encrypt.so
%attr(755,root,root) %{_datadir}/BitchX/plugins/fserv.so
%attr(755,root,root) %{_datadir}/BitchX/plugins/hint.so
%attr(755,root,root) %{_datadir}/BitchX/plugins/identd.so
%attr(755,root,root) %{_datadir}/BitchX/plugins/nap.so
%attr(755,root,root) %{_datadir}/BitchX/plugins/pkga.so
%attr(755,root,root) %{_datadir}/BitchX/plugins/possum.so
%attr(755,root,root) %{_datadir}/BitchX/plugins/qbx.so
%attr(755,root,root) %{_datadir}/BitchX/plugins/qmail.so
%attr(755,root,root) %{_datadir}/BitchX/plugins/scan.so
%attr(755,root,root) %{_datadir}/BitchX/plugins/wavplay.so
%attr(755,root,root) %{_datadir}/BitchX/wserv
%{_datadir}/BitchX/help
%{_datadir}/BitchX/script
%{_datadir}/BitchX/translation
%{_desktopdir}/*
%{_pixmapsdir}/*
%{_mandir}/man1/*
%lang(pl) %{_mandir}/pl/man1/*

%files europa
%defattr(644,root,root,755)
%doc dll/europa/{README,CREDITS}
%defattr(644,root,root,755)
%attr(755,root,root) %{_datadir}/BitchX/plugins/europa.so

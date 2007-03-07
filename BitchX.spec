%define	pre	-final
Summary:	Improved color IRC client with built-in scripts
Summary(es.UTF-8):	Cliente IRC para la consola Linux
Summary(pl.UTF-8):	Ulepszony, kolorowy klient IRC z wbudowanymi skryptami
Summary(pt_BR.UTF-8):	Cliente IRC para o console do Linux
Name:		BitchX
Version:	1.1
Release:	8
License:	GPL
Group:		Applications/Networking
Source0:	http://www.bitchx.org/files/source/ircii-pana-%{version}%{pre}.tar.gz
# Source0-md5:	611d2dda222f00c10140236f4c331572
Source1:	ircII.servers
Source2:	%{name}.desktop
Source3:	%{name}-bxglobal.script
Source4:	%{name}.1.pl
Patch0:		%{name}-config.h.patch
Patch1:		%{name}-doc.patch
Patch2:		%{name}-emacs.patch
Patch3:		%{name}-versioned-tcl.patch
Patch4:		%{name}-353fix.patch
Patch5:		%{name}-security.patch
Patch6:		%{name}-types.patch
Patch7:		%{name}-pic.patch
URL:		http://www.bitchx.org/
BuildRequires:	mysql-devel
BuildRequires:	ncurses-devel >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_datadir	%{_libdir}

%description
BitchX is a popular ANSI color ircII client by panasync. It
incorporates various features that would normally require a script.
It's interface is more colorful and cleaner than ircII.

%description -l pl.UTF-8
BitchX jest popularnym klientem ircII. Jego interfejs jest bardziej
kolorowy i przejrzysty niż interfejs standardowego klienta ircII.

%description -l pt_BR.UTF-8
O BitchX é um cliente de IRC com suporte a cores para o console do
Linux. Ele incorpora várias características que normalmente
requereriam um script, e a sua interface é mais colorida, e simples de
trabalhar que a do ircII :)

%package europa
Summary:	Europa Plugin
Summary(pl.UTF-8):	Wtyczka Europa
Group:		Applications/Networking
Requires:	BitchX = %{version}-%{release}

%description europa
Europa is a BitchX plugin to provide easy access to an SQL
knowledgebase. This is helpful for use in help channels where common
questions repeatedly come up.

%description europa -l pl.UTF-8
Europa jest wtyczką do BitchX zapewniającą łatwy dostęp do SQL-owej
bazy wiedzy. Jest przydatny na kanałach pomocy, gdzie często
powtarzają się te same pytania.

%prep
%setup -q -n %{name}
#%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

# kill any precompiled x86 binaries
rm -f dll/europa/corba/ai-client dll/europa/cse476/p1 \
	dll/nap/dragonap/napi/main dll/nap/test \
	bitchx-docs/findcomm

%build
CFLAGS="%{rpmcflags} -I/usr/include/ncurses -fno-strict-aliasing"
%configure \
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

install doc/BitchX.xpm	$RPM_BUILD_ROOT%{_pixmapsdir}

install doc/BitchX.1	$RPM_BUILD_ROOT%{_mandir}/man1

install %{SOURCE1}	$RPM_BUILD_ROOT%{_sysconfdir}/irc/ircII.servers
install %{SOURCE2}	$RPM_BUILD_ROOT%{_desktopdir}/BitchX.desktop
install %{SOURCE3}	$RPM_BUILD_ROOT%{_datadir}/%{name}/script/bxglobal
install %{SOURCE4}	$RPM_BUILD_ROOT%{_mandir}/pl/man1/BitchX.1


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog doc/BitchX{.doc,.faq} doc/tcl/BitchX.tcl IPv6-support dll/europa/{README,knowledgebase.sql}
%attr(755,root,root) %{_bindir}/*
%dir %{_sysconfdir}/irc
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/irc/*
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
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
%{_mandir}/man1/*
%lang(pl) %{_mandir}/pl/man1/*

%files europa
%defattr(644,root,root,755)
%doc dll/europa/{README,CREDITS}
%defattr(644,root,root,755)
%attr(755,root,root) %{_datadir}/BitchX/plugins/europa.so

Summary:	Improved color IRC client with built-in scripts
Summary(pl):	Ulepszony, kolorowy klient IRC z wbudowanymi skryptami
Name:		BitchX
Version:	1.0c17
Release:	7
License:	GPL
Group:		Applications/Networking
Group(de):	Applikationen/Netzwerkwesen
Group(pl):	Aplikacje/Sieciowe
Source0:	ftp://ftp.bitchx.com/pub/BitchX/source/%{name}-%{version}.tar.gz
Source1:	%{name}-config.h
Source2:	ircII.servers
Source3:	%{name}.desktop
Source4:	%{name}-bxglobal.script
Patch0:		%{name}-configure.patch
Patch1:		%{name}-pld.patch
Patch2:		%{name}-plugindir.patch
Icon:		BitchX.xpm
URL:		http://www.bitchx.com/
BuildRequires:	ncurses-devel >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description 
BitchX is a popular ANSI color ircII client by panasync. It
incorporates various features that would normally require a script.
It's interface is more colorful and cleaner than ircII.

%description -l pl 
BitchX jest popularnym klientem ircII. Jego interfejs jest bardziej
kolorowy i przejrzysty ni¿ interfejs standardowego kilienta ircII.

%prep
%setup -q -n %{name}
find . -type d -name 'CVS'| xargs rm -rf
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
cp -f %{SOURCE1} include/config.h

autoconf

CFLAGS="%{!?debug:$RPM_OPT_FLAGS}%{?debug:-O -g} -D_GNU_SOURCE -w -I%{_includedir}/ncurses"
%configure \
	--enable-ipv6 \
	--with-plugins=abot,acro,aim,amp,arcfour,blowfish,cavlink,cdrom,encrypt,fserv,hint,mail,nap,nicklist,possum,qbx,qmail,wavplay \
	--with-plugindir=%{_libdir}/BitchX

%{__make} INSTALL_WSERV=%{_bindir}/wserv-bx

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_prefix}/X11R6/share/pixmaps,%{_libdir}/BitchX,%{_applnkdir}/Network/IRC,%{_sysconfdir}/irc,%{_datadir}/BitchX/{script,translation,help},%{_mandir}/man1}

install source/{BitchX,scr-bx} \
			$RPM_BUILD_ROOT%{_bindir}

install source/wserv \
			$RPM_BUILD_ROOT%{_bindir}/wserv-bx

install doc/BitchX.png	$RPM_BUILD_ROOT%{_prefix}/X11R6/share/pixmaps

install BitchX.{ircnames,quit,reasons,help} \
			$RPM_BUILD_ROOT%{_datadir}/BitchX

install script/{bxtcl.tcl,example-.bitchxrc,file.tcl,fserve+vfs.tar.gz,menu.bx,query.bx} \
			$RPM_BUILD_ROOT%{_datadir}/BitchX/script

install %{SOURCE2} 	$RPM_BUILD_ROOT%{_sysconfdir}/irc/ircII.servers
install %{SOURCE3} 	$RPM_BUILD_ROOT%{_applnkdir}/Network/IRC/BitchX.desktop
install %{SOURCE4} 	$RPM_BUILD_ROOT%{_datadir}/BitchX/script/bxglobal

install translation/*	$RPM_BUILD_ROOT%{_datadir}/BitchX/translation

cp -pr bitchx-docs/[1-9]* bitchx-docs/{commands,functions,out,README_FIRST} \
			$RPM_BUILD_ROOT%{_datadir}/BitchX/help

install dll/*.so	$RPM_BUILD_ROOT%{_libdir}/BitchX

install doc/BitchX.1	$RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf doc/BitchX{-format,-idea,.bot,.doc,.faq,.tcl} IPv6-support

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.gz *.gz 
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/BitchX
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/irc/*
%{_datadir}/BitchX
%{_applnkdir}/Network/IRC/*
%{_prefix}/X11R6/share/pixmaps/*
%{_mandir}/man1/*

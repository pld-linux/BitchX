Summary:	Improved color IRC client with built-in scripts
Summary(pl):	Ulepszony, kolorowy klient IRC z wbudowanymi skryptami
Name:		BitchX
Version:	1.0c15
Release:	2	
Source0:	ftp://ftp.bitchx.com/pub/BitchX/source/%{name}-%{version}.tar.gz
Source1:	BitchX-config.h
Source2:	ircII.servers
Copyright:	GPL
Group:		Applications/Networking
Group(pl):	Aplikacje/Sieciowe
Patch0:		%{name}-configure.patch
Patch1:		%{name}-pld.patch
Patch2:         %{name}-antiroot.patch
URL:		http://www.bitchx.com/
BuildRoot:	/tmp/%{name}-%{version}-root
 
%description 
BitchX is a popular ANSI color ircII client by panasync. It
incorporates various features that would normally require a
script. It's interface is more colorful and cleaner than ircII.

%description -l pl 
BitchX jest popularnym klientem ircII. Jego interfejs jest bardziej 
kolorowy i przejrzysty ni¿ interfejs standardowego kilienta ircII.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
cp -f %{SOURCE1} include/config.h

autoconf

CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -w -I/usr/include/ncurses" LDFLAGS="-s" \
%configure

make all 

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/usr/{bin,share/BitchX/{script,translation,help}}
install -d $RPM_BUILD_ROOT/{%{_mandir}/man1,etc/irc}

strip source/BitchX
strip source/wserv
strip source/scr-bx

install %{SOURCE2} $RPM_BUILD_ROOT/etc/irc
install doc/BitchX.1.gz $RPM_BUILD_ROOT%{_mandir}/man1

install source/BitchX $RPM_BUILD_ROOT%{_bindir}
install source/wserv $RPM_BUILD_ROOT%{_bindir}/wserv-bx
install source/scr-bx $RPM_BUILD_ROOT%{_bindir}
#install install-bitchx $RPM_BUILD_ROOT%{_bindir}

install BitchX.help $RPM_BUILD_ROOT%{_datadir}/BitchX

cp -a bitchx-docs/* $RPM_BUILD_ROOT%{_datadir}/BitchX/help
cp -a translation $RPM_BUILD_ROOT%{_datadir}/BitchX
rm -rf $RPM_BUILD_ROOT%{_datadir}/BitchX/help/CVS

gzip -9nf  doc/* BitchX.quit BitchX.reasons || :
#\
	#$RPM_BUILD_ROOT%{_mandir}/man1/* || :

#changes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755) 
#changes.gz
%doc doc/* BitchX* 

%attr(755,root,root) %{_bindir}/*

%{_datadir}/BitchX

#%config(noreplace) %verify(not md5 size mtime) /etc/irc/*
#%{_mandir}/man1/*

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
Group:		Applications/Networking
Group(pl):	Aplikacje/Sieciowe
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
kolorowy i przejrzysty ni¿ interfejs standardowego kilienta ircII.

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

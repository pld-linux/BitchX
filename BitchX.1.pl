.\" Translation (c) 1999 Pawe� Wilk <siewca@dione.ids.pl>
.\" {PTM/PW/0.1/10-11-1999/"zaawansowany klient IRC"}
.TH BitchX 1 "Pi�tek, 23 Grudnia, 1998" "Slackware GNU/Linux" ""
.SH NAZWA
BitchX \- zaawansowany klient Internet Relay Chat
.SH SK�ADNIA
.B BitchX
[-aAbdfqxvBFRZP] [-R tty][-H nazwa_hosta] [-c kana�] [-p port] [-r plik] [-n ksywa] [-l plik] [-L plik] [ksywa] [lista serwer�w]
.SH OPIS
.B BitchX
jest bardzo zmodyfikowanym klientem ircII. Zawiera wiele rzeczy takich jak
wbudowane oferowanie CDCC (XDCC), wbudowana ochrona przed flood-em, itd.
�atwiejszym jest pisanie skrypt�w pod
.B BitchX
poniewa� w przeciwie�stwie do czystego, vanilla ircII, po�owa skryptu nie musi by�
po�wi�cona na zmiany wygl�du ircII. Zawiera te� wiele nowych udogodnie�,
takich jak skanowanie port�w, zaawansowany TCL, odtwarzacz CD, klient poczty
elektronicznej, od��czanie od terminala steruj�cego, itp.

.B BitchX 
- Bazuje na 
.B EPIC 
Software Labs 
.B epic ircII (1998).
Wersja (BitchX-75p2-8) -- Data (19980708).

Ta strona jest zmodyfikowan� wersj� istniej�cej strony dla
.BR Debiana ,
poniewa� by�a przestarza�a, a potrzebna by�a jaka� nowsza.
.SH OPCJE
.TP
.I -A 
Nie wy�wietla pocz�tkowej grafiki ansi.
.TP
.I -R <tty>
Nadmierne przywracanie odwieszonych proces�w, nie u�ywane obecnie
.TP
.I -H <nazwa_hosta>
U�ywa wirtualnej nazwy hosta, je�li to tylko mo�liwe.
.TP
.I -c <kana�>
Automatycznie wchodzi na kana�
.I <kana�>
po pod��czeniu si� do serwera
.TP
.I -b
�aduje
.I .bitchxrc
lub
.I .ircrc
po pod��czeniu si� do serwera.
.TP
.I -p <port>
U�ywa
.I <port>
do zainicjowania po��czenia z serwerem (normalnie 6667).
.TP
.I -f
M�wi
.B BitchX-owi
o tym, �e tw�j terminal u�ywa sterowania przep�ywem (^S/^Q), wi�c BitchX 
nie powinien u�ywa� tych kod�w.
.TP
.I -F
M�wi
.B BitchX-owi
o tym, �e tw�j terminal nie u�ywa sterowania przep�ywem (co jest opcj� domy�ln�).
.TP
.I -d
Instruuje, �e u�ywamy "g�upiego" terminala.
.TP
.I -Z
U�ywa adresu 
.B NAT
podczas wykonywania dcc. Pozwala ci okre�li� tw�j prawdziwy adres je�li
u�ywasz maszyny b�d�cej NAT-owan� (t�umaczenie adres�w). Je�li np.
tw�j adres jest mapowany N-do-M (IP-masquerading jest szczeg�lnym
przypadkiem t�umaczenia adres�w w stylu N-to-1).
Odwied�
.B http://www.csn.tu-chemnitz.de/HyperNews/get/linux-ip-nat.html 
po wi�cej informacji na ten temat.
.TP
.I -P
W��cza lub wy��cza tworzenie pliku pid.ksywa dla dzia�aj�cego programu.
.TP
.I -q
Nie �aduje przy starcie pliku
.I ~/.ircrc
.TP
.I -r <plik>
Czyta
.I <plik>
by otrzyma� list� serwer�w IRC.
.I <plik>
jest oddzielon� bia�ymi znakami list� nazw serwer�w.
.TP
.I -n <ksywa>
Ustawia twoj� ksywk� na
.IR <ksywa> .
.TP
.I -a
U�ywa domy�lnej listy serwer�w podanej w linii polece�.
.TP
.I -x
Uruchamia
.B BitchX
w trybie �ledzenia (debug mode).
.TP
.I -v
Pokazuje numer wersji.
.TP
.I -B
Zmusza
.B BitchX
by wykona� fork i powr�ci� do pow�oki.
.TP
.I -l <plik>
U�ywa
.I <pliku>
zamiast .ircrc
.TP
.I -L <plik>
U�ywa
.I <pliku>
zamiast 
.I .ircrc
i korzysta z rozszerze� $ .
.SH ZOBACZ TAK�E
Jak wszystkie klienty IRC
.B BitchX
posiada mn�stwo wewn�trznej dokumentacji. Spr�buj czasem u�y� opcji
.I /help
Jest tam r�wnierz mn�stwo innego typu rzeczy w twoim katalogu instalacyjnym,
pod nazw� docs
.SH PLIKI
.TP
.I /usr/local/lib/irc/
Globalny, systemowy katalog konfiguracyjny.
.TP
.I ~/.BitchX/BitchX.sav
Osobisty plik konfiguracyjny.
.TP
.I ~/.BitchX/BitchX.ircnames
Domy�lne, losowo wybierane prawdziwe imiona.
.TP
.I ~/.BitchX/BitchX.formats
Osobiste formaty wy�wietlania BitchX-a.
.TP
.I ~/.BitchX/BitchX.reasons
Domy�lna losowa wiadomo�� przy kopaniu.
.TP
.I ~/.BitchX/BitchX.quit
Domy�lna losowa wiadomo�� przy wyj�ciu.
.TP
.I ~/.Bitchx/BitchX.help
Plik pomocy u�ytkownika.
.TP
.I ~/.Bitchx/screens
Pami�� dla BitchX-owych sesji screen.
.SH ORYGINALNY AUTOR STRONY MAN
Wichert Akkerman
.B <wakkerma@debian.org>
.SH ODPOWIEDZIALNY ZA NOWE WERSJE
Robert Durdle
.B <dragoon@nightmail.com>
.SH Autor BitchX-a
Colten Edwards
.B <panasync@bitchx.com> 


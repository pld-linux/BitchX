.\" Translation (c) 1999 Pawe³ Wilk <siewca@dione.ids.pl>
.\" {PTM/PW/0.1/10-11-1999/"zaawansowany klient IRC"}
.TH BitchX 1 "Pi±tek, 23 Grudnia, 1998" "Slackware GNU/Linux" ""
.SH NAZWA
BitchX \- zaawansowany klient Internet Relay Chat
.SH SK£ADNIA
.B BitchX
[-aAbdfqxvBFRZP] [-R tty][-H nazwa_hosta] [-c kana³] [-p port] [-r plik] [-n ksywa] [-l plik] [-L plik] [ksywa] [lista serwerów]
.SH OPIS
.B BitchX
jest bardzo zmodyfikowanym klientem ircII. Zawiera wiele rzeczy takich jak
wbudowane oferowanie CDCC (XDCC), wbudowana ochrona przed flood-em, itd.
£atwiejszym jest pisanie skryptów pod
.B BitchX
poniewa¿ w przeciwieñstwie do czystego, vanilla ircII, po³owa skryptu nie musi byæ
po¶wiêcona na zmiany wygl±du ircII. Zawiera te¿ wiele nowych udogodnieñ,
takich jak skanowanie portów, zaawansowany TCL, odtwarzacz CD, klient poczty
elektronicznej, od³±czanie od terminala steruj±cego, itp.

.B BitchX 
- Bazuje na 
.B EPIC 
Software Labs 
.B epic ircII (1998).
Wersja (BitchX-75p2-8) -- Data (19980708).

Ta strona jest zmodyfikowan± wersj± istniej±cej strony dla
.BR Debiana ,
poniewa¿ by³a przestarza³a, a potrzebna by³a jaka¶ nowsza.
.SH OPCJE
.TP
.I -A 
Nie wy¶wietla pocz±tkowej grafiki ansi.
.TP
.I -R <tty>
Nadmierne przywracanie odwieszonych procesów, nie u¿ywane obecnie
.TP
.I -H <nazwa_hosta>
U¿ywa wirtualnej nazwy hosta, je¶li to tylko mo¿liwe.
.TP
.I -c <kana³>
Automatycznie wchodzi na kana³
.I <kana³>
po pod³±czeniu siê do serwera
.TP
.I -b
£aduje
.I .bitchxrc
lub
.I .ircrc
po pod³±czeniu siê do serwera.
.TP
.I -p <port>
U¿ywa
.I <port>
do zainicjowania po³±czenia z serwerem (normalnie 6667).
.TP
.I -f
Mówi
.B BitchX-owi
o tym, ¿e twój terminal u¿ywa sterowania przep³ywem (^S/^Q), wiêc BitchX 
nie powinien u¿ywaæ tych kodów.
.TP
.I -F
Mówi
.B BitchX-owi
o tym, ¿e twój terminal nie u¿ywa sterowania przep³ywem (co jest opcj± domy¶ln±).
.TP
.I -d
Instruuje, ¿e u¿ywamy "g³upiego" terminala.
.TP
.I -Z
U¿ywa adresu 
.B NAT
podczas wykonywania dcc. Pozwala ci okre¶liæ twój prawdziwy adres je¶li
u¿ywasz maszyny bêd±cej NAT-owan± (t³umaczenie adresów). Je¶li np.
twój adres jest mapowany N-do-M (IP-masquerading jest szczególnym
przypadkiem t³umaczenia adresów w stylu N-to-1).
Odwied¼
.B http://www.csn.tu-chemnitz.de/HyperNews/get/linux-ip-nat.html 
po wiêcej informacji na ten temat.
.TP
.I -P
W³±cza lub wy³±cza tworzenie pliku pid.ksywa dla dzia³aj±cego programu.
.TP
.I -q
Nie ³aduje przy starcie pliku
.I ~/.ircrc
.TP
.I -r <plik>
Czyta
.I <plik>
by otrzymaæ listê serwerów IRC.
.I <plik>
jest oddzielon± bia³ymi znakami list± nazw serwerów.
.TP
.I -n <ksywa>
Ustawia twoj± ksywkê na
.IR <ksywa> .
.TP
.I -a
U¿ywa domy¶lnej listy serwerów podanej w linii poleceñ.
.TP
.I -x
Uruchamia
.B BitchX
w trybie ¶ledzenia (debug mode).
.TP
.I -v
Pokazuje numer wersji.
.TP
.I -B
Zmusza
.B BitchX
by wykona³ fork i powróci³ do pow³oki.
.TP
.I -l <plik>
U¿ywa
.I <pliku>
zamiast .ircrc
.TP
.I -L <plik>
U¿ywa
.I <pliku>
zamiast 
.I .ircrc
i korzysta z rozszerzeñ $ .
.SH ZOBACZ TAK¯E
Jak wszystkie klienty IRC
.B BitchX
posiada mnóstwo wewnêtrznej dokumentacji. Spróbuj czasem u¿yæ opcji
.I /help
Jest tam równierz mnóstwo innego typu rzeczy w twoim katalogu instalacyjnym,
pod nazw± docs
.SH PLIKI
.TP
.I /usr/local/lib/irc/
Globalny, systemowy katalog konfiguracyjny.
.TP
.I ~/.BitchX/BitchX.sav
Osobisty plik konfiguracyjny.
.TP
.I ~/.BitchX/BitchX.ircnames
Domy¶lne, losowo wybierane prawdziwe imiona.
.TP
.I ~/.BitchX/BitchX.formats
Osobiste formaty wy¶wietlania BitchX-a.
.TP
.I ~/.BitchX/BitchX.reasons
Domy¶lna losowa wiadomo¶æ przy kopaniu.
.TP
.I ~/.BitchX/BitchX.quit
Domy¶lna losowa wiadomo¶æ przy wyj¶ciu.
.TP
.I ~/.Bitchx/BitchX.help
Plik pomocy u¿ytkownika.
.TP
.I ~/.Bitchx/screens
Pamiêæ dla BitchX-owych sesji screen.
.SH ORYGINALNY AUTOR STRONY MAN
Wichert Akkerman
.B <wakkerma@debian.org>
.SH ODPOWIEDZIALNY ZA NOWE WERSJE
Robert Durdle
.B <dragoon@nightmail.com>
.SH Autor BitchX-a
Colten Edwards
.B <panasync@bitchx.com> 


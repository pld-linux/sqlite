Summary:	SQLite library
Summary(pl):	Biblioteka SQLite
Name:		sqlite
Version:	2.5.4
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://www.hwaci.com/sw/sqlite/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.hwaci.com/sw/sqlite/
BuildRequires:	readline-devel
BuildRequires:	tcl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SQLite is a C library that implements an SQL database engine. A large
subset of SQL92 is supported. A complete database is stored in a
single disk file. The API is designed for convenience and ease of use.
Applications that link against SQLite can enjoy the power and
flexiblity of an SQL database without the administrative hassles of
supporting a separate database server. Because it omits the
client-server interaction overhead and writes directly to disk, SQLite
is also faster than the big database servers for most operations. In
addition to the C library, the SQLite distribution includes a
command-line tool for interacting with SQLite databases and SQLite
bindings for Tcl/Tk.

%description -l pl
SQLite jest bibliotek� j�zyka C, kt�ra implementuje silnik baz danych
SQL (obs�ugiwana jest wi�kszo�� standardu SQL92). Ca�a baza danych
przechowywana jest w jednym pliku. Aplikacje wykorzystuj�ce t�
bibliotek� charakteryzuj� si� si�� i elastyczno�cia SQLowych baz
danych bez konieczno�ci utrzymywania osobnego serwera baz danych.
Poniewa� pomijana jest komunikacja klient-serwer i dane s� zapisywane
bezpo�rednio na dysku, SQLite jest szybsza od du�ych serwer�w
bazodanowych przy wi�kszo�ci operacji na bazie danych. Dodatkowo
opr�cz biblioteki jezyka C, dostarczany jest program do zarz�dzania
bazami danych.

%package devel
Summary:	Header files for SQLite development
Summary(pl):	Pliki nag��wkowe SQLite
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
SQLite is a C library that implements an SQL database engine. A large
subset of SQL92 is supported. A complete database is stored in a
single disk file. The API is designed for convenience and ease of use.
Applications that link against SQLite can enjoy the power and
flexiblity of an SQL database without the administrative hassles of
supporting a separate database server. Because it omits the
client-server interaction overhead and writes directly to disk, SQLite
is also faster than the big database servers for most operations. In
addition to the C library, the SQLite distribution includes a
command-line tool for interacting with SQLite databases and SQLite
bindings for Tcl/Tk.

This package contains the header files needed to develop programs that
use these SQLite.

%description devel -l pl
SQLite jest bibliotek� j�zyka C, kt�ra implementuje silnik baz danych
SQL (obs�ugiwana jest wi�kszo�� standardu SQL92). Ca�a baza danych
przechowywana jest w jednym pliku. Aplikacje wykorzystuj�ce t�
bibliotek� charakteryzuj� si� si�� i elastyczno�cia SQLowych baz
danych bez konieczno�ci utrzymywania osobnego serwera baz danych.
Poniewa� pomijana jest komunikacja klient-serwer i dane s� zapisywane
bezpo�rednio na dysku, SQLite jest szybsza od du�ych serwer�w
bazodanowych przy wi�kszo�ci operacji na bazie danych. Dodatkowo
opr�cz biblioteki jezyka C, dostarczany jest program do zarz�dzania
bazami danych.

Pakiet zawiera pliki nag�wkowe niezbedne do kompilowania program�w
u�ywaj�cych biblioteki SQLite.

%package static
Summary:	Static libraries for SQLite development
Summary(pl):	Statyczne biblioteki SQLite
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
SQLite is a C library that implements an SQL database engine. A large
subset of SQL92 is supported. A complete database is stored in a
single disk file. The API is designed for convenience and ease of use.
Applications that link against SQLite can enjoy the power and
flexiblity of an SQL database without the administrative hassles of
supporting a separate database server. Because it omits the
client-server interaction overhead and writes directly to disk, SQLite
is also faster than the big database servers for most operations. In
addition to the C library, the SQLite distribution includes a
command-line tool for interacting with SQLite databases and SQLite
bindings for Tcl/Tk.

This package contains the static SQLite libraries.

%description static -l pl
SQLite jest bibliotek� j�zyka C, kt�ra implementuje silnik baz danych
SQL (obs�ugiwana jest wi�kszo�� standardu SQL92). Ca�a baza danych
przechowywana jest w jednym pliku. Aplikacje wykorzystuj�ce t�
bibliotek� charakteryzuj� si� si�� i elastyczno�cia SQLowych baz
danych bez konieczno�ci utrzymywania osobnego serwera baz danych.
Poniewa� pomijana jest komunikacja klient-serwer i dane s� zapisywane
bezpo�rednio na dysku, SQLite jest szybsza od du�ych serwer�w
bazodanowych przy wi�kszo�ci operacji na bazie danych. Dodatkowo
opr�cz biblioteki jezyka C, dostarczany jest program do zarz�dzania
bazami danych.

Pakiet zawiera statyczne biblioteki SQLite.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_includedir},%{_libdir},%{_mandir}/man1}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install sqlite.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/sqlite
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_mandir}/man1/sqlite.1*

%files devel
%defattr(644,root,root,755)
%{_includedir}/sqlite.h
%attr(755,root,root) %{_libdir}/lib*.la
%{_libdir}/lib*.so

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

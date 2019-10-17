#
# Conditional build:
%bcond_with	utf8	# build with UTF-8 support

Summary:	SQLite library
Summary(pl.UTF-8):	Biblioteka SQLite
Name:		sqlite
Version:	2.8.17
Release:	9
License:	LGPL
Group:		Libraries
# Source0Download: http://sqlite.org/download.html
Source0:	http://sqlite.org/%{name}-%{version}.tar.gz
# Source0-md5:	838dbac20b56d2c4292e98848505a05b
Patch0:		%{name}-DESTDIR.patch
Patch1:		format-security.patch
URL:		http://sqlite.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool >= 2:2.2
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

%description -l pl.UTF-8
SQLite jest biblioteką języka C, która implementuje silnik baz danych
SQL (obsługiwana jest większość standardu SQL92). Cała baza danych
przechowywana jest w jednym pliku. Aplikacje wykorzystujące tę
bibliotekę charakteryzują się siłą i elastycznością SQLowych baz
danych bez konieczności utrzymywania osobnego serwera baz danych.
Ponieważ pomijana jest komunikacja klient-serwer i dane są zapisywane
bezpośrednio na dysku, SQLite jest szybsza od dużych serwerów
bazodanowych przy większości operacji na bazie danych. Dodatkowo
oprócz biblioteki języka C, dostarczany jest program do zarządzania
bazami danych.

%package devel
Summary:	Header files for SQLite development
Summary(pl.UTF-8):	Pliki nagłówkowe SQLite
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

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

%description devel -l pl.UTF-8
SQLite jest biblioteką języka C, która implementuje silnik baz danych
SQL (obsługiwana jest większość standardu SQL92). Cała baza danych
przechowywana jest w jednym pliku. Aplikacje wykorzystujące tę
bibliotekę charakteryzują się siłą i elastycznością SQLowych baz
danych bez konieczności utrzymywania osobnego serwera baz danych.
Ponieważ pomijana jest komunikacja klient-serwer i dane są zapisywane
bezpośrednio na dysku, SQLite jest szybsza od dużych serwerów
bazodanowych przy większości operacji na bazie danych. Dodatkowo
oprócz biblioteki języka C, dostarczany jest program do zarządzania
bazami danych.

Pakiet zawiera pliki nagówkowe niezbedne do kompilowania programów
używających biblioteki SQLite.

%package static
Summary:	Static libraries for SQLite development
Summary(pl.UTF-8):	Statyczne biblioteki SQLite
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

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

%description static -l pl.UTF-8
SQLite jest biblioteką języka C, która implementuje silnik baz danych
SQL (obsługiwana jest większość standardu SQL92). Cała baza danych
przechowywana jest w jednym pliku. Aplikacje wykorzystujące tę
bibliotekę charakteryzują się siłą i elastycznością SQLowych baz
danych bez konieczności utrzymywania osobnego serwera baz danych.
Ponieważ pomijana jest komunikacja klient-serwer i dane są zapisywane
bezpośrednio na dysku, SQLite jest szybsza od dużych serwerów
bazodanowych przy większości operacji na bazie danych. Dodatkowo
oprócz biblioteki języka C, dostarczany jest program do zarządzania
bazami danych.

Pakiet zawiera statyczne biblioteki SQLite.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

find . -type d -name CVS | xargs %{__rm} -r

%build
%{__libtoolize} --install
%{__aclocal}
%{__autoconf}

%configure \
	%{?with_utf8:--enable-utf8}

%{__make}
%{__make} doc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_includedir},%{_libdir},%{_mandir}/man1}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -p sqlite.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/sqlite
%attr(755,root,root) %{_libdir}/libsqlite.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsqlite.so.0
%{_mandir}/man1/sqlite.1*

%files devel
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_libdir}/libsqlite.so
%{_libdir}/libsqlite.la
%{_includedir}/sqlite.h
%{_pkgconfigdir}/sqlite.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libsqlite.a

%bcond_with	utf8 # build with UTF-8 support
Summary:	SQLite library
Summary(pl):	Biblioteka SQLite
Name:		sqlite
Version:	2.8.13
Release:	1
License:	LGPL
Group:		Libraries
# Source0Download: http://sqlite.org/download.html
Source0:	http://sqlite.org/%{name}-%{version}.tar.gz
# Source0-md5:	628fa52b5580b38ade75985dd4ba46dd
Patch0:		%{name}-DESTDIR.patch
URL:		http://sqlite.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
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
SQLite jest bibliotek± jêzyka C, która implementuje silnik baz danych
SQL (obs³ugiwana jest wiêkszo¶æ standardu SQL92). Ca³a baza danych
przechowywana jest w jednym pliku. Aplikacje wykorzystuj±ce tê
bibliotekê charakteryzuj± siê si³± i elastyczno¶cia SQLowych baz
danych bez konieczno¶ci utrzymywania osobnego serwera baz danych.
Poniewa¿ pomijana jest komunikacja klient-serwer i dane s± zapisywane
bezpo¶rednio na dysku, SQLite jest szybsza od du¿ych serwerów
bazodanowych przy wiêkszo¶ci operacji na bazie danych. Dodatkowo
oprócz biblioteki jezyka C, dostarczany jest program do zarz±dzania
bazami danych.

%package devel
Summary:	Header files for SQLite development
Summary(pl):	Pliki nag³ówkowe SQLite
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
SQLite jest bibliotek± jêzyka C, która implementuje silnik baz danych
SQL (obs³ugiwana jest wiêkszo¶æ standardu SQL92). Ca³a baza danych
przechowywana jest w jednym pliku. Aplikacje wykorzystuj±ce tê
bibliotekê charakteryzuj± siê si³± i elastyczno¶cia SQLowych baz
danych bez konieczno¶ci utrzymywania osobnego serwera baz danych.
Poniewa¿ pomijana jest komunikacja klient-serwer i dane s± zapisywane
bezpo¶rednio na dysku, SQLite jest szybsza od du¿ych serwerów
bazodanowych przy wiêkszo¶ci operacji na bazie danych. Dodatkowo
oprócz biblioteki jezyka C, dostarczany jest program do zarz±dzania
bazami danych.

Pakiet zawiera pliki nagówkowe niezbedne do kompilowania programów
u¿ywaj±cych biblioteki SQLite.

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
SQLite jest bibliotek± jêzyka C, która implementuje silnik baz danych
SQL (obs³ugiwana jest wiêkszo¶æ standardu SQL92). Ca³a baza danych
przechowywana jest w jednym pliku. Aplikacje wykorzystuj±ce tê
bibliotekê charakteryzuj± siê si³± i elastyczno¶cia SQLowych baz
danych bez konieczno¶ci utrzymywania osobnego serwera baz danych.
Poniewa¿ pomijana jest komunikacja klient-serwer i dane s± zapisywane
bezpo¶rednio na dysku, SQLite jest szybsza od du¿ych serwerów
bazodanowych przy wiêkszo¶ci operacji na bazie danych. Dodatkowo
oprócz biblioteki jezyka C, dostarczany jest program do zarz±dzania
bazami danych.

Pakiet zawiera statyczne biblioteki SQLite.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__libtoolize}
cp -f /usr/share/automake/config.sub .
%{__aclocal}
%{__autoconf}
%configure \
	%{?with_utf8:--enable-utf8}
%{__make}
%{__make} doc

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
%doc doc/*
%{_includedir}/sqlite.h
%{_libdir}/lib*.la
%{_libdir}/lib*.so
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

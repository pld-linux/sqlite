Summary:	SQLite library
Name:		sqlite
Version:	2.2.5
Release:	1
License:	LGPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	Библиотеки
Group(uk):	Б╕бл╕отеки
Source0:	http://www.hwaci.com/sq/sqlite/%{name}.tar.gz
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.hwaci.com/sq/sqlite
BuildRequires:	readline-devel
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

%package devel
Summary:	Header files for SQLite development
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Разработка/Библиотеки
Group(uk):	Розробка/Б╕бл╕отеки
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
use these Atlas-C++

%package static
Summary:	Static libraries for SQLite development
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Разработка/Библиотеки
Group(uk):	Розробка/Б╕бл╕отеки
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

This package contains the static Atlas-C++ libraries.

%package progs
Summary:	CLI for SQLite
Group:		Applications/Databases
Group(de):	Applikationen/Dateibanken
Group(pl):	Aplikacje/Bazy danych
Requires:	%{name} = %{version}

%description progs
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

This package contains the command line interface for SQLite.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/{bin,include,lib,share/man/man1}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install sqlite.1 $RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.gz
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/sqlite.h
%attr(755,root,root) %{_libdir}/lib*.la
%{_libdir}/lib*.so

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sqlite

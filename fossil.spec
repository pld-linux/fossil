Summary:	Simple, high-reliability, distributed software configuration management
Summary(pl.UTF-8):	Proste, wiarygodne, rozproszone zarządzanie konfiguracją oprogramowania
Name:		fossil
Version:	2.7
Release:	2
License:	BSD
Group:		Development/Version Control
# see URL below for mapping between Version and date
#Source0Download: http://www.fossil-scm.org/download.html
Source0:	https://www.fossil-scm.org/index.html/uv/%{name}-src-%{version}.tar.gz
# Source0-md5:	b00819c45cb6518065540ce0704b0884
URL:		http://www.fossil-scm.org/
BuildRequires:	openssl-devel
BuildRequires:	readline-devel
BuildRequires:	sqlite3-devel >= 3.25.0
BuildRequires:	tcl >= 8.5
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fossil is simple, high-reliability, distributed software configuration
management. In comparison to other distributed version control systems
it has the following features:

1. Bug Tracking And Wiki - In addition to doing distributed version
control like Git and Mercurial, Fossil also supports distributed bug
tracking, distributed wiki, and a distributed blog mechanism all in a
single integrated package.

2. Web Interface - Fossil has a built-in and easy-to-use web interface
that simplifies project tracking and promotes situational awareness.
Simply type "fossil ui" from within any check-out and Fossil
automatically opens your web browser in a page that gives detailed
graphical history and status information on that project.

%description -l pl.UTF-8
Fossil to proste, wiarygodne, rozproszone zarządzanie konfiguracją
oprogramowania. W porównaniu z innymi rozproszonymi systemami kontroli
wersji ma następujące możliwości:

1. Śledzenie błędów i Wiki - poza rozproszoną kontrolą wersji, jak w
systemach Git czy Mercurial, Fossil obsługuje rozproszone mechanizmy
śledzenia błędów, wiki oraz bloga - wszystko w pojedynczym,
zintegrowanym pakiecie.

2. Interfejs WWW - Fossil ma wbudowany i łatwy w użyciu interfejs WWW,
upraszczający śledzenie projektu i promujący świadomość sytuacji.
Wystarczy napisać "fossil ui" z poziomu dowolnego wyciągniętego stanu
repozytorium, a Fossil automatycznie otworzy przeglądarkę WWW na
stronie podającej szczegółową historię oraz informacje o stanie
projektu w postaci graficznej.

%prep
%setup -q

%{__rm} src/sqlite3.c

%build
# some tcl-based strangeness, not autoconf configure
CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
CPPFLAGS="%{rpmcppflags}" \
LIBS="-lresolv" \
./configure \
	--disable-internal-sqlite \
	--with-openssl=auto
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	INSTALLDIR=$RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYRIGHT-BSD2.txt
%attr(755,root,root) %{_bindir}/fossil

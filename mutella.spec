Summary:	Commandline Gnutella servent
Summary(pl):	Tekstowy klient sieci Gnutella
Name:		mutella
Version:	0.4.3
Release:	2
License:	GPL v2
Group:		Applications/Networking
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	3fc7b649967dc722cd93532c2d043db1
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-gcc33.patch
URL:		http://mutella.sourceforge.net/
BuildRequires:	readline-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mutella is a terminal-mode Gnutella client with an intuitive and easy
to use interface. Mutella supports all the functionality required to
participate as a full-featured node in the Gnutella network, that is
supports file search, download and sharing.

Mutella is optimized for a high-bandwidth connection, it sets
standards for the server performance and stability. However, Mutella
is also happy to run on a modest-speed line.

%description -l pl
Mutella jest tekstowym klientem Gnutelli z intuicyjnym i ³atwym w
u¿yciu interfejsem. Mutella spe³nia wszystkie wymagania by byæ
pe³noprawnym wêz³em Gnutelli - obs³uguje wyszukiwanie, udostêpnianie
oraz ¶ci±ganie plików.

Mutella jest zoptymalizowana dla szerokopasmowych po³±czeñ, ustanawia
standard w szybko¶ci i stabilno¶ci dzia³ania, jednak¿e zadowala siê
tak¿e s³abymi ³±czami.

%package frontend-www
Summary:	Mutella's standard WWW frontend
Summary(pl):	Standardowy interfejs WWW Mutelli
Group:		Applications/Networking
Requires:	mutella

%description frontend-www
This package contains the WWW frontend for Mutella.

%description frontend-www -l pl
Ten pakiet zawiera interfejs WWW dla Mutelli.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d  $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/mutella.1*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png

%files frontend-www
%defattr(644,root,root,755)
%{_datadir}/mutella

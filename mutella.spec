Summary:	Commandline Gnutella servent
Name:		mutella
Version:	0.4.3
Release:	1
License:	GPL v2
Group:		Applications/Networking
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
URL:		http://mutella.sourceforge.net/
BuildRequires:	readline-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mutella is a terminal-mode Gnutella client with an intuitive and easy to
use interface.  Mutella supports all the functionality required to
participate as a full-featured node in the Gnutella network, that is
supports file search, download and sharing.

Mutella is optimized for a high-bandwidth connection, it sets standards for
the server performance and stability. However, Mutella is also happy to run
on a modest-speed line.

%package frontend-www
Summary:	Mutella's standard WWW frontend
Group:		Applications/Networking
Requires:	mutella

%description frontend-www
This package contains the WWW frontend for mutella.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/mutella.1*

%files frontend-www
%defattr(644,root,root,755)
%{_datadir}/mutella/remote/template/*

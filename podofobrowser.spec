Summary:	PDF object browser/editor
Summary(pl.UTF-8):	Przeglądarka/edytor obiektów w dokumentach PDF
Name:		podofobrowser
Version:	0.9.7
Release:	1
License:	GPL v2+
Group:		Applications/Publishing
Source0:	https://downloads.sourceforge.net/podofo/%{name}-%{version}.tar.gz
# Source0-md5:	1178fb40c1f46a5aa96684f211364a84
URL:		https://podofo.sourceforge.net/
BuildRequires:	Qt5Core-devel >= 5.0.0
BuildRequires:	Qt5Widgets-devel >= 5.0.0
BuildRequires:	cmake >= 2.4
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel >= 2.0
BuildRequires:	libjpeg-devel
BuildRequires:	podofo-devel >= 0.9.7
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PoDoFoBrowser is a Qt 5 application for browsing the objects in a PDF
file and modifying their keys easily. It is very useful if you want to
look on the internal structure of PDF files.

%description -l pl.UTF-8
PoDoFoBrowser to aplikacja Qt 5 do przeglądania obiektów w pliku PDF i
łatwego modyfikowania ich kluczy. Jest przydatna, jeśli chcemy
obejrzeć wewnętrzną strukturę plików PDF.

%prep
%setup -q

%build
install -d build
cd build
%cmake ..

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/podofobrowser

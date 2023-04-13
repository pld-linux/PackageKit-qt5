Summary:	packagekit-qt5 library
Summary(pl.UTF-8):	Biblioteka packagekit-qt5
Name:		PackageKit-qt5
Version:	0.9.6
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	https://www.freedesktop.org/software/PackageKit/releases/PackageKit-Qt-%{version}.tar.xz
# Source0-md5:	4369fcce287740191a1479c5ce403422
URL:		https://www.packagekit.org/
BuildRequires:	PackageKit-devel >= 0.8.11
BuildRequires:	Qt5Core-devel >= 5.6.0
BuildRequires:	Qt5DBus-devel >= 5.6.0
BuildRequires:	Qt5Xml-devel >= 5.6.0
BuildRequires:	cmake >= 2.8.6
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	pkgconfig
BuildRequires:	qt5-build >= 5.6.0
Requires:	Qt5Core >= 5.6.0
Requires:	Qt5DBus >= 5.6.0
Requires:	Qt5Xml >= 5.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
packagekit-qt5 library.

%description -l pl.UTF-8
Biblioteka packagekit-qt5.

%package devel
Summary:	Header files for packagekit-qt5 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki packagekit-qt5
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt5Core-devel >= 5.6.0
Requires:	Qt5DBus-devel >= 5.6.0
Requires:	Qt5Xml-devel >= 5.6.0

%description devel
Header files for packagekit-qt5 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki packagekit-qt5.

%prep
%setup -q -n PackageKit-Qt-%{version}

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS MAINTAINERS NEWS README.md TODO
%attr(755,root,root) %{_libdir}/libpackagekitqt5.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpackagekitqt5.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpackagekitqt5.so
%{_pkgconfigdir}/packagekitqt5.pc
%{_includedir}/packagekitqt5
%{_libdir}/cmake/packagekitqt5

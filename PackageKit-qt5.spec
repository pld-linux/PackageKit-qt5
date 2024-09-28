#
# Conditional build:
%bcond_without	qt5	# Qt5 library
%bcond_without	qt6	# Qt6 library

Summary:	Qt 5 bindings for PackageKit
Summary(pl.UTF-8):	Wiązania Qt 5 do biblioteki PackageKit
Name:		PackageKit-qt5
Version:	1.1.2
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	https://www.freedesktop.org/software/PackageKit/releases/PackageKit-Qt-%{version}.tar.xz
# Source0-md5:	1c51c24a1f7ebdad515bb7f77f55a138
URL:		https://www.freedesktop.org/software/PackageKit/
BuildRequires:	PackageKit-devel >= 0.8.11
BuildRequires:	cmake >= 3.6
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	pkgconfig
%if %{with qt5}
BuildRequires:	Qt5Core-devel >= 5.10.0
BuildRequires:	Qt5DBus-devel >= 5.10.0
BuildRequires:	qt5-build >= 5.10.0
%endif
%if %{with qt6}
BuildRequires:	Qt6Core-devel >= 6.0.0
BuildRequires:	Qt6DBus-devel >= 6.0.0
BuildRequires:	qt6-build >= 6.0.0
%endif
Requires:	Qt5Core >= 5.10.0
Requires:	Qt5DBus >= 5.10.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qt 5 bindings for PackageKit.

%description -l pl.UTF-8
Wiązania Qt 5 do biblioteki PackageKit.

%package devel
Summary:	Header files for packagekit-qt5 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki packagekit-qt5
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt5Core-devel >= 5.10.0
Requires:	Qt5DBus-devel >= 5.10.0

%description devel
Header files for packagekit-qt5 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki packagekit-qt5.

%package -n PackageKit-qt6
Summary:	Qt 6 bindings for PackageKit
Summary(pl.UTF-8):	Wiązania Qt 6 do biblioteki PackageKit
Group:		Libraries
Requires:	Qt6Core >= 6.0.0
Requires:	Qt6DBus >= 6.0.0

%description -n PackageKit-qt6
Qt 6 bindings for PackageKit.

%description -n PackageKit-qt6 -l pl.UTF-8
Wiązania Qt 6 do biblioteki PackageKit.

%package -n PackageKit-qt6-devel
Summary:	Header files for packagekit-qt6 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki packagekit-qt6
Group:		Development/Libraries
Requires:	PackageKit-qt6 = %{version}-%{release}
Requires:	Qt6Core-devel >= 6.0.0
Requires:	Qt6DBus-devel >= 6.0.0

%description -n PackageKit-qt6-devel
Header files for packagekit-qt6 library.

%description -n PackageKit-qt6-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki packagekit-qt6.

%prep
%setup -q -n PackageKit-Qt-%{version}

%build
%if %{with qt5}
install -d build-qt5
cd build-qt5
%cmake ..

%{__make}
cd ..
%endif

%if %{with qt6}
install -d build-qt6
cd build-qt6
%cmake .. \
	-DBUILD_WITH_QT6=ON

%{__make}
cd ..
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with qt5}
%{__make} -C build-qt5 install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%if %{with qt6}
%{__make} -C build-qt6 install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%if %{with qt5}
%files
%defattr(644,root,root,755)
%doc AUTHORS MAINTAINERS NEWS README.md TODO
%attr(755,root,root) %{_libdir}/libpackagekitqt5.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpackagekitqt5.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpackagekitqt5.so
%{_pkgconfigdir}/packagekitqt5.pc
%{_includedir}/packagekitqt5
%{_libdir}/cmake/packagekitqt5
%endif

%if %{with qt6}
%files -n PackageKit-qt6
%defattr(644,root,root,755)
%doc AUTHORS MAINTAINERS NEWS README.md TODO
%attr(755,root,root) %{_libdir}/libpackagekitqt6.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpackagekitqt6.so.1

%files -n PackageKit-qt6-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpackagekitqt6.so
%{_pkgconfigdir}/packagekitqt6.pc
%{_includedir}/packagekitqt6
%{_libdir}/cmake/packagekitqt6
%endif

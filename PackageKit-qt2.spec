Summary:	packagekit-qt2 library
Summary(pl.UTF-8):	Biblioteka packagekit-qt2
Name:		PackageKit-qt2
Version:	0.8.8
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://www.packagekit.org/releases/PackageKit-Qt-%{version}.tar.xz
# Source0-md5:	55ba87425a8d7a8b1f021e8769b88534
URL:		http://www.packagekit.org/
BuildRequires:	PackageKit-devel >= 0.8.11
BuildRequires:	QtCore-devel >= 4.4.0
BuildRequires:	QtDBus-devel >= 4.4.0
BuildRequires:	QtSql-devel >= 4.4.0
BuildRequires:	cmake >= 2.8.6
BuildRequires:	pkgconfig
BuildRequires:	qt4-build >= 4.4.0
Requires:	QtCore >= 4.4.0
Requires:	QtDBus >= 4.4.0
Requires:	QtSql >= 4.4.0
Obsoletes:	PackageKit-qt < 0.8.4
Obsoletes:	qpackagekit < 0.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
packagekit-qt2 library.

%description -l pl.UTF-8
Biblioteka packagekit-qt2.

%package devel
Summary:	Header files for packagekit-qt2 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki packagekit-qt2
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	QtCore-devel >= 4.4.0
Requires:	QtDBus-devel >= 4.4.0
Requires:	QtSql-devel >= 4.4.0
Obsoletes:	PackageKit-qt-devel < 0.8.4
Obsoletes:	PackageKit-qt-static < 0.8.4
Obsoletes:	PackageKit-qt2-static
Obsoletes:	qpackagekit-devel < 0.4.0

%description devel
Header files for packagekit-qt2 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki packagekit-qt2.

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
%doc AUTHORS MAINTAINERS NEWS TODO
%attr(755,root,root) %{_libdir}/libpackagekit-qt2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpackagekit-qt2.so.6

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpackagekit-qt2.so
%{_pkgconfigdir}/packagekit-qt2.pc
%{_includedir}/PackageKit/packagekit-qt2
%dir %{_libdir}/cmake/packagekit-qt2
%{_libdir}/cmake/packagekit-qt2/packagekit-qt2-config-version.cmake
%{_libdir}/cmake/packagekit-qt2/packagekit-qt2-config.cmake

%define upname  libebur128
%define major   1
%define libname %mklibname %{name}_ %{major}
%define devname %mklibname %{name} -d

Name:           ebur128
Version:	1.2.6
Release:	2
Summary:        A library implementing the EBU R128 loudness standard
License:        MIT
Group:          System/Libraries
Url:            https://github.com/jiixyj/libebur128
Source0:        https://github.com/jiixyj/libebur128/archive/v%{version}/%{upname}-%{version}.tar.gz
BuildRequires:  cmake

%description
This library library that implements the EBU R 128 standard for loudness 
normalisation.

#----------------------------------------------------

%package -n     %{libname}
Summary:        A library implementing the EBU R128 loudness standard
Group:          System/Libraries

%description -n %{libname}
This library library that implements the EBU R 128 standard for loudness 
normalisation.

This package contains the shared library.

#----------------------------------------------------

%package -n     %{devname}
Summary:        Development files for %{upname}
Group:          Development/C++
Requires:       %{libname} = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{upname}-devel = %{version}-%{release}

%description -n %{devname}
A library implementing the EBU R128 loudness standard.

This package contains header files and libraries needed to develop
application that use %{upname}.

#----------------------------------------------------

%prep
%setup -q -n %{upname}-%{version}

%build
%cmake
%make_build

%install
%make_install -C build

%files -n %{libname}
%doc COPYING
%{_libdir}/%{upname}.so.%{major}{,.*}

%files -n %{devname}
%{_includedir}/%{name}.h
%{_libdir}/%{upname}.so
%{_libdir}/pkgconfig/%{upname}.pc

%define _empty_manifest_terminate_build 0

%define libname %mklibname kvazaar
%define devname %mklibname -d kvazaar

Name:           kvazaar
Version:        2.3.0
Release:        1
Summary:        An open-source HEVC encoder
License:        LGPLv2+
URL:            http://ultravideo.cs.tut.fi/#encoder
Source0:        https://github.com/ultravideo/kvazaar/releases/download/v%{version}/kvazaar-%{version}.tar.xz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

Requires:	%{libname} = %{version}-%{release}

%description
Kvazaar is the leading academic open-source HEVC encoder developed from scratch
in C. This package contains the application for encoding videos.

%package -n %{libname}
Summary:        HEVC encoder %{name} libraries
Requires:  %{name} = %{version}-%{release}

%description -n %{libname}
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}. This package contains the shared libraries.

%package -n %{devname}
Summary:        Development files for %{name}
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1
autoreconf -vif
./configure --prefix='/usr' --libdir=%{_libdir} --disable-static 

%build
%make_build

%install
%make_install

find %{buildroot} -name '*.la' -delete

# Pick up docs in the files section
rm -fr %{buildroot}%{_docdir}

%files
%{_bindir}/*
%{_mandir}/man1/*

%files -n %{libname}
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc README.md CREDITS
%{_libdir}/*.so.*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

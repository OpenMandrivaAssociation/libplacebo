%define beta %{nil}
%define major 120

%define libname %mklibname placebo %{major}
%define devname %mklibname -d placebo

Name:		libplacebo
Version:	3.120.3
Release:	1
Source0:	https://code.videolan.org/videolan/libplacebo/-/archive/v%{version}/libplacebo-v%{version}.tar.bz2
Patch0:		libplacebo-dont-search-for-glslang-static-helpers.patch
Group:		System/Libraries
Summary:	Video rendering library
License:	LGPLv2.1+
BuildRequires:	meson ninja
BuildRequires:	pkgconfig(shaderc)
BuildRequires:	glslang-devel
BuildRequires:	pkgconfig(epoxy)
BuildRequires:	pkgconfig(lcms2)
BuildRequires:	pkgconfig(vulkan)
BuildRequires:	pkgconfig(SPIRV-Tools)
BuildRequires:	python-mako

%description
libplacebo is, in a nutshell, the core rendering algorithms and ideas of mpv
rewritten as an independent library.

As of today, libplacebo contains a large assortment of video processing
shaders, focusing on both quality and performance.

%package -n %{libname}
Summary:	Video rendering library

%description -n %{libname}
libplacebo is, in a nutshell, the core rendering algorithms and ideas of mpv
rewritten as an independent library.

As of today, libplacebo contains a large assortment of video processing
shaders, focusing on both quality and performance.

%package -n %{devname}
Summary:	Development files for the %{name} video rendering library
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
libplacebo is, in a nutshell, the core rendering algorithms and ideas of mpv
rewritten as an independent library.

As of today, libplacebo contains a large assortment of video processing
shaders, focusing on both quality and performance.

%prep
%autosetup -p1 -n %{name}-v%{version}
%meson

%build
%meson_build

%install
%meson_install

%files -n %{libname}
%{_libdir}/libplacebo.so.%{major}*

%files -n %{devname}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/libplacebo

#files

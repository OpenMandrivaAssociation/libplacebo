%define beta %{nil}
%define major 229

%define libname %mklibname placebo %{major}
%define devname %mklibname -d placebo

Name:		libplacebo
Version:	5.229.1
Release:	1
Source0:	https://code.videolan.org/videolan/libplacebo/-/archive/v%{version}/libplacebo-v%{version}.tar.bz2
#Patch0:		libplacebo-dont-search-for-glslang-static-helpers.patch
Group:		System/Libraries
Summary:	Video rendering library
License:	LGPLv2.1+
BuildRequires: meson ninja
BuildRequires: glad
BuildRequires: glslc
BuildRequires: glslang
BuildRequires: glslang-devel
BuildRequires: pkgconfig(libavcodec)
BuildRequires: pkgconfig(glfw3)
BuildRequires: pkgconfig(sdl2)
BuildRequires: pkgconfig(SDL2_image)
BuildRequires: pkgconfig(shaderc)
BuildRequires: pkgconfig(epoxy)
BuildRequires: pkgconfig(lcms2)
BuildRequires: pkgconfig(libunwind)
BuildRequires: pkgconfig(vulkan)
BuildRequires: pkgconfig(SPIRV-Tools)
BuildRequires: python-mako

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
%meson \
       -Dvulkan=enabled \
       -Dopengl=enabled \
       -Dshaderc=enabled \
       -Dglslang=disabled \
       -Dd3d11=disabled \
       -Dlcms=enabled

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

%files
%{_bindir}/plplay

%define beta %{nil}
%define major 349

%define oldlibname %mklibname placebo 229
%define libname %mklibname placebo
%define devname %mklibname -d placebo

# libplacebo doesn't like -Os because of the _Float32 confusion
# (causes build time error)
%global optflags %{optflags} -O3

Name:		libplacebo
Version:	7.349.0
Release:	1
Source0:	https://code.videolan.org/videolan/libplacebo/-/archive/v%{version}/libplacebo-v%{version}.tar.bz2
Patch0:		libplacebo-6.338-demos-buildfix.patch
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
BuildRequires: pkgconfig(dovi)
BuildRequires: pkgconfig(libxxhash)
BuildRequires: python-mako

Requires:	%{libname} = %{EVRD}

%description
libplacebo is, in a nutshell, the core rendering algorithms and ideas of mpv
rewritten as an independent library.

As of today, libplacebo contains a large assortment of video processing
shaders, focusing on both quality and performance.

%package -n %{libname}
Summary:	Video rendering library
Obsoletes:	%{oldlibname} < %{EVRD}

%description -n %{libname}
libplacebo is, in a nutshell, the core rendering algorithms and ideas of mpv
rewritten as an independent library.

As of today, libplacebo contains a large assortment of video processing
shaders, focusing on both quality and performance.

%package -n %{devname}
Summary:	Development files for the %{name} video rendering library
Requires:	%{libname} = %{EVRD}
Requires:	%{name} = %{EVRD}

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

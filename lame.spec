#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : lame
Version  : 3.100
Release  : 1
URL      : https://downloads.sourceforge.net/project/lame/lame/3.100/lame-3.100.tar.gz
Source0  : https://downloads.sourceforge.net/project/lame/lame/3.100/lame-3.100.tar.gz
Summary  : Shared and static libraries for LAME.
Group    : Development/Tools
License  : LGPL-2.0-or-later
Requires: lame-bin = %{version}-%{release}
Requires: lame-lib = %{version}-%{release}
Requires: lame-man = %{version}-%{release}
BuildRequires : nasm-bin
BuildRequires : ncurses-dev
BuildRequires : pkgconfig(gtk+-2.0)
BuildRequires : pkgconfig(sndfile)

%description
LAME is an educational tool to be used for learning about MP3 encoding.  The
goal of the LAME project is to use the open source model to improve the
psycho acoustics, noise shaping and speed of MP3.

%package bin
Summary: bin components for the lame package.
Group: Binaries

%description bin
bin components for the lame package.


%package dev
Summary: dev components for the lame package.
Group: Development
Requires: lame-lib = %{version}-%{release}
Requires: lame-bin = %{version}-%{release}
Provides: lame-devel = %{version}-%{release}
Requires: lame = %{version}-%{release}

%description dev
dev components for the lame package.


%package doc
Summary: doc components for the lame package.
Group: Documentation
Requires: lame-man = %{version}-%{release}

%description doc
doc components for the lame package.


%package lib
Summary: lib components for the lame package.
Group: Libraries

%description lib
lib components for the lame package.


%package man
Summary: man components for the lame package.
Group: Default

%description man
man components for the lame package.


%prep
%setup -q -n lame-3.100
cd %{_builddir}/lame-3.100

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1586632565
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static --enable-shared --enable-nasm
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1586632565
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/lame

%files dev
%defattr(-,root,root,-)
/usr/include/lame/lame.h
/usr/lib64/libmp3lame.so

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/lame/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libmp3lame.so.0
/usr/lib64/libmp3lame.so.0.0.0

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/lame.1

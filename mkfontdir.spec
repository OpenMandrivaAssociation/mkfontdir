Name: mkfontdir
Version: 1.0.2
Release: %mkrel 2
Summary: Create an index of X font files in a directory
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: x11-util-macros >= 1.0.1


%description
Mkfontdir creates an index of X font files in a directory.

For each directory argument, mkfontdir reads all of the font files in the
directory searching for properties named "FONT", or (failing that) the name of
the file stripped of its suffix. These are converted to lower case and used as
font names, and, along with the name of the font file, are written out to the
file "fonts.dir" in the directory. The X server and font server use "fonts.dir"
to find font files.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/mkfontdir
%{_mandir}/man1/mkfontdir.1x.bz2



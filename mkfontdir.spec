Name:		mkfontdir
Version:	1.0.7
Release:	2
Summary:	Create an index of X font files in a directory
Group:		Development/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source:		http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
BuildRequires:	x11-util-macros >= 1.0.1
# mkfontdir is currently nothing more than a call to mkfontscale
Requires:	mkfontscale
BuildArch:	noarch

%description
Mkfontdir creates an index of X font files in a directory.

For each directory argument, mkfontdir reads all of the font files in the
directory searching for properties named "FONT", or (failing that) the name of
the file stripped of its suffix. These are converted to lower case and used as
font names, and, along with the name of the font file, are written out to the
file "fonts.dir" in the directory. The X server and font server use "fonts.dir"
to find font files.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%{_bindir}/mkfontdir
%{_mandir}/man1/mkfontdir.1*


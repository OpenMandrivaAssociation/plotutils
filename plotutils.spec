%define	major 2
%define xmi_major 0
%define libplot %mklibname plot %{major}
%define libplotter %mklibname plotter %{major}
%define libxmi %mklibname xmi %{xmi_major}
%define devname %mklibname %{name} -d
%define _disable_rebuild_configure 1
%define _disable_lto 1

Summary:	GNU Plotting Utilities
Name:		plotutils
Version:	2.6
Release:	29
License:	GPLv2
Group:		Graphics
Url:		https://www.gnu.org/software/%{name}/plotutils.html
Source0:	ftp://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
Patch0:		plotutils-2.5.1-fix-str-fmt.patch
Patch1:		plotutils-2.6-libpng-1.5.patch
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	Xaw3d-devel
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(xaw7)
BuildRequires:	pkgconfig(zlib)
Requires:	ghostscript-fonts
Requires:	texinfo

%description 
The GNU plotting utilities, sometimes called 'plotutils', include:	
(1) GNU libplot, a shared library for exporting 2-D vector graphics files
and for performing vector graphics animation under the X Window System.
Its output file formats include the new WebCGM format, pseudo-GIF, PNM,
Adobe Illustrator, Postscript (editable with the free 'idraw' drawing
editor), Fig (editable with the free 'xfig' drawing editor), PCL 5, HP-GL
and HP-GL/2, Tektronix, and GNU metafile format. Many Postscript, PCL, and
Hershey fonts are supported. A separate class library, 'libplotter',
provides a C++ binding to libplot's functionality. (2) Sample command-line
applications 'graph', 'plot', 'tek2plot', 'pic2plot', and 'plotfont', which
are built on top of GNU libplot. 'graph' is a powerful utility for XY
plotting, 'plot' translates GNU metafiles to other formats, 'tek2plot'
translates legacy Tektronix data, 'pic2plot' translates box-and-arrow
diagrams in the pic language, and 'plotfont' plots character maps.
(3) Command-line applications 'spline', 'double', and 'ode', which are useful
in scientific plotting. 'spline' does spline interpolation of input data
of arbitrary dimensionality. It uses cubic splines, splines under tension,
or cubic Bessel interpolation. 'ode' is an interactive program that can
integrate a user-specified system of ordinary differential equations.

%package -n %{libplot}
Summary:	Shared library for %{name}
Group:		Graphics
Obsoletes:	%{_lib}plotutils2 < 2.16-17

%description -n %{libplot}
This package contains a shared library needed to run programs dynamically
linked with %{name}.

%package -n %{libplotter}
Summary:	Shared library for %{name}
Group:		Graphics
Conflicts:	%{_lib}plotutils2 < 2.16-17

%description -n %{libplotter}
This package contains a shared library needed to run programs dynamically
linked with %{name}.

%package -n %{libxmi}
Summary:	Shared library for %{name}
Group:		Graphics
Conflicts:	%{_lib}plotutils2 < 2.16-17

%description -n %{libxmi}
This package contains a shared library needed to run programs dynamically
linked with %{name}.

%package -n %{devname}
Summary:	Headers for developing programs that will use %{name}
Group:		Development/Other
Requires:	%{libplot} = %{version}-%{release}
Requires:	%{libplotter} = %{version}-%{release}
Requires:	%{libxmi} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%prep
%setup -q
%patch0 -p0
%patch1 -p0

%build
%configure2_5x \
	--disable-static \
	--enable-libplotter \
	--enable-libxmi

%make

%install
%makeinstall_std

mkdir -p %{buildroot}%{_libdir}/X11/fonts/misc
cp -p fonts/pcf/*.pcf %{buildroot}%{_libdir}/X11/fonts/misc

%post
export PATH=/sbin:/usr/bin/X11:/usr/X11/bin:/usr/bin:$PATH

cd %{_libdir}/X11/fonts/misc
mkfontdir
if ! test -f %{_libdir}/X11/fonts/Type1/a010013l.pfb ; then
if test -f %{_datadir}/ghostscript/fonts/a010013l.pfb ; then
cd %{_datadir}/ghostscript/fonts
for i in *.pfb ; do
ln -s %{_datadir}/ghostscript/fonts/$i %{_libdir}/X11/fonts/Type1/$i
done
cd %{_libdir}/X11/fonts/Type1
echo 'a010013l.pfb -adobe-itc avant garde gothic-book-r-normal--0-0-0-0-p-0-iso8859-1' >> fonts.scale
echo 'a010015l.pfb -adobe-itc avant garde gothic-demi-r-normal--0-0-0-0-p-0-iso8859-1' >> fonts.scale
echo 'a010033l.pfb -adobe-itc avant garde gothic-book-o-normal--0-0-0-0-p-0-iso8859-1' >> fonts.scale
echo 'a010035l.pfb -adobe-itc avant garde gothic-demi-o-normal--0-0-0-0-p-0-iso8859-1' >> fonts.scale
echo 'b018012l.pfb -adobe-itc bookman-light-r-normal--0-0-0-0-p-0-iso8859-1' >> fonts.scale
echo 'b018015l.pfb -adobe-itc bookman-demi-r-normal--0-0-0-0-p-0-iso8859-1' >> fonts.scale
echo 'b018032l.pfb -adobe-itc bookman-light-i-normal--0-0-0-0-p-0-iso8859-1' >> fonts.scale
echo 'b018035l.pfb -adobe-itc bookman-demi-i-normal--0-0-0-0-p-0-iso8859-1' >> fonts.scale
echo 'c059013l.pfb -adobe-new century schoolbook-medium-r-normal--0-0-0-0-p-0-iso8859-1' >> fonts.scale
echo 'c059016l.pfb -adobe-new century schoolbook-bold-r-normal--0-0-0-0-p-0-iso8859-1' >> fonts.scale
echo 'c059033l.pfb -adobe-new century schoolbook-medium-i-normal--0-0-0-0-p-0-iso8859-1' >> fonts.scale
echo 'c059036l.pfb -adobe-new century schoolbook-bold-i-normal--0-0-0-0-p-0-iso8859-1' >> fonts.scale
echo 'd050000l.pfb -adobe-itc zapf dingbats-medium-r-normal--0-0-0-0-p-0-adobe-fontspecific' >> fonts.scale
echo 'n019003l.pfb -adobe-helvetica-medium-r-normal--0-0-0-0-p-0-iso8859-1' >> fonts.scale
echo 'n019004l.pfb -adobe-helvetica-bold-r-normal--0-0-0-0-p-0-iso8859-1' >> fonts.scale
echo 'n019023l.pfb -adobe-helvetica-medium-i-normal--0-0-0-0-p-0-iso8859-1' >> fonts.scale
echo 'n019024l.pfb -adobe-helvetica-bold-i-normal--0-0-0-0-p-0-iso8859-1' >> fonts.scale
echo 'n019043l.pfb -adobe-helvetica-medium-r-narrow--0-0-0-0-p-0-iso8859-1' >> fonts.scale
echo 'n019044l.pfb -adobe-helvetica-bold-r-narrow--0-0-0-0-p-0-iso8859-1' >> fonts.scale
echo 'n019063l.pfb -adobe-helvetica-medium-i-narrow--0-0-0-0-p-0-iso8859-1' >> fonts.scale
echo 'n019064l.pfb -adobe-helvetica-bold-i-narrow--0-0-0-0-p-0-iso8859-1' >> fonts.scale
echo 'n021003l.pfb -adobe-times-medium-r-normal--0-0-0-0-p-0-iso8859-1' >> fonts.scale
echo 'n021004l.pfb -adobe-times-bold-r-normal--0-0-0-0-p-0-iso8859-1' >> fonts.scale
echo 'n021023l.pfb -adobe-times-medium-i-normal--0-0-0-0-p-0-iso8859-1' >> fonts.scale
echo 'n021024l.pfb -adobe-times-bold-i-normal--0-0-0-0-p-0-iso8859-1' >> fonts.scale
echo 'n022003l.pfb -adobe-courier-medium-r-normal--0-0-0-0-m-0-iso8859-1' >> fonts.scale
echo 'n022004l.pfb -adobe-courier-bold-r-normal--0-0-0-0-m-0-iso8859-1' >> fonts.scale
echo 'n022023l.pfb -adobe-courier-medium-o-normal--0-0-0-0-m-0-iso8859-1' >> fonts.scale
echo 'n022024l.pfb -adobe-courier-bold-o-normal--0-0-0-0-m-0-iso8859-1' >> fonts.scale
echo 'p052003l.pfb -adobe-palatino-medium-r-normal--0-0-0-0-p-0-iso8859-1' >> fonts.scale
echo 'p052004l.pfb -adobe-palatino-bold-r-normal--0-0-0-0-p-0-iso8859-1' >> fonts.scale
echo 'p052023l.pfb -adobe-palatino-medium-i-normal--0-0-0-0-p-0-iso8859-1' >> fonts.scale
echo 'p052024l.pfb -adobe-palatino-bold-i-normal--0-0-0-0-p-0-iso8859-1' >> fonts.scale
echo 's050000l.pfb -adobe-symbol-medium-r-normal--0-0-0-0-p-0-adobe-fontspecific' >> fonts.scale
echo 'z003034l.pfb -adobe-itc zapf chancery-medium-i-normal--0-0-0-0-p-0-iso8859-1' >> fonts.scale
mkfontdir
fi
fi
if test "$DISPLAY" != "" ; then xset fp rehash 2> /dev/null ; fi

%postun
export PATH=/sbin:/usr/bin/X11:/usr/X11/bin:$PATH
cd %{_libdir}/X11/fonts/misc
mkfontdir
if test "$DISPLAY" != "" ; then xset fp rehash 2> /dev/null ; fi

%files
%doc AUTHORS INSTALL.fonts KNOWN_BUGS NEWS ONEWS PROBLEMS README THANKS
%{_bindir}/*
%{_libdir}/X11/fonts/misc/*
%{_mandir}/man1/*
%{_infodir}/*
%dir %{_datadir}/ode
%{_datadir}/ode/*
%dir %{_datadir}/tek2plot
%{_datadir}/tek2plot/*
%dir %{_datadir}/pic2plot
%{_datadir}/pic2plot/*

%files -n %{libplot}
%{_libdir}/libplot.so.%{major}*

%files -n %{libplotter}
%{_libdir}/libplotter.so.%{major}*

%files -n %{libxmi}
%{_libdir}/libxmi.so.%{xmi_major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%dir %{_datadir}/libplot
%{_datadir}/libplot/*
%doc README


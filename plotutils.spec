%define	major	2
%define	 xmi_major 0
%define	libname	%mklibname %name %major
%define develname %mklibname %name -d

Summary:	GNU Plotting Utilities
Name:		plotutils
Version:	2.6
Release:	13
License:	GPLv2
Group:		Graphics
Source:		ftp://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
Patch0:		plotutils-2.5.1-fix-str-fmt.patch
Patch1:		plotutils-2.6-libpng-1.5.patch
URL:		http://www.gnu.org/software/%{name}/plotutils.html
Requires:	ghostscript-fonts texinfo
BuildRequires:	flex
BuildRequires:	Xaw3d-devel
BuildRequires:	zlib-devel
BuildRequires:	png-devel
BuildRequires:	bison
BuildRequires:	libxaw-devel

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


%package -n %libname
Summary: Main library for %{name}
Group: Graphics
Provides: lib%name = %version-%release
Obsoletes: %{mklibname xmi 0}

%description -n %libname
This package contains the library needed to run programs dynamically
linked with %{name}.


%package -n %{develname}
Summary: Headers for developing programs that will use %{name}
Group: Development/Other
Requires: %{libname} = %{version}-%{release}
Provides: lib%{name}-devel = %{version}-%{release}
Provides: %{name}-devel = %{version}
Provides: libxmi-devel
Obsoletes: %{libname}-devel
Obsoletes: %{mklibname xmi 0 -d}

%description -n %{develname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.


%prep
%setup -q
%patch0 -p0
%patch1 -p0

%build
%configure2_5x --enable-libplotter --enable-libxmi 
%make

%install
%makeinstall_std

mkdir -p %{buildroot}%{_libdir}/X11/fonts/misc
cp -p fonts/pcf/*.pcf %{buildroot}%{_libdir}/X11/fonts/misc

# We don't want .la files
find %{buildroot} -name *.la -delete

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

%files -n %{libname}
%{_libdir}/libplot.so.%{major}*
%{_libdir}/libplotter.so.%{major}*
%{_libdir}/libxmi.so.%{xmi_major}*

%files -n %{develname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%dir %{_datadir}/libplot
%{_datadir}/libplot/*
%doc README


%changelog

* Mon Feb 20 2012 kamil <kamil> 2.6-9.mga2
+ Revision: 211144
- bildrequire xaw3d-devel, not Xaw3d-devel
- stop providing .la files
- clean .spec a bit

* Sun Sep 11 2011 fwang <fwang> 2.6-8.mga2
+ Revision: 142407
- fix build with libpng 1.5
- rebuild for new libpng

* Wed Apr 13 2011 mikala <mikala> 2.6-7.mga1
+ Revision: 84075
- Don't put the .so file in the libname package

* Sat Feb 19 2011 ahmad <ahmad> 2.6-6.mga1
+ Revision: 54399
- obsolete libxmi to smooth upgrades

* Fri Feb 18 2011 mikala <mikala> 2.6-5.mga1
+ Revision: 53528
- Enable libxmi support
- Fix file list

* Sat Feb 12 2011 ahmad <ahmad> 2.6-4.mga1
+ Revision: 50729
+ rebuild (emptylog)

* Sat Feb 12 2011 ahmad <ahmad> 2.6-3.mga1
+ Revision: 50698
- drop old/unneeded scriptlets
- imported package plotutils

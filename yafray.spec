# TODO:
# - make use of macros in %%build section
#
Summary:	High quality photorealistic render system
Summary(pl):	Wysokiej jako¶ci fotorealistyczny system renderuj±cy
Name:		yafray
Version:	0.0.6
%define		subver 2
Release:	%{subver}.0.1
License:	GPL v2.1
Group:		Applications/Graphics
Source0:	http://www.coala.uniovi.es/~jandro/noname/downloads/%{name}-%{version}-%{subver}.tar.gz
# Source0-md5:	bf87b6018435f3bc5bfd1be598c1a28f
URL:		http://www.yafray.org/
BuildRequires:	libjpeg-devel
BuildRequires:	libstdc++-devel >= 5:3.3.2
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
YAFRAY is a free xml based 3d rendering engine.

%description -l pl
YAFRAY jest wolnodostêpnym silnikiem renderuj±cym 3d bazuj±cym na xml.

%prep
%setup -qn %{name}-%{version}-%{subver}

%build
./configure \
	--prefix=%{_prefix} \
	--sysconfdir=%{_sysconfdir}
	
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/yafray/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/*.yafray
%dir %{_libdir}/yafray
%attr(755,root,root) %{_libdir}/yafray/*.so
%attr(755,root,root) %{_libdir}/*.so

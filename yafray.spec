# TODO:
# - use %{__cc}, %{__cxx}, %{rpmcflags} to build (need SConscript hacking)
#
Summary:	High quality photorealistic render system
Summary(pl):	Wysokiej jako¶ci fotorealistyczny system renderuj±cy
Name:		yafray
Version:	0.0.7
Release:	0.1
License:	GPL v2.1
Group:		Applications/Graphics
Source0:	http://www.coala.uniovi.es/~jandro/noname/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	680d81f097962ed4a6773dbf09202159
Patch0:		%{name}-conf_path.patch
URL:		http://www.yafray.org/
BuildRequires:	libjpeg-devel
BuildRequires:	libstdc++-devel >= 5:3.3.2
BuildRequires:	scons
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
YAFRAY is a free XML based 3d rendering engine.

%description -l pl
YAFRAY jest wolnodostêpnym silnikiem renderuj±cym 3d opartym o XML.

%prep
%setup -q
%patch0 -p1

%build
scons prefix=%{_prefix} conf_path=%{_sysconfdir}

%install
rm -rf $RPM_BUILD_ROOT

scons install prefix=$RPM_BUILD_ROOT%{_prefix} conf_path=$RPM_BUILD_ROOT%{_sysconfdir}

find $RPM_BUILD_ROOT -name .sconsign -exec rm {} \;

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

%define		_name VCO-plugins
Summary:	Bandlimited VCO LADSPA plugin
Summary(pl):	Wtyczka LADSPA - ograniczany pasmowo VCO
Name:		ladspa-vco-plugins
Version:	0.3.0
Release:	1
License:	GPL
Group:		Applications/Sound
Source0:	http://users.skynet.be/solaris/linuxaudio/downloads/%{_name}-%{version}.tar.bz2
# Source0-md5:	6fdf4a7e3c716abbb89721645427cd52
Patch0:		%{name}-misc_fixes.patch
URL:		http://users.skynet.be/solaris/linuxaudio/
BuildRequires:	ladspa-devel
BuildRequires:	libstdc++-devel
Requires:	ladspa-common
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This LADSPA plugin contains a digital implementation of the
bandlimited VCO.

%description -l pl
Ta wtyczka LADSPA zawiera cyfrow± implementacjê ograniczanego
pasmowo VCO.

%prep
%setup -q -n %{_name}-%{version}
%patch0 -p1

%build
%{__make} \
	CXX="%{__cxx}" \
	CPPFLAGS="-I. -fPIC -D_REENTRANT -Wall %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/ladspa

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/ladspa/*.so

Summary:	Re-Connectable secure remote shell
Name:		EternalTerminal
Version:	5.1.9
Release:	1
License:	GPL v3+
Group:		Applications/Networking
Source0:	https://github.com/MisterTea/EternalTerminal/archive/et-v%{version}.tar.gz
# Source0-md5:	4492d0964095a012a30d64fd71d01e87
URL:		https://github.com/MisterTea/EternalTerminal
BuildRequires:	cmake
BuildRequires:	gflags-devel
BuildRequires:	libsodium-devel
BuildRequires:	protobuf-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Remote terminal with IP roaming.

%prep
%setup -q -n %{name}-et-v%{version}

%build
install -d build
cd build
%cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/et
%attr(755,root,root) %{_bindir}/etserver
%attr(755,root,root) %{_bindir}/etterminal
%attr(755,root,root) %{_bindir}/htm
%attr(755,root,root) %{_bindir}/htmd

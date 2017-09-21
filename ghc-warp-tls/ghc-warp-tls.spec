# generated by cabal-rpm-0.11.2
# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name warp-tls
%global pkgver %{pkg_name}-%{version}

Name:           ghc-%{pkg_name}
Version:        3.2.4
Release:        1%{?dist}
Summary:        HTTP over TLS support for Warp via the TLS package

License:        MIT
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-cryptonite-devel
BuildRequires:  ghc-data-default-class-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-streaming-commons-devel
BuildRequires:  ghc-tls-devel
BuildRequires:  ghc-tls-session-manager-devel
BuildRequires:  ghc-wai-devel
BuildRequires:  ghc-warp-devel
# End cabal-rpm deps

%description
SSLv1 and SSLv2 are obsoleted by IETF. We should use TLS 1.2 (or TLS 1.1 or TLS
1.0 if necessary). HTTP/2 can be negotiated by ALPN. API docs and the README
are available at <http://www.stackage.org/package/warp-tls>.


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the Haskell %{pkg_name} library development files.


%prep
%setup -q -n %{pkgver}


%build
%ghc_lib_build


%install
%ghc_lib_install


%post devel
%ghc_pkg_recache


%postun devel
%ghc_pkg_recache


%files -f %{name}.files
%license LICENSE


%files devel -f %{name}-devel.files
%doc ChangeLog.md README.md


%changelog
* Thu Sep 14 2017 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 3.2.4-1
- spec file generated by cabal-rpm-0.11.2
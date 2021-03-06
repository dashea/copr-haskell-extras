# generated by cabal-rpm-0.11.2
# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name storable-tuple
%global pkgver %{pkg_name}-%{version}

Name:           ghc-%{pkg_name}
Version:        0.0.3.3
Release:        1%{?dist}
Summary:        Storable instance for pairs and triples

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-base-orphans-devel
BuildRequires:  ghc-storable-record-devel
BuildRequires:  ghc-utility-ht-devel
# End cabal-rpm deps

%description
Provides a Storable instance for pair and triple which should be binary
compatible with C99 and C++. The only purpose of this package is to provide a
standard location for this instance so that other packages needing this
instance can play nicely together.


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


%changelog
* Mon Dec  4 2017 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.0.3.3-1
- spec file generated by cabal-rpm-0.11.2

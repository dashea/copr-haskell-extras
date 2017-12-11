# generated by cabal-rpm-0.11.2
# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name djinn-ghc
%global pkgver %{pkg_name}-%{version}

Name:           ghc-%{pkg_name}
Version:        0.0.2.3
Release:        1%{?dist}
Summary:        Generate Haskell code from a type. Bridge from Djinn to GHC API

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-djinn-lib-devel
BuildRequires:  ghc-ghc-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-transformers-devel
# End cabal-rpm deps

%description
Djinn uses an theorem prover for intuitionistic propositional logic to generate
a Haskell expression when given a type. This is the bridge from djinn-lib to
GHC API.


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
* Mon Dec 11 2017 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.0.2.3-1
- spec file generated by cabal-rpm-0.11.2
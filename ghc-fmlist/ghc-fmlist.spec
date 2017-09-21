# generated by cabal-rpm-0.11.2
# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name fmlist
%global pkgver %{pkg_name}-%{version}

Name:           ghc-%{pkg_name}
Version:        0.9
Release:        1%{?dist}
Summary:        FoldMap lists

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros

%description
FoldMap lists are lists represented by their foldMap function. FoldMap lists
have O(1) cons, snoc and append, just like DLists, but other operations might
have favorable performance characteristics as well. These wild claims are still
completely unverified though.


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
* Thu Sep 14 2017 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.9-1
- spec file generated by cabal-rpm-0.11.2

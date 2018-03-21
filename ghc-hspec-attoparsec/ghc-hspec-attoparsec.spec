# generated by cabal-rpm-0.12.1
# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name hspec-attoparsec
%global pkgver %{pkg_name}-%{version}

%bcond_without tests

Name:           ghc-%{pkg_name}
Version:        0.1.0.2
Release:        1%{?dist}
Summary:        Utility functions for testing your attoparsec parsers with hspec

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-hspec-expectations-devel
BuildRequires:  ghc-text-devel
%if %{with tests}
BuildRequires:  ghc-hspec-devel
%endif
# End cabal-rpm deps

%description
This package provides some helper functions for testing attoparsec parsers with
hspec.

See the documentation in 'Test.Hspec.Attoparsec' for examples, or this
package's own test suite.


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the Haskell %{pkg_name} library development
files.


%prep
%setup -q -n %{pkgver}


%build
%ghc_lib_build


%install
%ghc_lib_install


%check
%cabal_test


%post devel
%ghc_pkg_recache


%postun devel
%ghc_pkg_recache


%files -f %{name}.files
%license LICENSE


%files devel -f %{name}-devel.files


%changelog
* Wed Mar 21 2018 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.1.0.2-1
- spec file generated by cabal-rpm-0.12.1

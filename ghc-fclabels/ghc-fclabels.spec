# generated by cabal-rpm-0.11.2
# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name fclabels
%global pkgver %{pkg_name}-%{version}

%bcond_without tests

Name:           ghc-%{pkg_name}
Version:        2.0.3.2
Release:        1%{?dist}
Summary:        First class accessor labels implemented as lenses

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-transformers-devel
%if %{with tests}
BuildRequires:  ghc-HUnit-devel
%endif
# End cabal-rpm deps

%description
This package provides first class labels that can act as bidirectional record
fields. The labels can be derived automatically using Template Haskell which
means you don't have to write any boilerplate yourself. The labels are
implemented as /lenses/ and are fully composable. Lenses can be used to /get/,
/set/ and /modify/ parts of a data type in a consistent way.

See "Data.Label" for an introductory explanation or see the introductory blog
post at <http://fvisser.nl/post/2013/okt/1/fclabels-2.0.html>

* /Total and partial lenses/

Internally lenses do not used Haskell functions directly, but are implemented
as categories. Categories allow the lenses to be run in custom computational
contexts. This approach allows us to make partial lenses that point to fields
of multi-constructor datatypes in an elegant way.

See "Data.Label.Partial" for the use of partial labels.

* /Monomorphic and polymorphic lenses/

We have both polymorphic and monomorphic lenses. Polymorphic lenses allow
updates that change the type. The types of polymorphic lenses are slightly more
verbose than their monomorphic counterparts, but their usage is similar.
Because monomorphic lenses are built by restricting the types of polymorphic
lenses they are essentially the same and can be freely composed with eachother.

See "Data.Label.Mono" and "Data.Label.Poly" for the difference between
polymorphic and monomorphic lenses.

* /Using fclabels/

To simplify working with labels we supply both a set of labels for Haskell's
base types, like lists, tuples, Maybe and Either, and we supply a set of
combinators for working with labels for values in the Reader and State monad.

See "Data.Label.Base" and "Data.Label.Monadic" for more information.

* /Changelog from 2.0.3.1 to 2.0.3.2/

> - Allow HUnit 1.5.*.


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


%check
%cabal_test


%post devel
%ghc_pkg_recache


%postun devel
%ghc_pkg_recache


%files -f %{name}.files
%license LICENSE


%files devel -f %{name}-devel.files
%doc CHANGELOG README.md


%changelog
* Mon Dec 11 2017 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 2.0.3.2-1
- spec file generated by cabal-rpm-0.11.2

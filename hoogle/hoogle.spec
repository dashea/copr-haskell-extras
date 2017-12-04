# generated by cabal-rpm-0.11.2
# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name hoogle
%global pkgver %{pkg_name}-%{version}

Name:           %{pkg_name}
Version:        5.0.13
Release:        2%{?dist}
Summary:        Haskell API Search

License:        BSD
Url:            https://hackage.haskell.org/package/%{name}
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  chrpath
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-cmdargs-devel
BuildRequires:  ghc-conduit-devel
BuildRequires:  ghc-conduit-extra-devel
BuildRequires:  ghc-connection-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-extra-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-haskell-src-exts-devel
BuildRequires:  ghc-http-conduit-devel
BuildRequires:  ghc-http-types-devel
BuildRequires:  ghc-js-flot-devel
BuildRequires:  ghc-js-jquery-devel
BuildRequires:  ghc-mmap-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-network-uri-devel
BuildRequires:  ghc-old-locale-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-process-extras-devel
BuildRequires:  ghc-resourcet-devel
BuildRequires:  ghc-tar-devel
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-uniplate-devel
BuildRequires:  ghc-utf8-string-devel
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-wai-devel
BuildRequires:  ghc-wai-logger-devel
BuildRequires:  ghc-warp-devel
BuildRequires:  ghc-warp-tls-devel
BuildRequires:  ghc-zlib-devel
# End cabal-rpm deps

%description
Hoogle is a Haskell API search engine, which allows you to search many standard
Haskell libraries by either function name, or by approximate type signature.


%package -n ghc-%{name}
Summary:        Haskell %{name} library

%description -n ghc-%{name}
This package provides the Haskell %{name} shared library.


%package -n ghc-%{name}-devel
Summary:        Haskell %{name} library development files
Provides:       ghc-%{name}-static = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}
Requires:       ghc-%{name}%{?_isa} = %{version}-%{release}

%description -n ghc-%{name}-devel
This package provides the Haskell %{name} library development files.


%prep
%setup -q


%build
%ghc_lib_build


%install
%ghc_lib_install
%ghc_fix_rpath %{pkgver}


%post -n ghc-%{name}-devel
%ghc_pkg_recache


%postun -n ghc-%{name}-devel
%ghc_pkg_recache


%files
%license LICENSE
%doc CHANGES.txt README.md
%{_bindir}/%{name}


%files -n ghc-%{name} -f ghc-%{name}.files
%license LICENSE
%{_datadir}/%{pkgver}


%files -n ghc-%{name}-devel -f ghc-%{name}-devel.files
%doc CHANGES.txt README.md


%changelog
* Mon Dec  4 2017 David Shea <dshea@redhat.com> - 5.0.13-2
- Rebuild against rebuilt dependencies

* Thu Sep 14 2017 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 5.0.13-1
- spec file generated by cabal-rpm-0.11.2

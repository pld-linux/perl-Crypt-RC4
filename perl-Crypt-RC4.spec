%include	/usr/lib/rpm/macros.perl
%define	pdir	Crypt
%define	pnam	RC4
Summary:	Crypt::RC4 Perl module - RC4 encryption algorithm implementation
Summary(pl):	Modu³ Perla Crypt::RC4 - implementacja algorytmu szyfrowania RC4
Name:		perl-Crypt-RC4
Version:	2.02
Release:	3
# same as perl
License:	GPL v2+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4ca59a7e58ac9597c3b4f3f46ea22629
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A simple implementation of the RC4 algorithm. RC4 is a stream cipher
designed by Rivest for RSA Data Security (now RSA Security). It is a
variablekey-size stream cipher with byte-oriented operations. The
algorithm is based on the use of a random permutation.

%description -l pl
Prosta implementacja algorytmu RC4. RC4 jest szyfrem strumieniowym
opracowanym przez Rivesta dla RSA Data Security (teraz RSA Security).
Jest to szyfr strumieniowy o zmiennej d³ugo¶ci klucza z operacjami
zorientowanymi na bajty. Bazuje na u¿ywaniu losowych permutacji.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Crypt/RC4.pm
%{_mandir}/man3/*

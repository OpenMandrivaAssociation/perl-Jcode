%define modname	Jcode
%define modver	2.07

Summary:	Japanese Charset Handle
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	20
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{modname}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Jcode/%{modname}-%{modver}.tar.bz2
Buildrequires:	perl(Test::More)
Buildrequires:	perl(Test)
Buildrequires:	perl-devel

%description
Jcode.pm supports both object and traditional approach. With object approach,
you can go like;

$iso_2022_jp = Jcode->new($str)->h2z->jis;

Which is more elegant than;
 
$iso_2022_jp = &jcode::convert(\$str,'jis',jcode::getcode(\str), "z");

For those unfamiliar with objects, Jcode.pm still supports getcode() and
convert().

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"
cd Unicode
%__perl Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%install
%makeinstall_std
%makeinstall_std -C Unicode

%check
%make test

%files 
%doc README Changes
%{perl_vendorlib}/Jcode
%{perl_vendorlib}/Jcode.pm
%{perl_vendorarch}/Jcode
%{perl_vendorarch}/auto/Jcode
%{_mandir}/man3/*


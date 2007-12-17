%define module	Jcode
%define name	perl-%{module}
%define version 2.06
%define release %mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Japanese Charset Handle
License:	GPL or Artistic
Group:		Development/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Jcode/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}/
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
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"
cd Unicode
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%install
rm -rf %{buildroot}
%makeinstall_std
cd Unicode
%makeinstall_std

%check
%{__make} test

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/Jcode
%{perl_vendorlib}/Jcode.pm
%{perl_vendorarch}/Jcode
%{perl_vendorarch}/auto/Jcode
%{_mandir}/*/*


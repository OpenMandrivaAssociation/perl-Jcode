%define upstream_name	 Jcode
%define upstream_version 2.07

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 6

Summary:	Japanese Charset Handle
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Jcode/%{upstream_name}-%{upstream_version}.tar.bz2

Buildrequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Jcode.pm supports both object and traditional approach. With object approach,
you can go like;

$iso_2022_jp = Jcode->new($str)->h2z->jis;

Which is more elegant than;
 
$iso_2022_jp = &jcode::convert(\$str,'jis',jcode::getcode(\str), "z");

For those unfamiliar with objects, Jcode.pm still supports getcode() and
convert().

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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

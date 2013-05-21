%define upstream_name	 Jcode
%define upstream_version 2.07

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	8

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


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 2.70.0-6mdv2012.0
+ Revision: 765383
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 2.70.0-5
+ Revision: 763899
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.70.0-4
+ Revision: 667221
- mass rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 2.70.0-3mdv2011.0
+ Revision: 564521
- rebuild for perl 5.12.1

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 2.70.0-2mdv2011.0
+ Revision: 555968
- rebuild for perl 5.12

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 2.70.0-1mdv2010.1
+ Revision: 402034
- rebuild using %%perl_convert_version

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 2.07-2mdv2009.0
+ Revision: 265367
- rebuild early 2009.0 package (before pixel changes)

* Sat May 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.07-1mdv2009.0
+ Revision: 208354
- update to new version 2.07
- update to new version 2.07

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 2.06-3mdv2008.1
+ Revision: 152123
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sun Aug 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.06-2mdv2008.0
+ Revision: 67061
- rebuild


* Sun Jul 09 2006 Emmanuel Andry <eandry@mandriva.org> 2.06-1mdv2007.0
- New release 2.06
- %%mkrel

* Wed May 17 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.05-1mdk
- New release 2.05

* Wed May 03 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.04-1mdk
- New release 2.04
- better source URL

* Mon May 01 2006 Stefan van der Eijk <stefan@eijk.nu> 2.03-2mdk
-_rebuild_for_sparc

* Wed Jul 20 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.03-1mdk
- 2.03

* Fri Jun 03 2005 Guillaume Rousse <guillomovitch@mandriva.org> 2.00-1mdk
- New release 2.00
- make test in %%check

* Mon Apr 25 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.88-1mdk 
- new version
- spec cleanup
- better url
- rpmbuildupdate aware

* Mon Nov 15 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.86-2mdk 
- rebuild for new perl

* Tue Jun 29 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.86-1mdk
- 0.86

* Tue Dec 09 2003 Guillaume Rousse <guillomovitch@mandrake.org> 0.83-1mdk
- first mdk release


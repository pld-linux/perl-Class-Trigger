%include	/usr/lib/rpm/macros.perl
%define	pdir	Class
%define	pnam	Trigger
Summary:	%{pdir}::%{pnam} - Mixin to add / call inheritable triggers
Summary(pl):	%{pdir}::%{pnam} - dodawanie / wo³anie dziedziczalnych triggerów
Name:		perl-%{pdir}-%{pnam}
Version:	0.08
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Class::Trigger is a mixin class to add / call triggers (or hooks) that
get called at some points you specify.

%description -l pl
Class:Trigger jest klas± s³u¿±c± do dodawania i wywo³ywania triggerów
(lub hooków), które s± wywo³ywane w podanych miejscach.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}
#%%{__make} test

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/%{pnam}.pm
%{_mandir}/man3/*

#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Class
%define		pnam	Trigger
Summary:	Class:Trigger - mixin to add / call inheritable triggers
Summary(pl.UTF-8):	Class:Trigger - dodawanie / wołanie dziedziczalnych triggerów
Name:		perl-Class-Trigger
Version:	0.10
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5fbf56437f75b8f51debfa241c808846
URL:		http://search.cpan.org/dist/Class-Trigger/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-Data-Inheritable
BuildRequires:	perl-IO-stringy
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Class::Trigger is a mixin class to add / call triggers (or hooks) that
get called at some points you specify.

%description -l pl.UTF-8
Class::Trigger jest klasą służącą do dodawania i wywoływania triggerów
(lub hooków), które są wywoływane w podanych miejscach.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/%{pdir}/%{pnam}.pm
%{_mandir}/man3/*

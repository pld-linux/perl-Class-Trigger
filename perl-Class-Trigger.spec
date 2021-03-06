#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Class
%define		pnam	Trigger
Summary:	Class:Trigger - mixin to add / call inheritable triggers
Summary(pl.UTF-8):	Class:Trigger - dodawanie / wołanie wyzwalaczy umożliwiających dziedziczenie
Name:		perl-Class-Trigger
Version:	0.14
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Class/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b0a95ebe359a3c4e768d81fc58031c83
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
Class::Trigger jest klasą służącą do dodawania i wywoływania
wyzwalaczy (lub hooków), które są wywoływane w podanych miejscach.

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
%{perl_vendorlib}/Class/Trigger.pm
%{_mandir}/man3/Class::Trigger.3pm*

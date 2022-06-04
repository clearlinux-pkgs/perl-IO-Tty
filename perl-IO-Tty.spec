#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-IO-Tty
Version  : 1.16
Release  : 25
URL      : https://cpan.metacpan.org/authors/id/T/TO/TODDR/IO-Tty-1.16.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/T/TO/TODDR/IO-Tty-1.16.tar.gz
Summary  : 'Pseudo ttys and constants'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-IO-Tty-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
Patch1: 0001-Block-LTO-when-detecting-functions.patch

%description
NAME
IO::Tty - Low-level allocate a pseudo-Tty, import constants.
VERSION
1.16
SYNOPSIS
use IO::Tty qw(TIOCNOTTY);
...
# use only to import constants, see IO::Pty to create ptys.

%package dev
Summary: dev components for the perl-IO-Tty package.
Group: Development
Provides: perl-IO-Tty-devel = %{version}-%{release}
Requires: perl-IO-Tty = %{version}-%{release}

%description dev
dev components for the perl-IO-Tty package.


%package perl
Summary: perl components for the perl-IO-Tty package.
Group: Default
Requires: perl-IO-Tty = %{version}-%{release}

%description perl
perl components for the perl-IO-Tty package.


%prep
%setup -q -n IO-Tty-1.16
cd %{_builddir}/IO-Tty-1.16
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/IO::Pty.3
/usr/share/man/man3/IO::Tty.3
/usr/share/man/man3/IO::Tty::Constant.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*

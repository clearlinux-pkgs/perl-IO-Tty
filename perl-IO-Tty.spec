#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-IO-Tty
Version  : 1.12
Release  : 2
URL      : https://cpan.metacpan.org/authors/id/T/TO/TODDR/IO-Tty-1.12.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/T/TO/TODDR/IO-Tty-1.12.tar.gz
Summary  : 'Pseudo ttys and constants'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-IO-Tty-lib = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
IO::Tty and IO::Pty provide an interface to pseudo tty's
To build this distribution, run

%package dev
Summary: dev components for the perl-IO-Tty package.
Group: Development
Requires: perl-IO-Tty-lib = %{version}-%{release}
Provides: perl-IO-Tty-devel = %{version}-%{release}

%description dev
dev components for the perl-IO-Tty package.


%package lib
Summary: lib components for the perl-IO-Tty package.
Group: Libraries

%description lib
lib components for the perl-IO-Tty package.


%prep
%setup -q -n IO-Tty-1.12

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
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
/usr/lib/perl5/vendor_perl/5.26.1/x86_64-linux-thread-multi/IO/Pty.pm
/usr/lib/perl5/vendor_perl/5.26.1/x86_64-linux-thread-multi/IO/Tty.pm
/usr/lib/perl5/vendor_perl/5.26.1/x86_64-linux-thread-multi/IO/Tty/Constant.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/IO::Pty.3
/usr/share/man/man3/IO::Tty.3
/usr/share/man/man3/IO::Tty::Constant.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.26.1/x86_64-linux-thread-multi/auto/IO/Tty/Tty.so

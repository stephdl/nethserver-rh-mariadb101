Summary: NethServer mariadb101 configuration and templates.
Name: nethserver-rh-mariadb101
Version: 0.0.4
Release: 1%{?dist}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
BuildArch: noarch
Requires: rh-mariadb101
Requires: nethserver-base
Requires: nethserver-lib >= 1.0.1
Requires: procps-ng
BuildRequires: nethserver-devtools
AutoReq: no


%description
This package adds necessary startup and configuration items for
mysql.

%prep
%setup

%build
%{__mkdir} -p root/etc/e-smith/sql/init101
%{__mkdir} -p root/var/lib/rh-mariadb101
%{__mkdir} -p root/var/log/rh-mariadb101

perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
%{genfilelist} \
    --dir   /var/log/rh-mariadb101 'attr(0755,mysql,mysql)' \
    --dir   /var/lib/rh-mariadb101 'attr(0755,mysql,mysql)' \
    --file  /usr/bin/mysql101 'attr(0755,root,root)' \
    --file  /usr/bin/mysqladmin101 'attr(0755,root,root)' \
    --file  /usr/bin/mysqlbinlog101 'attr(0755,root,root)' \
    --file  /usr/bin/mysqlcheck101 'attr(0755,root,root)' \
    --file  /usr/bin/mysql_config_editor101 'attr(0755,root,root)' \
    --file  /usr/bin/mysqld_multi101 'attr(0755,root,root)' \
    --file  /usr/bin/mysqldump101 'attr(0755,root,root)' \
    --file  /usr/bin/mysqlimport101 'attr(0755,root,root)' \
    --file  /usr/bin/mysql_plugin101 'attr(0755,root,root)' \
    --file  /usr/bin/mysqlshow101 'attr(0755,root,root)' \
    --file  /usr/bin/mysqlslap101 'attr(0755,root,root)' \
$RPM_BUILD_ROOT \
    > %{name}-%{version}-filelist
echo "%doc COPYING"          >> %{name}-%{version}-filelist

%clean 
rm -rf $RPM_BUILD_ROOT


%preun

%post
/usr/bin/systemctl enable rh-mariadb101-mariadb

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%dir %{_nseventsdir}/%{name}-update
%changelog
* Sun Oct 1  2017 stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.4
- Stop mysqld_safe with 'mysqladmin101 shutdown'
- Restore the root password with post-restore-config

* Sat Sep 30 2017 stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.3
- Added phpMyAdmin configuration template

* Sun May 22 2016 stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.2
- backup and restore function added

* Tue May 10 2016 stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.1
- First release


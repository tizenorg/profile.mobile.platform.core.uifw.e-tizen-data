Name:          e-tizen-data
Version:       0.2.1
Release:       0
BuildArch:     noarch
Summary:       Enlightenment data files
Group:         Graphics & UI Framework/Other
License:       BSD-2-Clause
Source0:       %{name}-%{version}.tar.gz
Source1001:    %{name}.manifest
BuildRequires: pkgconfig(eet)
BuildRequires: pkgconfig(edje)
BuildRequires: eet-bin
BuildRequires: edje-tools
BuildRequires: xkb-tizen-data
Requires:      enlightenment
Requires:      e-mod-tizen-gesture

%global TZ_SYS_RO_SHARE  %{?TZ_SYS_RO_SHARE:%TZ_SYS_RO_SHARE}%{!?TZ_SYS_RO_SHARE:/usr/share}

%description
Data and configuration files for enlightenment

%prep
%setup -q
cp -a %{SOURCE1001} .

export TZ_SYS_RO_SHARE="%{TZ_SYS_RO_SHARE}"
default/config/tizen-mobile/make_keymap_conf.sh

%build
%autogen
%configure  \
    --with-systemdunitdir=%{_unitdir} \
    --with-engine=gl \
    --disable-skip-first-damage \
    --prefix=%{TZ_SYS_RO_SHARE}/enlightenment
make

%install
rm -rf %{buildroot}

#for license notification
mkdir -p %{buildroot}/%{TZ_SYS_RO_SHARE}/license
cp -a %{_builddir}/%{buildsubdir}/COPYING %{buildroot}/%{TZ_SYS_RO_SHARE}/license/%{name}

%__mkdir_p %{buildroot}/%{TZ_SYS_RO_SHARE}/enlightenment/data/config/tizen-mobile
%__mkdir_p %{buildroot}/%{TZ_SYS_RO_SHARE}/enlightenment/data/backgrounds
%__mkdir_p %{buildroot}/%{TZ_SYS_RO_SHARE}/enlightenment/data/themes
%__cp -afr default/config/*.cfg          %{buildroot}/%{TZ_SYS_RO_SHARE}/enlightenment/data/config
%__cp -afr default/config/tizen-mobile/*.cfg %{buildroot}/%{TZ_SYS_RO_SHARE}/enlightenment/data/config/tizen-mobile
%__cp -afr default/backgrounds/*.edj     %{buildroot}/%{TZ_SYS_RO_SHARE}/enlightenment/data/backgrounds
%__cp -afr default/themes/*.edj     %{buildroot}/%{TZ_SYS_RO_SHARE}/enlightenment/data/themes

%define daemon_user display
%define daemon_group display

# install service
%__mkdir_p %{buildroot}%{_unitdir}
install -m 644 data/units/display-manager-run.service %{buildroot}%{_unitdir}
install -m 644 data/units/display-manager.service %{buildroot}%{_unitdir}
install -m 644 data/units/display-manager.path %{buildroot}%{_unitdir}

%__mkdir_p %{buildroot}%{_unitdir_user}
install -m 644 data/units/enlightenment-user.service %{buildroot}%{_unitdir_user}
install -m 644 data/units/enlightenment-user.path %{buildroot}%{_unitdir_user}

# install env file for service
%__mkdir_p %{buildroot}%{_sysconfdir}/sysconfig
install -m 0644 data/units/enlightenment %{buildroot}%{_sysconfdir}/sysconfig

# install enlightenment.sh
%__mkdir_p %{buildroot}%{_sysconfdir}/profile.d
install -m 0644 data/units/enlightenment.sh %{buildroot}%{_sysconfdir}/profile.d

%pre
# create groups 'display'
getent group %{daemon_group} >/dev/null || %{_sbindir}/groupadd -r -o %{daemon_group}

# create user 'display'
getent passwd %{daemon_user} >/dev/null || %{_sbindir}/useradd -r -g %{daemon_group} -d /run/display -s /bin/false -c "Display daemon" %{daemon_user}

# setup display manager service
%__mkdir_p %{_unitdir}/graphical.target.wants/
ln -sf ../display-manager.path %{_unitdir}/graphical.target.wants/
ln -sf ../display-manager-run.service %{_unitdir}/graphical.target.wants/

%__mkdir_p %{_unitdir_user}/default.target.wants
ln -sf ../enlightenment-user.path %{_unitdir_user}/default.target.wants/

%postun
rm -f %{_unitdir}/graphical.target.wants/display-manager.path
rm -f %{_unitdir}/graphical.target.wants/display-manager-run.service
rm -f %{_unitdir_user}/default.target.wants/enlightenment-user.path

%files
%manifest %{name}.manifest
%defattr(-,root,root,-)
%{TZ_SYS_RO_SHARE}/license/%{name}
%{TZ_SYS_RO_SHARE}/enlightenment/data
%{TZ_SYS_RO_SHARE}/enlightenment/data/backgrounds/*.edj
%{TZ_SYS_RO_SHARE}/enlightenment/data/themes/*.edj
%{TZ_SYS_RO_SHARE}/enlightenment/data/config/*.cfg
%{TZ_SYS_RO_SHARE}/enlightenment/data/config/tizen-mobile/*.cfg
%{_unitdir}/display-manager.path
%{_unitdir}/display-manager.service
%{_unitdir}/display-manager-run.service
%{_unitdir_user}/enlightenment-user.path
%{_unitdir_user}/enlightenment-user.service
%config %{_sysconfdir}/sysconfig/enlightenment
%config %{_sysconfdir}/profile.d/enlightenment.sh

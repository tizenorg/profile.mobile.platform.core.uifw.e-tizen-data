%bcond_with wayland
%bcond_with x

Name:          e-tizen-data
Version:       0.1.6
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
%if %{with x}
    --with-x11 \
%endif
%if %{with wayland}
    --with-wayland \
%endif
    --with-systemdunitdir=%{_unitdir} \
    --with-engine=gl \
    --disable-skip-first-damage \
    --prefix=%{TZ_SYS_RO_SHARE}/enlightenment
make

%install
rm -rf %{buildroot}

%__mkdir_p %{buildroot}/%{TZ_SYS_RO_SHARE}/enlightenment/data/config/tizen-mobile
%__mkdir_p %{buildroot}/%{TZ_SYS_RO_SHARE}/enlightenment/data/backgrounds
%__mkdir_p %{buildroot}/%{TZ_SYS_RO_SHARE}/enlightenment/data/themes
%__cp -afr default/config/*.cfg          %{buildroot}/%{TZ_SYS_RO_SHARE}/enlightenment/data/config
%__cp -afr default/config/tizen-mobile/*.cfg %{buildroot}/%{TZ_SYS_RO_SHARE}/enlightenment/data/config/tizen-mobile
%__cp -afr default/backgrounds/*.edj     %{buildroot}/%{TZ_SYS_RO_SHARE}/enlightenment/data/backgrounds
%__cp -afr default/themes/*.edj     %{buildroot}/%{TZ_SYS_RO_SHARE}/enlightenment/data/themes

%if %{with x}
%__mkdir_p %{buildroot}%{_unitdir}
%__cp -afr default/x11/enlightenment.service %{buildroot}%{_unitdir}
%__mkdir_p %{buildroot}%{_unitdir}/graphical.target.wants
ln -sf ../enlightenment.service %{buildroot}%{_unitdir}/graphical.target.wants/enlightenment.service
%endif

%if %{with wayland}
%define daemon_user display
%define daemon_group display

# install service
%__mkdir_p %{buildroot}%{_unitdir}
install -m 644 default/wayland/display-manager-run.service %{buildroot}%{_unitdir}
install -m 644 default/wayland/display-manager.service %{buildroot}%{_unitdir}
install -m 644 default/wayland/display-manager.path %{buildroot}%{_unitdir}

%__mkdir_p %{buildroot}%{_unitdir_user}
install -m 644 default/wayland/enlightenment-user.service %{buildroot}%{_unitdir_user}
install -m 644 default/wayland/enlightenment-user.path %{buildroot}%{_unitdir_user}

# install env file for service
%__mkdir_p %{buildroot}%{_sysconfdir}/sysconfig
install -m 0644 default/wayland/enlightenment %{buildroot}%{_sysconfdir}/sysconfig

# install enlightenment.sh
%__mkdir_p %{buildroot}%{_sysconfdir}/profile.d
install -m 0644 default/wayland/enlightenment.sh %{buildroot}%{_sysconfdir}/profile.d

%endif

%pre
%if %{with wayland}
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
%endif

%postun
%if %{with wayland}
rm -f %{_unitdir}/graphical.target.wants/display-manager.path
rm -f %{_unitdir}/graphical.target.wants/display-manager-run.service
rm -f %{_unitdir_user}/default.target.wants/enlightenment-user.path
%endif

%files
%manifest %{name}.manifest
%defattr(-,root,root,-)
%license COPYING
%{TZ_SYS_RO_SHARE}/enlightenment/data
%{TZ_SYS_RO_SHARE}/enlightenment/data/backgrounds/*.edj
%{TZ_SYS_RO_SHARE}/enlightenment/data/themes/*.edj
%{TZ_SYS_RO_SHARE}/enlightenment/data/config/*.cfg
%{TZ_SYS_RO_SHARE}/enlightenment/data/config/tizen-mobile/*.cfg
%if %{with x}
%{_unitdir}/enlightenment.service
%{_unitdir}/graphical.target.wants/enlightenment.service
%endif
%if %{with wayland}
%{_unitdir}/display-manager.path
%{_unitdir}/display-manager.service
%{_unitdir}/display-manager-run.service
%{_unitdir_user}/enlightenment-user.path
%{_unitdir_user}/enlightenment-user.service
%config %{_sysconfdir}/sysconfig/enlightenment
%config %{_sysconfdir}/profile.d/enlightenment.sh
%endif

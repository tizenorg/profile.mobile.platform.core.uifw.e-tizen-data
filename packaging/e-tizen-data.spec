%bcond_with wayland
%bcond_with x

Name:          e-tizen-data
Version:       0.0.5
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
Requires:      enlightenment

%description
Data and configuration files for enlightenment

%prep
%setup -q
cp -a %{SOURCE1001} .

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
    --prefix=/usr/share/enlightenment
make

%install
rm -rf %{buildroot}

%__mkdir_p %{buildroot}/usr/share/enlightenment/data/config/tizen-mobile
%__mkdir_p %{buildroot}/usr/share/enlightenment/data/backgrounds
%__cp -afr default/config/*.cfg          %{buildroot}/usr/share/enlightenment/data/config
%__cp -afr default/config/tizen-mobile/*.cfg %{buildroot}/usr/share/enlightenment/data/config/tizen-mobile
%__cp -afr default/backgrounds/*.edj     %{buildroot}/usr/share/enlightenment/data/backgrounds

%if %{with x}
%__mkdir_p %{buildroot}%{_unitdir}
%__cp -afr default/x11/enlightenment.service %{buildroot}%{_unitdir}
%__mkdir_p %{buildroot}%{_unitdir}/graphical.target.wants
ln -sf ../enlightenment.service %{buildroot}%{_unitdir}/graphical.target.wants/enlightenment.service
%endif

%if %{with wayland}
%__mkdir_p %{buildroot}%{_unitdir}
%__cp -afr default/wayland/enlightenment.service %{buildroot}%{_unitdir}
%__cp -afr default/wayland/display-manager.path %{buildroot}%{_unitdir}
%__cp -afr default/wayland/display-manager.service %{buildroot}%{_unitdir}
%__cp -afr default/wayland/display-manager-run.service %{buildroot}%{_unitdir}
%__mkdir_p %{buildroot}%{_sysconfdir}/sysconfig
%__cp -afr default/wayland/enlightenment %{buildroot}%{_sysconfdir}/sysconfig
%__mkdir_p %{buildroot}%{_sysconfdir}/profile.d
%__cp -afr default/wayland/enlightenment.sh %{buildroot}%{_sysconfdir}/profile.d

%__mkdir_p %{buildroot}%{_unitdir}/graphical.target.wants
ln -sf ../enlightenment.service %{buildroot}%{_unitdir}/graphical.target.wants/enlightenment.service
ln -sf ../display-manager.service %{buildroot}%{_unitdir}/graphical.target.wants/display-manager.service
ln -sf ../display-manager-run.service %{buildroot}%{_unitdir}/graphical.target.wants/display-manager-run.service
%endif

%pre
if [ ! -e "/usr/share/enlightenment/data/config" ]
then
	mkdir -p /usr/share/enlightenment/data/config
fi

if [ ! -e "/usr/share/enlightenment/data/backgrounds" ]
then
	mkdir -p /usr/share/enlightenment/data/backgrounds
fi

%post

%files
%manifest %{name}.manifest
%defattr(-,root,root,-)
%license COPYING
/usr/share/enlightenment/data
/usr/share/enlightenment/data/backgrounds/*.edj
/usr/share/enlightenment/data/config/*.cfg
/usr/share/enlightenment/data/config/tizen-mobile/*.cfg
%if %{with x}
%{_unitdir}/enlightenment.service
%{_unitdir}/graphical.target.wants/enlightenment.service
%endif
%if %{with wayland}
%{_unitdir}/enlightenment.service
%{_unitdir}/display-manager.path
%{_unitdir}/display-manager.service
%{_unitdir}/display-manager-run.service
%{_unitdir}/graphical.target.wants/enlightenment.service
%{_unitdir}/graphical.target.wants/display-manager.service
%{_unitdir}/graphical.target.wants/display-manager-run.service
%{_sysconfdir}/sysconfig/enlightenment
%{_sysconfdir}/profile.d/enlightenment.sh
%endif

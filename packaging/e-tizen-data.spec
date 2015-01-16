Name:          e-tizen-data
Version:       0.0.2
Release:       0
Summary:       Enlightenment data files
Group:         Graphics/EFL
License:       BSD-2-Clause
Source0:       %{name}-%{version}.tar.gz
Source1001:    %{name}.manifest
BuildRequires: pkgconfig(eet)
BuildRequires: eet-bin
Requires:      enlightenment

%description
Data and configuration files for enlightenment

%prep
%setup -q
cp -a %{SOURCE1001} .

%build
%autogen
%configure --prefix=/usr/share/enlightenment
make

%install
rm -rf %{buildroot}

%__mkdir_p %{buildroot}/usr/share/enlightenment/data/config/tizen-mobile
%__cp -afr %{_arch}/config/*.cfg          %{buildroot}/usr/share/enlightenment/data/config
%__cp -afr %{_arch}/config/tizen-mobile/*.cfg %{buildroot}/usr/share/enlightenment/data/config/tizen-mobile

%pre
if [ ! -e "/usr/share/enlightenment/data/config" ]
then
	mkdir -p /usr/share/enlightenment/data/config
fi

%post

%files
%manifest %{name}.manifest
%defattr(-,root,root,-)
%license COPYING
/usr/share/enlightenment/data
/usr/share/enlightenment/data/config/*.cfg
/usr/share/enlightenment/data/config/tizen-mobile/*.cfg

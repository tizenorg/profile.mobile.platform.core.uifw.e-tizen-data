Name:          e-tizen-data
Version:       0.0.2
Release:       0
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
%configure --prefix=/usr/share/enlightenment
make

%install
rm -rf %{buildroot}

%__mkdir_p %{buildroot}/usr/share/enlightenment/data/config/tizen-mobile
%__mkdir_p %{buildroot}/usr/share/enlightenment/data/backgrounds
%__cp -afr %{_arch}/config/*.cfg          %{buildroot}/usr/share/enlightenment/data/config
%__cp -afr %{_arch}/config/tizen-mobile/*.cfg %{buildroot}/usr/share/enlightenment/data/config/tizen-mobile
%__cp -afr %{_arch}/backgrounds/*.edj     %{buildroot}/usr/share/enlightenment/data/backgrounds

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

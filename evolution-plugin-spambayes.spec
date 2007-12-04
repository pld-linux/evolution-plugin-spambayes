#
Summary:	Evolution plugin that allows to use the SpamBayes bayesian filtering system
Summary(pl.UTF-8):	Filtr SpamBayes dla Evolution
Name:		evolution-plugin-spambayes
Version:	0.1.4
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://dev.infonet.dk/debian/dists/testing/source/%{name}_%{version}.tar.gz
# Source0-md5:	266ba9541bda536add3340745eaf67e2
URL:		http://halfdans.net/wiki.py/EvolutionSpamBayesPlugin
Patch0:		%{name}-evo_plug_ver.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-devel >= 0.93
BuildRequires:	pkgconfig
BuildRequires:	python >= 1:2.4
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
BuildRequires:	evolution-devel >= 2.8.0
BuildRequires:	gtk+2-devel >= 2.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An Evolution plugin that allows Evolution to use the SpamBayes
bayesian filtering system.

The plugin is based on the Bogofilter EPlugin by Mikhail Zabaluev with
some "pass message to process" code from the built-in SpamAssassin
filtering plugin by Vivek Jain (amongst others).

%description -l pl.UTF-8

%prep
%setup -q
%patch0 -p1

%build
%{__autoconf}
%{__autoheader}
%{__automake}

%configure

%{__make} \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%gconf_schema_install sb-eplugin.schemas

%preun	-p /sbin/ldconfig
%gconf_schema_uninstall sb-eplugin.schemas

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/evolution/*/glade/*.glade
%attr(755,root,root) %{_libdir}/evolution/*/plugins/*.so
%{_libdir}/evolution/*/plugins/*.eplug
%{_sysconfdir}/gconf/schemas/sb-eplugin.schemas
%{_datadir}/dbus-1/services/*.service

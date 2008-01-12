Summary:	Evolution plugin that allows to use the SpamBayes bayesian filtering system
Summary(pl.UTF-8):	Wtyczka Evolution pozwalająca na używanie filtru bayesowskiego SpamBayes
Name:		evolution-plugin-spambayes
Version:	0.1.4
Release:	0.1
License:	GPL v2
Group:		Applications/Mail
Source0:	http://dev.infonet.dk/debian/dists/testing/source/%{name}_%{version}.tar.gz
# Source0-md5:	266ba9541bda536add3340745eaf67e2
Patch0:		%{name}-evo_plug_ver.patch
URL:		http://halfdans.net/wiki.py/EvolutionSpamBayesPlugin
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-devel >= 0.93
BuildRequires:	evolution-devel >= 2.8.0
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	pkgconfig
BuildRequires:	python >= 1:2.4
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires(post):	/sbin/ldconfig
Requires(post,preun):	GConf2
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An Evolution plugin that allows Evolution to use the SpamBayes
bayesian filtering system.

The plugin is based on the Bogofilter EPlugin by Mikhail Zabaluev with
some "pass message to process" code from the built-in SpamAssassin
filtering plugin by Vivek Jain (amongst others).

%description -l pl.UTF-8
Wtyczka Evolution pozwalająca na używanie systemu filtrowania
bayesowskiego SpamBayes.

Wtyczka jest oparta na wtyczce Bogofilter autorstwa Mikhaila Zabalueva
z dodanym kodem przekazywania wiadomości do przetworzenia z wbudowanej
wtyczki filtrującej SpamAssassina autorstwa Viveka Jaina (i innych).

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

%post
/sbin/ldconfig
%gconf_schema_install sb-eplugin.schemas

%preun
%gconf_schema_uninstall sb-eplugin.schemas

%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/evolution/*/plugins/*.so
%{_libdir}/evolution/*/plugins/*.eplug
%{_datadir}/evolution/*/glade/*.glade
%{_sysconfdir}/gconf/schemas/sb-eplugin.schemas
%{_datadir}/dbus-1/services/*.service

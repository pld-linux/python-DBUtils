%define 	module	DBUtils
Summary:	Database connections for multi-threaded environments
Summary(pl.UTF-8):	-
Name:		python-%{module}
Version:	1.0
Release:	0.1
License:	Open Software License v. 2.1
Group:		Development/Languages/Python
Source0:	http://www.webwareforpython.org/downloads/DBUtils/%{module}-%{version}.tar.gz
# Source0-md5:	33cad7d8dcfff07dea8600de9ed4119f
URL:		http://www.webwareforpython.org/DBUtils
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
# if py_postclean is used
BuildRequires:	rpmbuild(macros) >= 1.219
#Requires:		python-libs
Requires:		python-modules
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl.UTF-8

%prep
%setup -q -n %{module}-%{version}

%build
# CFLAGS is only for arch packages - remove on noarch packages
export CFLAGS="%{rpmcflags}"
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc DBUtils/Docs
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]
%dir %{py_sitescriptdir}/%{module}/Examples
%{py_sitescriptdir}/%{module}/Examples/*.py[co]
%dir %{py_sitescriptdir}/%{module}/Testing
%{py_sitescriptdir}/%{module}/Testing/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-*.egg-info
%endif

%define 	module	DBUtils
Summary:	Database connections for multi-threaded environments
#Summary(pl.UTF-8):	-
Name:		python-%{module}
Version:	1.1
Release:	0.1
License:	Open Software License v. 2.1
Group:		Development/Languages/Python
Source0:	http://www.webwareforpython.org/downloads/DBUtils/%{module}-%{version}.tar.gz
# Source0-md5:	aa13d60db0377234c5f9469212da5022
URL:		http://www.webwareforpython.org/DBUtils
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBUtils is a suite of tools providing solid, persistent and pooled
connections to a database that can be used in all kinds of
multi-threaded environments like Webware for Python or other web
application servers. The suite supports DB-API 2 compliant database
interfaces and the classic PyGreSQL interface.

# %description -l pl.UTF-8

%prep
%setup -q -n %{module}-%{version}

%build
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
%dir %{py_sitescriptdir}/%{module}/Tests
%{py_sitescriptdir}/%{module}/Tests/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-*.egg-info
%endif

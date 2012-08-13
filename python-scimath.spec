%define module	scimath
%define name	python-%{module}
%define version	4.1.0
%define	rel		1
%if %mdkversion < 201100
%define release %mkrel %{rel}
%else
%define	release %{rel}
%endif

Summary:	Enthought Tool Suite - scientific and mathematical calculations
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://www.enthought.com/repo/ets/%{module}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		https://github.com/enthought/scimath/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Obsoletes:	python-enthought-scimath
Requires:	python-traits >= 4.2.0
Requires:	python-numpy >= 1.1.0
Requires:	python-scipy >= 0.5.2
BuildRequires:	python-setuptools >= 0.6c8
BuildRequires:	python-numpy-devel >= 1.1.0
BuildRequires:	x11-server-xvfb, procps
BuildRequires:	python-setupdocs >= 1.0.5
BuildRequires:	python-sphinx

%description
The scimath project includes packages to support scientific and mathematical
calculations, beyond the capabilities offered by SciPy.

%prep
%setup -q -n %{module}-%{version}

%build
%__python setup.py build
Xvfb :100 -ac &
XPID=$!
export DISPLAY=:100.0
%__python setup.py build_docs
kill -9 $XPID

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc *.txt *.rst build/docs/html
%py_platsitedir/%{module}*

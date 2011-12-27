%define module	scimath
%define name	python-%{module}
%define version	4.0.1
%define release %mkrel 1

Summary:	Enthought Tool Suite - scimath project
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{module}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		https://github.com/enthought/scimath/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Obsoletes:	python-enthought-scimath
Requires:	python-traits >= 4.1.0
Requires:	python-numpy >= 1.1.0
Requires:	python-scipy >= 0.5.2
BuildRequires:	python-setuptools >= 0.6c8
BuildRequires:	python-numpy-devel >= 1.1.0
BuildRequires:	python-sphinx

%description
The scimath project includes packages to support scientific and mathematical
calculations, beyond the capabilities offered by SciPy.

- scimath.interpolate
- scimath.mathematics
- scimath.units
- scimath.physical_quantities

%prep
%setup -q -n %{module}-%{version}

%build

%__python setup.py build
pushd docs
make html
popd

%install
%__rm -rf %{buildroot}

PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc *.txt *.rst docs/build/html


%define module	scimath
%define name	python-%{module}
%define version	4.1.0
%define release 2

Summary:	Enthought Tool Suite - scimath project
Name:		%{name}
Version:	4.1.2
Release:	2
Source0:	https://www.enthought.com/repo/ets/scimath-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		https://github.com/enthought/scimath/
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

python setup.py build
pushd docs
make html
popd

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}
#--record=FILE_LIST

%files 
#-f FILE_LIST
%doc *.txt *.rst docs/build/html
%{python_sitearch}/%{module}*


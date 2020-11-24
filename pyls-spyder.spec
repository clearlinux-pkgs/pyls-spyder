#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyls-spyder
Version  : 0.2.0
Release  : 2
URL      : https://files.pythonhosted.org/packages/dc/10/3a164277b47d6fca04b182adee34944171a3b492922cae2e08574660d228/pyls-spyder-0.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/dc/10/3a164277b47d6fca04b182adee34944171a3b492922cae2e08574660d228/pyls-spyder-0.2.0.tar.gz
Summary  : Spyder extensions for the python-language-server
Group    : Development/Tools
License  : MIT
Requires: pyls-spyder-license = %{version}-%{release}
Requires: pyls-spyder-python = %{version}-%{release}
Requires: pyls-spyder-python3 = %{version}-%{release}
Requires: python-language-server
BuildRequires : buildreq-distutils3
BuildRequires : python-language-server

%description
# pyls-spyder
[![Project License - MIT](https://img.shields.io/pypi/l/pyls-spyder.svg)](https://raw.githubusercontent.com/spyder-ide/pyls-spyder/master/LICENSE)
[![pypi version](https://img.shields.io/pypi/v/pyls-spyder.svg)](https://pypi.org/project/pyls-spyder/)
[![conda version](https://img.shields.io/conda/vn/conda-forge/pyls-spyder.svg)](https://www.anaconda.com/download/)
[![download count](https://img.shields.io/conda/dn/conda-forge/pyls-spyder.svg)](https://www.anaconda.com/download/)
[![Downloads](https://pepy.tech/badge/pyls-spyder)](https://pepy.tech/project/pyls-spyder)
[![PyPI status](https://img.shields.io/pypi/status/pyls-spyder.svg)](https://github.com/spyder-ide/pyls-spyder)
![PyLS-Spyder tests](https://github.com/spyder-ide/pyls-spyder/workflows/PyLS-Spyder%20tests/badge.svg)

%package license
Summary: license components for the pyls-spyder package.
Group: Default

%description license
license components for the pyls-spyder package.


%package python
Summary: python components for the pyls-spyder package.
Group: Default
Requires: pyls-spyder-python3 = %{version}-%{release}

%description python
python components for the pyls-spyder package.


%package python3
Summary: python3 components for the pyls-spyder package.
Group: Default
Requires: python3-core
Provides: pypi(pyls_spyder)
Requires: pypi(python_language_server)

%description python3
python3 components for the pyls-spyder package.


%prep
%setup -q -n pyls-spyder-0.2.0
cd %{_builddir}/pyls-spyder-0.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1606234677
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pyls-spyder
cp %{_builddir}/pyls-spyder-0.2.0/LICENSE %{buildroot}/usr/share/package-licenses/pyls-spyder/3b8430679131d39161725b9b41dd652aeb125d39
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pyls-spyder/3b8430679131d39161725b9b41dd652aeb125d39

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

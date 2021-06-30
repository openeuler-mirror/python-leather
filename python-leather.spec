%{?python_enable_dependency_generator}
%global pypi_name leather
%global dir_name leather
%global github_name leather
%global commit e85dd30cc20270180c26c56fd895aff61e84f741

Name:           python-%{pypi_name}
Version:        0.3.3
Release:        1
Summary:        Python charting for 80% of humans

License:        MIT
URL:            https://pypi.python.org/pypi/leather
Source0:        https://github.com/%{project_owner}/%{github_name}/archive/%{commit}/%{github_name}-%{commit}.tar.gz
BuildArch:      noarch

%description
desc Leather is the Python charting library for those who need charts now and don’t\
care if they’re perfect.\
\
- A readable and user-friendly API.\
- Optimized for exploratory charting.\
- Produces scale-independent SVG charts.\
- Completely type-agnostic. Chart your data, whatever it is.\
- Designed with iPython, Jupyter and atom/hydrogen in mind.\
- Pure Python. No C dependencies to compile.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-nose >= 1.1.2
BuildRequires:  python3-sphinx >= 1.2.2
BuildRequires:  python3-coverage >= 3.7.1
BuildRequires:  python3-sphinx_rtd_theme >= 0.1.6
BuildRequires:  python3-lxml >= 3.6.0
BuildRequires:  python3-six >= 1.6.1
BuildRequires:  python3-cssselect
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
desc Leather is the Python charting library for those who need charts now and don’t\
care if they’re perfect.\
\
- A readable and user-friendly API.\
- Optimized for exploratory charting.\
- Produces scale-independent SVG charts.\
- Completely type-agnostic. Chart your data, whatever it is.\
- Designed with iPython, Jupyter and atom/hydrogen in mind.\
- Pure Python. No C dependencies to compile.


%package -n    python-%{pypi_name}-doc
Summary:       %{summary}

%description -n python-%{pypi_name}-doc
desc Leather is the Python charting library for those who need charts now and don’t\
care if they’re perfect.\
\
- A readable and user-friendly API.\
- Optimized for exploratory charting.\
- Produces scale-independent SVG charts.\
- Completely type-agnostic. Chart your data, whatever it is.\
- Designed with iPython, Jupyter and atom/hydrogen in mind.\
- Pure Python. No C dependencies to compile.

Documentation package.


%prep
%setup -qn %{github_name}-%{commit}
# Remove shebang on non executable scripts
sed -i '1{\@^#!/usr/bin/env python@d}' leather/*.py leather/**/*.py

# Remove hidden files in examples
rm examples/charts/.placeholder

%build
%py3_build
pushd docs
    make html
    # Remove hidden file
    rm _build/html/.buildinfo
popd


%install
%py3_install


%check
nosetests-%{python3_version} tests -v


%files -n python3-%{pypi_name}
%doc README.rst
%license COPYING
%{python3_sitelib}/%{dir_name}-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/%{dir_name}/


%files -n python-%{pypi_name}-doc
%doc examples docs/_build/html
%license COPYING


%changelog
* Mon Jun 28 2021 Cai Yuxin <caiyuxin@kylinos.cn> - 0.3.3-1
- Inital package

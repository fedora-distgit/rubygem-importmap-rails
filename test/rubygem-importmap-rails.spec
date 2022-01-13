# Generated from importmap-rails-1.0.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name importmap-rails

Name: rubygem-%{gem_name}
Version: 1.0.1
Release: 1%{?dist}
Summary: Use ESM with importmap to manage modern JavaScript in Rails without transpiling or bundling
License: MIT
URL: https://github.com/rails/importmap-rails
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.7.0
BuildArch: noarch

%description
Use ESM with importmap to manage modern JavaScript in Rails without
transpiling or bundling.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/



%check
pushd .%{gem_instdir}
# Run the test suite.
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/MIT-LICENSE
%{gem_instdir}/app
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile

%changelog
* Thu Jan 13 2022 Pavel Valena <pvalena@redhat.com> - 1.0.1-1
- Initial package

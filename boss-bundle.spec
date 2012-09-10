#
# spec file for package rubygem-ruote (Version 2.1.10)
#
# Copyright (c) 2009 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# norootforbuild
Name:           boss-bundle
Summary:        Bundle of gems used by BOSS
Version:        0.0.2
Release:        1
#
Group:          Development/Languages/Ruby
License:        GPLv2+ or Ruby
#
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  rubygems_with_buildroot_patch
%rubygems_requires
BuildRequires:  rubygem-bundler git gcc-c++ openssl-devel pkg-config
Requires:       rubygem-bundler
#
Url:            https://wiki.merproject.org/wiki/boss
# DEVSRC=/maemo/devel/BOSS/bundle-approach/home_lbt_bundler/bb
# cp $DEVSRC/vendor/cache/*gem .
# here=$(pwd);cd $DEVSRC;c=3;for src in $(find vendor/cache/  -mindepth 1 -maxdepth 1 -type d); do tar cfj $here/$(basename $src).tar.bz2 $src; echo Source$((c++)): $(basename $src).tar.bz2; done; cd $here
# for g in *gem; do echo Source$((c++)): $(basename $g); done; 
Source0: Gemfile
Source1: Gemfile.lock
Source2: boss-bundle.rpmlintrc
Source3: amqp-0aedfff3cf1b.tar.bz2
Source4: ruote-7afe764fc7e2.tar.bz2
Source5: ruote-amqp-c49c81f3ef3a.tar.bz2
Source6: ruote-kit-a6d500040eac.tar.bz2
Source7: amq-client-0.9.4.gem
Source8: amq-protocol-0.9.4.gem
Source9: blankslate-2.1.2.4.gem
Source10: diff-lcs-1.1.3.gem
Source11: eventmachine-0.12.10.gem
Source12: file-tail-1.0.11.gem
Source13: haml-3.1.7.gem
Source14: inifile-2.0.0.gem
Source15: parslet-1.4.0.gem
Source16: rack-1.4.1.gem
Source17: rack-protection-1.2.0.gem
Source18: rspec-2.11.0.gem
Source19: rspec-core-2.11.1.gem
Source20: rspec-expectations-2.11.3.gem
Source21: rspec-mocks-2.11.2.gem
Source22: ruby2ruby-1.3.1.gem
Source23: ruby_parser-2.3.1.gem
Source24: rufus-cloche-1.0.2.gem
Source25: rufus-dollar-1.0.4.gem
Source26: rufus-json-1.0.1.gem
Source27: rufus-mnemo-1.2.3.gem
Source28: rufus-scheduler-2.0.16.gem
Source29: rufus-treechecker-1.0.8.gem
Source30: sexp_processor-3.2.0.gem
Source31: sinatra-1.3.3.gem
Source32: sinatra-respond_to-0.8.0.gem
Source33: sourcify-0.5.0.gem
Source34: tilt-1.3.3.gem
Source35: tins-0.5.3.gem
Source36: tzinfo-0.3.33.gem
Source37: yajl-ruby-1.1.0.gem
# SourceEnd : This line is needed to make the script in the README work

Summary:        Gems needed to run BOSS
%description

This package is the bundle of gems needed to run BOSS

%prep
# We use the Gemfile, Gemfile,lock and rpmlintrc
cp %{SOURCE0} .
cp %{SOURCE1} .
cp %{SOURCE2} .

mkdir -p vendor/cache;
for file in %{lua: for i, p in ipairs(sources) do print(p.." ") end}; do if [[ ${file: -3:3} == "gem" ]]; then cp $file vendor/cache; elif [[ ${file: -3:3} == "bz2" ]]; then tar xf $file; fi; done

%build
%install
mkdir -p %{buildroot}/usr/lib/boss-bundle
bundle install --local --standalone --deployment --binstubs=%{buildroot}/usr/bin/ --no-cache --shebang=/usr/bin/ruby
find . -name .gitignore | xargs rm
cp -al . %{buildroot}/usr/lib/boss-bundle/


# Change #!/usr/local/bin/ruby to #!/usr/bin/ruby
sed -i -e 's_/usr/local/bin_/usr/bin_' $(grep -rl "usr/local/bin" %{buildroot})

%files
%defattr(-,root,root,-)
/usr/lib/boss-bundle/
/usr/bin/

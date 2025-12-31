%bcond tests 0

Name:           amber
Version:        0.5.1
Release:        1%{?dist}
Summary:        Programming language that compiles to Bash

License:        GPL-3.0-or-later
URL:            https://amber-lang.com/
Source0:        https://github.com/amber-lang/amber/archive/refs/tags/%{version}-alpha.tar.gz

BuildRequires:  cargo
BuildRequires:  rust
Requires:       bash

%description
A language compiled to Bash.
A modern, type-safe programming language that catches bugs and errors
at compile time.


%prep
%autosetup -n %{name}-%{version}-alpha


%build


%install
cargo install --path . --root "%{buildroot}%{_prefix}"
rm %{buildroot}%{_prefix}/.crates*

%{buildroot}%{_bindir}/amber run docs.ab


%check
%if %{with tests}
cargo test --release
%endif


%files
%license LICENSE.md
%doc README.md src/std/docs
%{_bindir}/amber


%changelog
* Wed Dec 31 2025 Jens Petersen <petersen@redhat.com> - 0.5.1-1
- initial package of 0.5.1-alpha

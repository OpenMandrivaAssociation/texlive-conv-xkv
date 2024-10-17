Name:		texlive-conv-xkv
Version:	43558
Release:	2
Summary:	Create new key-value syntax
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/conv-xkv
License:	lppl1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/conv-xkv.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/conv-xkv.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/conv-xkv.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This small package supports key-value syntax other than the
standard LaTeX syntax of <key>=<value>. Using this package,
create key-values of the form <key>:<value> or <key>-><value>,
for example. The package converts the new notation to xkeyval
notation and passes it on to xkeyval.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/conv-xkv
%{_texmfdistdir}/tex/latex/conv-xkv
%doc %{_texmfdistdir}/doc/latex/conv-xkv

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

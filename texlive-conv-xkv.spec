%global tl_name conv-xkv
%global tl_revision 43558

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Create new key-value syntax
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/conv-xkv
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/conv-xkv.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/conv-xkv.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/conv-xkv.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This small package supports key-value syntax other than the standard
LaTeX syntax of <key>=<value>. Using this package, create key-values of
the form <key>:<value> or <key>-><value>, for example. The package
converts the new notation to xkeyval notation and passes it on to
xkeyval.


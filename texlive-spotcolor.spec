Name:		texlive-spotcolor
Version:	15878
Release:	1
Summary:	Spot colours for pdfLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/spotcolor
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spotcolor.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spotcolor.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides procedures for using spot colors in LaTeX
documents and the generated pdf files. Predefined templates for
PANTONE and HKS color spaces are included but new ones can
easily be defined.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/spotcolor/spotcolor.sty
%{_texmfdistdir}/tex/latex/spotcolor/spotcolorhks.tex
%{_texmfdistdir}/tex/latex/spotcolor/spotcolorpantone.tex
%doc %{_texmfdistdir}/doc/latex/spotcolor/README
%doc %{_texmfdistdir}/doc/latex/spotcolor/readme.pdf
%doc %{_texmfdistdir}/doc/latex/spotcolor/readme.tcp
%doc %{_texmfdistdir}/doc/latex/spotcolor/readme.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}

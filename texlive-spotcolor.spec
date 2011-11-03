# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/spotcolor
# catalog-date 2007-03-12 11:51:09 +0100
# catalog-license lppl
# catalog-version 1.2
Name:		texlive-spotcolor
Version:	1.2
Release:	1
Summary:	Spot colours for pdfLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/spotcolor
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spotcolor.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spotcolor.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This package provides procedures for using spot colors in LaTeX
documents and the generated pdf files. Predefined templates for
PANTONE and HKS color spaces are included but new ones can
easily be defined.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
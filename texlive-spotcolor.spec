# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/spotcolor
# catalog-date 2007-03-12 11:51:09 +0100
# catalog-license lppl
# catalog-version 1.2
Name:		texlive-spotcolor
Version:	1.2
Release:	3
Summary:	Spot colours for pdfLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/spotcolor
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spotcolor.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spotcolor.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.2-2
+ Revision: 756159
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.2-1
+ Revision: 719569
- texlive-spotcolor
- texlive-spotcolor
- texlive-spotcolor
- texlive-spotcolor


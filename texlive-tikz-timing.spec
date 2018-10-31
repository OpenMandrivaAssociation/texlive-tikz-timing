Name:		texlive-tikz-timing
Version:	0.7f
Release:	2
Summary:	Easy generation of timing diagrams as tikz pictures
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/tikz-timing
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-timing.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-timing.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-timing.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-svn-prov

%description
This package provides macros and an environment to generate
timing diagrams (digital waveforms) without much effort. The
TikZ package is used to produce the graphics. The diagrams may
be inserted into text (paragraphs, \hbox, etc.) and into
tikzpictures. A tabular-like environment is provided to produce
larger timing diagrams.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tikz-timing
%doc %{_texmfdistdir}/doc/latex/tikz-timing
#- source
%doc %{_texmfdistdir}/source/latex/tikz-timing

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}

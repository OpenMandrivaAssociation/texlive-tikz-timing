%global tl_name tikz-timing
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.7f
Release:	%{tl_revision}.1
Summary:	Easy generation of timing diagrams as TikZ pictures
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/tikz-timing
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-timing.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-timing.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-timing.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(svn-prov)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides macros and an environment to generate timing
diagrams (digital waveforms) without much effort. The TikZ package is
used to produce the graphics. The diagrams may be inserted into text
(paragraphs, \hbox, etc.) and into tikzpictures. A tabular-like
environment is provided to produce larger timing diagrams.


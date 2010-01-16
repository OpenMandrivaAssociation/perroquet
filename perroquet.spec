Summary:	A listening comprehension tutor
Name:		perroquet
Version:	1.0.1
Release:	%mkrel 2
Source0:	http://launchpad.net/perroquet/trunk/1.0.1/+download/perroquet-1.0.1.tar.gz
License:	GPLv3
Group:		Education
URL:		http://perroquet.b219.org
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	python-devel
BuildRequires:	intltool
BuildRequires:	python-setuptools
BuildRequires:	desktop-file-utils
Requires:	gtk+2.0
Requires:	gstreamer0.10-plugins-good
Requires:	gstreamer0.10-python
Requires:	pygtk2.0
BuildArch:	noarch

%description
Perroquet is a educational program to improve playfully your listening in a
foreign language.

The principle of Perroquet is to use a video or audio file and the associated
subtitles to make you listen and understand the dialogue or lyrics. After
having identified the files to use, Perroquet will read a piece of video then
pause. It will show you the number of words to find and you will have to type
them to continue. You can listen a sequence as many times as necessary.
If you do not understand, Perroquet offers several means to help you.

%prep
%setup -q -n %{name}-%{version}

%build
python setup.py build 

%install
%__rm -rf %{buildroot}
python setup.py \
	--without-icon-cache \
	--without-mime-database \
	--without-desktop-database \
	install --root=%{buildroot}

desktop-file-install \
	--remove-key=Encoding \
	--remove-category=Application \
	--add-category=Languages \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/%{name}.desktop

%find_lang %name

%clean
%__rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc README AUTHORS ChangeLog NEWS MAINTAINERS
%{_bindir}/%{name}
%{python_sitelib}/*
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/*/*.*
%{_datadir}/%{name}/*
%{_datadir}/pixmaps/*
%{_datadir}/mime/packages/%{name}.xml

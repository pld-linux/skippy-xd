Summary:	Full-screen task-switcher for X11
Summary(pl.UTF-8):   Pełnoekranowy przełącznik zadań dla X11
Name:		skippy-xd
Version:	0.5.0
Release:	1
License:	GPL v2
Group:		X11/Window Managers
Source0:	http://thegraveyard.org/files/%{name}-%{version}.tar.bz2
# Source0-md5:	0e847845c4cb8c16f79bc4538ae288ad
Patch0:		%{name}-fix_noxinerama.patch
Patch1:		%{name}-fix_CARD32.patch
URL:		http://thegraveyard.org/skippy.php
BuildRequires:	imlib2-devel
BuildRequires:	pcre-devel
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Skippy is what (I think) is best described as a full-screen
task-switcher for X11. It tries to provide an alternative when
taskbars or regular task-switchers aren't the most efficient way of
switching tasks (like when you have a lot of applications open). When
activated (currently only through a hotkey), it will arrange and scale
snapshots of all windows on the current desktop and it'll let you pick
a window using a mouse or a keyboard. Yes, this is also what expocity
and Apple's Expose do (yeah, I know, Expose does more than just this),
but I don't like metacity (expocity is a 'hacked up' version of that)
and I don't have a Mac.

%description -l pl.UTF-8
Skippy może być najlepiej określony jako pełnoekranowy przełącznik
zadań dla X11. Stanowi alternatywę dla pasków zadań i tradycyjnych
przełączników zadań, które nie są najefektywniejszą metodą
przełączania między zadaniami (zwłaszcza, jeśli ma się dużo
uruchomionych aplikacji. Kiedy zostanie aktywowany (obecnie tylko przy
pomocy klawisza), ułoży i przeskaluje miniaturki wszystkich okien na
bieżącym pulpicie i pozwoli na wybór okna przy pomocy klawiatury lub
myszy. Tak samo robi to expocity i Expose Apple'a, ale expocity to
osobny zarządca okien a Expose jest tylko dla Maców.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p2

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG skippy-xd.rc-default
%attr(755,root,root) %{_bindir}/*

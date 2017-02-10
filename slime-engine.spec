%define major 0
%define snapshot 20170210
%define debug_package %nil

Summary:        A QML Web view wrappe
Name:           slime-engine
Version:        0.1
Release:        1
License:        LGPLv3
Url:            https://github.com/tim-sueberkrueb
Source0:	%{name}-%{version}-%{snapshot}.tar.xz

BuildRequires:  cmake
BuildRequires:  cmake(Vibe)
BuildRequires:  qt5-devel
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickTest)
BuildRequires:  cmake(Qt5QuickControls2)

%description
A QML Web view wrappe

%prep
%setup -qn %{name}-%{version}-%{snapshot}

%build
%qmake_qt5
%make

%install
%makeinstall_std INSTALL_ROOT="%{buildroot}"

%files
%{_libdir}/qt5/qml/SlimeEngine/

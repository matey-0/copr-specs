Name:           bitwarden
Version:        2026.7.0                                                                                                                                     
Release:        1%{?dist}                                                                                                                                      
Summary:        Bitwarden Desktop (Repackaged)                                                                                                                 
License:        GPLv3
URL:            https://bitwarden.com

%global _build_id_links none
%define _use_internal_dependency_generator 0
%global __find_requires %{nil}
%global __os_install_post %{nil}

Requires: at-spi2-core
Requires: gtk3
Requires: libXScrnSaver
Requires: libnotify
Requires: nss
Requires: xdg-utils
Requires: (libXtst or libXtst6)
Requires: (libuuid or libuuid1)

%description
Bitwarden Desktop repackaged for COPR.
%prep
curl -L -o bitwarden.rpm "https://github.com/bitwarden/clients/releases/download/desktop-v%{version}/Bitwarden-%{version}-x86_64.rpm"

%install
mkdir -p %{buildroot}
rpm2cpio bitwarden.rpm | cpio -idmv -D %{buildroot}
rm -rf %{buildroot}/usr/lib
rm -f %{buildroot}/bitwarden.spec
mkdir -p %{buildroot}%{_bindir}
ln -sf /opt/Bitwarden/bitwarden %{buildroot}%{_bindir}/bitwarden

%files
%defattr(-,root,root,-)
/opt/Bitwarden/
/usr/bin/bitwarden
/usr/share/applications/bitwarden.desktop
/usr/share/icons/hicolor/*/apps/bitwarden.png

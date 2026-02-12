Name:           bitwarden
Version:        2026.1.0                                                                                                                                     
Release:        1%{?dist}                                                                                                                                      
Summary:        Bitwarden Desktop (Repackaged)                                                                                                                 
License:        GPLv3
URL:            https://bitwarden.com

%global _build_id_links none
%global __os_install_post %{nil}
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

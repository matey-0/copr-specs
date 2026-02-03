Name:           bitwarden
Version:        2025.1.1
Release:        1%{?dist}
Summary:        Bitwarden Desktop (Repackaged)
License:        GPLv3
URL:            https://bitwarden.com

%description
Bitwarden Desktop repackaged for COPR.

%prep
curl -L -o bitwarden.rpm "https://github.com/bitwarden/clients/releases/download/desktop-v%{version}/Bitwarden-%{version}-x86_64.rpm"

%build

%install
mkdir -p %{buildroot}
rpm2cpio bitwarden.rpm | cpio -idmv -D %{buildroot}

%files
/opt/Bitwarden/
/usr/bin/bitwarden
/usr/share/applications/bitwarden.desktop
/usr/share/icons/hicolor/*/apps/bitwarden.png
%exclude /bitwarden.spec

%changelog
- Automatic update to version %{version}

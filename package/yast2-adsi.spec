#
# spec file for package yast-adsi
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           yast2-adsi
Version:        1.2
Release:        0
Summary:        ADSI Edit for YaST
License:        GPL-3.0
Group:          Productivity/Networking/Samba
Url:            https://github.com/yast/yast-adsi
Source:         %{name}-%{version}.tar.bz2

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  perl-XML-Writer
BuildRequires:  python3
BuildRequires:  update-desktop-files
BuildRequires:  yast2
BuildRequires:  yast2-devtools
BuildRequires:  yast2-testsuite

Requires:       krb5-client
Requires:       samba-client
Requires:       samba-python3
Requires:       yast2
Requires:       yast2-python3-bindings >= 4.0.0
Requires:       python3-ldap
Requires:       yast2-adcommon-python >= 0.3

BuildArch:      noarch

%description
The ADSI Edit for YaST module provides tools for viewing and modifying
an LDAP tree.

%prep
%setup -q

%build

%install
%yast_install
%yast_metainfo

%files
%{yast_clientdir}
%{yast_yncludedir}
%{yast_desktopdir}
%{yast_metainfodir}
%doc %{yast_docdir}
%license COPYING

%changelog

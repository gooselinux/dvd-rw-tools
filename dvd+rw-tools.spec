Summary:	Toolchain to master DVD+RW/+R media
Name:		dvd+rw-tools
Version:	7.1
Release:	5%{?dist}
License:	GPLv2
Group:		Applications/Multimedia
Source:		http://fy.chalmers.se/~appro/linux/DVD+RW/tools/dvd+rw-tools-%{version}.tar.gz
Source1:	index.html
Patch1:		dvd+rw-tools-7.0.manpatch
Patch2:		dvd+rw-tools-7.0-wexit.patch
Patch3:		dvd+rw-tools-7.0-glibc2.6.90.patch
Patch4: 	dvd+rw-tools-7.0-reload.patch
Patch5: 	dvd+rw-tools-7.0-wctomb.patch
Patch6:		dvd+rw-tools-7.0-dvddl.patch
URL:		http://fy.chalmers.se/~appro/linux/DVD+RW/
Requires:	mkisofs >= 2.0
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	kernel-headers m4

%description
Collection of tools to master DVD+RW/+R media. For further
information see http://fy.chalmers.se/~appro/linux/DVD+RW/.

%prep
%setup -q
%patch1 -p1 -b .manpatch
%patch2 -p1 -b .wexit
%patch3 -p1 -b .glibc2.6.90
%patch4 -p1 -b .reload
%patch5 -p0 -b .wctomb
%patch6 -p0 -b .dvddl

install -m 644 %{SOURCE1} index.html

%build
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
export CXXFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
make WARN="-DDEFAULT_BUF_SIZE_MB=16 -DRLIMIT_MEMLOCK" %{?_smp_mflags}

%install
rm -rf %{buildroot}
# make install DESTDIR= does not work here
%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc index.html LICENSE
%{_bindir}/*
%{_mandir}/man1/growisofs.1*

%changelog
* Tue Jun 22 2010 Roman Rakus <rrakus@redhat.com> - 7.1-5
- Compile with -fno-strict-aliasing CFLAG
  Resolves: #605148

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 7.1-4.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Dec 17 2008 Roman Rakus <rrakus@redhat.com> - 7.1-2
- Allow burn small images on dvd-dl
  Resolves: #476154

* Fri Aug 15 2008 Roman Rakus <rrakus@redhat.com> - 7.1-1
- new version 7.1

* Wed Mar 26 2008 Harald Hoyer <harald@redhat.com> 7.0-11
- fixed widechar overflow (bug #426068) (patch from Jonathan Kamens)

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 7.0-9
- Autorebuild for GCC 4.3

* Tue Nov 20 2007 Harald Hoyer <harald@redhat.com> - 7.0-8
- added a patch to fix a reload problem on some drives, 
  after a successful burn

* Fri Aug 31 2007 Matthias Saou <http://freshrpms.net/> 7.0-7
- Minor spec file cleanups (tabs vs. spaces, etc.).
- Use install instead of cp for the html file to avoid umask differences.

* Fri Aug 17 2007 Harald Hoyer <harald@rawhide.home> - 7.0-6
- changed license to GPLv2

* Wed Aug 15 2007 Harald Hoyer <harald@redhat.com> - 7.0-5
- added limits.h to transport.hxx

* Thu Jun 21 2007 Harald Hoyer <harald@redhat.com> - 7.0-4
- fixed exit status (#243036)
- Allow session to cross 4GB boundary regardless of medium type.
  Add a -F option (used instead of -M or -Z), which displays 
  next_session offset and capacity. (#237967)

* Tue Feb 27 2007 Harald Hoyer <harald@redhat.com> - 7.0-3
- fixed specfile issues (#209985)

* Thu Dec 14 2006 Harald Hoyer <harald@redhat.com> - 7.0-0.4
- set pthread stack size according to limit (#215818)

* Wed Dec 13 2006 Harald Hoyer <harald@redhat.com> - 7.0-0.3
- use _SC_PHYS_PAGES instead of _SC_AVPHYS_PAGES to determine available memory
- Resolves: rhbz#216794

* Fri Nov 03 2006 Harald Hoyer <harald@redhat.com> - 7.0-0.2
- define RLIMIT_MEMLOCK, which should resolve the memlock problems

* Thu Oct 26 2006 Harald Hoyer <harald@redhat.com> - 7.0-0.1
- new version 7.0

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 6.1-4.1
- rebuild

* Tue Jun 13 2006 Harald Hoyer <harald@redhat.com> - 6.1-4
- more build requirements

* Tue Apr 18 2006 Harald Hoyer <harald@redhat.com> - 6.1-2
- compile with smaller buffer size
- removed O_EXCL patch

* Fri Mar 24 2006 Harald Hoyer <harald@redhat.com> - 6.1-1
- version 6.1

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 5.21.4.10.8-6.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 5.21.4.10.8-6.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Mar 02 2005 Harald Hoyer <harald@redhat.com> 
- rebuilt

* Wed Feb 16 2005 Harald Hoyer <harald@redhat.com> - 5.21.4.10.8-5
- built with RPM_OPT_FLAGS

* Wed Feb 09 2005 Harald Hoyer <harald@redhat.com>
- rebuilt

* Thu Nov 18 2004 Harald Hoyer <harald@redhat.com> - 5.21.4.10.8-4
- removed wget dependency

* Wed Sep 01 2004 Harald Hoyer <harald@redhat.com> - 5.21.4.10.8-2
- added dvd+rw-tools-5.21.4.10.8-excl.patch to open O_EXCL

* Wed Sep 01 2004 Harald Hoyer <harald@redhat.com> - 5.21.4.10.8-1
- version 5.21.4.10.8

* Mon Jul 26 2004 Harald Hoyer <harald@redhat.com> - 5.20.4.10.8-1
- version 5.20.4.10.8

* Wed Jun 16 2004 Harald Hoyer <harald@redhat.com> - 5.19.1.4.9.7-1
- version 5.19.1.4.9.7

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Jan 29 2004 Harald Hoyer <harald@redhat.com> - 5.17.4.8.6-1
- version 5.17.4.8.6
- fixes 110740 110700

* Wed Oct  8 2003 Harald Hoyer <harald@redhat.de> 5.13.4.7.4-1
- version 5.13.4.7.4

* Mon Sep 08 2003 Harald Hoyer <harald@redhat.de> 5.12.4.7.4-1
* updated to version 5.12.4.7.4

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Apr 15 2003 Harald Hoyer <harald@redhat.de> 5.3.4.2.4-1
- updated to version 5.3.4.2.4

* Mon Feb 3 2003 Chris Kloiber <ckloiber@redhat.com>
- Updated version to 5.1.4.0.4
- Requires mkisofs 2.0

* Thu Nov 4 2002 Andy Polyakov <appro@fy.chalmers.se>
- Minor growisofs update. Uninitialized errno at exit when
  -Z /dev/scd0=image.iso is used.

* Thu Nov 3 2002 Andy Polyakov <appro@fy.chalmers.se>
- Initial packaging. Package version is derived from growisofs,
  dvd+rw-format and dvd+rw-booktype version. 4.0.3.0.3 means
  growisofs 4.0, dvd+rw-format 3.0 dvd+rw-booktype 3.
  

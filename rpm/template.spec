Name:           ros-hydro-hector-gazebo-worlds
Version:        0.3.5
Release:        1%{?dist}
Summary:        ROS hector_gazebo_worlds package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/hector_gazebo_worlds
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-gazebo-ros
Requires:       ros-hydro-hector-gazebo-plugins
BuildRequires:  ros-hydro-catkin

%description
hector_gazebo_worlds provides gazebo scenarios used by Team Hector Darmstadt

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Mon Feb 23 2015 Johannes Meyer <meyer@fsr.tu-darmstadt.de> - 0.3.5-1
- Autogenerated by Bloom

* Mon Feb 23 2015 Johannes Meyer <meyer@fsr.tu-darmstadt.de> - 0.3.5-0
- Autogenerated by Bloom

* Mon Sep 01 2014 Johannes Meyer <meyer@fsr.tu-darmstadt.de> - 0.3.4-0
- Autogenerated by Bloom


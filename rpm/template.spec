Name:           ros-indigo-hector-gazebo
Version:        0.3.6
Release:        0%{?dist}
Summary:        ROS hector_gazebo package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/hector_gazebo
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-hector-gazebo-plugins
Requires:       ros-indigo-hector-gazebo-thermal-camera
Requires:       ros-indigo-hector-gazebo-worlds
BuildRequires:  ros-indigo-catkin

%description
hector_gazebo provides packages related to to simulation of robots using gazebo
(gazebo plugins, world files etc.)

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sat Mar 21 2015 Johannes Meyer <meyer@fsr.tu-darmstadt.de> - 0.3.6-0
- Autogenerated by Bloom

* Mon Feb 23 2015 Johannes Meyer <meyer@fsr.tu-darmstadt.de> - 0.3.5-0
- Autogenerated by Bloom

* Mon Sep 01 2014 Johannes Meyer <meyer@fsr.tu-darmstadt.de> - 0.3.4-0
- Autogenerated by Bloom


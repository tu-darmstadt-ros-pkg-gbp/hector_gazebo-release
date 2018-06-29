Name:           ros-melodic-hector-sensors-gazebo
Version:        0.5.1
Release:        0%{?dist}
Summary:        ROS hector_sensors_gazebo package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/hector_sensors_gazebo
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-gazebo-plugins
Requires:       ros-melodic-hector-gazebo-plugins
Requires:       ros-melodic-hector-sensors-description
BuildRequires:  ros-melodic-catkin

%description
hector_sensors_gazebo depends on the necessary plugins for using the sensors
from the hector_models repository.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Fri Jun 29 2018 Johannes Meyer <johannes@intermodalics.eu> - 0.5.1-0
- Autogenerated by Bloom


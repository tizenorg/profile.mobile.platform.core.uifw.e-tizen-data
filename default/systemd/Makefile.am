MAINTAINERCLEANFILES = Makefile.in

systemddir = @SYSTEMD_UNIT_DIR@

if WITH_SYSTEMD_FILE_X11
systemd_DATA = x11/enlightenment.service
endif

if WITH_SYSTEMD_FILE_WAYLAND
systemd_DATA = wayland/display-manager.path	\
			   wayland/display-manager.service \
			   wayland/display-manager-run.service
endif

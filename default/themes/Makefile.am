MAINTAINERCLEANFILES = Makefile.in

EDJE_CC = @EDJE_CC@
EDJE_FLAGS = -v	-id $(top_srcdir)/default/themes/img

filesdir = ${TZ_SYS_RO_SHARE}/enlightenment/data/themes
files_DATA = \
	launch.edj \
	default.edj \
	e-policy.edj

created="launch.edj default.edj"

EXTRA_DIST_LAUNCH = \
	launch.edc
EXTRA_DIST_DEFAULT = \
	default.edc \
	img/pointer_entry_bar.png \
	img/pointer_glow.png \
	img/pointer_mono.png \
	img/pointer.png \
	img/add_glow_small.png \
	img/led_dot_white.png \
	img/mini_box_glow.png

launch.edj: Makefile $(EXTRA_DIST_LAUNCH)
	$(EDJE_CC) $(EDJE_FLAGS) \
	$(top_srcdir)/default/themes/launch.edc \
	$(top_builddir)/default/themes/launch.edj

default.edj: Makefile $(EXTRA_DIST_DEFAULT)
	$(EDJE_CC) $(EDJE_FLAGS) \
	$(top_srcdir)/default/themes/default.edc \
	$(top_builddir)/default/themes/default.edj

clean-local:
	rm -f $(created)

MAINTAINERCLEANFILES = Makefile.in

EDJE_CC = @EDJE_CC@
EDJE_FLAGS = -v

filesdir = ${TZ_SYS_RO_SHARE}/enlightenment/data/themes
files_DATA = \
	launch.edj

EXTRA_DIST = \
	launch.edc

launch.edj: Makefile $(EXTRA_DIST)
	$(EDJE_CC) $(EDJE_FLAGS) \
	$(top_srcdir)/default/themes/launch.edc \
	$(top_builddir)/default/themes/launch.edj

clean-local:
	rm -f *.edj

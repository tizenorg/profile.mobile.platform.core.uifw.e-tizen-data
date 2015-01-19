MAINTAINERCLEANFILES = Makefile.in

EDJE_CC = @EDJE_CC@
EDJE_FLAGS = -v

filesdir = /usr/share/enlightenment/data/backgrounds
files_DATA = \
Black_Screen.edj

EXTRA_DIST = \
Black_Screen.edc

Black_Screen.edj: Makefile $(EXTRA_DIST)
	$(EDJE_CC) $(EDJE_FLAGS) \
	$(top_srcdir)/i386/backgrounds/Black_Screen.edc \
	$(top_builddir)/i386/backgrounds/Black_Screen.edj

clean-local:
	rm -f *.edj

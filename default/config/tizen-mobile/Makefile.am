MAINTAINERCLEANFILES = Makefile.in

EET_EET = @eet_eet@

EXTRA_DIST = \
             e_bindings.src \
             e_comp.src \
             e.src

filesdir = $(prefix)/data/config/tizen-mobile/
files_DATA = \
             e_bindings.cfg \
             e_comp.cfg \
             e.cfg

SUFFIXES = .cfg

.src.cfg:
	$(EET_EET) -e \
	$(top_builddir)/default/config/tizen-mobile/$@ config \
	$< 1

clean-local:
	rm -rf *.cfg *~

MAINTAINERCLEANFILES = Makefile.in
SUBDIRS = tizen-mobile

EET_EET = @eet_eet@

EXTRA_DIST = profile.src

filesdir = $(prefix)/data/config/

files_DATA = profile.cfg

SUFFIXES = .cfg

.src.cfg:
	$(EET_EET) -i \
	$(top_builddir)/x86_64/config/$@ config \
	$< 0

clean-local:
	rm -rf *.cfg *~

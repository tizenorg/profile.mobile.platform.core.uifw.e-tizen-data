AC_INIT(e-tizen-data, 0.1, gl77.lee@samsung.com)
AM_INIT_AUTOMAKE
AC_CONFIG_SRCDIR(configure.ac)

AC_PREFIX_DEFAULT(/usr/share/enlightenment)

PKG_CHECK_MODULES(EET, [eet])
AC_ARG_WITH(eet-eet,
[   --with-eet-eet=PATH             specify a specific path to eet utility],
[
   v=$withval;
   eet_eet=$v
   echo "   Enlightenment eet explicitly set to "$eet_eet;
],[
   eet_eet=$(pkg-config --variable=prefix eet)/bin/eet
])
AC_SUBST(eet_eet)

AC_CONFIG_FILES([
Makefile
arm/Makefile
arm/config/Makefile
arm/config/tizen-mobile/Makefile
aarch64/Makefile
aarch64/config/Makefile
aarch64/config/tizen-mobile/Makefile
i386/Makefile
i386/config/Makefile
i386/config/tizen-mobile/Makefile
emulator/Makefile
emulator/config/Makefile
emulator/config/tizen-mobile/Makefile
x86_64/Makefile
x86_64/config/Makefile
x86_64/config/tizen-mobile/Makefile
])
AC_OUTPUT

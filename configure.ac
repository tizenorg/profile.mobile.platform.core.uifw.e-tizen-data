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

PKG_CHECK_MODULES(EDJE, [edje])
AC_ARG_WITH(edje-cc,
  AC_HELP_STRING([--with-edje-cc=PATH], [specify a specific path to edje_cc]),
  [
    v=$withval;
    EDJE_CC=$v
  ],[
    EDJE_CC=$(pkg-config --variable=prefix edje)/bin/edje_cc
  ]
)
AC_SUBST(EDJE_CC)

## X11
AC_ARG_WITH([x11],
            AC_HELP_STRING([--with-x11], [use x11]),
            [WITH_X="1"
            AC_SUBST([WITH_X])])

## Wayland
AC_ARG_WITH([wayland],
            AC_HELP_STRING([--with-wayland], [use wayland]),
            [WITH_WAYLAND="1"
             AC_SUBST([WIHT_WAYLAND])])

### define MODULES
if test "$WITH_X"; then
 ENABLED_MODULES='group "modules" list {
    group "E_Config_Module" struct {
      value "name" string: "e-mod-tizen-wm-policy";
      value "enabled" uchar: 1;
      value "delayed" uchar: 0;
      value "priority" int: 0;
    }
    group "E_Config_Module" struct {
      value "name" string: "e-mod-tizen-keyrouter";
      value "enabled" uchar: 1;
      value "delayed" uchar: 0;
      value "priority" int: 0;
    }
    group "E_Config_Module" struct {
      value "name" string: "e-mod-tizen-effect";
      value "enabled" uchar: 1;
      value "delayed" uchar: 0;
      value "priority" int: 0;
    }
    group "E_Config_Module" struct {
      value "name" string: "e-mod-tizen-devicemgr";
      value "enabled" uchar: 1;
      value "delayed" uchar: 0;
      value "priority" int: 0;
    }
  }'
 BAD_MODULES='group "bad_modules" list {
    value "module" string: "e-mod-tizen-wm-policy";
    value "module" string: "e-mod-tizen-keyrouter";
    value "module" string: "e-mod-tizen-effect";
    value "module" string: "e-mod-tizen-devicemgr";
  }'
 FIRST_DRAW_DELAY=2.5
elif test "$WITH_WAYLAND"; then
 ENABLED_MODULES='group "modules" list {
    group "E_Config_Module" struct {
      value "name" string: "wl_drm";
      value "enabled" uchar: 1;
      value "delayed" uchar: 0;
      value "priority" int: 0;
    }
    group "E_Config_Module" struct {
      value "name" string: "wl_desktop_shell";
      value "enabled" uchar: 1;
      value "delayed" uchar: 0;
      value "priority" int: 0;
    }
    group "E_Config_Module" struct {
      value "name" string: "policy_mobile";
      value "enabled" uchar: 1;
      value "delayed" uchar: 0;
      value "priority" int: 0;
    }
  }'
 BAD_MODULES=''
 FIRST_DRAW_DELAY=0.1499999999999999944488849
fi
AC_SUBST([ENABLED_MODULES])
AM_SUBST_NOTMAKE([ENABLED_MODULES])
AC_SUBST([BAD_MODULES])
AM_SUBST_NOTMAKE([BAD_MODULES])
AC_SUBST([FIRST_DRAW_DELAY])
AM_SUBST_NOTMAKE([FIRST_DRAW_DELAY])
### Done MODULES

### composite engine
AC_ARG_WITH(engine,
            AC_HELP_STRING([--with-engine=sw|gl], [composite engine to be used]),
            [if test "x$withval" = "xgl"; then
               COMP_ENGINE=2
             elif test "x$withval" = "xsw"; then
               COMP_ENGINE=1
             else
               COMP_ENGINE=0
             fi
            ],
            [COMP_ENGINE=0])
AC_SUBST([COMP_ENGINE])
### Done COMP_ENGINE

AC_CONFIG_FILES([
default/config/tizen-mobile/e.src
default/config/tizen-mobile/e_comp.src
default/config/tizen-mobile/e_bindings.src
Makefile
default/Makefile
default/backgrounds/Makefile
default/config/Makefile
default/config/tizen-mobile/Makefile
])
AC_OUTPUT([
])


if [ "$USER" == "root" ]; then
	export XDG_RUNTIME_DIR=/run
else
	export XDG_RUNTIME_DIR=/run/user/$UID
        export TIZEN_WAYLAND_SHM_DIR=/run/.efl
fi

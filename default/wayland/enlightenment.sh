if [ "$USER" == "root" ]; then
	export XDG_RUNTIME_DIR=/run
else
	export XDG_RUNTIME_DIR=/run/user/$UID
        export TIZEN_APP_SHARE_DIR=/run/.efl
fi

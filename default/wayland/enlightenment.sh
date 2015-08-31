if [ "$USER" == "root" ]; then
	export XDG_RUNTIME_DIR=/run
else
	export XDG_RUNTIME_DIR=/run/user/$UID
fi

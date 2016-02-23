#!/bin/sh

TIZEN_PROFILE="mobile"
KEYMAP_FILE_PATH="/usr/share/X11/xkb/tizen_key_layout.txt"
NUM_KEYCODE=0
MAX_KEYCODE=0
KEYROUTER_CONFIG_FILE_PATH="default/config/tizen-${TIZEN_PROFILE}/module.keyrouter.src"
KEYROUTER_TEMP_FILE_PATH="default/config/tizen-${TIZEN_PROFILE}/module.keyrouter.src.temp"
WS="   "
KEYGAP=8

if [ -e ${KEYMAP_FILE_PATH} ]
then
	echo "${TIZEN_PROFILE} have a key layout file: ${KEYMAP_FILE_PATH}"
else
	echo "${TIZEN_PROFILE} doesn't have a key layout file: ${KEYMAP_FILE_PATH}"
	exit
fi

cat ${KEYROUTER_CONFIG_FILE_PATH} | sed '$d' > ${KEYROUTER_TEMP_FILE_PATH}

echo "$WS group \"KeyList\" list {" >> ${KEYROUTER_TEMP_FILE_PATH}

while read KEYNAME KEYCODE KEYBOARD_OPT
do
	VAL_KEYCODE=$(echo $KEYCODE | awk '{print $1}')
	NUM_KEYCODE=$(echo $NUM_KEYCODE 1 | awk '{print $1 + $2}')
	WINSYS_KEYCODE=$(echo $VAL_KEYCODE $KEYGAP | awk '{print $1 + $2}')
	NO_PRIVCHECK=0

	[[ $KEYBOARD_OPT == *"no_priv"* ]] && NO_PRIVCHECK=1

	if [ "$MAX_KEYCODE" -lt "$WINSYS_KEYCODE" ]
	then
		MAX_KEYCODE=$WINSYS_KEYCODE
	fi
	echo "$WS $WS group \"E_Keyrouter_Config_Key\" struct {" >> $KEYROUTER_TEMP_FILE_PATH
	echo "$WS $WS $WS value "name" string: \"$KEYNAME\";" >> $KEYROUTER_TEMP_FILE_PATH
	echo "$WS $WS $WS value "keycode" int: $WINSYS_KEYCODE;" >> $KEYROUTER_TEMP_FILE_PATH
	echo "$WS $WS $WS value "no_privcheck" int: $NO_PRIVCHECK;" >> $KEYROUTER_TEMP_FILE_PATH
	echo "$WS $WS }" >> $KEYROUTER_TEMP_FILE_PATH
done < ${KEYMAP_FILE_PATH}

echo "$WS }" >> $KEYROUTER_TEMP_FILE_PATH
echo "$WS value \"num_keycode\" int: $NUM_KEYCODE;" >> $KEYROUTER_TEMP_FILE_PATH
echo "$WS value \"max_keycode\" int: $MAX_KEYCODE;" >> $KEYROUTER_TEMP_FILE_PATH
echo "}" >> $KEYROUTER_TEMP_FILE_PATH

mv $KEYROUTER_TEMP_FILE_PATH $KEYROUTER_CONFIG_FILE_PATH

#!/bin/sh

if [ "$TZ_SYS_RO_SHARE" = "" ]; then
	TZ_SYS_RO_SHARE="/usr/share"
fi

TIZEN_PROFILE="mobile"
KEYMAP_FILE_PATH="${TZ_SYS_RO_SHARE}/X11/xkb/tizen_key_layout.txt"
NUM_KEYCODE=0
MAX_KEYCODE=0
KEYROUTER_CONFIG_FILE_PATH="default/config/tizen-${TIZEN_PROFILE}/module.keyrouter.src"
KEYROUTER_TEMP_FILE_PATH="default/config/tizen-${TIZEN_PROFILE}/module.keyrouter.src.temp"
GESTURE_CONFIG_FILE_PATH="default/config/tizen-${TIZEN_PROFILE}/module.gesture.src"
GESTURE_TEMP_FILE_PATH="default/config/tizen-${TIZEN_PROFILE}/module.gesture.src.temp"
WS="   "
KEYGAP=8

GESTURE_BACK_KEY_OPTION=0
GESTURE_COMBINE_KEY_OPTION=0
BACK_KEY_CODE=0
POWER_KEY_CODE=0

if [ -e ${KEYMAP_FILE_PATH} ]
then
	echo "${TIZEN_PROFILE} have a key layout file: ${KEYMAP_FILE_PATH}"
else
	echo "${TIZEN_PROFILE} doesn't have a key layout file: ${KEYMAP_FILE_PATH}"
	exit
fi

if [ -e ${KEYROUTER_CONFIG_FILE_PATH} ]
then
	echo "Generate a keyrouter config file"
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

		[[ $KEYNAME == "XF86Back" ]] && BACK_KEY_CODE=$VAL_KEYCODE
		[[ $KEYNAME == "XF86PowerOff" ]] && POWER_KEY_CODE=$VAL_KEYCODE

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
else
	echo "Just check keymap file"
	while read KEYNAME KEYCODE KEYBOARD_OPT
	do
		VAL_KEYCODE=$(echo $KEYCODE | awk '{print $1}')

		[[ $KEYNAME == "XF86Back" ]] && BACK_KEY_CODE=$VAL_KEYCODE
		[[ $KEYNAME == "XF86PowerOff" ]] && POWER_KEY_CODE=$VAL_KEYCODE
	done < ${KEYMAP_FILE_PATH}
fi

if [ -e ${GESTURE_CONFIG_FILE_PATH} ]
then
echo "Check a gesture config file"
while read VTEMP VALUE_NAME VALUE_TYPE VALUE
do
	if [ "$BACK_KEY_CODE" != "0" ]
	then
	[[ $VALUE_NAME == *"back_key"* ]] && GESTURE_BACK_KEY_OPTION=1
	fi
	if [ "$POWER_KEY_CODE" != "0" ]
	then
	[[ $VALUE_NAME == *"combine_key"* ]] && GESTURE_COMBINE_KEY_OPTION=1
	fi

	if [ $GESTURE_BACK_KEY_OPTION == 1 ]
	then
		BACK_KEY_CODE=$(echo $BACK_KEY_CODE $KEYGAP | awk '{print $1 + $2}')
		VALUE=$BACK_KEY_CODE";"
		GESTURE_BACK_KEY_OPTION=0
	fi
	if [ $GESTURE_COMBINE_KEY_OPTION == 1 ]
	then
		POWER_KEY_CODE=$(echo $POWER_KEY_CODE $KEYGAP | awk '{print $1 + $2}')
		VALUE=$POWER_KEY_CODE";"
		GESTURE_COMBINE_KEY_OPTION=0
	fi

	echo $VTEMP $VALUE_NAME $VALUE_TYPE $VALUE >> $GESTURE_TEMP_FILE_PATH
done < ${GESTURE_CONFIG_FILE_PATH}

mv $GESTURE_TEMP_FILE_PATH $GESTURE_CONFIG_FILE_PATH
fi

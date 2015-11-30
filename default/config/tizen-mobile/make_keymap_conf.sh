#!/bin/sh

KEYMAP_FILE_PATH="/usr/share/X11/xkb/tizen_key_layout.txt"
NUM_KEYCODE=0
MAX_KEYCODE=0
KEYROUTER_CONFIG_FILE_PATH="default/config/tizen-mobile/module.keyrouter.src"
KEYROUTER_TEMP_FILE_PATH="default/config/tizen-mobile/module.keyrouter.src.temp"
WS="   "
TIZEN_PROFILE="mobile"

if [ -e ${KEYMAP_FILE_PATH} ]
then
	echo "${TIZEN_PROFILE} have a key layout file: ${KEYMAP_FILE_PATH}"
else
	echo "${TIZEN_PROFILE} doesn't have a key layout file: ${KEYMAP_FILE_PATH}"
	exit
fi

pwd

cat ${KEYROUTER_CONFIG_FILE_PATH} | sed '$d' > ${KEYROUTER_TEMP_FILE_PATH}

echo "$WS group \"KeyList\" list {" >> ${KEYROUTER_TEMP_FILE_PATH}

while read KEYNAME KEYCODE
do
	VAL_KEYCODE=$(echo $KEYCODE | awk '{print $1}')
	if [ "$MAX_KEYCODE" -lt "$VAL_KEYCODE" ]
	then
		MAX_KEYCODE=$KEYCODE
	fi
	NUM_KEYCODE=$(echo $NUM_KEYCODE 1 | awk '{print $1 + $2}')
	echo "$WS $WS group \"E_Keyrouter_Config_Key\" struct {" >> $KEYROUTER_TEMP_FILE_PATH
	echo "$WS $WS $WS value "name" string: \"$KEYNAME\";" >> $KEYROUTER_TEMP_FILE_PATH
	echo "$WS $WS $WS value "keycode" int: $KEYCODE;" >> $KEYROUTER_TEMP_FILE_PATH
	echo "$WS $WS }" >> $KEYROUTER_TEMP_FILE_PATH
done < ${KEYMAP_FILE_PATH}

echo "$WS }" >> $KEYROUTER_TEMP_FILE_PATH
echo "$WS value \"num_keycode\" int: $NUM_KEYCODE;" >> $KEYROUTER_TEMP_FILE_PATH
echo "$WS value \"max_keycode\" int: $MAX_KEYCODE;" >> $KEYROUTER_TEMP_FILE_PATH
echo "}" >> $KEYROUTER_TEMP_FILE_PATH

mv $KEYROUTER_TEMP_FILE_PATH $KEYROUTER_CONFIG_FILE_PATH

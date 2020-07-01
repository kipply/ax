function add-ax() {
  local _BUFFER="$BUFFER";
  [[ $_BUFFER = ax* ]] || [[ $_BUFFER = "" ]] || _BUFFER="ax $BUFFER";
  echo ''
  ZLE_QAL_LAST="$BUFFER"
  eval $_BUFFER
  BUFFER=""
  ZLE_QAL_STATUS=$?
  zle reset-prompt
}
zle -N accept-line add-ax

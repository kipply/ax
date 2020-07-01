add-ax() {
  local _BUFFER="$BUFFER";
  [[ $_BUFFER = ax* ]] || [[ $_BUFFER = "" ]] || _BUFFER="ax $BUFFER";
  echo ''
  eval $_BUFFER
  BUFFER=""
  zle reset-prompt
}
zle -N accept-line add-ax

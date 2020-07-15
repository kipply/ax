ax_ignore_types=("vi ssh man")
ax_min_duration=1

ax_pre() {
  ax start
  ax_last_exec=$(date +%s)
  ax_cmd=$1
}

ax_post() {
	if [ -z "$ax_last_exec" ]
	then
    ax_last_exec=$(date +%s)
  fi

  local duration=$(($(date +%s) - $ax_last_exec))
  local cmd_type=$(echo $ax_cmd | awk '{print $1;}')

  if [[ "$duration" -gt "$ax_min_duration" && ! " ${ax_ignore_types[@]} " =~ " ${cmd_type} " ]]; then
    echo "hi"
    ax end
  fi
}

add-zsh-hook preexec ax_pre
add-zsh-hook precmd ax_post

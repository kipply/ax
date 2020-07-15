# ax
Pause and play music when your processes start or end

Installation until I get `pip`

1. clone it
2. `python3 setup.py install` 
3. `ax auth` (enter details, mildly annoying) 
4. Add `source path/to/ax.plugin.zsh` to your zshrc


Configure min duration with `ax_min_duration` and set ignored cmds with `ax_ignore_types`


Behaviour is: 
- if no current playback (defined by spotify, basically if spotify doesn't have an active device / playlist known) then do nothing
- on executing cmd, start music (if applicable)
- on ending cmd, pause music IF the duration requirement is fulfilled

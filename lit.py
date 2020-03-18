from literal import literal; print((lambda x: x if x == 'MUTE' else literal(int(x))+'%')('$VOLUME_LEV'))

from libqtile import widget

def left_arrow(bg_color, fg_color):
    return widget.TextBox(text='\uE0B2',padding=0,fontsize=36,background=bg_color,foreground=fg_color)


def left_half_circle(fg_color, bg_color):
    return widget.TextBox(text='\uE0B6',fontsize=36,foreground=fg_color,background=bg_color,padding=-4)



def right_half_circle(fg_color, bg_color):
    return widget.TextBox(text='\uE0B4',fontsize=36,foreground=fg_color,background=bg_color,padding=-1)

# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal


from libqtile import hook

from configs.myColors import myColor


import subprocess
import random
import string

def texto_aleatorio():
    caracteres = string.ascii_letters + string.digits  # Incluye letras mayúsculas, minúsculas y dígitos
    texto = ''.join(random.choice(caracteres) for _ in range(4))
    return texto



BAR_COLORS=[
    ["#9837A8","#9837A8"],
    ["#8754ff","#8754ff"],
    ["#350859","#350859"], # Background 
    ["#54dbff","#54dbff"], # Background 
    ["#FB17F4","#FB17F4"], # Select 
    ["#6f04f7","#6f04f7"],  # white 
    ["#52238e","#52238e"]  # inactive 

]


subprocess.call(["feh", "--bg-fill", "/home/perico/Imágenes/1331544.png"])

# En la sección de aplicaciones predeterminadas
# Puedes agregar o modificar la línea que configura el navegador web
# Asegúrate de tener una entrada similar a esta:

# Define el navegador web predeterminado
browser = "firefox"




mod = "mod4"
terminal = guess_terminal()

keys = [

    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "u", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn("kitty"), desc="Launch terminal"),
    Key([mod], "m", lazy.spawn("rofi -show run"), desc="Launch terminal"),
    Key([mod], "b", lazy.spawn("firefox"), desc="Launch terminal"),
    Key([mod], "n", lazy.spawn("kitty ranger"), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "f", lazy.window.toggle_fullscreen()),
]

groups = [
    Group("1", label="󰋜 Home"),
    Group("2", label="󰈹 Bwsr"),
    Group("3", label="󰨞 Code"),
    Group("4", label=" term"),
    Group("5", label="󰛊 Coffe"),
    Group("6", label="󰗃 YouT"),
    Group("7", label="󰙯 Disc"),
]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ],

    )



layouts = [
    layout.Columns(border_focus=BAR_COLORS[4],border_normal=BAR_COLORS[2],  border_width=4,margin=8),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="FiraCode Nerd Font",
    fontsize=18,
    padding=10,
)

def getVolume():
    try:
        comando="pactl list sinks | grep -i '%' | awk -F'/' 'NR==1 {print $2; exit}'"
        # Ejecuta el comando de Bash y captura la salida estándar
        resultado = subprocess.check_output(comando, shell=True, text=True)
        texto = resultado.strip() + " 󰕾"
        return texto
    except subprocess.CalledProcessError as e:
        # En caso de que el comando falle, puedes manejar la excepción aquí
        print(f"Error al ejecutar el comando: {e}")
        return None

def getWifi():
    try:
        comando=" nmcli device wifi | grep '*' | awk -F'Infra' '{print $2}' | awk '{print $2, $4}'"
        # Ejecuta el comando de Bash y captura la salida estándar
        resultado = subprocess.check_output(comando, shell=True, text=True)
        texto = resultado.strip()
        if(texto==""):
            return "󰢾 "
        numeros_separados = texto.split()



        numero2= int(numeros_separados[1] )
        if numero2>75:
            return  "󰢾 "+ str(numero2)
        elif numero2 > 40:
            return "󰢽 "+ str(numero2)
        else:
            return "󰢾 "+ str(numero2)

        return texto
    except subprocess.CalledProcessError as e:
        # En caso de que el comando falle, puedes manejar la excepción aquí
        print(f"Error al ejecutar el comando: {e}")
        return None



extension_defaults = widget_defaults.copy()

from configs.bar import left_arrow, left_half_circle, right_half_circle


screens = [
    Screen(

        top=bar.Bar(
            [
                left_half_circle(myColor(2),myColor(0)),
                widget.GroupBox(
                    highlight_method='text',
                    active=myColor(9),
                    inactive=myColor(1),
                    this_current_screen_border =myColor(6),
                    background=myColor(2),
                ),
                right_half_circle(myColor(2),myColor(0)),
                widget.Spacer(),
                left_arrow("#444444.1",myColor(6)),
                widget.TextBox(
                    text="Term", 
                    mouse_callbacks={'Button1': lazy.spawn("kitty") },
                    background=myColor(6),
                    foreground=myColor(1),
                ),
                left_arrow(myColor(6),myColor(2)),
                widget.GenPollText(
                    update_interval=1,  # Intervalo de actualización en segundos
                    func=lambda: getVolume(),
                    mouse_callbacks={'Button1': lazy.spawn("pavucontrol") },
                    background=myColor(2),
                    foreground=myColor(9),
                ),
                left_arrow(myColor(2),myColor(6)),
                widget.GenPollText(
                    update_interval=15,  # Intervalo de actualización en segundos
                    func=lambda: getWifi(),
                    mouse_callbacks={'Button1': lazy.spawn("kitty nmtui") },
                    background=myColor(6),
                    foreground=myColor(1),
                ),
                left_arrow(myColor(6),myColor(2)),
                widget.TextBox(
                    text="", 
                    mouse_callbacks={'Button1': lazy.spawn("kitty") },
                    background=myColor(2),
                    foreground=myColor(5),
                ),
                widget.TextBox(
                    text="󰤁", 
                    mouse_callbacks={'Button1': lazy.spawn("kitty") },
                    background=myColor(2),
                    foreground=myColor(4),
                ),
                widget.TextBox(
                    text="󰐥", 
                    mouse_callbacks={'Button1': lazy.spawn("kitty askshutdown.sh") },
                    background=myColor(2),
                    foreground=myColor(3),
                ),
                right_half_circle(myColor(2),myColor(0)),
            ],
            40,
            margin=10,
            background="#ffffff.0",
            pacity=1

        ),
    ),
]



# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

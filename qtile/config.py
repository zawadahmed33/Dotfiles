#########################
### IMPORT STATEMENTS ###
#########################

import os
import subprocess
from libqtile import hook
from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

#################
### VARIABLES ###
#################

mod = "mod4"
terminal = "kitty"

####################
### KEYBINDINGS  ###
####################

keys = [
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "control"], "Left", lazy.layout.shrink(), desc="Shrink window"),
    Key([mod, "control"], "Right", lazy.layout.grow(), desc="Grow window to"),
    Key([mod], "n", lazy.layout.reset(), desc="Reset all window sizes"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(),desc="Toggle fullscreen on the focused window"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod], "c", lazy.window.center(), desc="Center Floating Window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "r", lazy.spawn("rofi -show drun"), desc="Launch run launcher"),
    Key([mod], "F1", lazy.spawn("chromium"), desc="Launch browser"),
    Key([mod], "F2", lazy.spawn("pcmanfm"), desc="Launch file manager"),
    Key([mod], "F3", lazy.spawn("mousepad"), desc="Launch text editor"),
    Key([mod], "F4", lazy.spawn("kitty -e htop"), desc="Launch sytem monitor"),
    Key([mod], "F5", lazy.spawn("gthumb"), desc="Launch image viewer"),
    Key([mod], "F6", lazy.spawn("vlc"), desc="Launch video player"),
    Key([mod], "F7", lazy.spawn("spotify-launcher"), desc="Launch music player"),
    Key([mod], "F8", lazy.spawn("libreoffice"), desc="Launch office suite"),
    Key([mod], "F9", lazy.spawn("flameshot"), desc="Launch screenshot tool"),
    Key([mod], "F10", lazy.spawn("pavucontrol"), desc="Launch volume control"),
    Key([mod], "F11", lazy.spawn("nm-connection-editor"), desc="Launch network manager"),
    Key([mod], "F12", lazy.spawn("i3lock"), desc="Lock screen"),
]

for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )


##############
### GROUPS ###
##############

groups = [Group(f"{i+1}", label="") for i in range(9)] 

for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc=f"Switch to group {i.name}",
            ),
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc=f"Switch to & move focused window to group {i.name}",
            ),
        ]
)


##############
### COLORS ###
##############

colors = [
    "#191919",  # Background, 0
    "#bbbbbb",  # Foreground, 1
    "#3d3839",  # Bright Black, 2
    "#f77890",  # Red, 3
    "#819b69",  # Green, 4
    "#b77e64",  # Yellow, 5
    "#6099c0",  # Blue, 6
    "#b279a7",  # Magenta, 7
    "#66a5ad",  # Cyan, 8
]

###############
### LAYOUTS ###
###############

layout_theme = {
    "margin": 4, 
    "border_focus": colors[6], 
    "border_normal": colors[2]
}

layouts = [
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
]

#########################
### SCREENS & WIDGETS ###
#########################

widget_defaults = dict(
    font="JetBrains Mono SemiBold",
    fontsize=14,
    padding=0,
    margin=0,
    background=colors[0],
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Spacer(
                    length=16
                ),
                widget.TextBox(
                    text="",
                    mouse_callbacks={"Button1": lazy.spawn("rofi -show drun")},
                    foreground=colors[6]
                ),
                widget.Spacer(
                    length=16
                ),
                widget.GroupBox(
                    highlight_method="text",
                    urgent_alert_method="text",
                    spacing=8,
                    margin_x=0,
                    margin_y=4,
                    active=colors[1],
                    inactive=colors[2],
                    this_current_screen_border=colors[4],
                    urgent_text=colors[3]
                ),
                widget.Spacer(
                    length=16
                ),
                widget.Mpris2(
                    name="spotify",
                    objname="org.mpris.MediaPlayer2.spotify",
                    playing_text=" {track}",
                    paused_text=" {track}",
                    foreground=colors[1],
                ),
                widget.Spacer(), 
                widget.Systray(
                    icon_size=20,
                    padding=8
                ),
                widget.Spacer(
                    length=16
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[7]
                ),
                widget.Spacer(
                    length=8
                ),
                widget.DF(
                    visible_on_warn=False,
                    format="{uf} {m}",
                    foreground=colors[1]
                ),
                widget.Spacer(
                    length=16
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[8]
                ),
                widget.Spacer(
                    length=8
                ),
                widget.Load(
                    update_interval=15,
                    format="{load:.2f}",
                    foreground=colors[1]
                ),
                widget.Spacer(
                    length=16
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[7]
                ),
                widget.Spacer(
                    length=8
                ),
                widget.Memory(
                    update_interval=15,
                    format="{NotAvailable:.2f} {mm}",
                    measure_mem="G",
                    foreground=colors[1]
                ),
                widget.Spacer(
                    length=16
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[8]
                ),
                widget.Spacer(
                    length=8
                ),
                widget.Net(
                    update_interval=15,
                    format="{down:.0f} {down_suffix}",
                    foreground=colors[1]
                ),
                widget.Spacer(
                    length=16
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[7]
                ),
                widget.Spacer(
                    length=8
                ),
                widget.Net(
                    update_interval=15,
                    format="{up:.0f} {up_suffix}",
                    foreground=colors[1]
                ),
                widget.Spacer(
                    length=16
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[8]
                ),
                widget.Spacer(
                    length=8
                ),
                widget.Volume(
                    unmute_format="{volume}",
                    mute_format="0",
                    foreground=colors[1]
                ),
                widget.Spacer(
                    length=16
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[7]
                ),
                widget.Spacer(
                    length=8
                ),
                widget.Wttr(
                    format="%t, %C",
                    foreground=colors[1]
                ),
                widget.Spacer(
                    length=16
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[8]
                ),
                widget.Spacer(
                    length=8
                ),
                widget.Clock(
                    format="%d-%m-%y, %H:%M", 
                    foreground=colors[1]
                ),
                widget.Spacer(
                    length=16
                ),
                widget.TextBox(
                    text="",
                    mouse_callbacks={"Button3": lazy.shutdown()},
                    foreground=colors[3]
                ),
                widget.Spacer(
                    length=16
                ),
            ],
            36,
            margin=[4,4,0,4]
        ),
    ),
]

#####################
### DEFAULT STUFF ###
#####################

mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),
        Match(wm_class="makebranch"),
        Match(wm_class="maketag"),
        Match(wm_class="ssh-askpass"),
        Match(title="branchdialog"),
        Match(title="pinentry"),
    ],
    border_width=0,
)

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True

wl_input_rules = None

wl_xcursor_theme = None
wl_xcursor_size = 24

wmname = "LG3D"

####################
### STARTUP HOOK ###
####################

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.call(home)

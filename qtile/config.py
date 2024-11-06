### IMPORT STATEMENTS ###


import os
import subprocess
from libqtile import hook
from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal


### VARIABLES ###


mod = "mod4"
terminal = "kitty"


### KEYBINDS ###


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

# Add key bindings to switch VTs in Wayland.
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )


### GROUPS ###


# Naming of the groups
groups = [Group(f"{i+1}", label="") for i in range(8)] 

# Switching between groups
for i in groups:
    keys.extend(
        [
            # mod + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc=f"Switch to group {i.name}",
            ),
            # mod + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc=f"Switch to & move focused window to group {i.name}",
            ),
        ]
    )


### COLORS ###


colors = [
    "#151718",  # dull_black, 0
    "#1d1f21",  # black, 1
    "#373b41",  # bright_black, 2
    "#707880",  # dull_white, 3
    "#c5c8c6",  # white, 4
    "#eaeaea",  # bright_white, 5
    "#cc6666",  # red, 6
    "#b5bd68",  # green, 7
    "#f0c674",  # yellow, 8
    "#81a2be",  # blue, 9
    "#b294bb",  # magenta, 10
    "#8abeb7",  # cyan, 11
]


### LAYOUTS ###


# Theme for layouts
layout_theme = {
        "margin": 4, 
        "border_focus": colors[7], 
        "border_normal": colors[2]
}

# Added layouts
layouts = [
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.Floating(**layout_theme),
]

# Theme for widgets
widget_defaults = dict(
    font="Monaspace Neon SemiBold, Font Awesome 6 Free",
    fontsize=14,
    padding=12,
    background=colors[1],
    foreground=colors[4],
)

# Theme for extensions
extension_defaults = widget_defaults.copy()


### SCREENS ###


# Screen objects
screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    highlight_method="text",
                    urgent_alert_method="text",
                    active = colors[9],
                    inactive = colors[4],
                    this_current_screen_border = colors[7]
                ),
                widget.Systray(
                    icon_size = 20
                ),
                widget.Spacer(),
                widget.CurrentLayout(
                    fmt=" {}", foreground=colors[10]
                ),
                widget.CPU(
                    update_interval=5,
                    format=" CPU: {load_percent}",
                    foreground=colors[11],
                ),
                widget.Memory(
                    update_interval=5,
                    format=" Memory: {MemUsed:.2f} GiB",
                    measure_mem="G",
                    foreground=colors[10],
                ),
                widget.Volume(
                    unmute_format=" Volume: {volume}",
                    mute_format=" Volume: 0",
                    foreground=colors[11],
                ),
                widget.Wlan(
                    format=" Network: {essid}", foreground=colors[10]
                ),
                widget.Clock(
                    format=" %a, %d %b, %H:%M", foreground=colors[11]
                ),
            ],
            36,
            margin=[4, 4, 0, 4],
        ),
    ),
]


### DEFAULT STUFF ###


# Drag floating layouts.
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
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
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
    ],
    border_width=0,  # remove border from flaoting windows
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 24

# Name of the window manager
wmname = "Qtile"

### STARTUP HOOK ###

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.call(home)

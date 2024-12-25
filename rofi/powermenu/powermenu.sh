#! /bin/sh

chosen=$(printf "\n\n\n" | rofi -dmenu -i -theme-str '@import "~/.config/rofi/powermenu/powermenu.rasi"')

urgent=""

case "$chosen" in
	"") i3lock ;;
	"") qtile cmd-obj -o cmd -f shutdown ;;
	"") reboot ;;
	"") shutdown now ;;
	*) exit 1 ;;
esac

if [[ $chosen == "" ]]; then
    urgent="-a 1"

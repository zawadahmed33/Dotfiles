#! /bin/sh

chosen=$(printf "\n\n\n" | rofi -dmenu -i -theme-str '@import "~/.config/rofi/quicklinks.rasi"')

case "$chosen" in
	"") chromium https://www.google.com ;;
	"") chromium https://www.youtube.com ;;
	"") chromium https://www.reddit.com ;;
	"") chromium https://www.github.com ;;
	*) exit 1 ;;
esac

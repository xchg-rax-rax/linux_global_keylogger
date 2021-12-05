# Device Level Linux Keylogger

This is a simple low level key logger written in C that is capable of capturing every keystroke typed on a computer both inside of an X windows environment and on any tty sessions running on the target.
It gets keystroke information by reading events directly from the device file(s) for the systems keyboard(s) (found in the /dev/input directory) and as such requires root privileges to run.
It has VERY extensive event decoding and will produce useful output for every key on even quite unusual keyboard.

## Compilation

## Usage

## Disclaimer

I made this as a fun project for my own amusement and as a means of learning more about how input devices work on linux.
I did not make this as a tool for people with malicious intent to use in order to spy on other, steal from them or otherwise cause harm.
Never use this on a system you don't own or have permission to modify.
I am not responsible for your actions.

#!/bin/bash

# 실행 명령어 기록 삭제
export HISTFILE=~/.bash_history
rm -f ~/.bash_history
unset HISTFILE
history -c

# SSH 접속 로그 삭제
sudo sh -c 'cat /dev/null > /var/log/auth.log'   # Ubuntu/Debian 계열
sudo sh -c 'cat /dev/null > /var/log/secure'     # CentOS/RHEL 계열

# WTMP, UTMP, Lastlog 삭제 (로그인 기록 삭제)
sudo sh -c 'cat /dev/null > /var/log/wtmp'
sudo sh -c 'cat /dev/null > /var/log/btmp'
sudo sh -c 'cat /dev/null > /var/log/lastlog'

# syslog 및 messages 로그 삭제
sudo sh -c 'cat /dev/null > /var/log/syslog'
sudo sh -c 'cat /dev/null > /var/log/messages'

# Journald 로그 삭제
sudo journalctl --rotate
sudo journalctl --vacuum-time=1s

# SSH 접속 및 sudo 로그 삭제
sudo rm -f /var/log/auth.log /var/log/secure /var/log/wtmp /var/log/btmp /var/log/lastlog /var/log/syslog /var/log/messages /var/log/sudo.log
sudo touch /var/log/auth.log /var/log/secure /var/log/wtmp /var/log/btmp /var/log/lastlog /var/log/syslog /var/log/messages /var/log/sudo.log
sudo chmod 600 /var/log/auth.log /var/log/secure /var/log/wtmp /var/log/btmp /var/log/lastlog /var/log/syslog /var/log/messages /var/log/sudo.log

# Journald 로그 삭제
sudo journalctl --rotate
sudo journalctl --vacuum-time=1s
sudo rm -rf /var/log/journal/*
sudo systemctl restart systemd-journald

# 명령 실행 후 즉시 로그아웃
history -c && exit
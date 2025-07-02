#!/bin/bash

BASE_DIR="$HOME/Task6"
LOGFILE="$BASE_DIR/myupdater.log"
LOCKFILE="/tmp/myupdater.lock"
NETWORK_CHECKS=5
NETWORK_WAIT=20 


REPOS_DIR="$BASE_DIR/git_repos"
MIRRORS=(
  "git://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git"
  "git://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git"
)

mkdir -p "$REPOS_DIR"

log() {
  echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> "$LOGFILE"
}


if [ -e "$LOCKFILE" ]; then
  PID=$(cat "$LOCKFILE")
  if kill -0 "$PID" 2>/dev/null; then
    log "Scriptul rulează deja cu PID $PID. Ieșire."
    exit 1
  else
    log "Lockfile găsit, dar procesul $PID nu există. Ștergere lockfile."
    rm -f "$LOCKFILE"
  fi
fi

echo $$ > "$LOCKFILE"


for ((i=1; i<=NETWORK_CHECKS; i++)); do
  if ping -c1 8.8.8.8 &>/dev/null; then
    break
  else
    log "Fără conexiune la rețea. Încercare $i/$NETWORK_CHECKS."
    if [ "$i" -eq "$NETWORK_CHECKS" ]; then
      log "Nicio conexiune la rețea după $((NETWORK_CHECKS * NETWORK_WAIT)) secunde. Ieșire."
      rm -f "$LOCKFILE"
      exit 1
    fi
    sleep "$NETWORK_WAIT"
  fi
done


sudo apt update && sudo apt upgrade -y >> "$LOGFILE" 2>&1 &
APT_PID=$!


for repo in "${MIRRORS[@]}"; do
  reponame=$(basename "$repo" .git)
  if [ ! -d "$REPOS_DIR/$reponame" ]; then
    git clone "$repo" "$REPOS_DIR/$reponame" >> "$LOGFILE" 2>&1 &
  else
    (cd "$REPOS_DIR/$reponame" && git pull) >> "$LOGFILE" 2>&1 &
  fi
done

wait "$APT_PID"
wait

log "Update finalizat cu succes."

rm -f "$LOCKFILE"
exit 0

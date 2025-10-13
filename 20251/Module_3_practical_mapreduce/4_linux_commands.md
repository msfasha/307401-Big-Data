# LINUX & COMMAND LINE CRASH COURSE

## PART 1: What is Linux?

**Linux** is an open-source, Unix-like operating system that powers:

* Servers
* Desktops
* Embedded systems
* Android devices

It is known for stability, security, and flexibility.

Common distributions (distros):
Ubuntu, Debian, Fedora, Arch, CentOS, Kali, Mint.

---

## PART 2: The Command Line Interface (CLI)

The **command line** is a text-based interface for interacting with the system.
You type commands into a **terminal**, and the system executes them.

Common **shells**:

* bash (default on many systems)
* zsh
* fish

---

## PART 3: Linux Filesystem Structure

Linux uses a single-root hierarchy starting at `/`.

| Directory       | Purpose                                |
| --------------- | -------------------------------------- |
| `/`             | Root directory                         |
| `/home`         | User home directories                  |
| `/etc`          | System and service configuration files |
| `/var`          | Logs and variable data                 |
| `/usr`          | Applications and libraries             |
| `/bin`, `/sbin` | Essential system binaries              |
| `/tmp`          | Temporary files                        |
| `/dev`          | Device files                           |

---

## PART 4: Navigation and File Management

### Navigation

| Command | Example         | Description                                      |
| ------- | --------------- | ------------------------------------------------ |
| `pwd`   | `pwd`           | Print working directory                          |
| `ls`    | `ls -l`         | List files and directories                       |
| `cd`    | `cd /home/user` | Change directory                                 |
| `tree`  | `tree`          | Show directory structure (requires installation) |

### Files and Directories

| Command         | Example                  | Description                   |
| --------------- | ------------------------ | ----------------------------- |
| `mkdir`         | `mkdir myfolder`         | Create directory              |
| `rmdir`         | `rmdir myfolder`         | Remove empty directory        |
| `rm`            | `rm file.txt`            | Delete file                   |
| `rm -r`         | `rm -r folder`           | Delete folder recursively     |
| `cp`            | `cp file1.txt file2.txt` | Copy files                    |
| `mv`            | `mv old.txt new.txt`     | Move or rename file           |
| `touch`         | `touch file.txt`         | Create empty file             |
| `cat`           | `cat file.txt`           | Show file contents            |
| `less`          | `less file.txt`          | View file page by page        |
| `head` / `tail` | `head -n 10 file.txt`    | View beginning or end of file |

---

## PART 5: System and Process Management

| Command         | Example     | Description                                                       |
| --------------- | ----------- | ----------------------------------------------------------------- |
| `whoami`        |             | Show current user                                                 |
| `uname -a`      |             | Show system information                                           |
| `top`           |             | Show running processes                                            |
| `htop`          |             | Interactive process viewer (install with `sudo apt install htop`) |
| `ps aux`        |             | List all running processes                                        |
| `kill`          | `kill 1234` | Kill process by PID                                               |
| `df -h`         |             | Show disk usage                                                   |
| `du -sh folder` |             | Show folder size                                                  |
| `free -h`       |             | Show memory usage                                                 |
| `uptime`        |             | Show system uptime                                                |
| `history`       |             | Show command history                                              |

---

## PART 6: Permissions and Ownership

Each file and directory has permissions for **user**, **group**, and **others**.
Permissions: **r** (read), **w** (write), **x** (execute)

| Command | Example                 | Description              |
| ------- | ----------------------- | ------------------------ |
| `ls -l` |                         | Show permissions         |
| `chmod` | `chmod 755 script.sh`   | Change permissions       |
| `chown` | `chown user:group file` | Change owner and group   |
| `sudo`  | `sudo apt update`       | Run command as superuser |

---

## PART 7: Networking Commands

| Command         | Example                        | Description             |
| --------------- | ------------------------------ | ----------------------- |
| `ping`          | `ping google.com`              | Test connectivity       |
| `ip a`          |                                | Show network interfaces |
| `curl`          | `curl https://example.com`     | Fetch data from URL     |
| `wget`          | `wget file_url`                | Download file           |
| `ssh`           | `ssh user@host`                | Connect to remote host  |
| `scp`           | `scp file.txt user@host:/path` | Copy files securely     |
| `netstat -tuln` |                                | Show open ports         |

---

## PART 8: Package Management

### Debian/Ubuntu (APT)

```bash
sudo apt update
sudo apt install package
sudo apt remove package
sudo apt upgrade
```

### Fedora/RHEL (DNF)

```bash
sudo dnf install package
sudo dnf update
sudo dnf remove package
```

### Arch (pacman)

```bash
sudo pacman -S package
sudo pacman -R package
sudo pacman -Syu
```

---

## PART 9: Searching and Filtering

| Command  | Example                      | Description                         |
| -------- | ---------------------------- | ----------------------------------- |
| `grep`   | `grep "error" logfile.log`   | Search text in file                 |
| `find`   | `find / -name file.txt`      | Find files                          |
| `locate` | `locate config.json`         | Search file database                |
| `wc`     | `wc -l file.txt`             | Count lines, words, characters      |
| `sort`   | `sort data.txt`              | Sort text                           |
| `uniq`   | `uniq file.txt`              | Remove duplicate lines              |
| `cut`    | `cut -d ":" -f1 /etc/passwd` | Extract specific fields             |
| `awk`    | `awk '{print $1}' file.txt`  | Pattern scanning and processing     |
| `sed`    | `sed 's/old/new/g' file.txt` | Stream editor for text substitution |

---

## PART 10: Shell Shortcuts and Tricks

| Shortcut   | Description                                       |                                         |               |
| ---------- | ------------------------------------------------- | --------------------------------------- | ------------- |
| `Tab`      | Autocomplete command or filename                  |                                         |               |
| `Ctrl + C` | Cancel running command                            |                                         |               |
| `Ctrl + L` | Clear terminal screen                             |                                         |               |
| `Ctrl + R` | Search through command history                    |                                         |               |
| `!!`       | Repeat last command                               |                                         |               |
| `>`        | Redirect output to file (`ls > files.txt`)        |                                         |               |
| `>>`       | Append output to file (`echo "text" >> file.txt`) |                                         |               |
| `          | `                                                 | Pipe output to another command (`ps aux | grep python`) |

---

## PART 11: File Compression and Archiving

| Command    | Example                        | Description          |
| ---------- | ------------------------------ | -------------------- |
| `tar -cvf` | `tar -cvf archive.tar folder/` | Create tar archive   |
| `tar -xvf` | `tar -xvf archive.tar`         | Extract tar archive  |
| `gzip`     | `gzip file.txt`                | Compress file        |
| `gunzip`   | `gunzip file.txt.gz`           | Decompress gzip file |
| `zip`      | `zip archive.zip file1 file2`  | Create zip archive   |
| `unzip`    | `unzip archive.zip`            | Extract zip archive  |

---

## PART 12: Daily Useful Commands

| Command              | Description                   |
| -------------------- | ----------------------------- |
| `man command`        | Display manual for a command  |
| `alias ll='ls -lah'` | Create shortcut for a command |
| `date`               | Show date and time            |
| `cal`                | Display calendar              |
| `echo $PATH`         | Show environment variable     |
| `nano file.txt`      | Edit file with nano           |
| `vim file.txt`       | Edit file with Vim            |
| `shutdown now`       | Shut down system              |
| `reboot`             | Restart system                |

---

## PRACTICE MINI-PROJECT

```bash
cd /tmp
mkdir linux_practice
cd linux_practice
touch test.txt
echo "Hello Linux" > test.txt
cat test.txt
cp test.txt copy.txt
mv copy.txt renamed.txt
tar -cvf myfiles.tar ./
ls -l
```

---

## RECOMMENDED LEARNING RESOURCES

* Online terminal practice: [https://linuxcommand.org/lc3_learning_the_shell.php](https://linuxcommand.org/lc3_learning_the_shell.php)
* Book: *The Linux Command Line* by William Shotts
* Cheat sheet: [https://cheat.sh](https://cheat.sh)


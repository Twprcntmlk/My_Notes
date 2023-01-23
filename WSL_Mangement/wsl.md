# WSL Instance Creation and Mangement Notes

## Create Base WSL Instance

### List Available Distribution
```
wsl -l -o
    --list, -l [Options]
            Lists distributions.
    --online, -o
            Displays a list of available distributions for install with 'wsl --install'.
```

###  Create New Distribution
```
wsl --install -d Ubuntu-20.04
wsl --install -d {Latest Version}
```

### Ubuntu Terminal Will Show Up
```
Unix Username
username: ec2-user
password: player
(temp for set-up)

Later it will be:
username: vagrant
password:
```
#### In that Ubuntu Terminal run following commands:
```
sudo apt update
- This will update all dependencies

```

### Installing GitKraken
[GitKraken Setup Link](https://chuckdries.medium.com/installing-gitkraken-in-wsl-2-15bf6459f823)
[X-Server Download Link](https://sourceforge.net/projects/vcxsrv/))
- Run Below Seperately, They have issues otherwise
```
wget https://release.gitkraken.com/linux/gitkraken-amd64.deb

sudo dpkg -i ./gitkraken-amd64.deb

sudo apt-get install -f

sudo gitkraken
```

#### Outside Stuff Need for GitKraken
```
sudo apt install fonts-noto-color-emoji
sudo apt install fonts-noto

```
#### Set the DISPLAY environment variable in your bash_profile
```
export DISPLAY=$(cat /etc/resolv.conf | grep nameserver | awk '{print $2; exit;}'):0.0
export GDK_SCALE=2
```


### Edit bashprofile
```
ls -a
cd ~
nano .bashrc

ctrl-x
enter


```
### Pull current changes to bashrc
```
source .bashrc
```

# Now we have base file that works

## Creating Tar File?
```
- wsl --export <Distro> <FileName>
- wsl --export Ubuntu-20.04 <FileName>.tar

- wsl --export Ubuntu-20.04 goldmine_v1_07_25_2022.tar


- wsl --import <Distro> <InstallLocation> <FileName> [Options]


- wsl --import goldmine_v1_07_25_2022 goldmine_v1_07_25_2022 <FileName>.tar
```

## Getting to my wsl Instances
```
cd C:\WSL
```
## wsl help
```
wsl -h

```
## how to start my wsl instance? --distribution
```
wsl -d GoldMine -u ec2-user
password: player
```

## Create mmwork file
```
mkdir mmwork
```

## Open gitkraken for pulling in our repos
```
git pull
- see Udemy for additional GitKraken Help
mmconfig
goldmine
```

## In file explorer, we can find our instance
```
\\wsl$
```

## Rudy's Installs

[Run-Once-MMConfig](https://github.com/monetarymetals/mmconfig/blob/master/install/dev-tools/run_once/README.md)
```
mmconfig --> install --> dev-tools-->run_once --> gitconfig
- open and edit gitconfig update email and name

private key
if you need to generate a key
in mmwork/mmconfig/install/dev-tools/run_once
```

```
ssh-keygen
```

save file name as: mm-github

```
cat mm-github.pub
upload this to github
```

## running the first time script
```
check ./first-time.sh
sudo chmod +x first-time.sh
./first-time.sh
```



## back into mmconfig folder
```
./install-dev-profile.sh
exit
wsl -d GoldMine -u ec2-user
Now notice the IP address

cd mmconfig
cd install
cd server-lemp-v3

This is installing PHP, MySQL, NGINX etc.

./install-server.sh
- Yes to all
```

## Rudy MathieuMM Config Update
```
- Primary README file now points to installation README text has a little more description here.
	- Please see : https://github.com/monetarymetals/mmconfig
- Default default firewall settings for WSL
- Moved mmconfig from ~/ to ~/mmwork on first-time.sh installation
- Changed first-time.sh script's permission mode to be executable by default
- Goldmine Installation/Provisioning Update
- At the bottom of the run_once README has the instructions for installing the database fake data
	- Please see: https://github.com/monetarymetals/mmconfig/blob/master/install/dev-tools/run_once/README.md
- Edited<https://teams.microsoft.com/l/message/19:b1b566ff920a42eba2987f94bec8a2ba@thread.tacv2/1658677722000?tenantId=7815f913-24ef-45b7-a2ae-287d7d346bc8&amp;groupId=d43b3199-0c49-4407-af8b-517e8976f24d&amp;parentMessageId=1658677722000&amp;teamName=SW Team&amp;channelName=General&amp;createdTime=1658677722000>

```
```
sql.ramdisk on 8
```

# Basic Commands
```
wsl -l -v
wsl -d GoldMine -u ec2-user
wsl --shutdown goldmineV1
```

## delete uneeded wsl
```
wsl --unregister GoldMine
```

## Starting
```
wsl -d GoldMine -u ec2-user

cd ~

sql.ramdisk on 3

manager.sh start

asynctrigger.on

- from goldmine
cd  ~/mmwork/goldmine
install/install.sh local

cd ~/mmwork/goldmine/v3/data
./install.sh

from mmwork explorer type cmd

wsl -d GoldMine -u ec2-user
sql.file login_cred.sql
```

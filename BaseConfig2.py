# source /Users/przemyslawmajdanski/Desktop/GeneralWorkspace/env/bin/activate
# brew install git
# cd Prepare/Vagrant 
# vagrant plugin install vagrant-docker-compose
# git clone https://github.com/PandaAcademy/Vagrant
# cd Vagrant/     
# git checkout Bare
# git branch 
# vagrant up
# sudo "/Library/Application Support/VirtualBox/LaunchDaemons/VirtualBoxStartup.sh" restart
# - reinstall virtualboxa
# vagrant up
# vagrant ssh
# ------------------------------------
# Zajęcia Pierwsze - Vagrant
# ------------------------------------
#  Vagrant:
#  - przechowuje konfig dla maszyn wirtualnych;
#  - 
# vagrant halt ab491d4
# vagrant destroy (usnie wszystko - lepiej więc nie)
# vagrant ssh-config
# ------------------------------------
# Zajęcia Drugie - GIT
# ------------------------------------
# git --version
# git init - na folderze który nas interesuje tworze folder gira i wszystko poniej jest objete gitem
# git config -- system - dla wszystki uytkowników
# git config -- global - pod konkretnego uytkownika
# git status - show status, nietrakowane/trakowane pliki
# pliki mogą być trakc or untrack
# git add . - wszystko
# git add file 
# git add dodaje pliki do snapshota
# git commit -m 'nazwakomikakomentarz'
# tylko pliki które były poddane add przechodzą do komita
# git log --oneline - pokazuje stan 
# git log 
# git log --graph --simplify-by-decoration --pretty=format:'%d' --all
# git log --graph
# rm <plik> + git add - by wywalić plik z repo
# git rm <file>
# git reset --sofr - cofa do staggingu daną wersje commita;
# git checkout - załaduje heada
# git checkout <id> przechodzimy do starego commita
# git checkout master
# git branch dev && git checkout dev
# git checkout -b dev 
# git branch -d <dev> usuwamy
# git config alias.st status -> w efekcie git st będzie działało jak git status
# git branch -D dev
# ------------------------------------
# Zajęcia Trzecie - Marven
# ------------------------------------
# artefakt - zbudowana aplikacja
# jdk - java development kid (ma w środku maszynę wirtualną +  standardowe blibliteki = jre (java runtime enviromnet - wszystko do uruchomienia app) + wszystkie narzędzia developerskie )
# sudo apt install default-jdk
# sudo apt update
# zdefinuj zmienne dla javy:
#   export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
#   export PATH=$JAVA_HOME/bin:$PATH
# java -version
# javac -version
# javac src/main/java/pl/pandait/Intro.java -d target -kompilacja paczek do javy
# javac $(find . -name "*.java") -d target
# jar cfm target/Intro.jar Project/JavaIntro/manifest.txt -C target .   - budowanie archiwum jar
# java -jar target/Intro.jar  -sprawdzanie
# javac $(find . -name "*.java") -cp src/resources/lib/\* -d target
# Main-Class: pl.pandait.Intro
# Class-Path: /home/panda/projects/JavaIntro/src/resources/lib/chuck-0.0.2.jar
# 
# Maven:
# - struktura projektu jest wazna
# sudo apt install maven
# export M2_HOME=/usr/share/maven
# export MAVEN_HOME=/usr/share/maven
# export PATH=${M2_HOME}/bin:${PATH}
# mvn clean
# git clone https://github.com/PandaAcademy/panda_application.git
# git remote -v
# git remote set-url origin --push https://github.com/przemaj1990/panda_aplication.git
# git init
# git remote set-url origin https://github.com/PandaAcademy/panda_application.git
# git remote set-url origin --push https://github.com/przemaj1990/panda_aplication.git
# git push origin master
#
#

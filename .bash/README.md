# How to
.setupファイルを実効して下さい。
```bash:.setup
# command for exec ./.setup
. ./.setup
```

下記のコマンドをターミナルで実行することに相当します。
```
CURD=$(pwd)
ln -is ${CURD}/.bash_private ~/.bash_private
ln -is ${CURD}/.bash_aliases ~/.bash_aliases
ln -is ${CURD}/.vimrc ~/.vimrc
```

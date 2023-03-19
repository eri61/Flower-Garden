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

ホームディレクトリのbashファイル(~/.bashrc)に下記を追記。
```
# User settings
if [ -f ~/.bash_private ]; then
        . ~/.bash_private
fi
```

ホームディレクトリのbashファイルを実行し、問題が無いことを確認。
```
source ~/.bashrc
```

※参考
- [BashのプロンプトにGitのブランチを含める](https://qiita.com/jun68ykt/items/d95010ad7dae2f802474)
- [git/git-prompt.sh at master git・git](https://github.com/git/git/blob/master/contrib/completion/git-prompt.sh)

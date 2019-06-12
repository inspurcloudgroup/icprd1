# Git 与 GitHub 简介

## Github

### 仓库（Repository）

+ 仓库用来存放项目代码
+ 每个项目对应一个仓库，多个开源项目则有多个仓库

### 收藏（Star）

+ 收藏项目，方便下次查看

### 复制克隆项目（Fork）

+ 注意：在李四中fork的项目改变不会对源仓库产生影响。

### 发起请求（Pull Request）

+ pull是从远程主机取回某个分支的更新，再与本地的指定分支合并；pull request指的是希望作者能从你这里取回某个分支的更新并与他的分支进行合并。
+ 在李四中修改项目后，发起改变源仓库的请求。

### 关注（Watch）

+ 关注项目，当项目更新可以接收到通知

### 事务卡片（Issue）

+ 提交使用问题或者建议或者想法

### Github 主页

+ 账号创建成功或点击网址导航栏 github 图标都可进入 github 主页：该页左侧主要显示用户动态以及关注用户或关注仓库的动态；右侧显示所有的 git 库

### 仓库主页

+ 仓库主页主要显示项目的信息，如：项目代码，版本，收藏/关注/fork 情况等

### 个人主页

+ 个人信息：头像，个人简介，关注我的人，我关注的人，我关注的 git 库，我的开源项目，我贡献的开源项目等信息

### 开源项目贡献流程

1. Issue
2. Pull Request
   1、 fork 项目
   2、 修改自己仓库的项目代码
   3、 新建 pull request
   4、 等待作者操作审核

## Git

### Git的诞生

Linus在1991年创建了开源的Linux，但Linux的壮大是靠全世界热心的志愿者参与的，这么多人在世界各地为Linux编写代码，那Linux的代码是如何管理的呢？

1. us选择了一个商业的版本控制系统BitKeeper，但是Linux社区有人试图破解BitKeeper的协议，于是BitMover公司怒了，要收 回Linux社区的免费使用权。
2. Linus花了两周时间用C写了个分布式版本控制系统，这就是Git！一个月之内，Linux系统的源码已经由Git管理了！

### 集中式vs分布式

+ 集中式版本控制系统，版本库是集中存放在中央服务器的，干活的时候，用的都是自己的电脑，所以要先从中央服务器取得最新的版本，然后开始干 活，干完活了，再把自己的活推送给中央服务器。中央服务器就好比是个图书馆，你要改一本书，必须先从图书馆借出来，然后回到家改，改完了，再放回图书馆。集中式版本控制系统最大的毛病就是必须联网才能工作。如果在局域网内还好，带宽够大，速度够快，可如果在互联网上，遇到网速慢的话，可能提交一个10M的文件就需要5分钟。
+ 分布式版本控制系统根本没有“中央服务器”，每个人的电脑上都是一个完整的版本库，这 样，你工作的时候，就不需要联网了。在实际使用分布式版本控制系统的时候，其实很少在两人之间的电脑上推送版本库的修改，因为可能你们俩不在一个局域网内，两台电脑互相访问不了，也可 能今天你的同事病了，他的电脑压根没有开机。因此，分布式版本控制系统通常也有台充当“中央服务器”的电脑，但这个服务器的作用仅仅是用来便“交换” 大家的修改，没有它大家也照样干活，只是交换修改不方便而已。

### Git的help用法

+ 比如我们想要看看git add的用法：`git help add`，这时会在浏览器中打开帮助文档

# Git 基础操作

### 创建版本库，添加文件到版本库

+ 通过git init命令把这个目录变成Git可以管理的仓库
+ 用命令git add告诉Git，把文件添加到仓库中的暂存区
+ 用命令git commit告诉Git，把文件提交到仓库的当前分支

### 版本回退

+ HEAD指向的版本就是当前版本，因此，Git允许我们在版本的历史之间穿梭，使用命令git reset --hard commit_id。
+ 穿梭前，用git log可以查看提交历史，以便确定要回退到哪个版本。git log的第一行是最新的提交。
+ 要重返未来，用git reflog查看命令历史，以便确定要回到未来的哪个版本。
+ 使用--graph参数可以图的方式显示提交日志
+ 如果嫌输出信息太多，看得眼花缭乱的，可以试试加上--pretty=oneline参数。
+ --abbrev-commit参数可以仅显示commit id号的前几位，而不是全部显示
+ 退出git log是 q
+ git reset 作用：
  + 回退版本
  + 撤销暂存区的添加(git add)，实际上是用head分支的指向的目录树替换暂存区的文件

### 工作区和暂存区

+ 工作区（Working Directory）就是你在电脑里能看到的目录。工作区有一个隐藏目录.git，这个不算工作区，而是Git的版本库（Repository）。
+ 用“git add”把文件添加进去，实际上就是把文件修改添加到暂存区(stage or index)；用“git commit”提交更改，实际上就是把暂存区的所有内容提交到当前分支(head指向)。当使用git commit后，\.git\refs\remotes\github\master 并没有改变，\.git\refs\heads\master改变了,当使用git push后，.git\refs\remotes\github\master发生改变

### 修改

+ Remove files from the working tree and from the index
  从工作树和索引中删除文件

### 撤销修改

1. 当你改乱了工作区某个文件的内容，想直接丢弃工作区的修改时，用命令git checkout -- file。实际上是用暂存区指定的文件替换工作区的文件。
2. 当你不但改乱了工作区某个文件的内容，还添加到了暂存区时，想丢弃修改，分两步，第一步用命令git reset HEAD file，就回到了场景1，第二步按场景1操作。实际上是用head分支的指向的目录树替换暂存区的文件，这里的HEAD的意思就是当前分支
3. 当你已经提交了不合适的修改到版本库时，想要撤销本次提交，参考版本回退一节，不过前提是没有推送到远程库。
4. git checkout：Switch branches or restore working tree files

### 查看修改

+ 要随时掌握工作区的状态，使用git status命令。
+ 如果git status告诉你有文件被修改过，用git diff可以查看修改内容。
+ git diff：Show changes between commits, commit and working tree, etc
  在提交，提交和工作树等之间显示更改
  git diff 不加参数即默认比较工作区与暂存区，如果已经add了，就打印不出有什么修改了，这一步骤应该在add之前，即添加之前可以用来看看做了什么修改。
+ git status ：
  + 显示文件的三种状态
    Untracked files：文件没有添加到暂存区。
    Changes not staged for commit：文件已经添加到暂存区，还没有提交到版本库又更改了一次，如果此时直接提交，则新的改变不会提交到版本库。
    Changes to be committed：文件已经添加到暂存区，还没有提交到版本库。
  + 同时也显示分支信息

### 远程仓库

- SSH Key
  - 由于你的本地Git仓库和GitHub仓库之间的传输是通过SSH加密的，故需设置：   ssh是linux的命令，可以直接使用，但是要输入密码。ssh-keygen用来创建公钥和私钥，
    如果结点A和B想要通过免密码登录，则需要在各自的.ssh文件夹下建立authorized_keys文件且其内容是A和B的公钥 参考见4.玩转大数据→hadoop→1.hadoop入门学习→5.hadoop1伪分布搭建
  - 创建密钥：ssh-keygen -t rsa -C "youremail@example.com"
  - 关联公钥到 Github 账号下
    - 选择 Settings，然后在 Settings 页面中选择左边菜单里的 SSH and GPG keys，然后点击右上角的 New SSH key 按钮，填写 Title 和 Key(在Key文本框里粘贴id_rsa.pub文件的内容)，然后点击 Add SSH key 按钮提交。
- git中sshkey有何作用
  - 众所周知ssh是加密传输。 secure shell
  - 加密传输的算法有好多，git可使用rsa，rsa要解决的一个核心问题是，如何使用一对特定的数字，使其中一个数字可以用来加密，而另外一个数字可以用来解密。这两个数字就是你在使用git和github的时候所遇到的public key也就是公钥以及private key私钥。
  - 其中，公钥就是那个用来加密的数字，这也就是为什么你在本机生成了公钥之后，要上传到github的原因。从github发回来的，用那公钥加密过的数据，可以用你本地的私钥来还原。
  - 如果你的key丢失了，不管是公钥还是私钥，丢失一个都不能用了，解决方法也很简单，重新再生成一次，然后在github.com里再设置一次就行。
- 现在的情景是，你已经在本地创建了一个Git仓库后，又想在GitHub创建一个Git仓库，并且让这两个仓库进行远程同步，这样，GitHub上的仓库既可以作为备份，又可以让其他人通过该仓库来协作，真是一举多得。
  - 要关联一个远程库： git remote add origin git@github.com:LeisureZhao/learngit.git；
  - 可以使用命令git push origin master推送最新修改。
- 从远程库克隆 
  - 远程库在github已经准备好了，下一步是用命令git clone克隆一个本地库
    - git clone git@github.com:LeisureZhao/gitskills.git
  - 该命令会在本地生成一个目录，与远程仓库同名。如果要指定不同的目录名，可以将目录名作为git clone命令的第二个参数。
    - git clone <版本库的网址> <本地目录名>
  - 克隆版本库的时候，所使用的远程库自动被Git命名为origin。如果想用其他的名，需要用git clone命令的-o选项指定 o就是origin，使用o就是替换掉origin
    - git clone -o github git@github.com:LeisureZhao/notes-git-tutorials.git
  - 默认情况下，只能看到本地的master分支，要在dev分支上开发，就必须创建远程origin的dev分支到本地，于是用这个命令创建本地dev分支：
    - git checkout -b dev origin/dev

# Git 分支操作

### 关联、撤销本地分支与远程分支

+ 查看本地分支与远程分支的映射关系：git branch -vv
+ 建立当前分支与远程分支的映射关系: git branch --set-upstream-to=origin/branchname branchname
+ 撤销本地分支与远程分支的映射关系：git branch --unset-upstream

### 创建与合并分支

+ 查看分支： git branch   # -a 参数查看本地和远程分支的情况； -vv查看本地分支与远程分支的映射关系
+ 创建分支： git branch <name>
+ 切换分支： git checkout <name>
+ 创建+切换分支： git checkout -b <name>
+ 合并某分支到当前分支： git merge <name>  
+ 删除分支： git branch -d <name>

### 解决冲突

+ 当Git无法自动合并分支时，就必须首先解决冲突。解决冲突后，再add与commit，合并完成。
+ 用git log --graph命令可以看到分支合并图。

### 合并分支的模式选择

+ 合并分支时，加上--no-ff参数就可以用普通模式合并，合并后的历史有分支，能看出来曾经做过合并，
+ 而fast forward  快进模式合并就看不出来曾经做过合并

### 分支管理策略

+ 首先，master分支应该是非常稳定的，也就是仅用来发布新版本，平时不能在上面干活；
+ 那在哪干活呢？干活都在dev分支上，也就是说，dev分支是不稳定的，到某个时候，比如1.0版本发布时，再把dev分支合并到master上，在master分支发布1.0版本；
+ 你和你的小伙伴们每个人都在dev分支上干活，每个人都有自己的分支，时不时地往dev分支上合并就可以了。 develop

### Bug分支

+ 当手头工作没有完成时,还不想提交时要去解决mater分支的一个bug（比如我在分支dev），先把工作现场git stash一下。
+ 此时工作区是干净的，工作现场存到哪去了？用git stash list命令看看。
+ 然后切换到master分支去修复bug，修复bug时，我们会通过创建新的bug分支(issue001)进行修复，然后合并，最后删除issue001分支；
+ 修复后，先切换回dev分支，再git stash pop，回到工作现场，这样恢复的同时把stash内容也删了。
+ 还可以用git stash apply恢复，但是恢复后，stash内容并不删除，你需要用git stash drop来删除；

### Feature分支

+ 开发一个新feature(新的功能)，最好新建一个分支
+ 如果要丢弃一个没有被合并过的分支，可以通过git branch -D name强行删除

# 多人协作 GitHub 部分

+ 在GitHub上，可以任意Fork开源仓库；
+ 一定要从自己的账号下clone仓库，这样你才能推送修改。如果从bootstrap的作者的仓库地址git@github.com:twbs/bootstrap.git克隆，因为没有权限，你将不能推送修改。Bootstrap的官方仓库twbs/bootstrap、你在GitHub上fork的仓库my/bootstrap。
+ 可以推送pull request给官方仓库来贡献代码。pull是从远程主机取回某个分支的更新，再与本地的指定分支合并；pull request指的是希望作者能从你这里取回某个分支的更新并与他的分支进行合并。

# 多人协作 Git 部分

### 多人协作

1. 首先，可以试图用git push origin branch-name推送自己的修改；

2. 如果推送失败，则因为远程分支比你的本地要新，需要先用git pull试图合并；

3. 如果合并有冲突，则解决冲突，并在本地add和commit；

4. 没有冲突或者解决掉冲突后，再用git push origin branch-name推送就能成功！

   如果git pull提示“no tracking information”，则说明本地分支和远程分支的链接关系没有创建，用命令

   git branch --set-upstream-to=origin/branchname branchname。

### git fetch

+ 将 orgin所有分支更新(不是本地，而是origin/) ：git fetch origin
+ 更新origin/master：git fetch origin master

### git pull

+ git pull命令的作用是，取回远程主机某个分支的更新，再与本地的指定分支合并,如果远程分支是与当前分支合并，则冒号后面的部分可以省略。
+ 命令语法：git pull 远程主机名 远程分支名:本地分支名
+ git pull origin next：上面命令表示，取回origin/next分支，再与当前分支合并。实质上，这等同于先做git fetch，再做git merge。

### git push

+ git push命令用于将本地分支的更新，推送到远程仓库。
  + git push <远程仓库名> <本地分支名>:<远程分支名>

# Git标签tag和GitHub版本releases

### 标签管理

+ tag就是一个让人容易记住的有意义的名字，它跟某个commit绑在一起。
+ 命令git tag name用于新建一个标签，默认为HEAD，也可以指定一个commit id；
+ git tag -a tagname -m "blablabla..."可以指定标签信息； annotate  message
+ 命令git tag可以查看所有标签。
+ 可以用git show tagname查看标签信息

### 操作标签

+ 命令git push origin tagname可以推送一个本地标签；
+ 命令git push origin --tags可以推送全部未推送过的本地标签；
+ 命令git tag -d tagname可以删除一个本地标签；
+ 命令git push origin :refs/tags/tagname可以删除一个远程标签。  这是删除远程tag的方法，推送一个空tag到远程tag。

### git的版本查看

- `git --version`


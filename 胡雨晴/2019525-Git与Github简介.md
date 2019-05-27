# 一．Git与Github简介

1**.****安装Git、升级Git到最新版**

打开终端使用 `git --version` 命令查看版本

更新版本：

在终端执行如下命令下载安装 Git 所需的秘钥：

sudo apt update  # 更新源

sudo apt install software-properties-common # 安装 PPA 需要的依赖

sudo add-apt-repository ppa:git-core/ppa    # 向 PPA 中添加 git的软件源

执行如下命令选择 Python3.4 即可：

```
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.4 1
sudo update-alternatives --display python3   # 查看可选版本
sudo update-alternatives --config python3   # 选择 python3.4
```

重复前一个命令下载秘钥

执行 `sudo apt update` 更新源

执行 `sudo apt install -y git` 重新安装 Git

2.**克隆GitHub上的仓库到本地**

克隆前面我们在 GitHub 上创建的仓库，使用 `git clone + [``仓库地址]` 命令即可

GitHub 可以看成是免费的 Git 服务器，在 GitHub 上创建仓库，会自动生成一个仓库地址，主机就是指代这个仓库，主机名就等于这个仓库地址。克隆一个 GitHub 仓库（也叫远程仓库）到本地，本地仓库则会自动关联到这个远程仓库，执行 `git remote -v` 命令可以查看本地仓库所关联的远程仓库信息

`git remote` 命令就用于管理本地仓库所关联的主机，一个本地仓库可以关联任意多个主机（即远程仓库）。

另一个在其它 Git 教程中常见的命令 `git init` ，它会把当前所在目录变成一个本地仓库

1. Go语言特性

（1）  并发编程：调用go关键字，让函数一协程为单位运行，协程比线程更能节省系统资源。

（2）  错误处理：

（3）  垃圾回收：go自带垃圾回收的功能，不需要delete和free()来释放内存，系统自动进行垃圾回收。

（4）  多返回值：不需要为一次返回多个值来定义一个结构体，开发者可以选择要返回的值，用下划线为占位符丢掉不要的返回值

 
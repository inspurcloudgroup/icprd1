# 实验2 基本概念及操作

1. Shell重要快捷键

终端，即所谓的命令行界面，又称命令终端。终端本质上是对应着 Linux 上的 /dev/tty 设备，Linux 的多用户登陆就是通过不同的 /dev/tty 设备完成的，Linux 默认提供了 6 个纯命令行界面的 “terminal”（准确的说这里应该是 6 个 virtual consoles）来让用户登录。

Shell（壳），有壳就有核，这里的核就是指 UNIX/Linux 内核，Shell 是指“提供给使用者使用界面”的软件（命令解析器），普通意义上的 Shell 就是可以接受用户输入命令的程序。它之所以被称作 Shell 是因为它隐藏了操作系统底层的细节。在 UNIX/Linux 中比较流行的常见的 Shell 有 bash、zsh、ksh、csh 等等，Ubuntu 终端默认使用的是 bash，默认的桌面环境是 GNOME 或者 Unity（基于 GNOME）

| **按键**   | **作用**                         |
| ---------- | -------------------------------- |
| Shift+PgUp | 将终端显示向上滚动               |
| Shift+PgDn | 将终端显示向下滚动               |
| Tab        | 补全命令，补全目录、补全命令参数 |
| Ctrl+c     | 强行终止当前程序                 |
| ↑          | 恢复你之前输入过的命令           |

2. Linux通配符

   1. 通配符规则：
      - *：代表任意字符(0到多个)
      - ？：代表一个字符
      - [ ]：中间为字符组合，仅匹配其中任意一个字符
   2. 我们示例目录中包含如下5个TXT文件 

   ```shell
   [zhangqi@localhost nornal]$ ll
   total 0
   -rw-rw-r--. 1 zhangqi zhangqi 0 Jul 26 22:25 abd.txt
   -rw-rw-r--. 1 zhangqi zhangqi 0 Jul 26 22:26 ade.txt
   -rw-rw-r--. 1 zhangqi zhangqi 0 Jul 26 22:25 at.txt
   -rw-rw-r--. 1 zhangqi zhangqi 0 Jul 26 22:25 a.txt
   -rw-rw-r--. 1 zhangqi zhangqi 0 Jul 26 22:25 bcd.txt
   [zhangqi@localhost nornal]$
   ```

   3. ls a*.txt 找以a开头的txt文件

   ```shell
   [zhangqi@localhost nornal]$ ls a*.txt
   abd.txt  ade.txt  at.txt  a.txt
   [zhangqi@localhost nornal]$	
   ```

   4. ls a[bcd].txt 找以a开头，且文件名以bcd中任一字符结尾的txt文件

   ```shell
   [zhangqi@localhost nornal]$ ls a[bcd].txt
   ls: cannot access a[bcd].txt: No such file or directory
   [zhangqi@localhost nornal]$ ls a[bct].txt
   at.txt
   [zhangqi@localhost nornal]$
   ```

   ==备注：对于[] 中连续的字符串可以采用简写的形式，包含首尾字符，中间使用-连接
   如 ls a[bcd][cde].txt 可以简写为 lsa[b-d][c-e].txt   而不是~==

3. 帮助命令

| **命令**  | **描述**                                                 |
| --------- | -------------------------------------------------------- |
| ls --help | linux 命令自带的帮助信息                                 |
| man ls    | linux 提供的一个手册，包含了绝大部分的命令、函数使用说明 |

# 实验3 用户及文件权限管理

1. 用户管理

   1. Linux 是一个可以实现多用户登录的操作系统，比如“李雷”和“韩梅梅”都可以同时登录同一台主机，他们共享一些主机的资源，但他们也分别有自己的用户空间，用于存放各自的文件。但实际上他们的文件都是放在同一个物理磁盘上的甚至同一个逻辑分区或者目录里，但是由于 Linux 的 用户管理 和 权限机制，不同用户不可以轻易地查看、修改彼此的文件
   2. 查看用户

   ```shell
   root@kvm:~# who am i
   root     pts/0        2019-05-22 06:35 (192.168.34.1)
   ```

   root是用户名；pts/0是伪终端，所谓伪是相对于 /dev/tty 设备而言的，伪终端就是当你在图形用户界面使用 /dev/tty7 时每打开一个终端就会产生一个伪终端， pts/0 后面那个数字就表示打开的伪终端序号，你可以尝试再打开一个终端，然后在里面输入 who am i ，看第二列是不是就变成 pts/1 了；第三列则表示当前伪终端的启动时间。

   3. 创建用户（要创建用户需要 root 权限）

   ```shell
   root@kvm:~# adduser leisure
   Adding user `leisure' ...
   Adding new group `leisure' (1001) ...
   Adding new user `leisure' (1001) with group `leisure' ...
   Creating home directory `/home/leisure' ...
   Copying files from `/etc/skel' ...
   Enter new UNIX password: 
   Retype new UNIX password: 
   passwd: password updated successfully
   Changing the user information for leisure
   Enter the new value, or press ENTER for the default
   	Full Name []: 
   	Room Number []: 
   	Work Phone []: 
   	Home Phone []: 
   	Other []: 
   Is the information correct? [Y/n] y
   ```

   退出当前用户跟退出终端一样可以使用 exit 命令或者使用快捷键 Ctrl+d。给leisure设置好密码后，后面的选项的一些内容你可以选择直接回车使用默认值。

   4. 用户组

      1. 在 Linux 里面每个用户都有一个归属（用户组），用户组简单地理解就是一组用户的集合，它们共享一些资源和权限，同时拥有私有资源。一个用户是可以属于多个用户组的，正如你既属于家庭，又属于学校或公司。
      2. 每次新建用户如果不指定用户组的话，默认会自动创建一个与用户名相同的用户组（差不多就相当于家长的意思，或者说是老总）冒号之前表示用户，后面表示该用户所属的用户组
      3. 默认情况下新创建的用户是不具有 root 权限的，也不在 sudo 用户组，可以让其加入 sudo 用户组从而获取 root 权限

      ```shell
      root@kvm:~# adduser zhao
      Adding user `zhao' ...
      Adding new group `zhao' (1002) ...
      Adding new user `zhao' (1002) with group `zhao' ...
      Creating home directory `/home/zhao' ...
      Copying files from `/etc/skel' ...
      Enter new UNIX password: 
      Retype new UNIX password: 
      passwd: password updated successfully
      Changing the user information for zhao
      Enter the new value, or press ENTER for the default
      	Full Name []: 
      	Room Number []: 
      	Work Phone []: 
      	Home Phone []: 
      	Other []: 
      Is the information correct? [Y/n] y
      root@kvm:~# su zhao
      zhao@kvm:/root$ sudo ls
      sudo: unable to resolve host kvm: Connection timed out
      [sudo] password for zhao: 
      zhao is not in the sudoers file.  This incident will be reported.
      zhao@kvm:/root$ su root
      Password: 
      root@kvm:~# groups zhao
      zhao : zhao
      #让其加入 sudo 用户组从而获取 root 权限
      root@kvm:~# usermod -G sudo zhao
      root@kvm:~# groups zhao
      zhao : zhao sudo
      root@kvm:~# su zhao
      To run a command as administrator (user "root"), use "sudo <command>".
      See "man sudo_root" for details.
      zhao@kvm:/root$ sudo ls
      sudo: unable to resolve host kvm: Connection timed out
      [sudo] password for zhao:					
      ```

   5. 删除用户

   ```shell
   root@kvm:~# su leisure
   leisure@kvm:/root$ exit
   exit
   root@kvm:~# deluser leisure --remove-home
   Looking for files to backup/remove ...
   Removing files ...
   Removing user `leisure' ...
   Warning: group `leisure' has no more members.
   Done.
   root@kvm:~# su leisure
   No passwd entry for user 'leisure'
   ```

2. 文件权限

   1. 查看文件权限

      1. 使用ll命令进行查看
      2. Linux 里面一切皆文件，正因为这一点才有了设备文件（ /dev 目录下有各种设备文件，大都跟具体的硬件设备相关）
      3. 所属用户组权限，是指你所在的用户组中的所有其它用户对于该文件的权限。![img](https://doc.shiyanlou.com/linux_base/3-10.png/wm)

   2. 变更文件所有者

      1. ```shell
         root@kvm:~# adduser zhao
         Adding user `zhao' ...
         Adding new group `zhao' (1001) ...
         Adding new user `zhao' (1001) with group `zhao' ...
         Creating home directory `/home/zhao' ...
         Copying files from `/etc/skel' ...
         Enter new UNIX password: 
         Retype new UNIX password: 
         passwd: password updated successfully
         Changing the user information for zhao
         Enter the new value, or press ENTER for the default
         	Full Name []: 
         	Room Number []: 
         	Work Phone []: 
         	Home Phone []: 
         	Other []: 
         Is the information correct? [Y/n] y
         root@kvm:~# usermod -G sudo zhao
         root@kvm:~# groups zhao
         zhao : zhao sudo
         root@kvm:~# su zhao
         To run a command as administrator (user "root"), use "sudo <command>".
         See "man sudo_root" for details.
         #创建文件查看文件所有者
         zhao@kvm:~$ touch /home/zhao/iphone4
         zhao@kvm:~$ ll /home/zhao/iphone4 
         -rw-rw-r-- 1 zhao zhao 0 May 23 08:05 /home/zhao/iphone4
         zhao@kvm:~$ su root
         Password: 
         #更改文件所有者
         root@kvm:/home/zhao# chown root iphone4 
         root@kvm:/home/zhao# ll iphone4 
         -rw-rw-r-- 1 root zhao 0 May 23 08:05 iphone4	
         ```

         change owner

   3. 修改文件权限

      1. chmod [ugoa...][[+-=][rwx] file

      2. u User即文件或目录的拥有者，g group即文件或目录的所属群组，o Other除了文件或目录拥有者或所属群组之外，其他用户皆属于这个范围，aAll，即全部的用户

      3. +表示增加权限、- 表示取消权限、= 表示唯一设定权限

      4. r 表示可读取，w 表示可写入，x 表示可执行

      5. 此外chmod也可以用数字来表示权限：

         1. r=4，w=2，x=1

      6. 将文件 file1.txt 与 file2.txt 设为该文件拥有者，与其所属同一个群体者可写入，但其他以外的人则不可写入 

         1. ```
            chmod ug+w,o-w file1.txt file2.txt
            ```

      7. 此外chmod也可以用数字来表示权限

         1. ```
            chmod 771 file等价于chmod ug=rwx,o=x file
            ```

# 实验4 Linux 目录结构及文件基本操作

1. linux目录结构

   1. /etc  etcetera	这个目录用来存放所有的系统管理所需要的配置文件和子目录，如配置域名解析文件参考见4.玩转大数据→hadoop→1.hadoop入门学习→5.hadoop1伪分布搭建。

   2. /home	存放用户主目录的文件夹/home/xxx，在Linux中，每个用户都有一个自己的目录就是xxx，以用户的账号命名的，每个用户都含有自己的Desktop、Music等文件夹。

   3. /root	该目录为系统管理员，也称作超级权限者的用户主目录，内部含有Desktop、Music等文件夹。

   4. /usr	这是一个非常重要的目录，用户的很多应用程序和文件都放在这个目录下，类似于windows下的program files目录。一般将你的程序放在/usr/local目录下

   5. /bin	bin是Binary的缩写, 这个目录存放着最经常使用的命令

   6. /tmp	这个目录是用来存放一些临时文件的。

   7. /proc process information pseudo-file system查看内存情况：也可以查看cpu是否支持Intel VT和AMD-V技术 

      1. ```shell
         root@zhaolei-1-openstack:~# cat /proc/meminfo | grep MemTotal
         MemTotal:        8174768 kB
         root@zhaolei-1-openstack:~# cat /proc/meminfo                
         MemTotal:        8174768 kB
         MemFree:         7899688 kB
         ```

      2. 是一个伪文件系统，它只存在内存当中，而不占用外存空间。目录下的文件提供了很多系统重要信息，这些信息随着系统配置的变化而变化。在平时工作中我们会经常查看，比如想要知道服务器CPU数量cpuinfo、内存情况等等。

   8. /var	这个目录中存放着在不断扩充着的东西，我们习惯将那些经常被修改的目录放在这个目录下。包括各种日志文件。

   9. /lib	这个目录里存放着系统最基本的动态连接共享库，其作用类似于Windows里的DLL文件。几乎所有的应用程序都需要用到这些共享库。

   10. /dev dev是Device(设备)的缩写	该目录下存放的是Linux的外部设备，在Linux中访问设备的方式和访问文件的方式是相同的。linux下设备都是以文件的方式来管理的，硬盘表示为/dev/hda1或/dev/sda1，前两位为设备类型，如并口硬盘为hd，串口硬盘或SCSI硬盘为sd；第三位为该类型设备的顺序号为abc……，如SATA（串口硬盘）第一个设备为sda，第二个设备为sdb，依次类推；
         文件名的第四位为该硬盘的分区号1~4，为主分区或扩展分区，从5以后为逻辑分区

2. 切换目录

   1. cd    进入用户主目录；
   2. cd ~  进入用户主目录；
   3. cd -  返回到上一次的工作目录；
   4. cd ..  返回上级目录（若当前目录为“/“(根目录)，则执行完后还在“/"；".."为上级目录的意思）；
   5. cd ../..  返回上两级目录；

3. 文件基本操作

   - touch
   - cp
   - rm
   - mv
   - cat
   - vim

# 实验5 环境变量与文件查找

1. 变量

```shell
[root@hadoop1 Desktop]# a=2
[root@hadoop1 Desktop]# echo a
a
[root@hadoop1 Desktop]# echo $a
2
```

​	使用$引用变量，否则会被当做字符串看待

2. 环境变量

   1. 环境变量的作用域比自定义变量的要大，如 Shell 的环境变量作用于自身和它的子进程。Shell 程序也作为一个进程运行在操作系统之上，而我们在 Shell 中运行的大部分命令都将以 Shell 的子进程的方式运行

   2. 关于哪些变量是环境变量，可以简单地理解成在当前进程的子进程有效则为环境变量，否则不是。![此处输入图片的描述](https://doc.shiyanlou.com/document-uid735639labid60timestamp1532339293501.png/wm)

      

   3. 在 UNIX/Linux 中比较流行的常见的 Shell 有 bash、zsh、ksh、csh 等等，Ubuntu 终端默认使用的是 bash

   4. set 显示当前 Shell 所有变量，包括其内建环境变量（与 Shell 外观等相关），用户自定义变量比如tmp=3及导出的环境变量。

   5. export 显示从 Shell 中导出成环境变量的变量，也能通过它将自定义变量导出为环境变量。

   ```shell
   root@kvm:~# zhao=3
   root@kvm:~# export|grep zhao
   root@kvm:~# set|grep zhao
   zhao=3s
   ```

   6. 列出当前所有的环境变量 :`export -p`
   7. 定义环境变量并赋值：`export MYENV=7`
   8. 当你关机后，或者关闭当前的 shell 之后，环境变量就没了啊。怎么才能让环境变量对所有用户永久生效呢？写在配置文件/etc/profile里

3. 命令的查找路径

   1. 我们在 Shell 中输入一个命令，Shell 是怎么知道去哪找到这个命令然后执行的呢？这是通过环境变量 PATH 来进行搜索的
   2. 查看 PATH 环境变量的内容

```shell
$ echo $PATH
# 默认情况下你会看到如下输出
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games 
```

​		 3. PATH 里面的路径是以 : 作为分割符的，可以这样添加自定义路径：`$ PATH=$PATH:/home/newpath`

这样在/home/newpath中的脚本可以在任意目录运行了

​	 	4. 当给 PATH 环境变量追加了一个路径，它也只是在当前 Shell 有效，我一旦退出终端，再打开就会发现又失效了。在每个用户的 home 目录中有一个 Shell 每次启动时会默认执行一个配置脚本，以初始化环境，包括添加一些用户自定义环境变量等等。相应 Bash 的配置文件为 .bashrc。因此可以将3中的命令添加到.bashrc文件中。

​		5. 添加到配置文件后，每次都要退出终端重新打开甚至重启主机之后其才能生效，可以使用 source 命令来让其立即生效，它还有个别名是.。

```shell
$ cd /home/shiyanlou
$ source .bashrc
$ . ./.bashrc
#注意第一个点后面有一个空格，而且后面的文件必须指定完整的绝对或相对路径名，source 则不需要
```

4. 变量的修改和删除

   1. 为了避免操作失误导致命令找不到，我们先将 PATH 赋值给一个新的自定义变量 path

   2. ```shell
      root@kvm:/etc# path=$PATH
      root@kvm:/etc# echo $path
      /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/root/
      root@kvm:/etc# path=${path%~/}
      root@kvm:/etc# echo $path
      /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:
      ```

   3. ${变量名%匹配字串} ：从尾向前开始匹配，删除符合匹配字串的最短数据

   4. 可以使用 unset 命令删除一个环境变量

   5. ```shell
      root@kvm:/etc# unset path
      root@kvm:/etc# echo $path
      ```

5. 文件查找→1.find

```shell
[root@hadoop2 sources]# ll
total 892
-rw-r--r--. 1 root root      2 Aug 10 01:27 a0
-rw-r--r--. 1 root root      2 Aug 10 01:27 a1
-rw-r--r--. 1 root root      0 Aug 10 01:04 a1.txt
-rw-r--r--. 1 root root      2 Aug 10 01:27 a2
-rw-r--r--. 1 root root      0 Aug 10 01:04 a2.txt
-rw-r--r--. 1 root root      2 Aug 10 01:27 a3
-rw-r--r--. 1 root root      2 Aug 10 01:27 a4
-rw-r--r--. 1 root root      0 Aug 10 01:04 b1.txt
-rw-r--r--. 1 root root      0 Aug 10 01:04 b2.txt
-rw-r--r--. 1 root root      0 Aug 10 01:04 c1.txt
-rw-r--r--. 1 root root      0 Aug 10 01:04 c2.txt
-rw-r--r--. 1 root root      0 Aug 10 01:04 d1.txt
-rw-r--r--. 1 root root      0 Aug 10 01:04 d2.txt
-rw-r--r--. 1 root root  14237 Aug  5 05:57 hadoop-archives-2.5.0-cdh5.2.0-sources.jar
-rw-r--r--. 1 root root  11127 Aug  5 05:57 hadoop-archives-2.5.0-cdh5.2.0-test-sources.jar
-rw-r--r--. 1 root root  16724 Aug  5 05:57 hadoop-datajoin-2.5.0-cdh5.2.0-sources.jar
-rw-r--r--. 1 root root  11733 Aug  5 05:57 hadoop-datajoin-2.5.0-cdh5.2.0-test-sources.jar
-rw-r--r--. 1 root root  72293 Aug  5 05:57 hadoop-distcp-2.5.0-cdh5.2.0-sources.jar
-rw-r--r--. 1 root root  57949 Aug  5 05:57 hadoop-distcp-2.5.0-cdh5.2.0-test-sources.jar
-rw-r--r--. 1 root root  35175 Aug  5 05:57 hadoop-extras-2.5.0-cdh5.2.0-sources.jar
-rw-r--r--. 1 root root  18411 Aug  5 05:57 hadoop-extras-2.5.0-cdh5.2.0-test-sources.jar
-rw-r--r--. 1 root root 125817 Aug  5 05:57 hadoop-gridmix-2.5.0-cdh5.2.0-sources.jar
-rw-r--r--. 1 root root  76203 Aug  5 05:57 hadoop-gridmix-2.5.0-cdh5.2.0-test-sources.jar
-rw-r--r--. 1 root root 174549 Aug  5 05:57 hadoop-rumen-2.5.0-cdh5.2.0-sources.jar
-rw-r--r--. 1 root root  13833 Aug  5 05:57 hadoop-rumen-2.5.0-cdh5.2.0-test-sources.jar
-rw-r--r--. 1 root root  52035 Aug  5 05:57 hadoop-sls-2.5.0-cdh5.2.0-sources.jar
-rw-r--r--. 1 root root  22514 Aug  5 05:57 hadoop-sls-2.5.0-cdh5.2.0-test-sources.jar
-rw-r--r--. 1 root root  78495 Aug  5 05:57 hadoop-streaming-2.5.0-cdh5.2.0-sources.jar
-rw-r--r--. 1 root root  80681 Aug  5 05:57 hadoop-streaming-2.5.0-cdh5.2.0-test-sources.jar
[root@hadoop2 sources]# find . -name "[a-d]1.txt"
./a1.txt
./b1.txt
./c1.txt
./d1.txt
[root@hadoop2 sources]# find . -name "hadoop-archives-2.5.0-cdh5.2.0*"
./hadoop-archives-2.5.0-cdh5.2.0-test-sources.jar
./hadoop-archives-2.5.0-cdh5.2.0-sources.jar
```

6. 文件查找→2.which

```shell
root@ctl-1:~# find mysql
find: 'mysql': No such file or directory
root@ctl-1:~# which mysql
/usr/bin/mysql
```

# 挑战1 寻找文件

1. 步骤：

```shell
root@kvm:~# find /etc/ -name 'sources.list'
/etc/apt/sources.list
root@kvm:~# ll /etc/apt/sources.list
-rw-r--r-- 1 root root 1682 May  4 20:32 /etc/apt/sources.list
root@kvm:~# chown root /etc/apt/sources.list
root@kvm:~# ll /etc/apt/sources.list
-rw-r--r-- 1 root root 1682 May  4 20:32 /etc/apt/sources.list
root@kvm:~# chmod u+rw,g-rw,o-rw /etc/apt/sources.list
root@kvm:~# ll /etc/apt/sources.list
-rw------- 1 root root 1682 May  4 20:32 /etc/apt/sources.list
root@kvm:~# chmod u+rw,g+r,o+r /etc/apt/sources.list
root@kvm:~# ll /etc/apt/sources.list
-rw-r--r-- 1 root root 1682 May  4 20:32 /etc/apt/sources.list
```

# 实验6：文件打包与解压缩

1. 首先要弄清两个概念：打包和压缩。打包是指将一大堆文件或目录变成一个总的文件；压缩则是将一个大的文件通过一些压缩算法变成一个小文件。
2. 为什么要区分这两个概念呢？这源于Linux中很多压缩程序只能针对一个文件进行压缩，这样当你想要压缩一大堆文件时，你得先将这一大堆文件先打成一个包（tar命令），然后再用压缩程序进行压缩（gzip bzip2命令）。
3. 仅打包，不压缩！
   1. -c 建立新的压缩文件
   2. -v 显示操作过程
   3. -f  指定备份文件

```shell
[root@hadoop1 Documents]# touch test1.txt
[root@hadoop1 Documents]# touch test2.txt
[root@hadoop1 Documents]# tar -cvf test.tar test1.txt test2.txt 
test1.txt
test2.txt
[root@hadoop1 Documents]# ls
test1.txt  test2.txt  test.tar
```

4. 打包后，以gzip或bzip2压缩
   1. -z gzip
   2. -j bzip2
   3. -J xz

```shell
[root@hadoop1 Documents]# tar -zcvf t1.tar.gz text1.txt text2.txt 
text1.txt
text2.txt
[root@hadoop1 Documents]# tar -jcvf t2.tar.bz2 text1.txt text2.txt 
text1.txt
text2.txt
```

5. 查阅gz包内有哪些文件
   1. -z  通过gzip指令处理备份文件
   2. -t   列出备份文件的内容

```shell
[root@hadoop1 Documents]# tar -ztvf t1.tar.gz 
-rw-r--r-- root/root         0 2018-07-23 17:34 text1.txt
-rw-r--r-- root/root         0 2018-07-23 17:34 text2.txt
```

6. 将tar包解压缩
   1. -x  从压缩的文件中提取文件

```shell
[root@hadoop1 Documents]# rm text1.txt text2.txt 
rm: remove regular empty file `text1.txt'? y
rm: remove regular empty file `text2.txt'? y
[root@hadoop1 Documents]# tar -zxvf t1.tar.gz
text1.txt
text2.txt
```

## 
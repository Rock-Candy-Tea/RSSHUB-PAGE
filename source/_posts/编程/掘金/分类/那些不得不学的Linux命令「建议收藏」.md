
---
title: '那些不得不学的Linux命令「建议收藏」'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7107'
author: 掘金
comments: false
date: Thu, 17 Jun 2021 01:53:46 GMT
thumbnail: 'https://picsum.photos/400/300?random=7107'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一、命令的原理</h2>
<p>命令分为内部命令和外部命令，
命令行也是一个程序，通过把用户输入的字符的第一个空格前面的内容当作命令来执行
如果内部命令直接执行，外部命令就要根据环境变量去找对应的文件，然后执行文件</p>
<pre><code class="copyable">type ：命令的类型
内部命令 | 外部命令
help :内部帮助命令
查看这个命令的作用
help cd
<span class="copy-code-btn">复制代码</span></code></pre>
<p>man :帮助手册manual
也是查看命令的作用，但是更详细
每一种命令都有它的类别，同一个命令可能会有多种类别
man
1：用户命令(/bin, /usr/bin, /usr/local/bin)
2：系统调用
3：库用户
4：特殊文件(设备文件)
5：文件格式(配置文件的语法)
6：游戏
7：杂项(Miscellaneous)
8: 管理命令(/sbin, /usr/sbin, /usr/local/sbin)</p>
<pre><code class="copyable">file ：查看文件的类型
ELF:一个二进制文件
[root@node01 ~]# type ifconfig
ifconfig is /sbin/ifconfig
[root@node01 ~]# file /sbin/ifconfig
/sbin/ifconfig: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.18, stripped
<span class="copy-code-btn">复制代码</span></code></pre>
<p>echo :打印到标准输出
将你写在后面的内容打印到下面
[root@node01 ~]# echo abcd
abcd</p>
<pre><code class="copyable">环境变量
可以用下面命令显示所有环境变量的路径
[root@node01 ~]# echo $PATH
/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:/root/bin
<span class="copy-code-btn">复制代码</span></code></pre>
<p>whereis ：查看命令的位置
当前系统语言
[root@node01 ~]# echo $LANG
en_US.UTF-8</p>
<pre><code class="copyable">ps
-ef ：查看系统所有正在运行的进程
变量
linux里也可以定义变量
单个变量
[root@node01 ~]# a=1
[root@node01 ~]# echo $a
1
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">数组</h3>
<pre><code class="copyable">linux对空格敏感，而非逗号
[root@node01 ~]# b=(1 k 2 4)
[root@node01 ~]# echo $b
1
[root@node01 ~]# echo $&#123;b[1]&#125;
k
<span class="copy-code-btn">复制代码</span></code></pre>
<p>hash ：一个缓存的区域
一些命令的路径使用过后就会缓存在这里而不用再去磁盘找
-r :清除缓存</p>
<h2 data-id="heading-2">二、文件系统命令</h2>
<p><strong>目录</strong></p>
<pre><code class="copyable">/boot: 系统启动相关的文件，如内核、initrd，以及grub(bootloader)
/dev: 设备文件
/etc：配置文件
/home：用户的家目录，每一个用户的家目录通常默认为/home/USERNAME
/root：管理员的家目录；
/lib：库文件
/media：挂载点目录，移动设备
/mnt：挂载点目录，额外的临时文件系统
/opt：可选目录，第三方程序的安装目录
/proc：伪文件系统，内核映射文件
/sys：伪文件系统，跟硬件设备相关的属性映射文件
/tmp：临时文件, /var/tmp
/var：可变化的文件
/bin: 可执行文件, 用户命令
/sbin：管理命令
<span class="copy-code-btn">复制代码</span></code></pre>
<p>文件及目录显示的属性</p>
<h2 data-id="heading-3">文件类型</h2>
<pre><code class="copyable">出现在第一个字母
-：普通文件 (f)
d: 目录文件

b: 块设备文件 (block)
c: 字符设备文件 (character)

l: 符号链接文件(symbolic link file)

p: 命令管道文件(pipe)
s: 套接字文件(socket)

<span class="copy-code-btn">复制代码</span></code></pre>
<p>文件权限
第一个：文件所有者(u)的权限，这里是root
第二个：所属组(g)的权限
第三个：其他人(o)的权限</p>
<p>9位，每3位一组
每一组：rwx(读，写，执行)
硬链接的次数</p>
<p>硬链接相当于是windows的创建快捷方式（被创建了几次快捷方式）
文件的属主(owner)</p>
<p>文件属于谁
文件的属组(group)</p>
<p>文件属于哪个组
文件大小(size)，单位是字节</p>
<p>文件大小
时间戳(timestamp)：最近一次被修改的时间</p>
<p>最近一次被修改的时间
df:显示磁盘使用情况</p>
<p>-h：显示大小的单位
装系统的时候会进行分区，看每个分区的大小及目录
du：显示文件使用情况</p>
<p>-s：所有文件大小的总和
-h：显示大小的单位
-a：连隐藏文件大小也显示
ls：显示目录</p>
<p>-r：颠倒文件显示的顺序
-t：按照文件修改时间来显示文件顺序
-lha
使用ls命令可以同时list多个文件夹下的内容
//同时显示etc和temp下的文件
ls /etc /temp</p>
<pre><code class="copyable">-cd：切换工作目录

-mkdir：创建目录

-p：可以创建在不存在的目录下创建目录
一次创建多个目录
//在a目录下创建1，2，3目录
mkdir a/&#123;1,2,3&#125;dir
<span class="copy-code-btn">复制代码</span></code></pre>
<p>rm：删除
cp：拷贝
mv：移动
ln：链接
默认硬链接
cp -p
-s：软链接
相当于windows的创建快捷方式
源文件删除，这个链接就删除
ln -s test test.soft</p>
<pre><code class="copyable">stat：显示元数据信息

touch
把文件的三个时间都变为现在的时间
应用：
创建一个文件
touchh abc.txt
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">三、文件操作命令</h2>
<pre><code class="copyable">cat ：把文件这个显示到命令行里
如果文件太大有些内容就会看不到
more ：分页显示文件
一次显示一个屏幕的文件内容
空格：显示下一页
但是这个命令无法向上翻页，翻到最后一页后就会退出
less ：分页显示文件
能向上翻页，向下翻页
空格：向下翻页
b：向上翻页
q：退出
很明显，less将文件加载到了内存中，才能上下翻页，如果文件太大超过内存就会出现文问题
head :显示文件的头十行内容
默认显示文件头十行内容
-number:显示文件的前number行
-2:显示文件前两行
tail :显示文件最后十行
默认显示文件最后十行内容
同上可以自定义显示几行
-f:显示这个文件刚刚追加的内容
//先使用这个命令,此时命令行会暂停状态
//如果此时在另一个窗口动态的给abc.log追加内容,内容就会在暂停的窗口里显示出来
//e.g.比如运行hadoop时可以通过这个命令来显示有什么错误
tail -f abc.log
<span class="copy-code-btn">复制代码</span></code></pre>
<p>| :管道命令
把前面命令作为standard output传到一个命令里
//显示b.txt的前三行
cat b.txt | head -3
//显示文件第五行
head -5 b.txt | tail -1</p>
<p>xargs :build and execute command lines from standard input
把前一个命令的标准输出作为后一个命令的参数</p>
<pre><code class="copyable">//当前目录是是root家目录
//如果没有加上xargs是不会打印根目录下的内容的
//xargs把/作为参数传递给ls命令
[root@node01 ~]# echo "/" | xargs ls -l
total 90
dr-xr-xr-x.  2 root root  4096 Jul  5 18:16 bin
dr-xr-xr-x.  5 root root  1024 Jul  5 18:17 boot
drwxr-xr-x. 18 root root  3700 Jul 11 18:40 dev
drwxr-xr-x. 61 root root  4096 Jul 11 18:40 etc
drwxr-xr-x.  2 root root  4096 Sep 23  2011 home
dr-xr-xr-x.  8 root root  4096 Jul  5 18:16 lib
dr-xr-xr-x.  9 root root 12288 Jul  5 18:17 lib64
drwx------.  2 root root 16384 Jul  5 18:15 lost+found
drwxr-xr-x.  2 root root  4096 Sep 23  2011 media
drwxr-xr-x.  2 root root  4096 Sep 23  2011 mnt
drwxr-xr-x.  2 root root  4096 Sep 23  2011 opt
dr-xr-xr-x. 85 root root     0 Jul 11 18:40 proc
dr-xr-x---.  7 root root  4096 Jul 12 05:39 root
dr-xr-xr-x.  2 root root 12288 Jul  5 18:17 sbin
drwxr-xr-x.  7 root root     0 Jul 11 18:40 selinux
drwxr-xr-x.  2 root root  4096 Sep 23  2011 srv
drwxr-xr-x. 13 root root     0 Jul 11 18:40 sys
drwxrwxrwt.  3 root root  4096 Jul 12 05:43 tmp
drwxr-xr-x. 13 root root  4096 Jul  5 18:16 usr
drwxr-xr-x. 17 root root  4096 Jul  5 18:16 var
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            
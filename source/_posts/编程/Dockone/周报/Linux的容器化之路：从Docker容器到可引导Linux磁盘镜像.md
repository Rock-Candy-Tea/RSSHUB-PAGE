
---
title: 'Linux的容器化之路：从Docker容器到可引导Linux磁盘镜像'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211129/532cb8c1e6ed70f508eda4bd08b82225.png'
author: Dockone
comments: false
date: 2021-11-30 09:06:47
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211129/532cb8c1e6ed70f508eda4bd08b82225.png'
---

<div>   
<br>【编者的话】自这篇文章发表后的两年多时间里，我看到人们对于从容器和Dockerfiles构建VM镜像很感兴趣。这有利于鼓励我继续这个工具的第二版开发，新的版本将涵盖更多的实际应用场景，具备更友好的用户使用体验。<br>
<br>虽然还没有没有看到上述方法的任何实际应用，但我坚定地认为对这一方法的持续探索是获得系统内部深层次知识的唯一途径。本文的讨论将主要涉及Docker和Linux。<br>
<br>我们是否可以获取一个真正意义上的Docker基础镜像？这个镜像只包含单行FROM debian:latest的Dockerfile，并能够转在物理机或虚拟机上启动运行。换句话说，是否可以创建一个磁盘镜像，既具备与容器相同的Linux用户环境，又具备引导能力？为此，实现目标的第一步就是DUMP容器根文件系统，这个步骤约等于执行docker export。不过后面还需要一系列其他的步骤，才能最终实现目标。<br>
<h3>理论</h3>开始之前引入一点支撑理论。Linux操作系统安装完成后，基本上是文件系统下一系列文件的组合，包括Linux内核二进制文件、初始裸盘二进制文件以及用户空间程序和调用库（通常是GNU内核应用）等，其中也包括重要的引导加载程序：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211129/532cb8c1e6ed70f508eda4bd08b82225.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211129/532cb8c1e6ed70f508eda4bd08b82225.png" class="img-polaroid" title="图片_1.png" alt="图片_1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
提供运行tree -L 1 /命令，验证检查一下根目录的结构：<br>
<pre class="prettyprint">$ cat /etc/os-release | grep NAME<br>
PRETTY_NAME="Debian GNU/Linux 9 (stretch)"<br>
NAME="Debian GNU/Linux"<br>
<br>
$ tree -L 1 /<br>
/<br>
├── bin<br>
├── boot<br>
├── data<br>
├── dev<br>
├── etc<br>
├── home<br>
├── initrd.img -> boot/initrd.img-4.9.0-9-amd64  # initial ramdisk<br>
├── lib<br>
├── lib64<br>
├── media<br>
├── mnt<br>
├── opt<br>
├── proc<br>
├── root<br>
├── run<br>
├── sbin<br>
├── srv<br>
├── sys<br>
├── tmp<br>
├── usr<br>
├── var<br>
└── vmlinuz -> boot/vmlinuz-4.9.0-9-amd64        # kernel binary<br>
</pre><br>
接下来，再简要地看看Docker环境。Docker采用操作系统级虚拟化方式来封装其容器。这意味着容器运行共享了宿主机的内核，用户空间来自于Linux发行版系统，是完全隔离的：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211129/c1fd128cefdd632e6a49a7a3d92d34aa.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211129/c1fd128cefdd632e6a49a7a3d92d34aa.png" class="img-polaroid" title="图片_2.png" alt="图片_2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
我们启动一个容器，来探究一下容器环境的根目录：<br>
<pre class="prettyprint">$ docker run -it debian:latest bash<br>
<br>
root@62376e4c451b:/# cat /etc/os-release | grep NAME<br>
PRETTY_NAME="Debian GNU/Linux 9 (stretch)"<br>
NAME="Debian GNU/Linux"<br>
<br>
root@62376e4c451b:/# apt-get update && apt-get install -y tree<br>
root@62376e4c451b:/# tree -L 1<br>
.<br>
|-- bin<br>
|-- boot<br>
|-- dev<br>
|-- etc<br>
|-- home<br>
|-- lib<br>
|-- lib64<br>
|-- media<br>
|-- mnt<br>
|-- opt<br>
|-- proc<br>
|-- root<br>
|-- run<br>
|-- sbin<br>
|-- srv<br>
|-- sys<br>
|-- tmp<br>
|-- usr<br>
`--  var<br>
<br>
19 directories, 0 files<br>
<br>
root@62376e4c451b:/# tree -L 1 /boot<br>
boot/<br>
0 directories, 0 files<br>
</pre><br>
可以发现上图所示的内容是Debian的用户空间，但没有内核相关的数据。然而，这还不是唯一的区别。当Linux操作系统将INIT守护进程作为PID 1进程运行时，Docker容器通常将shell或用户定义可执行进程作为PID 1进程。因此，我们还需要解决这个差异，以便使容器的环境状态尽可能接近完整的Debian系统部署。<br>
<h3>实践</h3>开始动手实践的第一步是创建一个具有以下内容的Dockerfile，此步骤具备重复操作性：<br>
<pre class="prettyprint">FROM debian:stretch<br>
</pre><br>
用docker build -t mydebian命令构建一个容器镜像。用wagoodman/dive命令查看这个镜像：dive mydebian。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211129/630d044a7b167f35570810107ce94fad.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211129/630d044a7b167f35570810107ce94fad.png" class="img-polaroid" title="图片_3.png" alt="图片_3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>只包含Debian用户空间的镜像</em><br>
<br>如图所示，尽管该镜像包含了功能完整的Debian用户空间，镜像的总大小也只有101 MB。但这个镜像缺少内核，需要下载并安装系统的内核二进制文件，通过以下方式修改Dockerfile可以很容易实现：<br>
<pre class="prettyprint">FROM debian:stretch<br>
RUN apt-get -y update<br>
RUN apt-get -y install --no-install-recommends \<br>
linux-image-amd64<br>
</pre><br>
重新构建并查看更新后的新镜像：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211129/fc0854b217bba564291207a4502852c5.gif" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211129/fc0854b217bba564291207a4502852c5.gif" class="img-polaroid" title="图片_4.gif" alt="图片_4.gif" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>包括Debian用户空间和内核的镜像</em><br>
<br>目测linux-image-amd64包带来了232 MB的数据，其中24 MB来自/boot文件夹，大约200 MB来自/lib文件夹。继续往下分析……<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211129/ffc10ca406e08f934b809409695b5179.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211129/ffc10ca406e08f934b809409695b5179.png" class="img-polaroid" title="图片_5.png" alt="图片_5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>包括Debian用户空间和内核的镜像（详细）</em><br>
<br>请注意/boot/vmlinux -4.9.0-9-amd64内核包只有4.2 MB，/boot/initrd.img-4.9.0-9-amd64初始化裸盘包约16 MB，剩下的约200 MB是/lib/modules中的内核模块，以及常见的驱动文件。<br>
<br>接下来安装并分析一下init守护进程- systemd：<br>
<pre class="prettyprint">FROM debian:stretch<br>
RUN apt-get -y update<br>
RUN apt-get -y install --no-install-recommends \<br>
linux-image-amd64<br>
RUN apt-get -y install --no-install-recommends \<br>
systemd-sysv<br>
</pre><br>
重新构建镜像并查看更新后的新镜像：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211129/0fadcf3fea064a22f38095a732d53bc0.gif" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211129/0fadcf3fea064a22f38095a732d53bc0.gif" class="img-polaroid" title="图片_6.gif" alt="图片_6.gif" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>包括Debian用户空间、systemd和内核的镜像</em><br>
<br>如图所示，这部分约有30M数据。我们导出容器的文件系统到一个tar包：<br>
<pre class="prettyprint">$ CID=$(docker run -d mydebian /bin/true)<br>
$ docker export -o linux.tar $&#123;CID&#125;<br>
<br>
# List files in the archive:<br>
$ tar -tf linux.tar | grep -E '^[^/]*/?$'<br>
.dockerenv<br>
bin/<br>
boot/<br>
dev/<br>
etc/<br>
home/<br>
initrd.img<br>
initrd.img.old<br>
lib/<br>
lib64/<br>
media/<br>
mnt/<br>
opt/<br>
proc/<br>
root/<br>
run/<br>
sbin/<br>
srv/<br>
sys/<br>
tmp/<br>
usr/<br>
var/<br>
vmlinuz<br>
vmlinuz.old<br>
</pre><br>
完成上述安装步骤之后，我们开始从tar文件中创建一个可引导的磁盘镜像。下面的步骤可以在Linux宿主机上直接执行，但由于我使用的是macOS，所以我将采用另一个Debian容器作为构建用机器：<br>
<pre class="prettyprint">$ docker run -it -v `pwd`:/os:rw            \<br>
--cap-add SYS_ADMIN --device /dev/loop0 \<br>
debian:stretch bash<br>
</pre><br>
第1步：创建一个足够大的磁盘镜像文件：<br>
<pre class="prettyprint">$ IMG_SIZE=$(expr 1024 \* 1024 \* 1024)<br>
$ dd if=/dev/zero of=/os/linux.img bs=$&#123;IMG_SIZE&#125; count=1<br>
</pre><br>
第2步：在新创建的磁盘镜像上创建一个磁盘分区：<br>
<pre class="prettyprint">$ sfdisk /os/linux.img <<EOF<br>
label: dos<br>
label-id: 0x5d8b75fc<br>
device: new.img<br>
unit: sectors<br>
<br>
linux.img1 : start=2048, size=2095104, type=83, bootable<br>
EOF<br>
<br>
Checking that no-one is using this disk right now ... OK<br>
<br>
Disk /os/linux.img: 1 GiB, 1073741824 bytes, 2097152 sectors<br>
Units: sectors of 1 * 512 = 512 bytes<br>
Sector size (logical/physical): 512 bytes / 512 bytes<br>
I/O size (minimum/optimal): 512 bytes / 512 bytes<br>
<br>
>>> Script header accepted.<br>
>>> Script header accepted.<br>
>>> Script header accepted.<br>
>>> Script header accepted.<br>
>>> Created a new DOS disklabel with disk identifier 0x5d8b75fc.<br>
/os/linux.img1: Created a new partition 1 of type 'Linux' and of size 1023 MiB.<br>
/os/linux.img2: Done.<br>
<br>
New situation:<br>
<br>
Device         Boot Start     End Sectors  Size Id Type<br>
/os/linux.img1 *     2048 2097151 2095104 1023M 83 Linux<br>
<br>
The partition table has been altered.<br>
Syncing disks.<br>
</pre><br>
第3步：挂载镜像，使用ext3文件系统格式化，并将前面步骤中导出的tar文件内容复制到文件系统中：<br>
<pre class="prettyprint">$ OFFSET=$(expr 512 \* 2048)<br>
$ losetup -o $&#123;OFFSET&#125; /dev/loop0 /os/linux.img<br>
$ mkfs.ext3 /dev/loop0<br>
$ mkdir /os/mnt<br>
$ mount -t auto /dev/loop0 /os/mnt/<br>
$ tar -xvf /os/linux.tar -C /os/mnt/<br>
</pre><br>
第4步：安装引导加载程序并卸载镜像：<br>
<pre class="prettyprint">$ apt-get update -y<br>
$ apt-get install -y extlinux<br>
<br>
$ extlinux --install /os/mnt/boot/<br>
$ cat > /os/mnt/boot/syslinux.cfg <<EOF<br>
DEFAULT linux<br>
SAY Now booting the kernel from SYSLINUX...<br>
LABEL linux<br>
KERNEL /vmlinuz<br>
APPEND ro root=/dev/sda1 initrd=/initrd.img<br>
EOF<br>
<br>
$ dd if=/usr/lib/syslinux/mbr/mbr.bin of=/os/linux.img bs=440 count=1 conv=notrunc<br>
<br>
$ umount /os/mnt<br>
$ losetup -D<br>
</pre><br>
上述步骤的结果将在工作目录生成一个linux.img的磁盘镜像文件，实现预期目标。<br>
<h3>结果</h3>我们按照前文的步骤，创建了一个可引导的Linux磁盘镜像。这个镜像支持转储到一个物理或虚拟的磁盘驱动器上。我们可以用这个镜像文件启动一台QEMU虚拟机：<br>
<pre class="prettyprint">$ qemu-system-x86_64 -drive file=linux.img,index=0,media=disk,format=raw<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211129/7e5ebf8155c9af744eaf212173caa7cd.gif" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211129/7e5ebf8155c9af744eaf212173caa7cd.gif" class="img-polaroid" title="图片_7.gif" alt="图片_7.gif" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>虚拟机运行linux.img镜像</em><br>
<br>或者用VirtualBox将将这个镜像转换为VDI磁盘：<br>
<pre class="prettyprint">$ VBoxManage convertfromraw --format vdi linux.img linux.vdi<br>
</pre><br>
<h3>福利：小巧的Alpine Linux</h3>对于用户而言，如果约400 MB大小的Debian镜像太大的话，那么100 MB 大小的Alpine Linux也可以提供类似的功能：<br>
<pre class="prettyprint">FROM alpine:3.9.4<br>
RUN apk update<br>
RUN apk add linux-virt<br>
RUN apk add openrc<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211129/107d10de0975909a3a0f6e4b415a349a.gif" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211129/107d10de0975909a3a0f6e4b415a349a.gif" class="img-polaroid" title="图片_8.gif" alt="图片_8.gif" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>结束语</h3>本人创建了一个使用Docker自动创建磁盘镜像的项目，目前已经完成Debian和Alpine发行版的自动化创建，有兴趣的读者可以在<a href="https://github.com/iximiuz/docker-to-linux">GitHub</a>上获取。并提供一下本人关于容器的更多文章：<br>
<ul><li><a href="https://iximiuz.com/en/posts/not-every-container-has-an-operating-system-inside/">Not every container has an operating system inside</a></li><li><a href="https://iximiuz.com/en/posts/you-dont-need-an-image-to-run-a-container/">You don't need an image to run a container</a></li><li><a href="https://iximiuz.com/en/posts/you-need-containers-to-build-an-image/">You need containers to build images</a></li></ul><br>
<br><strong>原文链接：<a href="https://iximiuz.com/en/posts/from-docker-container-to-bootable-linux-disk-image/">From Docker Container to Bootable Linux Disk Image</a>（翻译：易理林）</strong>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            
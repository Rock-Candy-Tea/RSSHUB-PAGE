
---
title: '聊聊Linux系统中的僵尸进程'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/195230-abbbad9dfc11b943.png'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/195230-abbbad9dfc11b943.png'
---

<div>   
<h3>车祸现场</h3>
<p>今天下午，笔者正在认真搬砖，日志集群中有一台机器忽然报init进程占用100% CPU。strace之，发现疯狂输出如下系统调用。</p>
<pre><code>~ strace -p 1
rt_sigprocmask(SIG_BLOCK, ~[RTMIN RT_1], [], 8) = 0
clone(child_stack=0, flags=CLONE_CHILD_CLEARTID|CLONE_CHILD_SETTID|SIGCHLD, child_tidptr=0x7f7cc15789d0) = -1 ENOMEM (Cannot allocate memory)
rt_sigprocmask(SIG_SETMASK, [], NULL, 8) = 0
close(9)                                = 0
close(10)                               = 0
pipe([9, 10])                           = 0
rt_sigprocmask(SIG_BLOCK, ~[RTMIN RT_1], [], 8) = 0
clone(child_stack=0, flags=CLONE_CHILD_CLEARTID|CLONE_CHILD_SETTID|SIGCHLD, child_tidptr=0x7f7cc15789d0) = -1 ENOMEM (Cannot allocate memory)
rt_sigprocmask(SIG_SETMASK, [], NULL, 8) = 0
close(9)                                = 0
close(10)                               = 0
pipe([9, 10])                           = 0
rt_sigprocmask(SIG_BLOCK, ~[RTMIN RT_1], [], 8) = 0
clone(child_stack=0, flags=CLONE_CHILD_CLEARTID|CLONE_CHILD_SETTID|SIGCHLD, child_tidptr=0x7f7cc15789d0) = -1 ENOMEM (Cannot allocate memory)
rt_sigprocmask(SIG_SETMASK, [], NULL, 8) = 0
close(9)                                = 0
close(10)                               = 0
pipe([9, 10])                           = 0
</code></pre>
<p>然后top和ps发现大量PPID为1的僵尸进程，说明init进程不知为何不再回收僵尸进程了。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="930" data-height="343"><img data-original-src="//upload-images.jianshu.io/upload_images/195230-abbbad9dfc11b943.png" data-original-width="930" data-original-height="343" data-original-format="image/png" data-original-filesize="56181" src="https://upload-images.jianshu.io/upload_images/195230-abbbad9dfc11b943.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="755" data-height="722"><img data-original-src="//upload-images.jianshu.io/upload_images/195230-4e88e9cc267578ee.png" data-original-width="755" data-original-height="722" data-original-format="image/png" data-original-filesize="111370" src="https://upload-images.jianshu.io/upload_images/195230-4e88e9cc267578ee.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>原因未查明（高度怀疑CentOS 6系统/内核bug，或是硬件问题？下图是查找到的一种可能性），并且僵尸进程还在不断增多，急呼运维同学reboot，遂恢复正常。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="903" data-height="270"><img data-original-src="//upload-images.jianshu.io/upload_images/195230-012bb0ec5f76485a.png" data-original-width="903" data-original-height="270" data-original-format="image/png" data-original-filesize="57905" src="https://upload-images.jianshu.io/upload_images/195230-012bb0ec5f76485a.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>折腾了半天，今晚简单说说僵尸进程吧。</p>
<h3>僵尸进程、产生原因及危害</h3>
<p>"zombie process"或者"defunct process"，是类Unix系统中的概念，指那些<strong>实际运行已经完成或终止</strong>［如通过<code>exit()</code>系统调用，或者发生错误、收到终止信号］，<strong>但是在系统进程表中仍然残留着对应的进程项</strong>，<strong>没有完全被清理的进程</strong>。僵尸进程已经释放了除进程表项外的所有内存空间，无法再被调度执行，只是在等待其他进程来收集它的退出状态信息而已。</p>
<p>在正常情况下，父进程会通过<code>wait()</code>或<code>waitpid()</code>系统调用进行善后处理，即获取其子进程的退出状态。一旦成功获取，该僵尸子进程就会被销毁（reaped）而不复存在，其进程表项也会被释放。所以子进程退出时，应该只会在<code>exit()</code>和<code>wait()</code>之间很短暂地处于僵尸状态。</p>
<p>但是，如果父进程没有通过<code>wait()</code>或<code>waitpid()</code>系统调用获取其子进程的退出状态，也没有显式地处理或者忽略掉SIGCHLD信号［该信号是子进程结束时发送给父进程的］，并且父进程保持运行，那么它的子进程结束后就一直处于僵尸状态了，此时就可以被用户观察到。在top命令下，僵尸进程的状态会显示为"Z"，在ps命令下则会带上"<defunct>"标记。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1200" data-height="700"><img data-original-src="//upload-images.jianshu.io/upload_images/195230-8763b2515c5c700d.png" data-original-width="1200" data-original-height="700" data-original-format="image/png" data-original-filesize="218209" src="https://upload-images.jianshu.io/upload_images/195230-8763b2515c5c700d.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>很显然，如果僵尸进程一直不被销毁，那么它们将永远占用PID和进程表中的空间。Linux系统中的PID取值范围是有限制的（在<code>/proc/sys/kernel/pid_max</code>下，默认值32768），过多的僵尸进程会导致系统PID耗尽，无法再创建新的进程。</p>
<h3>如何手动清理？</h3>
<p>僵尸进程是无法被直接kill掉的，而造成僵尸进程无法销毁的罪魁祸首是它的父进程不做善后工作。所以，我们可以通过kill命令发送SIGKILL/SIGTERM信号直接干掉父进程，它的子进程就会成为所谓“孤儿进程”（orphan process）。孤儿进程会被根进程init收养，并且init进程会在后台执行<code>wait()</code>或<code>waitpid()</code>系统调用，代替它们的父进程完成清理工作。</p>
<p>但是在极端情况下，仍然有可能出现init出现大量僵尸子进程的情况（比如本文开头），这时就只能干掉init进程——即重启系统了。</p>
<h3>如何避免？</h3>
<p>父进程一定要尽职尽责，避免出现长时间僵尸进程的方法有：</p>
<ul>
<li>在<code>signal()</code>系统调用中设定SIGCHLD信号的handler回调，并显式<code>wait()</code>处理之。</li>
<li>在<code>signal()</code>系统调用中设定handler为SIG_IGN，即显式忽略该信号，子进程的回收会由内核直接负责。</li>
<li>在产生子进程时做两次<code>fork()</code>，并立即杀掉一级子进程，令二级子进程（即真正的子进程）成为孤儿并被init收养。没那么“负责任”，但是也比较安全。</li>
</ul>
<h3>The End</h3>
<p>民那晚安晚安。</p>
  
</div>
            
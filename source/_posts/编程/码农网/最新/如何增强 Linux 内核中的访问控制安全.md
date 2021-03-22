
---
title: '如何增强 Linux 内核中的访问控制安全'
categories: 
    - 编程
    - 码农网
    - 最新

author: 码农网
comments: false
date: Thu, 13 Dec 2018 01:05:00 GMT
thumbnail: 'http://static.codeceo.com/images/2018/12/1.png'
---

<div>   
<h2>背景</h2>
<p>前段时间，我们的项目组在帮客户解决一些操作系统安全领域的问题，涉及到windows，Linux，macOS三大操作系统平台。无论什么操作系统，本质上都是一个软件，任何软件在一开始设计的时候，都不能百分之百的满足人们的需求，所以操作系统也是一样，为了尽可能的满足人们需求，不得不提供一些供人们定制操作系统的机制。当然除了官方提供的一些机制，也有一些黑魔法，这些黑魔法不被推荐使用，但是有时候面对具体的业务场景，可以作为一个参考的思路。</p>
<h2>Linux中常见的拦截过滤</h2>
<p>本文着重介绍Linux平台上常见的拦截：</p>
<ol>
<li>用户态动态库拦截。</li>
<li>内核态系统调用拦截。</li>
<li>堆栈式文件系统拦截。</li>
<li>inline hook拦截。</li>
<li>LSM(Linux Security Modules)</li>
</ol>
<h2>动态库劫持</h2>
<p>Linux上的动态库劫持主要是基于LD_ PRELOAD环境变量，这个环境变量的主要作用是改变动态库的加载顺序，让用户有选择的载入不同动态库中的相同函数。但是使用不当就会引起严重的安全问题，我们可以通过它在主程序和动态连接库中加载别的动态函数，这就给我们提供了一个机会，向别人的程序注入恶意的代码。</p>
<p>假设有以下用户名密码验证的函数：</p>
<pre class="brush: c; gutter: true; first-line: 1">#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int main(int argc, char **argv)
&#123;
char passwd[] = "password";
if (argc < 2) &#123;
printf("Invalid argc!\n");
return;
&#125;
if (!strcmp(passwd, argv[1])) &#123;
printf("Correct Password!\n");
return;
&#125;
printf("Invalid Password!\n");
&#125;</pre>
<p>我们再写一段hookStrcmp的程序，让这个比较永远正确。</p>
<pre class="brush: c; gutter: true; first-line: 1">#include <stdio.h>
int strcmp(const char *s1, const char *s2)
&#123;
/* 永远返回0，表示两个字符串相等 */
return 0;
&#125;</pre>
<p>依次执行以下命令，就会使我们的hook程序先执行。</p>
<pre class="brush: c; gutter: true; first-line: 1">gcc -Wall -fPIC -shared -o hookStrcmp.so hookStrcmp.c
export LD_PRELOAD=”./hookStrcmp.so</pre>
<p>结果会发现，我们自己写的strcmp函数优先被调用了。这是一个最简单的劫持 ，但是如果劫持了类似于geteuid/getuid/getgid，让其返回0，就相当于暴露了root权限。所以为了安全起见，一般将LD_ PRELOAD环境变量禁用掉。</p>
<h2>Linux系统调用劫持</h2>
<p>最近发现在4.4.0的内核中有513多个系统调用(很多都没用过)，系统调用劫持的目的是改变系统中原有的系统调用，用我们自己的程序替换原有的系统调用。Linux内核中所有的系统调用都是放在一个叫做sys_ call _table的内核数组中，数组的值就表示这个系统调用服务程序的入口地址。整个系统调用的流程如下：</p>
<p><img class="aligncenter size-full wp-image-56629" title="1" src="http://static.codeceo.com/images/2018/12/1.png" alt width="974" height="652" referrerpolicy="no-referrer"></p>
<p>当用户态发起一个系统调用时，会通过80软中断进入到syscall hander，进而进入全局的系统调用表sys_ call _table去查找具体的系统调用，那么如果我们将这个数组中的地址改成我们自己的程序地址，就可以实现系统调用劫持。但是内核为了安全，对这种操作做了一些限制：</p>
<ol>
<li>sys_ call _table的符号没有导出，不能直接获取。</li>
<li>sys_ call _table所在的内存页是只读属性的，无法直接进行修改。</li>
</ol>
<p>对于以上两个问题，解决方案如下（方法不止一种）：</p>
<ol>
<li>获取sys<em> call </em>table的地址 ：grep sys _ call _table /boot/System.map-uname -r</li>
<li>控制页表只读属性是由CR0寄存器的WP位控制的，只要将这个位清零就可以对只读页表进行修改。</li>
</ol>
<div>
<pre class="brush: c; gutter: true; first-line: 1">/* make the page writable */
int make_rw(unsigned long address)
&#123;
unsigned int level;
pte_t *pte = lookup_address(address, &level);//查找虚拟地址所在的页表地址
pte->pte |= _PAGE_RW;//设置页表读写属性
return 0;
&#125;</pre>
</div>
<div>
<pre class="brush: c; gutter: true; first-line: 1">/* make the page write protected */
int make_ro(unsigned long address)
&#123;
unsigned int level;
pte_t *pte = lookup_address(address, &level);
pte->pte &= ~_PAGE_RW;//设置只读属性
return 0;
&#125;</pre>
</div>
<h3>开始替换系统调用</h3>
<p>本文实现的是对 ls这个命令对应的系统调用，系统调用号是 _ NR _getdents。</p>
<pre class="brush: c; gutter: true; first-line: 1">static int syscall_init_module(void)
&#123;
orig_getdents = sys_call_table[__NR_getdents];
make_rw((unsigned long)sys_call_table); //修改页属性
sys_call_table[__NR_getdents] = (unsigned long *)hacked_getdents; //设置新的系统调用地址
make_ro((unsigned long)sys_call_table);
return 0;
&#125;</pre>
<h3>恢复原状</h3>
<pre class="brush: c; gutter: true; first-line: 1">static void syscall_cleanup_module(void)
&#123;
printk(KERN_ALERT "Module syscall unloaded.\n");
make_rw((unsigned long)sys_call_table);
sys_call_table[__NR_getdents] = (unsigned long *)orig_getdents;
make_ro((unsigned long)sys_call_table);
&#125;</pre>
<p>使用Makefile编译，insmod插入内核模块后，再执行ls时，就会进入到我们的系统调用，我们可以在hook代码中删掉某些文件，ls就不会显示这些文件，但是这些文件还是存在的。</p>
<h2>堆栈式文件系统</h2>
<p>Linux通过vfs虚拟文件系统来统一抽象具体的磁盘文件系统，从上到下的IO栈形成了一个堆栈式。通过对内核源码的分析，以一次读操作为例，从上到下所执行的流程如下：</p>
<p><img class="aligncenter size-full wp-image-56630" title="2" src="http://static.codeceo.com/images/2018/12/2.png" alt width="974" height="897" referrerpolicy="no-referrer"></p>
<p>内核中采用了很多c语言形式的面向对象，也就是函数指针的形式，例如read是vfs提供用户的接口，具体底下调用的是ext2的read操作。我们只要实现VFS提供的各种接口，就可以实现一个堆栈式文件系统。Linux内核中已经集成了一些堆栈式文件系统，例如Ubuntu在安装时会提醒你是否需要加密home目录，其实就是一个堆栈式的加密文件系统（eCryptfs），原理如下：</p>
<p><img class="aligncenter size-full wp-image-56631" title="3" src="http://static.codeceo.com/images/2018/12/3.png" alt width="974" height="720" referrerpolicy="no-referrer"></p>
<p>实现了一个堆栈式文件系统，相当于所有的读写操作都会进入到我们的文件系统，可以拿到所有的数据，就可以进行做一些拦截过滤。</p>
<p>以下是我实现的一个最简单的堆栈式文件系统，实现了最简单的打开、读写文件，麻雀虽小但五脏俱全。</p>
<p><a href="https://github.com/wangzhangjun/wzjfs" target="_blank">https://github.com/wangzhangjun/wzjfs</a></p>
<h2>inline hook</h2>
<p>我们知道内核中的函数不可能把所有功能都在这个函数中全部实现，它必定要调用它的下层函数。如果这个下层函数可以得到我们想要的过滤信息内容，就可以把下层函数在上层函数中的offset替换成新的函数的offset，这样上层函数调用下层函数时，就会跳到新的函数中，在新的函数中做过滤和劫持内容的工作。所以从原理上来说，inline hook可以想hook哪里就hook哪里。</p>
<p><img class="aligncenter size-full wp-image-56632" title="4" src="http://static.codeceo.com/images/2018/12/4.png" alt width="974" height="725" referrerpolicy="no-referrer"></p>
<h3>inline hook 有两个重要的问题：</h3>
<ol>
<li>如何定位hook点。</li>
<li>如何注入hook函数入口。</li>
</ol>
<h3>对于第一个问题:</h3>
<p>需要有一点的内核源码经验，比如说对于read操作，源码如下：</p>
<p><img class="aligncenter size-full wp-image-56633" title="5" src="http://static.codeceo.com/images/2018/12/5.png" alt width="974" height="437" referrerpolicy="no-referrer"></p>
<p>在这里当发起read系统调用后，就会进入到sys<em> read,在sys</em> read中会调用vfs<em> read函数，在vfs</em> read的参数中正好有我们需要过滤的信息，那么就可以把vfs_ read当做一个hook点。</p>
<h3>对于第二个问题:</h3>
<p>如何Hook？这里介绍两种方式：</p>
<p>第一种方式：直接进行二进制替换，将call指令的操作数替换为hook函数的地址。</p>
<p><img class="aligncenter size-full wp-image-56634" title="6" src="http://static.codeceo.com/images/2018/12/6.png" alt width="974" height="275" referrerpolicy="no-referrer"></p>
<p>第二种方式：Linux内核提供的kprobes机制。</p>
<p>其原理是在hook点注入int 3(x86)的机器码，让cpu运行到这里的时候会触发sig<em> trap信号，然后将用户自定义的hook函数注入到sig</em> trap的回调函数中，达到触发hook函数的目的。这个其实也是调试器的原理。</p>
<h2>LSM</h2>
<p>LSM是Linux Secrity Module的简称，即linux安全模块。是一种通用的Linux安全框架，具有效率高，简单易用等特点。原理如下：</p>
<p><img class="aligncenter size-full wp-image-56635" title="7" src="http://static.codeceo.com/images/2018/12/7.png" alt width="974" height="908" referrerpolicy="no-referrer"></p>
<p>LSM在内核中做了以下工作：</p>
<ol>
<li>在特定的内核数据结构中加入安全域。</li>
<li>在内核源代码中不同的关键点插入对安全钩子函数的调用。</li>
<li>加入一个通用的安全系统调用。</li>
<li>提供了函数允许内核模块注册为安全模块或者注销。</li>
<li>将capabilities逻辑的大部分移植为一个可选的安全模块,具有可扩展性。</li>
</ol>
<h2>适用场景</h2>
<p>对于以上几种Hook方式，有其不同的应用场景。</p>
<ol>
<li>动态库劫持不太完全，劫持的信息有可能满足不了我们的需求，还有可能别人在你之前劫持了，一旦禁用LD_ PRELOAD就失效了。</li>
<li>系统调用劫持，劫持的信息有可能满足不了我们的需求，例如不能获取struct file结构体，不能获取文件的绝对路径等。</li>
<li>堆栈式文件系统，依赖于Mount,可能需要重启系统。</li>
<li>inline hook，灵活性高，随意Hook，即时生效无需重启，但是在不同内核版本之间通用性差，一旦某些函数发生了变化，Hook失效。</li>
<li>LSM，在早期的内核中，只能允许一个LSM内核模块加载，例如加载了SELinux，就不能加载其他的LSM模块，在最新的内核版本中不存在这个问题。</li>
</ol>
<h2>总结</h2>
<p>篇幅有限，本文只是介绍了Linux上的拦截技术，后续有机会可以一起探讨windows和macOS上的拦截技术。事实上类似的审计HOOK放到任何一个系统中都是刚需，不只是kernel，我们可以看到越来越多的vm和runtime甚至包括很多web组件、前端应用都提供了更灵活的hook方式，这是透明化和实时性两个安全大趋势下最常见的解决方案。</p>


<a id="soft-link" name="soft-link" href="http://www.codeceo.com/article/undefined"></a>




<!--开源软件资源链接-->
<!--开源软件资源链接结束-->







  
</div>
            
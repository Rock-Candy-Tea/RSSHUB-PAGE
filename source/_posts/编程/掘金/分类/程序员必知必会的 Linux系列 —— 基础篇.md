
---
title: '程序员必知必会的 Linux系列 —— 基础篇'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6a0252621a554bf6afef2f4011e8fe60~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 27 Mar 2021 23:39:16 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6a0252621a554bf6afef2f4011e8fe60~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">1. Linux</h2>
<ul>
<li>Linux是一套免费使用和自由传播的类Unix操作系统</li>
<li>在服务器端领域和嵌入式领域有非常广泛的应用</li>
</ul>
<h2 data-id="heading-1">2.版本</h2>
<p>分为内核版本和发型版本</p>
<ul>
<li><a href="https://www.kernel.org/" target="_blank" rel="nofollow noopener noreferrer">kernel</a></li>
<li>各个厂商会制作自己的发行版本
<ul>
<li>redhat</li>
<li>CentOS</li>
<li>ubuntu</li>
<li>fedora</li>
</ul>
</li>
</ul>
<h2 data-id="heading-2">3. Linux与Windows的不同</h2>
<ul>
<li>Linux严格区分大小写</li>
<li>Linux中所有的内容以文件形式保存，包括硬件、用户和文件。</li>
<li>Linux不靠扩展名区分文件类型，是靠权限来区分，但是有一些约定的扩展名，是给管理员看的
<ul>
<li>压缩包 <code>.gz</code> <code>.bz2</code> <code>.tar.bz2</code> <code>.tgz</code></li>
<li>二进制文件 <code>.rpm</code></li>
<li>网页文件 <code>.html .php</code></li>
<li>脚本文件 <code>.sh</code></li>
<li>配置文件 <code>.conf</code></li>
</ul>
</li>
<li>Windows下的程序不能直接在Linux中安装和运行</li>
<li>Linux更多使用字符界面
<ul>
<li>占用的系统资源更少</li>
<li>减少了出错和被攻击的可能性，会让系统更稳定</li>
</ul>
</li>
</ul>
<h2 data-id="heading-3">3. 购买服务器</h2>
<ul>
<li><a href="https://www.aliyun.com/" target="_blank" rel="nofollow noopener noreferrer">阿里云 ECS</a></li>
<li><a href="https://cloud.tencent.com/product/cvm" target="_blank" rel="nofollow noopener noreferrer">腾讯云 CVM</a></li>
<li><a href="https://aws.amazon.com/cn/" target="_blank" rel="nofollow noopener noreferrer">亚马逊 AWS</a></li>
<li><a href="https://cloud.baidu.com/" target="_blank" rel="nofollow noopener noreferrer">百度云</a></li>
</ul>
<h2 data-id="heading-4">4. 连接服务器</h2>
<ul>
<li>git bash</li>
<li>mac shell</li>
<li><a href="http://img.golderbrother.cn/xftp4.zip" target="_blank" rel="nofollow noopener noreferrer">xshell4</a></li>
<li><a href="http://img.golderbrother.cn/xftp4.zip" target="_blank" rel="nofollow noopener noreferrer">xftp4</a></li>
</ul>
<h2 data-id="heading-5">5.linux常用命令</h2>
<h3 data-id="heading-6">5.1 常见目录</h3>

















































































<table><thead><tr><th align="left">目录</th><th align="left">用途</th></tr></thead><tbody><tr><td align="left">/</td><td align="left">根目录</td></tr><tr><td align="left">/boot</td><td align="left">启动目录，启动相关文件</td></tr><tr><td align="left">/dev</td><td align="left">设备文件</td></tr><tr><td align="left">/etc</td><td align="left">配置文件</td></tr><tr><td align="left">/home</td><td align="left">普通用户的家目录,可以操作</td></tr><tr><td align="left">/lib</td><td align="left">系统库保存目录</td></tr><tr><td align="left">/mnt</td><td align="left">移动设备挂载目录</td></tr><tr><td align="left">/media</td><td align="left">光盘挂载目录</td></tr><tr><td align="left">/misc</td><td align="left">磁带机挂载目录</td></tr><tr><td align="left">/root</td><td align="left">超级用户的家目录,可以操作</td></tr><tr><td align="left">/tmp</td><td align="left">临时目录,可以操作</td></tr><tr><td align="left">/proc</td><td align="left">正在运行的内核信息映射, 主要输出进程信息、内存资源信息和磁盘分区信息等等</td></tr><tr><td align="left">/sys</td><td align="left">硬件设备的驱动程序信息</td></tr><tr><td align="left">/var</td><td align="left">变量</td></tr><tr><td align="left">/bin</td><td align="left">普通的基本命令，如ls,chmod等,一般的用户也都可以使用</td></tr><tr><td align="left">/sbin</td><td align="left">基本的系统命令，如shutdown，reboot，用于启动系统，修复系统,只有管理员才可以运行</td></tr><tr><td align="left">/usr/bin</td><td align="left">是你在后期安装的一些软件的运行脚本</td></tr><tr><td align="left">/usr/sbin</td><td align="left">放置一些用户安装的系统管理的必备程序</td></tr></tbody></table>
<h3 data-id="heading-7">5.2 命令基本格式</h3>
<h4 data-id="heading-8">5.2.1 命令提示符</h4>
<pre><code class="hljs language-sh copyable" lang="sh">[root@james ~]<span class="hljs-comment">#</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>root 当前登录用户</li>
<li>localhost 主机名</li>
<li>~ 当前工作目录,默认是当前用户的家目录，root就是/root,普通用户是 /home/用户名</li>
<li>提示符 超级用户是 #,普通用户是$</li>
</ul>
<h4 data-id="heading-9">5.2.2 命令格式</h4>
<ul>
<li>命令 [选项] [参数]</li>
<li>当有多个选项时，可以写在一起</li>
<li>一般参数有简化和完整写法两种 <code>-a</code> 与 <code>--all</code>等效</li>
</ul>
<h4 data-id="heading-10">5.2.3 ls</h4>
<ul>
<li>查询目录中的内容</li>
<li>ls [选项] [文件或者目录]</li>
<li>选项
<ul>
<li>-a 显示所有文件，包括隐藏文件</li>
<li>-l 显示详细信息</li>
<li>-d 查看目录本身的属性而非子文件 ls /etc/</li>
<li>-h 人性化的方式显示文件大小</li>
</ul>
</li>
<li>默认当前目录下的文件列表</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">ls -l
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-11">5.2.3.1 -l</h5>
<p>显示详细信息</p>
<pre><code class="hljs language-sh copyable" lang="sh">drwxr-xr-x  root  root   800 Sep 16 00:19 logs
<span class="copy-code-btn">复制代码</span></code></pre>





















<table><thead><tr><th align="left">drwxr-xr-x</th><th align="left">root</th><th align="left">root</th><th align="left">800</th><th align="left">Sep 16 00:19</th><th align="left">logs</th></tr></thead><tbody><tr><td align="left">文件类型和权限</td><td align="left">所有者</td><td align="left">所属组</td><td align="left">文件大小</td><td align="left">最后修改时间</td><td align="left">文件名</td></tr></tbody></table>
<h3 data-id="heading-12">5.3 文件处理命令</h3>
<h4 data-id="heading-13">5.3.1 mkdir</h4>
<ul>
<li>建立目录 make directory</li>
<li>mkdir -p [目录名]
<ul>
<li>-p 递归创建</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">mkdir -p hello
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-14">5.3.2 cd</h4>
<ul>
<li>切换所在目录 change directory</li>
<li>cd [目录]
<ul>
<li>~ 家目录</li>
<li>. 当前目录</li>
<li>.. 上级目录</li>
</ul>
</li>
<li>相对路径是参照当前所在目录</li>
<li>绝对路径是从根目录开始</li>
<li>按TAB键可以补全命令和目录</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">cd hello
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-15">5.3.3 pwd</h4>
<ul>
<li>显示当前目录 pwd</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">pwd
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-16">5.3.4 rmdir</h4>
<ul>
<li>删除目录 remove empty directory</li>
<li>rmdir [目录名]</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">rmdir hello
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-17">5.3.5 rm</h4>
<ul>
<li>删除文件或者目录 remove</li>
<li>rm [文件或者目录]
<ul>
<li>-r 删除目录</li>
<li>-f 强制删除</li>
</ul>
</li>
<li>rm -rf 文件或者目录] 递归强制删除所有目录</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">rm -rf hello
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-18">5.3.6 cp</h4>
<ul>
<li>copy 复制命令</li>
<li>copy [源文件或者目录] [目标文件]
<ul>
<li>-r 复制目录,默认是复制文件</li>
<li>-i 会在复制文件的时候给提示,如果复制的目标文件存在,会给你提示是否要覆盖</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">mkdir afolder
mkdir bfolder
cd afolder/
touch <span class="hljs-number">1.</span>txt
cp <span class="hljs-number">1.</span>txt ~<span class="hljs-regexp">/bfolder/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-19">5.3.7 mv</h4>
<ul>
<li>移动文件或者改名 move</li>
<li>mv [源文件或者目录] [目标文件]</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">mv <span class="hljs-number">1.</span>txt <span class="hljs-number">11.</span>txt
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-20">5.3.8 ln</h4>
<ul>
<li>链接命令,生成链接文件 <code>link</code></li>
<li>ln -s [源文件] [目标文件]
<ul>
<li>-s 创建软链接</li>
</ul>
</li>
<li>类似Windows快捷方式</li>
<li>修改任意一个文件，另一个都会改变</li>
<li>删除源文件，软链接不能使用</li>
<li>软链接源文件必须写绝对路径</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"># ln -s /root/bfolder/<span class="hljs-number">11.</span>txt <span class="hljs-number">22.</span>txt
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-21">5.4 文件搜索命令</h3>
<h4 data-id="heading-22">5.4.1 locate</h4>
<ul>
<li>在后台数据库中按文件名搜索，速度比较快</li>
<li>数据保存在<code>/var/lib/mlocate/mlocate.db</code>后台数据库，每天更新一次</li>
<li>可以<code>updatedb</code>命令立刻更新数据库</li>
<li>只能搜索文件名</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">yum  -y install mlocate
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-23">5.4.2 whereis</h4>
<ul>
<li>
<p>搜索命令所在路径以及帮助文档所在位置</p>
</li>
<li>
<p>whereis 命令名</p>
<pre><code class="copyable">whereis ls
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>-b 只查找可执行文件</li>
<li>-m 只查找帮助文件</li>
</ul>
</li>
<li>
<p>可以查看Shell自带的命令，如 <code>whereis cd</code></p>
</li>
</ul>
<h4 data-id="heading-24">5.4.3 which</h4>
<ul>
<li>可以看到别名 <code>which ls</code></li>
<li>能看到的都是外部安装的命令</li>
<li>无法查看Shell自带的命令，如 <code>which cd</code></li>
</ul>
<h4 data-id="heading-25">5.4.4 环境变量</h4>
<pre><code class="copyable">/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>定义的是系统搜索命令的路径</li>
<li>echo $PATH</li>
</ul>
<h4 data-id="heading-26">5.4.5 find</h4>
<ul>
<li>文件搜索命令</li>
<li>find [搜索范围] [搜索条件]</li>
</ul>
<h5 data-id="heading-27">5.4.5.1 按名称搜索</h5>
<ul>
<li>
<p>避免大范围的搜索，会非常消耗系统资源</p>
<pre><code class="hljs language-sh copyable" lang="sh">find / -name 11.txt
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h5 data-id="heading-28">5.4.5.2 通配符</h5>
<ul>
<li>find是在系统当中搜索符合条件的文件名，如果需要匹配，使用通配符匹配，通配符是完全匹配</li>
<li>通配符
<ul>
<li><code>*</code> 匹配任意内容</li>
<li><code>?</code> 匹配任意一个字符</li>
<li><code>[]</code> 匹配任意一个中括号内的字符</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-sh copyable" lang="sh"><span class="hljs-comment"># touch abc.txt</span>
<span class="hljs-comment"># find . -name "ab[cdef].txt"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-29">5.4.5.3 -i</h5>
<ul>
<li>不区分大小写</li>
</ul>
<pre><code class="hljs language-sh copyable" lang="sh">find . -iname <span class="hljs-string">"Ab[cdef].txt"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-30">5.4.5.4 -user</h5>
<ul>
<li>按所有者进行搜索</li>
</ul>
<pre><code class="hljs language-sh copyable" lang="sh">find /root -user root
find /root -nouser
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-31">5.4.5.5 按时间搜索</h5>
<pre><code class="hljs language-sh copyable" lang="sh">find . -mtime +5
<span class="copy-code-btn">复制代码</span></code></pre>





















<table><thead><tr><th align="left">参数</th><th align="left">含义</th></tr></thead><tbody><tr><td align="left">atime</td><td align="left">文件访问时间</td></tr><tr><td align="left">ctime</td><td align="left">改变文件属性</td></tr><tr><td align="left">mtime</td><td align="left">修改文件内容</td></tr></tbody></table>





















<table><thead><tr><th align="left">参数</th><th align="left">含义</th></tr></thead><tbody><tr><td align="left">-5</td><td align="left">5天内修改的文件</td></tr><tr><td align="left">5</td><td align="left">5天前当前修改的文件</td></tr><tr><td align="left">+5</td><td align="left">5天前修改的文件</td></tr></tbody></table>
<h5 data-id="heading-32">5.4.5.6 按大小搜索</h5>
<ul>
<li>k小写,M大写</li>
</ul>
<pre><code class="hljs language-sh copyable" lang="sh">find . -size +0k
<span class="copy-code-btn">复制代码</span></code></pre>

























<table><thead><tr><th align="left">参数</th><th align="left">含义</th></tr></thead><tbody><tr><td align="left">-8k</td><td align="left">小于8K</td></tr><tr><td align="left">8k</td><td align="left">等于8K</td></tr><tr><td align="left">+8k</td><td align="left">大于8K</td></tr><tr><td align="left">+8M</td><td align="left">小于8M</td></tr></tbody></table>
<h5 data-id="heading-33">5.4.5.7 综合应用</h5>
<pre><code class="hljs language-sh copyable" lang="sh">find /tmp -size +10k -a -size -20k
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>查找/etc目录下，大于10KB并且小于20KB的文件</li>
<li>-a and 逻辑与，两个条件都满足</li>
<li>-o or 逻辑或，两个条件满足一个就可以</li>
</ul>
<pre><code class="hljs language-sh copyable" lang="sh">find /tmp -size +10k -a -size -20k -<span class="hljs-built_in">exec</span> ls -lh &#123;&#125; \;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>exec 对上个命令的结果进行操作</li>
</ul>
<h5 data-id="heading-34">5.4.5.9 grep</h5>
<ul>
<li>在文件当中匹配符合条件的字符串
<ul>
<li><code>-i</code> 忽略大小写</li>
<li><code>-v</code> 排除指定字符串</li>
</ul>
</li>
<li>find命令，在系统当中搜索符合条件的文件名，如果需要匹配，使用通配符匹配，通配符是完全匹配</li>
<li>grep命令 在文件当中搜索符合条件的字符串，如果需要匹配，使用正则表达式进行匹配，正则表达式时包含匹配</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">vi a.txt
grep b a.txt
grep -v b a.txt
grep -i f a.txt
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-35">5.5 压缩与解压缩命令</h3>
<h4 data-id="heading-36">5.5.1 zip格式</h4>
<ul>
<li>压缩文件或目录,是一种压缩格式</li>
</ul>





















<table><thead><tr><th align="left">功能</th><th align="left">命令</th></tr></thead><tbody><tr><td align="left">压缩文件</td><td align="left">zip 压缩文件名.zip 源文件</td></tr><tr><td align="left">压缩目录</td><td align="left">zip -r 压缩目录名.zip 源目录</td></tr><tr><td align="left">解压</td><td align="left">unzip 压缩目录名.zip</td></tr></tbody></table>
<pre><code class="hljs language-js copyable" lang="js">yum install -y unzip zip

mkdir book
touch book/<span class="hljs-number">1.</span>txt
touch book/<span class="hljs-number">2.</span>txt
zip -r book.zip book
rm -rf book/ rmdir book
unzip book.zip
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-37">5.5.2 gzip</h4>
<ul>
<li>gzip为高压，可以把文件压缩得更小</li>
<li>gzip命令不支持目录</li>
</ul>



































<table><thead><tr><th align="left">命令</th><th align="left">示例</th><th align="left">含义</th></tr></thead><tbody><tr><td align="left">gzip 源文件</td><td align="left">gzip book.txt</td><td align="left">压缩为.gz格式的压缩文件，源文件会消失</td></tr><tr><td align="left">gzip -c 源文件 > 压缩文件</td><td align="left">gzip -c book.txt > book.txt.gz</td><td align="left">压缩为.gz格式的压缩文件，源文件不会消失</td></tr><tr><td align="left">gzip -r 目录</td><td align="left">gzip -r book</td><td align="left">把目录下的每个子文件都变成压缩包，并删除原文件，当前目录无变化</td></tr><tr><td align="left">gzip -d 压缩文件名</td><td align="left">gzip -d 1.txt.gz</td><td align="left">解压缩文件,不保留压缩包</td></tr><tr><td align="left">gunzip 压缩文件</td><td align="left">gunzip 2.txt.gz</td><td align="left">解压缩文件,也不保留压缩包</td></tr></tbody></table>
<ul>
<li>压缩是压缩目录下的文件</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">touch book.txt
mkdir book
touch book/<span class="hljs-number">1.</span>txt
touch book/<span class="hljs-number">2.</span>txt
gzip book.txt <span class="hljs-comment">//源文件会消失</span>
gzip -c <span class="hljs-number">1.</span>txt > <span class="hljs-number">1.</span>txt.gz <span class="hljs-comment">//源文件不消失</span>
gzip book.txt  <span class="hljs-comment">//压缩为.gz格式文件，源文件会消失</span>
gzip -r book <span class="hljs-comment">//把目录下的每个子文件都变成压缩包</span>
cd book
gzip -d <span class="hljs-number">1.</span>txt.gz  <span class="hljs-comment">//解压缩文件,不保留压缩包</span>
gunzip <span class="hljs-number">2.</span>txt.gz 
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-38">5.5.3 tar</h4>
<ul>
<li>
<p>打包命令,只打包并不压缩</p>
</li>
<li>
<pre><code class="copyable">tar -cvf
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打包文件名 源文件</p>
<ul>
<li>-c 打包</li>
<li>-v 显示过程</li>
<li>-f 指定打包后的文件名</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">tar -cvf book.tar book    <span class="hljs-comment">//会打包出一个book.tar文件</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>x 解开包</p>
<pre><code class="hljs language-sh copyable" lang="sh">tar -xvf book.tar 
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h4 data-id="heading-39">5.5.4 tar.gz压缩格式</h4>
<ul>
<li><code>zip</code>可以压缩目录但压缩效率不高,<code>gzip</code>压缩效率高但不支持目录</li>
<li>可以先打包为<code>.tar</code>格式，再压缩为<code>.gz</code>格式 -c 压缩为.tar.gz格式 -x 解压缩.tar.gz格式</li>
</ul>




















<table><thead><tr><th align="left">命令</th><th align="left">示例</th><th align="left">含义</th></tr></thead><tbody><tr><td align="left">tar -zcvf 压缩包名 <code>.tar.gz</code>源文件</td><td align="left">tar -zcvf book.tar.gz book</td><td align="left">可以先打包为<code>.tar</code>格式，再压缩为<code>.gz</code>格式</td></tr><tr><td align="left">tar -zxvf 压缩包名.tar.gz</td><td align="left">tar -zxvf book.tar.gz</td><td align="left">解压tar.gz压缩包</td></tr></tbody></table>
<pre><code class="hljs language-js copyable" lang="js">tar -zcvf book.tar.gz book
tar -zxvf book.tar.gz
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-40">5.6 关机和重启命令</h3>
<h4 data-id="heading-41">5.6.1 shutdown</h4>
<ul>
<li>shutdown 关机命令
<ul>
<li>-c 取消前一个关机命令</li>
<li>-h 关机</li>
<li>-r 重启</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">shutdown -r <span class="hljs-number">06</span>:<span class="hljs-number">00</span>
shutdown -c
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-42">5.6.2 init</h4>
<p>关机</p>
<pre><code class="hljs language-js copyable" lang="js">init <span class="hljs-number">0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>重启</p>
<pre><code class="hljs language-js copyable" lang="js">init <span class="hljs-number">6</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-43">5.6.3 logout</h4>
<p>退出登录</p>
<pre><code class="hljs language-sh copyable" lang="sh"><span class="hljs-built_in">logout</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-44">5.7 查看登录用户信息</h3>
<h4 data-id="heading-45">5.7.1 w</h4>
<p>查看登录用户信息</p>
<ul>
<li>USER 登录的用户名</li>
<li>TTY 登录的终端 tty1 本地终端 pts/0远程终端</li>
<li>FROM 登录的IP</li>
<li>LOGIN 登录时间</li>
<li>IDLE 用户闲置时间</li>
<li>JCPU 该终端所有进程占用的时间</li>
<li>PCPU 当前进程所占用的时间</li>
<li>WHAT 正在执行的命令</li>
</ul>
<h4 data-id="heading-46">5.7.2 who</h4>
<ul>
<li>查看登录用户信息
<ul>
<li>USER 登录的用户名</li>
<li>TTY 登录的终端 tty1 本地终端 pts/0远程终端</li>
<li>LOGIN 登录时间（登录的IP）</li>
</ul>
</li>
</ul>
<h4 data-id="heading-47">5.7.3 last</h4>
<ul>
<li>
<p>查看当前登录和过去登录的用户信息</p>
</li>
<li>
<p>默认读取</p>
<pre><code class="copyable">/var/log/wtmp
<span class="copy-code-btn">复制代码</span></code></pre>
<p>文件</p>
<ul>
<li>用户名</li>
<li>登录终端</li>
<li>登录IP</li>
<li>登录时间</li>
<li>退出时间(在线时间)</li>
</ul>
</li>
</ul>
<h4 data-id="heading-48">5.7.4 lastlog</h4>
<ul>
<li>查看所有用户的最后一次登录时间
<ul>
<li>用户名</li>
<li>登录终端</li>
<li>登录IP</li>
<li>最后一次登录时间</li>
</ul>
</li>
</ul>
<h3 data-id="heading-49">5.8 文件查看命令</h3>
<h4 data-id="heading-50">5.8.1 cat</h4>
<ul>
<li>
<p>cat 命令用于连接文件并打印到标准输出设备上。</p>
</li>
<li>
<p>cat [-AbeEnstTuv] [--help] [--version] fileName</p>
</li>
<li>
<p>参数</p>
<ul>
<li>
<p>-n 或 --number：由 1 开始对所有输出的行数编号。</p>
<pre><code class="hljs language-js copyable" lang="js">cat -n textfile1
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
</li>
</ul>
<h4 data-id="heading-51">5.8.2 more</h4>
<ul>
<li>Linux more 命令类似 cat ，不过会以一页一页的形式显示，更方便使用者逐页阅读，而最基本的指令就是按空白键（space）就往下一页显示，按 b 键就会往回（back）一页显示，而且还有搜寻字串的功能（与 vi 相似），使用中的说明文件，请按 h 。</li>
<li>more fileName</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">more  testfile
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-52">5.8.3 head</h4>
<ul>
<li>用来显示开头某个数量的文字区块</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">head -<span class="hljs-number">5</span> readme.txt
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-53">5.8.4 tail</h4>
<ul>
<li>
<p>tail命令可用于查看文件的内容</p>
</li>
<li>
<p>有一个常用的参数 -f 常用于查阅正在改变的日志文件。</p>
</li>
<li>
<p>tail [参数] [文件]</p>
</li>
<li>
<p>参数</p>
<ul>
<li>
<p>-f 循环读取</p>
</li>
<li>
<p>-n<行数> 显示文件的尾部 n 行内容</p>
<pre><code class="hljs language-js copyable" lang="js">tail -<span class="hljs-number">5</span> mail.txt
tail -f access.log
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
</li>
</ul>
<h4 data-id="heading-54">5.8.5 第二页</h4>
<pre><code class="hljs language-js copyable" lang="js">　head -<span class="hljs-number">10</span> file | tail -<span class="hljs-number">5</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-55">6. 硬件设备文件名</h2>
<ul>
<li>只要插入硬盘，Linux会自动检测和分配名称</li>
<li>一个硬盘可以分成多个分区，每个分区都会有一个系统分配的名称</li>
<li>第一块SCSI硬盘名称叫<code>sda</code>,它的第一个分区叫<code>sda1</code></li>
<li>第一块虚拟化环境的磁盘是<code>vda</code>,它的第一个分区叫<code>vda1</code></li>
<li><code>df(disk free)</code> 命令用于显示目前在 Linux 系统上的文件系统磁盘使用情况统计</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">df -h
<span class="copy-code-btn">复制代码</span></code></pre>





















<table><thead><tr><th align="left">硬件</th><th align="left">设备文件名</th></tr></thead><tbody><tr><td align="left">IDE硬盘</td><td align="left">/dev/hd[a-d]</td></tr><tr><td align="left">SCSI/SATA/USB硬盘</td><td align="left">/dev/sd[a-p]</td></tr><tr><td align="left">virtio磁盘</td><td align="left">/dev/vd[a-p]</td></tr></tbody></table>
<h3 data-id="heading-56">6.1 IDE硬盘接口</h3>
<p><img alt="idedisk" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6a0252621a554bf6afef2f4011e8fe60~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-57">6.2 SCSI硬盘接口</h3>
<p><img alt="SCSIdisk" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/559e33c334d74a95af17ac1ca0195388~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-58">6.3 SATA硬盘接口</h3>
<p><img alt="satadisk" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/713953af6359467eab12bdefc57b1838~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-59">7. 分区</h2>
<p><img alt="diskformat2" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fd05c105a32a444fbd0f93689a65c67b~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>磁盘分区是使用分区编辑器在磁盘上划分几个逻辑部分</li>
<li>磁盘一旦划分成多个分区，不同类的目录与文件可以存储进不同的分区内</li>
</ul>
<h2 data-id="heading-60">8. 挂载点</h2>
<ul>
<li>为了让Linux系统中可以访问这些分区，需要把这些分区挂载到对应的目录上</li>
<li>在Linux中是把目录称为<code>挂载点</code></li>
<li>把目录和分区链接在一起的过程成为<code>挂载</code></li>
<li><code>/</code>为根目录，必须挂载到一个分区上，默认所有子目录都会写入这个分区</li>
<li>同一级目录下面的所有子目录可以有自己的独立存储空间</li>
<li>必须有的分区
<ul>
<li>/ 根分区</li>
<li>swap分区(交换分区，虚拟内存，一般为内存的2倍，不要超过2G)</li>
</ul>
</li>
<li>推荐分区
<ul>
<li>/boot (启动分区,200M) 单独分区，避免分区写满造成系统无法启动</li>
</ul>
</li>
</ul>
<h3 data-id="heading-61">9.1 挂载示例</h3>
<ul>
<li><code>/dev/sd2</code>挂载到了 <code>/</code>目录上,也就是说向<code>/</code>目录下在写文件就是往<code>/dev/sd2</code>分区里写文件</li>
<li><code>/dev/sd1</code>挂载到了 <code>/boot</code>目录上,也就是说向<code>/boot</code>目录下在写文件就是往<code>/dev/sd1</code>分区里写文件</li>
<li><code>/dev/sd3</code>挂载到了 <code>//home</code>目录上,也就是说向<code>//home</code>目录下在写文件就是往<code>/dev/sd3</code>分区里写文件</li>
</ul>
<p><img alt="mount" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3bf3bdf9e50b4f65bd6636fdcfca8a95~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            
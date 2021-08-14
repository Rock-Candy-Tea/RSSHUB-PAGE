
---
title: 'Iptables防火墙配置'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb952e83bd2c499188985ab550791c28~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 13 Aug 2021 06:51:41 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb952e83bd2c499188985ab550791c28~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第13天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h4 data-id="heading-0">一、防火墙简介</h4>
<p>1、功能：</p>
<pre><code class="copyable">    1）通过源端口，源IP地址，源MAC地址，包中特定标记和目标端口，IP，MAC来确定数据包是否可以通过防火墙

    2）分割内网和外网【附带的路由器的功能】

    3）划分要被保护的服务器

如果Linux服务器启用了防火墙，SELinux等的防护措施，那么，他的安全级别可以达到B2[原来是C2]

<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、防火墙分类</p>
<pre><code class="copyable">    1）数据包过滤【绝大多数的防火墙】

            分析IP地址，端口和MAC是否符合规则，如果符合，接受

    2）代理服务器
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3、防火墙的限制</p>
<pre><code class="copyable">    1）防火墙不能有效防止病毒，所以防火墙对病毒攻击基本无效，但是对木马还是有一定的限制作用的。

    2）防火墙一般不设定对内部[服务器本机]访问规则，所以对内部攻击无效
<span class="copy-code-btn">复制代码</span></code></pre>
<p>【附】现当今的杀毒软件对病毒的识别率大约在30%左右。也就是说，大部分的病毒是杀毒软件并不认识的！</p>
<p>4、防火墙配置原则【交叉使用】</p>
<pre><code class="copyable">    拒绝所有，逐个允许

    允许所有，逐个拒绝
<span class="copy-code-btn">复制代码</span></code></pre>
<p>【附：】防火墙规则：谁先配置，谁先申请！</p>
<p>5、Linux常见防火墙</p>
<pre><code class="copyable">    2.4/2.6内核        iptables #现在常用的

    2.2内核              ipchains
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-1">二 、iptables防火墙</h4>
<p>1、结构：表-------链--------规则  </p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb952e83bd2c499188985ab550791c28~tplv-k3u1fbpfcp-watermark.image" alt="404231203453.png" loading="lazy" referrerpolicy="no-referrer">
2、表：在iptables中默认有以下三个表</p>
<pre><code class="copyable">     filter表        数据过滤表 #filter过滤，渗透

     NAT表        内网与外网地址转换

     Mangle    特殊数据包标记
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3、链</p>
<pre><code class="copyable"> filter表中： INPUT OUTPUT FORWARD
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">三、iptables基础语法</h4>
<p>1、规则的查看和清楚</p>
<pre><code class="copyable"> iptables [-t表名] [选项]

选项：

    -L    查看

    -F    清除所有规则

    -X    清除自定义链

    -Z    清除所有链统计

    -n    以端口和ip显示

<span class="copy-code-btn">复制代码</span></code></pre>
<p>   
示例：</p>
<pre><code class="copyable">    iptables -t nat -L    #查看nat表中规则

    iptables -L             #查看filter表中规则，不写表名默认查看的是filter表！
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、定义默认策略</p>
<pre><code class="copyable">   iptables  -t 表名  -P 链名 ACCEPT|DROP        #-P（大） 定义默认策略
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实例：</p>
<pre><code class="copyable">    iptables -t filter -P INPUT DROP
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意：不要把自己踢出服务器，所以这条规则应该最后设定。</p>
<p>   
 3、限定IP和网卡接口设置</p>
<pre><code class="copyable">    iptables [-AI 链] [-io 网卡接口] [-p 协议] [-s 源IP] [-d 目标ip] -j 动作
<span class="copy-code-btn">复制代码</span></code></pre>
<p>说明：</p>
<pre><code class="copyable">    -A    追加链规则     #在链规则最后加入此规则

    -I      INPUT 2     #把此规则插入到INPUT链，变成第二条规则

   -D     链 条数         #删除指定链的指定条数防火墙
<span class="copy-code-btn">复制代码</span></code></pre>
<p>示例：</p>
<pre><code class="copyable">    iptables -D INPUT 2 #删除input链上的第二条规则

   -i     eth0 #指定进入接口，要在INPUT链上定义

  -o     eth0 #指定传出接口，要在OUTPUT链上定义

  -p    协议  #[tcp/udp/icmp/all]

  -j     动作  #[ACCEPT|DROP]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实例：</p>
<pre><code class="copyable">      iptables -A INPUT -i lo -j ACCEPT
<span class="copy-code-btn">复制代码</span></code></pre>
<p>允许本机回环网卡通信，在INPUT链</p>
<pre><code class="copyable">      iptables-A INPUT -i eth0 -s 192.168.140.254 -j ACCEPT
<span class="copy-code-btn">复制代码</span></code></pre>
<p>允许254进入eth0</p>
<pre><code class="copyable">      iptables-A INPUT -i eth0 -s 192.168.140.0/24 -j DROP
<span class="copy-code-btn">复制代码</span></code></pre>
<p>拒绝140网段访问  </p>
<p>4、设定端口访问</p>
<pre><code class="copyable">iptables -A INPUT -i eth0 -p all -s源ip --sport 源端口 -d 目标IP --dport 目标端口-j 动作

#一般需要指定的是目标端口，而且一定要设置协议类型！
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实例：</p>
<pre><code class="copyable">iptables -A INPUT -i eth0 -p tcp -s 192.168.140.0/24 --dport 22 -j DROP

iptables -A INPUT -i eth0 -p tcp -s 192.168.140.0/24 --dport 137:139 -j ACCEPT 
 #允许访问137到139端口
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意：指定端口时，协议不能用all，要指定确切协议，如TCP</p>
<p>5、模块调用</p>
<p>-m 模块名 模块选项加载iptables功能模块</p>
<pre><code class="copyable">1） -m state --state ESTABLISHED,RELATED

iptables -A INPUT -i eth0 -m state --state ESTABLISHED,RELATED -j ACCEPT

#state状态模块常见状态ESTABLISHED【联机成功的状态】RELATED【返回包状态】
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2）-m mac --mac-source按照mac地址限制访问</p>
<pre><code class="copyable">iptables -A INPUT -m mac --mac-source aa:bb:cc:dd:ee:ff -j DROP

#拒绝某mac访问
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3）-mstring --string "想要匹配的数据包中字串"</p>
<pre><code class="copyable">iptables -A FORWARD -p udp --dport 53 -m string --string "tencent"--algo kmp -j DROP

#通过dns拒绝QQ登录

#--algo指定字符串模式匹配策略，支持KMP和BM两种字符串搜索算法，任意指定一个即可
<span class="copy-code-btn">复制代码</span></code></pre>
<p>6、简易防火墙实例</p>
<pre><code class="copyable">iptables -F

iptables -A INPUT -i lo -j ACCEPT

iptables -A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT

iptables -A INPUT -p tcp --dport 80 -j ACCEPT

iptables -A INPUT -p tcp --dport 22 -j ACCEPT

#iptables -A INPUT -p tcp --dport 22 -s <IP地址>-j ACCEPT

iptables -A INPUT -p tcp --dport 873 -j ACCEPT

iptables -A INPUT -p tcp --dport 139 -j ACCEPT

iptables -A INPUT -p tcp --dport 21 -j ACCEPT

iptables -P INPUT DROP
<span class="copy-code-btn">复制代码</span></code></pre>
<p>7、防火墙服务开机自启动</p>
<pre><code class="copyable">chkconfig iptables on
<span class="copy-code-btn">复制代码</span></code></pre>
<p>8、防火墙规则开启自启动</p>
<pre><code class="copyable">
1） service iptables save

会把规则保存到/etc/sysconfig/iptables文件中，重启会自动读取
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2） a.手工写防火墙脚本</p>
<pre><code class="hljs language-js copyable" lang="js">如 vi /root/iptables.rule

iptables -A INPUT -i lo -j ACCEPT

iptables -A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT

iptables -A INPUT -p tcp --dport <span class="hljs-number">80</span> -j ACCEPT

iptables -A INPUT -p tcp --dport <span class="hljs-number">22</span> -j ACCEPT

iptables -A INPUT -p tcp --dport <span class="hljs-number">873</span> -j ACCEPT

iptables -A INPUT -p tcp --dport <span class="hljs-number">139</span> -j ACCEPT

iptables -A INPUT -p tcp --dport <span class="hljs-number">21</span> -j ACCEPT

iptables -P INPUT DROP


b.赋予执行权限 chmod <span class="hljs-number">755</span> /root/iptables.rule

c.开机运行 vi/etc/rc.local

d.写入 /root/iptables.rule
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            
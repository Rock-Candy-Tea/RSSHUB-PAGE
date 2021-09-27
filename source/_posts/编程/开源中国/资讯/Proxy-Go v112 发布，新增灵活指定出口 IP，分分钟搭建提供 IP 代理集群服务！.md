
---
title: 'Proxy-Go v11.2 发布，新增灵活指定出口 IP，分分钟搭建提供 IP 代理集群服务！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://img.d1xz.net/d/2021/05/60af8940292f6.jpg_art'
author: 开源中国
comments: false
date: Mon, 27 Sep 2021 16:44:00 GMT
thumbnail: 'https://img.d1xz.net/d/2021/05/60af8940292f6.jpg_art'
---

<div>   
<div class="content">
                                                                                            <p><img alt="国庆节是农历几月几日 国庆节活动意义" src="https://img.d1xz.net/d/2021/05/60af8940292f6.jpg_art" referrerpolicy="no-referrer"></p> 
<p>预祝各位oscer国庆节快乐，goproxy也迎来11.2国庆版本。</p> 
<p style="color:#24292f; text-align:start">新增特性：</p> 
<p style="color:#24292f; text-align:start">1、<code>--bind-ip</code>参数的<code>IP</code>部分，支持指定<code>网卡名称</code>，<code>通配符</code>，还能指定多个，详细说明如下：</p> 
<ul> 
 <li>指定网卡名称，比如：<code>--bind-ip eth0:7777</code>，那么客户端访问<code>7777</code>端口，出口IP就是eth0网卡的IP。</li> 
 <li>网卡名称支持通配符，比如：<code>--bind-ip eth0.*:7777</code>，那么客户端访问<code>7777</code>端口，出口IP就是<code>eth0.</code>开头网卡的IP中随机选择的一个。</li> 
 <li>IP支持通配符，比如：<code>--bind-ip 192.168.?.*:7777</code>，那么客户端访问<code>7777</code>端口，出口IP就是机器所有IP中，匹配<code>192.168.?.*</code>的IP中随机选择的一个。</li> 
 <li>还可以是网卡名称和IP的多个组合，多个使用半角逗号分割，比如：<code>--bind-ip pppoe??,192.168.?.*:7777</code>，那么客户端访问<code>7777</code>端口，出口IP就是机器网卡名称匹配<code>pppoe??</code> 和机器所有IP中匹配<code>192.168.?.*</code>的IP中随机选择的一个。</li> 
 <li>通配符<code>*</code>代表0至任意多个字符，<code>?</code>代表1个字符。</li> 
 <li>如果网卡IP发生变化，也会实时生效。</li> 
 <li>可以通过<code>--bind-refresh</code>参数，指定刷新本地网卡信息的间隔，默认<code>5</code>，单位秒。</li> 
</ul> 
<p style="color:#24292f; text-align:start">2、所有日志重构，使用gmc框架，日志输出更加规范，排查问题更准确。</p> 
<h1 style="margin-left:0; margin-right:0; text-align:start">手册新增典型用法，13，14，15。</h1> 
<p style="color:#24292f; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsnail007.host900.com%2Fgoproxy%2Fmanual%2Fzh%2F%23%2F" target="_blank">手册地址</a></p> 
<h2 style="text-align:start">13.典型用法-拨号VPS</h2> 
<p style="color:#24292f; text-align:start">为了方便说明，假设背景情况如下：</p> 
<p style="color:#24292f; text-align:start">1、vps有一个主网卡，名称是eth0，ip是1.1.1.1，然后vps可以pppoe拨号，拨号建立的网卡名称前缀都是<code>pppoe_</code>。</p> 
<p style="color:#24292f; text-align:start">实现的效果：</p> 
<ul> 
 <li>提供动态IP代理服务，客户端访问<code>1.1.1.1</code>的代理端口<code>7777</code>，可以使用拨号的ip随机选择一个作为出口，<code>7777</code>端口支持代理认证。</li> 
 <li>7777端口同时支持http/socks5代理。</li> 
</ul> 
<p style="color:#24292f; text-align:start">操作步骤：</p> 
<ol> 
 <li>vps执行<code>proxy sps -p :7777 --bind-ip pppoe_*:7777 -a user1:password1 -a user2:password2<span> </span></code>。</li> 
 <li>命令中<code>-a</code>是设置<code>代理认证用户</code>，多个用户，可以重复<code>-a</code>参数，格式是：<code>用户名:密码</code>。</li> 
 <li>更多认证方式可以参考手册<code>API认证</code>，<code>认证</code>部分。</li> 
</ol> 
<h2 style="text-align:start">14.典型用法-多IP的VPS</h2> 
<p style="color:#24292f; text-align:start">为了方便说明，假设背景情况如下：</p> 
<p style="color:#24292f; text-align:start">1、vps有一个主网卡，名称是<code>eth0</code>，ip是1.1.1.1，然后<code>eth0</code>配置了255个子网卡并设置了IP，比如：<code>eth0:1</code>,<code>eth0:255</code>，子网卡名称前缀都是：<code>eth0:</code>。</p> 
<p style="color:#24292f; text-align:start">实现的效果：</p> 
<ul> 
 <li>提供动态IP代理服务，客户端访问<code>1.1.1.1</code>的代理端口<code>7777</code>，可以使用配置的255个子网卡的ip中随机选择一个作为出口，<code>7777</code>端口支持代理认证。</li> 
 <li>7777端口同时支持http/socks5代理。</li> 
</ul> 
<p style="color:#24292f; text-align:start">操作步骤：</p> 
<ol> 
 <li>vps执行<code>proxy sps -p :7777 --bind-ip eth0::7777 -a user1:password1 -a user2:password2<span> </span></code>。</li> 
 <li>命令中<code>-a</code>是设置<code>代理认证用户</code>，多个用户，可以重复<code>-a</code>参数，格式是：<code>用户名:密码</code>。</li> 
 <li>更多认证方式可以参考手册<code>API认证</code>，<code>认证</code>部分。</li> 
</ol> 
<h2 style="text-align:start">15.典型用法-拨号的VPS集群</h2> 
<p style="color:#24292f; text-align:start">为了方便说明，假设背景情况如下：</p> 
<p style="color:#24292f; text-align:start">1、有一批vps，它们每个都有一个主网卡配置了固定的IP：x.x.x.x，然后vps可以pppoe拨号，拨号建立的网卡名称前缀都是<code>pppoe_</code>。</p> 
<p style="color:#24292f; text-align:start">2、有一个VPS作为代理入口，它的ip是2.2.2.2。</p> 
<p style="color:#24292f; text-align:start">实现的效果：</p> 
<ul> 
 <li><code>2.2.2.2</code>提供动态IP代理服务，客户端访问<code>2.2.2.2</code>的代理端口<code>8888</code>，可以随机选择拨号vps集群中一个，然后使用拨号vps的拨号ip随机选择一个作为出口ip，<code>8888</code>端口支持代理认证。</li> 
 <li><code>8888</code>端口同时支持http/socks5代理。</li> 
</ul> 
<p style="color:#24292f; text-align:start">操作步骤：</p> 
<p style="color:#24292f; text-align:start">拨号VPS：</p> 
<ol> 
 <li>拨号的vps执行<code>proxy sps -p :7777 --bind-ip pppoe_:7777<span> </span></code>。</li> 
</ol> 
<p style="color:#24292f; text-align:start">入口VPS:</p> 
<ol> 
 <li><code>2.2.2.2</code> 的vps执行<code>proxy sps -p :8888 -a user1:password1 -a user2:password2 -P http://x.x.x.1:7777 -P http://x.x.x.2:7777</code>。</li> 
 <li>命令中<code>-a</code>是设置<code>代理认证用户</code>，多个用户，可以重复<code>-a</code>参数，格式是：<code>用户名:密码</code>。</li> 
 <li><code>x.x.x.1</code>,<code>x.x.x.2</code>是拨号vps的固定IP，有多个，重复<code>-P</code>参数即可</li> 
</ol> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">更新： v10.7及以后版本，执行：<code>proxy update</code>，即可完成快速更新到最新版。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><strong>特色功能</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li style="text-align:left">链式代理，程序本身可以作为一级代理，如果设置了上级代理那么可以作为二级代理，乃至N级代理。</li> 
 <li>通讯加密，如果程序不是一级代理，而且上级代理也是本程序，那么可以加密和上级代理之间的通讯，采用底层tls高强度加密，安全无特征。</li> 
 <li>智能HTTP代理，HTTPS代理，SOCKS5代理，会自动判断访问的网站是否屏蔽，如果被屏蔽那么就会使用上级代理(前提是配置了上级代理)访问网站;如果访问的网站没有被屏蔽，为了加速访问，代理会直接访问网站，不使用上级代理。</li> 
 <li>域名黑白名单，更加自由的控制网站的访问方式。</li> 
 <li>跨平台性，无论你是widows，linux，还是mac，甚至是树莓派，都可以很好的运行proxy。</li> 
 <li>多协议支持，支持HTTP(S)，TCP，UDP，Websocket，SOCKS5代理。</li> 
 <li>TCP/UDP端口转发。</li> 
 <li>游戏盾，游戏代理，高仿服务器。</li> 
 <li>内网穿透，P2P传输，协议支持TCP和UDP，针对HTTP的优化穿透。</li> 
 <li>SSH中转，HTTP(S)，SOCKS5代理支持SSH中转，上级Linux服务器不需要任何服务端，本地一个proxy即可开心上网。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxtaci%2Fkcp-go" target="_blank">KCP</a>协议支持，HTTP(S)，SOCKS5代理支持KCP协议传输数据，降低延迟，提升浏览体验。</li> 
 <li>动态选择上级代理，通过外部API，HTTP(S)，SOCKS5，SPS代理可以实现基于用户或者IP的限速，连接数限制，动态获取上级。</li> 
 <li>灵活的上级分配，HTTP(S)，SOCKS5，SPS代理可以通过配置文件实现基于用户或者IP的限速，连接数限制，指定上级。</li> 
 <li>反向代理，支持直接把域名解析到proxy监听的ip，然后proxy就会帮你代理访问需要访问的HTTP(S)网站。</li> 
 <li>透明HTTP(S)代理，配合iptables，在网关直接把出去的80，443方向的流量转发到proxy，就能实现无感知的智能路由器代理。</li> 
 <li>协议转换，可以把已经存在的HTTP(S)或SOCKS5或SS代理转换为一个端口同时支持HTTP(S)和SOCKS5和SS代理，转换后的SOCKS5和SS代理如果上级是SOCKS5代理，那么支持UDP功能，同时支持强大的级联认证功能。</li> 
 <li>自定义底层加密传输，http(s)\\sps\\socks代理在tcp之上可以通过tls标准加密以及kcp协议加密tcp数据，除此之外还支持在tls和kcp之后进行自定义加密，也就是说自定义加密和tls|kcp是可以联合使用的，内部采用AES256加密，使用的时候只需要自己定义一个密码即可。</li> 
 <li>底层压缩高效传输，http(s)\\sps\\socks代理在tcp之上可以通过自定义加密和tls标准加密以及kcp协议加密tcp数据，在加密之后还可以对数据进行压缩，也就是说压缩功能和自定义加密和tls|kcp是可以联合使用的。</li> 
 <li>安全的DNS代理，可以通过本地的proxy提供的DNS代理服务器与上级代理加密通讯实现安全防污染的DNS查询。</li> 
 <li>负载均衡，高可用，HTTP(S)\\SOCKS5\\SPS代理支持上级负载均衡和高可用，多个上级重复-P参数即可。</li> 
 <li>指定出口IP，HTTP(S)\\SOCKS5\\SPS\\TCP代理支持客户端用入口IP连接过来的，就用入口IP作为出口IP访问目标网站的功能。如果入口IP是内网IP，出口IP不会使用入口IP</li> 
 <li>支持限速，HTTP(S)\\SOCKS5\\SPS\\TCP代理支持限速。</li> 
 <li> <p style="margin-left:0; margin-right:0">支持限连接数，HTTP(S)\\SOCKS5\\SPS\\TCP代理支持限连接数。</p> </li> 
 <li>SOCKS5代理支持级联认证。</li> 
 <li>证书参数使用base64数据，默认情况下-C，-K参数是crt证书和key文件的路径，如果是base64://开头，那么就认为后面的数据是base64编码的，会解码后使用。</li> 
 <li>支持客户端IP黑白名单，更加安全的控制客户端对代理服务的访问，如果黑白名单同时设置，那么只有白名单生效。socks/http(s)/sps/tcp/udp/dns/内网穿透bridge/内网穿透tbridge，都支持客户端IP黑白名单。</li> 
 <li>端口范围批量监听，HTTP(S)\\SOCKS5\\SPS\\TCP代理支持指定端口范围监听，避免启动过多进程，提高性能。</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">下载地址:</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><a href="https://gitee.com/snail/proxy/" target="_blank">Gitee</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsnail007%2Fgoproxy" target="_blank">Github</a></p> </li> 
</ul>
                                        </div>
                                      
</div>
            
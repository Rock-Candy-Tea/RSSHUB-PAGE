
---
title: 'QuantumTunnel v0.1-beta 发布，内网穿透工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://img-blog.csdnimg.cn/0e5f8e1d120e42c389e42ceb7359f8b2.png'
author: 开源中国
comments: false
date: Sat, 23 Oct 2021 22:13:00 GMT
thumbnail: 'https://img-blog.csdnimg.cn/0e5f8e1d120e42c389e42ceb7359f8b2.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">经过一段时间的代码优化，QuantumTunnel发布了 <a href="https://gitee.com/liumian/quantum-tunnel/releases/v0.1-beta">v0.1-beta版本</a>，满足大部分内网穿透的使用场景。</p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">快速开始</h1> 
<h2 style="margin-left:0; margin-right:0; text-align:left">方式一：直接下载Jar包</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">使用下载 Jar 包的方式，只需要<code>两行启动命令即可搭建好内网穿透服务</code>。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">下载Jar包</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">访问 <a href="https://gitee.com/liumian/quantum-tunnel/releases/v0.1-beta">v0.1-beta版本</a> 页面，下载 quantum-tunnel-server.jar 和 quantum-tunnel-client.jar；</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">执行启动命令</h3> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">启动内网穿透服务端： java -jar quantum-tunnel-server.jar -proxy_server_port 9090 -user_server_port 8090<span> </span><img alt="服务启动成功" src="https://img-blog.csdnimg.cn/0e5f8e1d120e42c389e42ceb7359f8b2.png" referrerpolicy="no-referrer"></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">启动内网穿透客户端：java -jar quantum-tunnel-client.jar -network_id localTest -proxy_server_host 127.0.0.1 -proxy_server_port 9090</p> </li> 
</ol> 
<p style="margin-left:0; margin-right:0"><span> </span><img alt="客户端启动成功" src="https://img-blog.csdnimg.cn/34575e6832674eb7871686e9e1f6e5de.png" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">验证链路</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">启动命令执行完成后，内网穿透服务就搭建好了，内网穿透服务端会把接收到的流量转发到内网穿透客户端，并由客户端发起真正的请求。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">我们使用访问百度的 curl 命令来验证一下，命令如下：</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-shell"><span style="color:#005cc5">curl</span> --location --request GET <span style="color:#032f62">'127.0.0.1:8090/'</span> \
--header <span style="color:#032f62">'targetPort: 80'</span> \
--header <span style="color:#032f62">'networkId: localTest'</span> \
--header <span style="color:#032f62">'Host: www.baidu.com'</span> \
--header <span style="color:#032f62">'targetHost: www.baidu.com'</span> \
--header <span style="color:#032f62">'Cookie: BDSVRTM=11; BD_HOME=1'</span>
</code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="访问成功" src="https://img-blog.csdnimg.cn/ddc69a4766774c128c58f9ffa14602e5.png" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">方式二：编译源码</h2> 
<h3 style="margin-left:0; margin-right:0; text-align:left">克隆仓库</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">仓库地址：<a href="https://gitee.com/liumian/quantum-tunnel">乐天派 / quantum-tunnel</a></p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-shell"><span style="color:#d73a49">git</span>@<span style="color:#d73a49">gitee</span><span style="color:#6f42c1">.com</span><span style="color:#6f42c1">:liumian</span>/<span style="color:#d73a49">quantum-tunnel</span><span style="color:#6f42c1">.git</span>
</code></pre> 
<h3 style="margin-left:0; margin-right:0; text-align:left">编译源码</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">进入仓库根目录，执行已经写好编译脚本：</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-shell"><span style="color:#6a737d"># 编译内网穿透服务端</span>
<span style="color:#6f42c1">sh</span> <span style="color:#032f62">package_server.sh</span>
<span style="color:#6a737d">
# 编译内网穿透客户端</span>
<span style="color:#6f42c1">sh</span> <span style="color:#032f62">package_client.sh</span>
</code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">编译完成后会生成两个jar包：quantum-tunnel-server.jar和quantum-tunnel-client.jar，启动和验证的流程可以参考<code>方式一：直接下载Jar包</code>。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">是不是很简单~</p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">最后</h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">目前 QuantumTunnel 支持 Http 和 WebSocket 协议的内网穿透，满足大部分的使用场景。若要支持更多协议，只需要简单开发对应协议的解析路由信息Handler即可。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">赶紧来使用吧，有任何问题可以提 issue 或者留言哦。</p>
                                        </div>
                                      
</div>
            
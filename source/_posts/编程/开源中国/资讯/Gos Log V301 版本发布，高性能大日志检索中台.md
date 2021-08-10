
---
title: 'Gos Log V3.0.1 版本发布，高性能大日志检索中台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9379'
author: 开源中国
comments: false
date: Tue, 10 Aug 2021 11:42:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9379'
---

<div>   
<div class="content">
                                                                                            <p>Gos Log V3.0.1 版本发布，V3.0.1支持功能如下</p> 
<ol> 
 <li> <p>支持客户端logc启动即注册</p> </li> 
 <li> <p>支持服务端logs定时检测客户端在线状态</p> </li> 
 <li> <p>支持关键字不唯一时，也能全部检索</p> </li> 
 <li> <p>优化删除逻辑</p> </li> 
</ol> 
<h2>版本地址</h2> 
<p><a href="https://gitee.com/dianjiu/gos-log/releases/V3.0.1">https://gitee.com/dianjiu/gos-log/releases/V3.0.1</a></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdianjiu%2Fgos-log%2Freleases%2Ftag%2FV3.0.1" target="_blank">https://github.com/dianjiu/gos-log/releases/V3.0.1</a></p> 
<h1 style="text-align:start">仓库地址</h1> 
<h1 style="text-align:start">gos-log</h1> 
<p style="text-align:start"><a href="https://gitee.com/dianjiu/gos-log" target="_blank">https://gitee.com/dianjiu/gos-log(opens new window)</a></p> 
<p style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdianjiu%2Fgos-log" target="_blank">https://github.com/dianjiu/gos-log(opens new window)</a></p> 
<h2 style="text-align:start">gos-log-vue</h2> 
<p style="text-align:start"><a href="https://gitee.com/dianjiu/gos-log-vue" target="_blank">https://gitee.com/dianjiu/gos-log-vue(opens new window)</a></p> 
<p style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdianjiu%2Fgos-log-vue" target="_blank">https://github.com/dianjiu/gos-log-vue</a></p> 
<h1 style="text-align:start">打包</h1> 
<div style="text-align:start"> 
 <h3><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoslog.dianjiu.org.cn%2Fdocument%2Fdoc07.html%23gos-log" target="_blank">#</a>gos-log</h3> 
 <div> 
  <pre style="text-align:left"><code><span style="color:#999999"><span style="color:#6a737d"># 打包服务端</span></span>
<span style="color:#cc99cd"><span style="color:#6f42c1">cd</span></span> <span style="color:#032f62">gos-log/logs</span>
<span style="color:#6f42c1">bee</span> <span style="color:#032f62">pack -be </span><span style="color:#7ec699"><span style="color:#032f62">GOOS</span></span><span style="color:#67cdcc"><span style="color:#032f62">=</span></span><span style="color:#032f62">linux</span>
<span style="color:#999999"><span style="color:#6a737d"># 打包客户端</span></span>
<span style="color:#cc99cd"><span style="color:#6f42c1">cd</span></span> <span style="color:#032f62">gos-log/logc</span>
<span style="color:#6f42c1">bee</span> <span style="color:#032f62">pack -be </span><span style="color:#7ec699"><span style="color:#032f62">GOOS</span></span><span style="color:#67cdcc"><span style="color:#032f62">=</span></span><span style="color:#032f62">linux</span>
<span style="color:#999999"><span style="color:#6a737d"># 准备数据库 见gos-log项目下的sql文件夹</span></span>
<span style="color:#999999"><span style="color:#6a737d"># 将打包后的文件上传到服务器指定目录</span></span>
</code></pre> 
 </div> 
 <h3><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoslog.dianjiu.org.cn%2Fdocument%2Fdoc07.html%23gos-log-vue" target="_blank">#</a>gos-log-vue</h3> 
 <div> 
  <pre style="text-align:left"><code><span style="color:#999999"><span style="color:#6a737d"># 打包构建</span></span>
<span style="color:#f08d49"><span style="color:#6f42c1">yarn</span></span> <span style="color:#032f62">run build</span>
<span style="color:#999999"><span style="color:#6a737d"># 把dist目录下的文件上传到服务器的指定目录</span></span>
</code></pre> 
 </div> 
 <h2><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoslog.dianjiu.org.cn%2Fdocument%2Fdoc07.html%23%25E5%2590%25AF%25E5%258A%25A8" target="_blank">#</a>启动</h2> 
 <h3><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoslog.dianjiu.org.cn%2Fdocument%2Fdoc07.html%23gos-log-logs" target="_blank">#</a>gos-log-logs</h3> 
 <div> 
  <pre style="text-align:left"><code><span style="color:#999999"><span style="color:#6a737d"># 解压缩</span></span>
<span style="color:#f08d49"><span style="color:#6f42c1">tar</span></span> <span style="color:#032f62">-zxf logs.tar.gz -C ./ </span>
<span style="color:#999999"><span style="color:#6a737d"># 授权</span></span>
<span style="color:#f08d49"><span style="color:#6f42c1">chmod</span></span> <span style="color:#032f62">-x logs </span>
<span style="color:#999999"><span style="color:#6a737d"># 修改数据库配置、临时目录</span></span>
<span style="color:#f08d49"><span style="color:#6f42c1">sudo</span></span> <span style="color:#f08d49"><span style="color:#032f62">vim</span></span><span style="color:#032f62"> conf/app.conf </span>
<span style="color:#999999"><span style="color:#6a737d"># 启动</span></span>
<span style="color:#f08d49"><span style="color:#6f42c1">nohup</span></span> <span style="color:#032f62">./logs </span><span style="color:#67cdcc"><span style="color:#032f62">>></span></span><span style="color:#032f62"> logs.log </span><span style="color:#67cdcc"><span style="color:#032f62">&</span></span><span style="color:#032f62"> </span>
</code></pre> 
 </div> 
 <h3><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoslog.dianjiu.org.cn%2Fdocument%2Fdoc07.html%23gos-log-logc" target="_blank">#</a>gos-log-logc</h3> 
 <div> 
  <pre style="text-align:left"><code><span style="color:#999999"><span style="color:#6a737d"># 解压缩</span></span>
<span style="color:#f08d49"><span style="color:#6f42c1">tar</span></span> <span style="color:#032f62">-zxf logc.tar.gz -C ./ </span>
<span style="color:#999999"><span style="color:#6a737d"># 授权</span></span>
<span style="color:#f08d49"><span style="color:#6f42c1">chmod</span></span> <span style="color:#032f62">-x logc </span>
<span style="color:#999999"><span style="color:#6a737d"># 修改临时目录</span></span>
<span style="color:#f08d49"><span style="color:#6f42c1">sudo</span></span> <span style="color:#f08d49"><span style="color:#032f62">vim</span></span><span style="color:#032f62"> conf/app.conf </span>
<span style="color:#999999"><span style="color:#6a737d"># 启动</span></span>
<span style="color:#f08d49"><span style="color:#6f42c1">nohup</span></span> <span style="color:#032f62">./logc </span><span style="color:#67cdcc"><span style="color:#032f62">>></span></span><span style="color:#032f62"> logc.log </span><span style="color:#67cdcc"><span style="color:#032f62">&</span></span><span style="color:#032f62"> </span>
</code></pre> 
 </div> 
 <h3><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoslog.dianjiu.org.cn%2Fdocument%2Fdoc07.html%23gos-log-vue-2" target="_blank">#</a>gos-log-vue</h3> 
 <div> 
  <pre style="text-align:left"><code><span style="color:#999999"><span style="color:#6a737d"># nginx部署如下nginx.conf</span></span>
<span style="color:#22863a">server</span> <span style="color:#cccccc">&#123;</span>
<span style="color:#005cc5">listen</span>       <span style="color:#f08d49">2022</span><span style="color:#cccccc">;</span>
<span style="color:#005cc5">server_name</span>  localhost<span style="color:#cccccc">;</span>

<span style="color:#005cc5">location</span> / <span style="color:#cccccc">&#123;</span>
<span style="color:#005cc5">root</span> /web/gos-log/vue<span style="color:#cccccc">;</span>
<span style="color:#005cc5">index</span>  index.html index.htm<span style="color:#cccccc">;</span>
<span style="color:#005cc5">try_files</span> <span style="color:#7ec699"><span style="color:#032f62">$uri</span></span> <span style="color:#7ec699"><span style="color:#032f62">$uri</span></span>/ /index.html<span style="color:#cccccc">;</span> 
<span style="color:#cccccc">&#125;</span>
<span style="color:#005cc5">location</span> /api <span style="color:#cccccc">&#123;</span>
<span style="color:#005cc5">rewrite</span>  ^/api/<span style="color:#cccccc">(</span>.*<span style="color:#cccccc">)</span>$ /<span style="color:#7ec699"><span style="color:#032f62">$1</span></span> <span style="color:#cc99cd"><span style="color:#005cc5">break</span></span><span style="color:#cccccc">;</span>
<span style="color:#005cc5">proxy_pass</span> http://127.0.0.1:2021<span style="color:#cccccc">;</span>
<span style="color:#cccccc">&#125;</span>
<span style="color:#cccccc">&#125;</span></code></pre> 
 </div> 
</div>
                                        </div>
                                      
</div>
            
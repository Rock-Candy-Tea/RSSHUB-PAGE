
---
title: 'Gos Log V21.05.20 版本发布，高性能大日志检索中台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6905'
author: 开源中国
comments: false
date: Mon, 24 May 2021 11:03:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6905'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:#ffffff; color:#40485b">V21.05.20 版本更新内内容</span><br> <span style="background-color:#ffffff; color:#40485b">✅ 1、 上线Gos Log 官网 </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoslog.dianjiu.org.cn%2F" target="_blank">https://goslog.dianjiu.org.cn</a><br> <span style="background-color:#ffffff; color:#40485b">✅ 2、 优化并行查询速度，查询全部服务器理论耗时于单台服务相当</span><br> <span style="background-color:#ffffff; color:#40485b">✅ 3、 每次查询响应后自动清理临时文件，优化磁盘空间</span><br> <span style="background-color:#ffffff; color:#40485b">✅ 4、优化向下截取行可输入，解决默认1000行有时不够用的问题</span></p> 
<h2 style="text-align:start">版本地址</h2> 
<p style="text-align:start"><a href="https://gitee.com/dianjiu/gos-log/releases/V21.05.20" target="_blank">https://gitee.com/dianjiu/gos-log/releases/V21.05.20</a></p> 
<p style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdianjiu%2Fgos-log%2Freleases%2FV21.05.20" target="_blank">https://github.com/dianjiu/gos-log/releases/V21.05.20</a></p> 
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
  <pre style="text-align:left"><code><span style="color:#999999"># 打包服务端</span>
<span style="color:#cc99cd">cd</span> gos-log/logs
bee pack -be <span style="color:#7ec699">GOOS</span><span style="color:#67cdcc">=</span>linux
<span style="color:#999999"># 打包客户端</span>
<span style="color:#cc99cd">cd</span> gos-log/logc
bee pack -be <span style="color:#7ec699">GOOS</span><span style="color:#67cdcc">=</span>linux
<span style="color:#999999"># 准备数据库 见gos-log项目下的sql文件夹</span>
<span style="color:#999999"># 将打包后的文件上传到服务器指定目录</span>
</code></pre> 
 </div> 
 <h3><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoslog.dianjiu.org.cn%2Fdocument%2Fdoc07.html%23gos-log-vue" target="_blank">#</a>gos-log-vue</h3> 
 <div> 
  <pre style="text-align:left"><code><span style="color:#999999"># 打包构建</span>
<span style="color:#f08d49">yarn</span> run build
<span style="color:#999999"># 把dist目录下的文件上传到服务器的指定目录</span>
</code></pre> 
 </div> 
 <h2><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoslog.dianjiu.org.cn%2Fdocument%2Fdoc07.html%23%25E5%2590%25AF%25E5%258A%25A8" target="_blank">#</a>启动</h2> 
 <h3><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoslog.dianjiu.org.cn%2Fdocument%2Fdoc07.html%23gos-log-logs" target="_blank">#</a>gos-log-logs</h3> 
 <div> 
  <pre style="text-align:left"><code><span style="color:#999999"># 解压缩</span>
<span style="color:#f08d49">tar</span> -zxf logs.tar.gz -C ./ 
<span style="color:#999999"># 授权</span>
<span style="color:#f08d49">chmod</span> -x logs 
<span style="color:#999999"># 修改数据库配置、临时目录</span>
<span style="color:#f08d49">sudo</span> <span style="color:#f08d49">vim</span> conf/app.conf 
<span style="color:#999999"># 启动</span>
<span style="color:#f08d49">nohup</span> ./logs <span style="color:#67cdcc">>></span> logs.log <span style="color:#67cdcc">&</span> 
</code></pre> 
 </div> 
 <h3><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoslog.dianjiu.org.cn%2Fdocument%2Fdoc07.html%23gos-log-logc" target="_blank">#</a>gos-log-logc</h3> 
 <div> 
  <pre style="text-align:left"><code><span style="color:#999999"># 解压缩</span>
<span style="color:#f08d49">tar</span> -zxf logc.tar.gz -C ./ 
<span style="color:#999999"># 授权</span>
<span style="color:#f08d49">chmod</span> -x logc 
<span style="color:#999999"># 修改临时目录</span>
<span style="color:#f08d49">sudo</span> <span style="color:#f08d49">vim</span> conf/app.conf 
<span style="color:#999999"># 启动</span>
<span style="color:#f08d49">nohup</span> ./logc <span style="color:#67cdcc">>></span> logc.log <span style="color:#67cdcc">&</span> 
</code></pre> 
 </div> 
 <h3><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoslog.dianjiu.org.cn%2Fdocument%2Fdoc07.html%23gos-log-vue-2" target="_blank">#</a>gos-log-vue</h3> 
 <div> 
  <pre style="text-align:left"><code><span style="color:#999999"># nginx部署如下nginx.conf</span>
server <span style="color:#cccccc">&#123;</span>
listen       <span style="color:#f08d49">2022</span><span style="color:#cccccc">;</span>
server_name  localhost<span style="color:#cccccc">;</span>

location / <span style="color:#cccccc">&#123;</span>
root /web/gos-log/vue<span style="color:#cccccc">;</span>
index  index.html index.htm<span style="color:#cccccc">;</span>
try_files <span style="color:#7ec699">$uri</span> <span style="color:#7ec699">$uri</span>/ /index.html<span style="color:#cccccc">;</span> 
<span style="color:#cccccc">&#125;</span>
location /api <span style="color:#cccccc">&#123;</span>
rewrite  ^/api/<span style="color:#cccccc">(</span>.*<span style="color:#cccccc">)</span>$ /<span style="color:#7ec699">$1</span> <span style="color:#cc99cd">break</span><span style="color:#cccccc">;</span>
proxy_pass http://127.0.0.1:2021<span style="color:#cccccc">;</span>
<span style="color:#cccccc">&#125;</span>
<span style="color:#cccccc">&#125;</span>
</code></pre> 
 </div> 
</div>
                                        </div>
                                      
</div>
            
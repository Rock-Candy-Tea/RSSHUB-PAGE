
---
title: 'Java 进程启停及诊断 Jarboot v2.1.0'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/majz0908/jarboot/raw/develop/doc/overview.png'
author: 开源中国
comments: false
date: Fri, 26 Nov 2021 11:36:00 GMT
thumbnail: 'https://gitee.com/majz0908/jarboot/raw/develop/doc/overview.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>在2.0.0版本基础上修复部分火狐、Safari浏览器的小问题，图标优化。修复了Docker挂载logs目录可能会出现的问题，推荐升级！</p> 
<p>建议使用Safari和Chrome浏览器，火狐浏览器尽量更新到90版本以上，IE浏览器使用10以上版本。</p> 
<p><img alt height="518" src="https://gitee.com/majz0908/jarboot/raw/develop/doc/overview.png" width="1000" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">可通过Gitee和GitHub下载最新的安装包，使用Docker的请更新下Jarboot的Docker镜像。</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span style="color:#000000">GitHub:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmajianzheng%2Fjarboot" target="_blank">https://github.com/majianzheng/jarboot</a></span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span style="color:#000000">Gitee:<span> </span><a href="https://gitee.com/majz0908/jarboot">https://gitee.com/majz0908/jarboot</a></span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span style="color:#000000">Docker Hub:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fregistry.hub.docker.com%2Fr%2Fmazheng0908%2Fjarboot" target="_blank">https://registry.hub.docker.com/r/mazheng0908/jarboot</a></span></p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-bash"><span style="color:#6f42c1">sudo</span> <span style="color:#032f62">docker run -itd --name jarboot -p 9899:9899 mazheng0908/jarboot</span></code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">使用Docker时建议将<span><strong>/jarboot/services</strong>和<strong>/jarboot/logs</strong>挂载宿主机</span></p> 
<h2 style="margin-left:0em; margin-right:0em; text-align:start">修复问题</h2> 
<ul> 
 <li>修复在Docker下启动多个容器时，将logs目录挂载后出现的状态不对的问题</li> 
 <li>修复Safari浏览器滚动条下部有一个小白点的问题</li> 
 <li>隐藏火狐浏览器滚动条</li> 
 <li>前端样式代码优化统一</li> 
 <li>在线调试增加正在Attach的图标过渡</li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:start">新特性:</h4> 
<ul> 
 <li>图标更新美化</li> 
 <li>支持以客户端的模式与k8s、Docker集成使用，集中管理、诊断</li> 
</ul> 
<p>集成的方法步骤可以参考：<a href="https://my.oschina.net/oldapple/blog/5326295">Jarboot以客户端形式集成到k8s、Docker的方法</a></p> 
<p><img alt height="237" src="https://oscimg.oschina.net/oscnet/up-cb1dabb524e94509b9dfade091136e915dc.png" width="360" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            
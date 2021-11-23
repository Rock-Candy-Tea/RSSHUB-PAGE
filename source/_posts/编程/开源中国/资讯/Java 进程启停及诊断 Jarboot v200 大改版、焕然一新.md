
---
title: 'Java 进程启停及诊断 Jarboot v2.0.0 大改版、焕然一新'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-9dc90fc4193acee94d83780b62652e865a3.png'
author: 开源中国
comments: false
date: Tue, 23 Nov 2021 09:32:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-9dc90fc4193acee94d83780b62652e865a3.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>增加分组管理，界面大改版，焕然一新！</p> 
<p><img height="1326" src="https://oscimg.oschina.net/oscnet/up-9dc90fc4193acee94d83780b62652e865a3.png" width="2558" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">可通过Gitee和GitHub下载最新的安装包，使用Docker的请更新下Jarboot的Docker镜像。</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span style="color:#000000">GitHub:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmajianzheng%2Fjarboot" target="_blank">https://github.com/majianzheng/jarboot</a></span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span style="color:#000000">Gitee:<span> </span><a href="https://gitee.com/majz0908/jarboot">https://gitee.com/majz0908/jarboot</a></span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span style="color:#000000">Docker Hub:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fregistry.hub.docker.com%2Fr%2Fmazheng0908%2Fjarboot" target="_blank">https://registry.hub.docker.com/r/mazheng0908/jarboot</a></span></p> 
<pre><code class="language-bash">sudo docker run -itd --name jarboot -p 9899:9899 mazheng0908/jarboot</code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">使用Docker时建议将<span><strong>/jarboot/services</strong>和<strong>/jarboot/logs</strong>挂载宿主机</span></p> 
<h2 style="margin-left:0em; margin-right:0em; text-align:start">问题修改及优化：</h2> 
<ul> 
 <li>服务状态通知机制优化</li> 
 <li>服务配置界面增加服务状态显示</li> 
 <li>修复服务数量过多时服务配置界面显示异常问题</li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:start">新特性：</h4> 
<ul> 
 <li>界面大改版，菜单结构大调整</li> 
 <li>主题色修改，紧凑版布局</li> 
 <li>服务配置新增名字和组的配置，可以重命名和配置所属组</li> 
 <li>服务管理增加底部工具栏，一键启动等按钮、树显示VS列表显示、控制台VS服务配置</li> 
 <li>服务管理新增组显示，可与列表显示相互切换</li> 
 <li>服务管理侧栏固定式布局</li> 
 <li>部分图标更新、美化</li> 
 <li>服务配置由菜单移至服务管理，服务管理右侧界面可以在控制台和服务配置之间相互切换</li> 
 <li>插件管理移到设置中</li> 
 <li>统一滚动条样式</li> 
</ul> 
<p><img height="1326" src="https://oscimg.oschina.net/oscnet/up-406c2ef470cc2c21595538aa96d94cb5d15.png" width="2558" referrerpolicy="no-referrer"></p> 
<p> </p>
                                        </div>
                                      
</div>
            

---
title: 'Java 进程启停及诊断 Jarboot v2.2.1 稳定版发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/majz0908/jarboot/raw/develop/doc/overview.png'
author: 开源中国
comments: false
date: Tue, 07 Dec 2021 02:25:00 GMT
thumbnail: 'https://gitee.com/majz0908/jarboot/raw/develop/doc/overview.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>本次更新修复了部分问题，进行了较大的功能性改进及性能优化，占用更少的内存和CPU，推荐升级。</p> 
<p><img alt height="414" src="https://gitee.com/majz0908/jarboot/raw/develop/doc/overview.png" width="688" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">可通过Gitee和GitHub下载最新的安装包，升级时直接覆盖原目录即可，使用Docker的请更新下Jarboot的Docker镜像。</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span style="color:#000000">GitHub:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmajianzheng%2Fjarboot" target="_blank">https://github.com/majianzheng/jarboot</a></span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span style="color:#000000">Gitee:<span> </span><a href="https://gitee.com/majz0908/jarboot">https://gitee.com/majz0908/jarboot</a></span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span style="color:#000000">Docker Hub:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fregistry.hub.docker.com%2Fr%2Fmazheng0908%2Fjarboot" target="_blank">https://registry.hub.docker.com/r/mazheng0908/jarboot</a></span></p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-bash"><span style="color:#6f42c1">sudo</span> <span style="color:#032f62">docker run -itd --name jarboot -p 9899:9899 mazheng0908/jarboot</span></code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">使用Docker时建议将<span><strong>/jarboot/services</strong>和<strong>/jarboot/logs</strong>挂载宿主机</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">关于与k8s的集成使用请参考：<a href="https://my.oschina.net/oldapple/blog/5326295">Jarboot以客户端形式集成到k8s、Docker的方法</a> 和 <a href="https://my.oschina.net/oldapple/blog/5195501">Jarboot容器镜像使用及Dockerfile分享</a></p> 
<h2 style="margin-left:0em; margin-right:0em; text-align:start">更新内容</h2> 
<ul> 
 <li>修复工作空间变更后工作空间文件监控功能还是旧目录的问题</li> 
 <li>大幅度优化std的IO性能，重构缓存刷新机制，实现空闲期 0 CPU占用</li> 
 <li>dashboard、jad、heapdump命令的渲染界面优化，交互设计改进</li> 
 <li>内存优化，占用更少的内存空间</li> 
 <li>修复Attach本地进程时未初始化而不显示控制台输出的问题</li> 
 <li>优化工作空间文件监控逻辑，原file-record.temp文件废弃，可删除</li> 
 <li>修复derby日志文件在根目录的问题，移到logs目录，原derby.log文件可删除</li> 
 <li>优化后端线程的调度管理</li> 
 <li>修复删除服务时，文件太多无响应的问题，增加全局loading提示</li> 
 <li>修复导入服务时，压缩文件内容过多时无响应的问题，增加全局loading提示</li> 
 <li>代码优化，可读性优化，完善代码注释</li> 
 <li>远程进程连接网络断开时，增加心跳及尝试重连机制，每隔一段时间探测一次</li> 
 <li>优化命令执行的通讯协议</li> 
 <li>修复notice接口指定sessionId时仍通知所以客户端的问题，优化notice的前后端交互机制</li> 
 <li>优化前端布局，权限控制、设置、帮助使用左侧固定右侧自适应布局方式</li> 
</ul> 
<p> </p> 
<p>有对代码感兴趣的同学，欢迎联系我，新功能或修复bug，欢迎提交PR。技术栈前端是React、Less，后端是Java。</p> 
<p>注意：提交PR需要在GitHub上fork分支，Gitee每次会从GitHub强制同步。</p>
                                        </div>
                                      
</div>
            
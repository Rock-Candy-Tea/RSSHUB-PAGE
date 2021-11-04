
---
title: 'Java 进程管理、调试平台——Jarboot v1.1.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5022'
author: 开源中国
comments: false
date: Thu, 04 Nov 2021 09:18:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5022'
---

<div>   
<div class="content">
                                                                                            <h2 style="text-align:start">1.1.0 (11.3, 2021)</h2> 
<p>GitHub: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmajianzheng%2Fjarboot" target="_blank">https://github.com/majianzheng/jarboot</a></p> 
<p>镜像仓库Gitee：<a href="https://gitee.com/majz0908/jarboot">https://gitee.com/majz0908/jarboot</a></p> 
<p>可以选择使用安装包下载安装，安装包下载请到Github；</p> 
<p>也可以使用Docker，<span style="background-color:#ffffff; color:#24292f">Docker Hub:<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fregistry.hub.docker.com%2Fr%2Fmazheng0908%2Fjarboot" target="_blank">https://registry.hub.docker.com/r/mazheng0908/jarboot</a></p> 
<pre style="text-align:left"><span><span style="color:#0086b3">sudo </span>docker run <span style="color:#000080">-itd</span> <span style="color:#000080">--name</span> jarboot-test <span style="color:#000080">-p</span> 9899:9899 mazheng0908/jarboot</span>
</pre> 
<p>更新内容：</p> 
<ul> 
 <li>服务配置："<em><strong>是否可执行jar</strong></em>"、"<em><strong>启动的jar文件</strong></em>"和"<em><strong>自定义的命令</strong></em>"这3项配置合bing为一个"<em><strong>启动命令</strong></em>"的配置项， 若为空且仅有一个jar文件则默认使用-jar选项启动，旧版本配置内容将失效</li> 
 <li>使用重新设计的进程识别机制，解决无法启动<strong><code>seata</code></strong>这种带传入参数的Java程序，目前已经测试可以正常启动<strong>seata</strong></li> 
 <li>修复启动服务时Console终端未清理bug</li> 
 <li>shell和debug插件优化修改</li> 
 <li>thread命令不再显示内部线程信息，兼容jdk11及以上的环境编译</li> 
 <li>重连成功和工作空间变化时自动刷新服务列表</li> 
</ul> 
<h4 style="text-align:start">FEATURES:</h4> 
<ul> 
 <li>前端界面框架升级优化</li> 
 <li>服务管理界面增加按名称、状态搜索过滤的功能</li> 
 <li>服务配置界面增加搜索过滤功能</li> 
</ul>
                                        </div>
                                      
</div>
            
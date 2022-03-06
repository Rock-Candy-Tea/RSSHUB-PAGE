
---
title: 'IntelliJ IDEA 2022.1 EAP 4 发布，大量 Kubernetes_Docker 改进'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-575e05287021b8d88deac8f265c976afe4a.gif'
author: 开源中国
comments: false
date: Sun, 06 Mar 2022 08:01:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-575e05287021b8d88deac8f265c976afe4a.gif'
---

<div>   
<div class="content">
                                                                                            <p>IntelliJ IDEA 2022.1 EAP 4 版本现已<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fidea%2F2022%2F03%2Fintellij-idea-2022-1-eap-4%2F" target="_blank">发布</a>，此版本对 Docker 和 Kubernetes 功能进行了许多更新，并在运行和调试代码时增强了用户体验。</p> 
<h2 style="margin-left:0px">Kubernetes</h2> 
<h3 style="margin-left:0px">编辑集群上的资源</h3> 
<p style="margin-left:0px">现在可以从编辑器选项卡中修改从集群加载的资源。</p> 
<p style="margin-left:0px"><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-575e05287021b8d88deac8f265c976afe4a.gif" width="700" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0px">kubectl 的自定义路径</h3> 
<p style="margin-left:0px">如果 kubectl 不在标准位置，现在可以手动配置路径。</p> 
<p style="margin-left:0px"><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-8fcc6ca200a51ea83e64afd2d4dfaef73e5.png" width="700" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0px">转发端口 </h3> 
<p style="margin-left:0px">该版本为 pod 添加了端口转发功能。要转发端口，可以使用工具栏上的图标或选择上下文菜单项。</p> 
<p style="margin-left:0px"><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-bbd237f5630441cbcf2a6de552d58980f60.gif" width="700" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0px">服务视图中的 <em>描述资源操作</em></h3> 
<p style="margin-left:0px"><em>“服务</em>”视图中的所有资源都有一个新的“<em>描述资源”操作，</em>可以从上下文菜单中调用它或使用工具栏按钮。</p> 
<p style="margin-left:0px"><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-0a75c4a75d5a00d67d655e25f90d6393a68.png" width="700" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0px">支持集群中的<em>事件</em></h3> 
<p style="margin-left:0px">集群事件现在显示在 <em>服务 </em>视图的单独节点中，提供有关系统中最近事件的数据。</p> 
<p style="margin-left:0px"><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-41e69659009f2eece845952339e8dec11aa.png" width="700" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0px">要查看特定 pod 的事件，请在其上面调用 <em>Describe Resource </em>并在操作结果中 查找 <em>Events 部分</em></p> 
<p style="margin-left:0px"><em><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-48af28fd3bb2bbdbf8782eb3548e1455352.png" width="700" referrerpolicy="no-referrer"></em></p> 
<h3 style="margin-left:0px">支持</h3> 
<p style="margin-left:0px">为 werf.yaml 和相关 Helm 模板文件 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwerf.io%2F" target="_blank">https://werf.io</a> ) 引入了有限的编辑器支持，包括代码补全功能、检查和快速修复建议、重构/重命名 . <em>Values.werf.image.*</em>，以及一些字段的验证，如 <em>boolean </em>和 <em>int</em>。  </p> 
<p style="margin-left:0px"><img alt height="300" src="https://oscimg.oschina.net/oscnet/up-f061e9f7be0e12ea28c82f1c3c5e1c8a4e1.png" width="700" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0px"><img alt height="300" src="https://oscimg.oschina.net/oscnet/up-cbdea67533f0cd278c902bb42f160452ab9.png" width="700" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0px">对 Helm 的导入子值支持</h3> 
<p style="margin-left:0px">支持通过 <em>import-values </em>设置导入子值，这些设置影响模板中内置对象的完成/导航。尚未提供对 import-values 字段的增强编辑器支持。</p> 
<p style="margin-left:0px"><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-20829152d1418cb227b345e3bc4855f5c45.gif" width="700" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0px"><span style="color:#27282c">请注意，Kubernetes 功能仅适用于 IntelliJ IDEA Ultimate，并且需要安装插件。</span></p> 
<p style="margin-left:0px"> </p> 
<h2 style="margin-left:0px; margin-right:0px; text-align:start">Docker</h2> 
<h3 style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>新的服务视图 UI</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h3> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>在 <em>服务 </em>工具窗口中对 Docker 的 UI 进行了重大修改，已经对容器、图像、网络和卷实施了改造。 </span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-0973ec3f5b9a20a3db5a59d8c3abd32e042.png" width="700" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>支持 Docker Compose 目标</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h3> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>添加了对 Docker-compose 目标的支持。例如，要在 compose 目标上运行 Spring Boot 应用程序，请转到运行配置，通过 <em>Manage targets </em>创建一个 compose 目标，然后运行该应用程序。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-d3ac7a9fa6e920ce37a6f6adf970c52cb84.png" width="700" referrerpolicy="no-referrer"></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<h3 style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Docker Registry V2 支持</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h3> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>添加了对 <em>Docker Registry HTTP API V2 </em>的支持，以便与 Docker 1.6+ 一起使用。可以创建简单或受密码保护的 Docker V2 注册表并执行所有常用操作，例如查看、推送和拉取映像。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-85ba249d76feede01b7b55bd188c1068717.png" width="700" referrerpolicy="no-referrer"></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<h2 style="margin-left:.5em; margin-right:0; text-align:start"><span><span><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>用户体验</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h2> 
<h3 style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>运行当前文件</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h3> 
<ul> 
 <li style="text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>为了在没有专用运行配置的情况下更轻松地运行和调试单个文件，该版本在 <em>运行/调试 </em>小部件中添加了一个新项目。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li style="text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>如果没有为项目配置运行配置，则运行和调试按钮现在也处于活动状态，并允许立即运行当前打开的文件。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li style="text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>IDE 将自动使用最适合此文件的运行配置类型，就像从上下文菜单运行文件时一样。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-f2b7d92f666a011551fef066152719157aa.png" width="700" referrerpolicy="no-referrer"></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start">要运行当前文件，请确保编辑器已聚焦，否则图标将被禁用。</p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span style="background-color:#ffffff; color:#27282c">如果项目包含运行配置，但你只想运行当前打开的文件，仍然可以从工具栏上的组合框中选择此选项。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span style="background-color:#ffffff; color:#27282c"><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-200aa92167ffeb677cde210710ae5e6de4f.png" width="700" referrerpolicy="no-referrer"></span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span style="background-color:#ffffff; color:#27282c">以这种方式运行文件时，不会创建临时运行配置。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"> </p> 
<p style="margin-left:0px; margin-right:0px; text-align:start">以上是 IntelliJ IDEA 2022.1 EAP 4 中最显着的更新。要查看完整的更新列表和引入的改进，请参阅<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Farticles%2FIDEA-A-101%2FIntelliJ-IDEA-2022.1-EAP-4-%28221.4906.8-build%29-Release-Notes" target="_blank">发行说明</a>。</p>
                                        </div>
                                      
</div>
            
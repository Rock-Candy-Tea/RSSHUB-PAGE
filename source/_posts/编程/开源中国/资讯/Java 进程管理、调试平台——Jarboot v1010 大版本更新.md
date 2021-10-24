
---
title: 'Java 进程管理、调试平台——Jarboot v1.0.10 大版本更新'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://cdn.nlark.com/yuque/0/2021/png/1305156/1631542077031-451f73cb-8eb2-4102-b3d9-be44ba6ecb29.png?x-oss-process=image%2Fresize%2Cw_1500%2Climit_0'
author: 开源中国
comments: false
date: Sun, 24 Oct 2021 22:06:00 GMT
thumbnail: 'https://cdn.nlark.com/yuque/0/2021/png/1305156/1631542077031-451f73cb-8eb2-4102-b3d9-be44ba6ecb29.png?x-oss-process=image%2Fresize%2Cw_1500%2Climit_0'
---

<div>   
<div class="content">
                                                                    
                                                        <h1><em>1.0.10 (10.24, 2021)</em></h1> 
<h2><em>修改点</em></h2> 
<p>配置文件修改jarboot.services.root-dir -> jarboot.services.workspace</p> 
<p>目录结构变更，jar文件放入bin文件夹中，增加插件目录plugins</p> 
<h2>新特性</h2> 
<h3>Console控制台支持print和退格</h3> 
<h3>支持数据库驱动放入plugins/server下以支持更多数据库</h3> 
<h3>支持插件式开发扩展，agent类型插件可扩充命令，server类型插件可增强服务端功能</h3> 
<div style="text-align:start"> 
 <p style="margin-left:0; margin-right:0"><span>插件分为</span><code><span>server</span></code><span>和</span><code><span>agent</span></code><span>两种类型，其中</span><code><span>server</span></code><span>类型的插件可用于增强Jarboot server的能力，比如增加新的HTTP接口、增加后置处理逻辑等，</span><code><span>agent</span></code><span>类型的插件可用于扩充调试命令，增加新的调试命令。</span></p> 
</div> 
<p>开发文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.yuque.com%2Fjarboot%2Fusage%2Fplugins" target="_blank">https://www.yuque.com/jarboot/usage/plugins</a></p> 
<p><img alt="plugins.png" src="https://cdn.nlark.com/yuque/0/2021/png/1305156/1631542077031-451f73cb-8eb2-4102-b3d9-be44ba6ecb29.png?x-oss-process=image%2Fresize%2Cw_1500%2Climit_0" width="2530" referrerpolicy="no-referrer"></p> 
<h3>命令输入框支持历史记录上下翻页，快速输入历史命令</h3> 
<p>命令输入框可以使用上下键获取历史命令</p> 
<h3>docker支持，识别是否在docker中运行，在docker中运行时示例程序没有界面</h3> 
<p><span style="background-color:#ffffff; color:#40485b">Docker Hub:<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fregistry.hub.docker.com%2Fr%2Fmazheng0908%2Fjarboot" target="_blank">https://registry.hub.docker.com/r/mazheng0908/jarboot</a></p> 
<div style="text-align:start"> 
 <p style="margin-left:0; margin-right:0"><span>使用Docker，镜像名为</span><strong><span>mazheng0908/jarboot</span></strong><span>，执行如下docker命令：</span></p> 
</div> 
<p><span style="color:#595959">sudo docker run -itd --name jarboot-test -p 9899:9899 mazheng0908/jarboot</span></p> 
<h3>增加自定义启动参数配置，不局限于可执行的jar文件，可以自定义执行字节码文件（***.class），可以使用classpath和-cp指定执行类</h3> 
<p>支持自定义执行参数，可以使用.class文件、jar文件，支持多种启动参数设定。</p> 
<p><img height="1056" src="https://oscimg.oschina.net/oscnet/up-2059a49202f44c121d3185343e3d08d297b.png" width="2518" referrerpolicy="no-referrer"></p> 
<h3>示例程序增加2个SPI自定义命令pow和fib，在docker中可以通过开启两个浏览器界面同时测试多个调试命令</h3>
                                        </div>
                                      
</div>
            
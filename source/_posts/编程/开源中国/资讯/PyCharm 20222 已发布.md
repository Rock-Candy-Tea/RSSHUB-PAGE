
---
title: 'PyCharm 2022.2 已发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-8be4984f942804f2ef3078a8257bffbcb14.gif'
author: 开源中国
comments: false
date: Sat, 30 Jul 2022 07:26:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-8be4984f942804f2ef3078a8257bffbcb14.gif'
---

<div>   
<div class="content">
                                                                    
                                                        <p>PyCharm 2022.2 已发布，此版本提供对 Python 3.11 语言功能和新 PyScript 框架的支持，主要有如下内容：</p> 
<ul> 
 <li>Python 3.11 支持</li> 
 <li>HTTP 客户端</li> 
 <li>用于设置远程解释器的新 UI</li> 
 <li>运行当前文件</li> 
 <li>对 PyScript 的初始支持</li> 
 <li>Jupyter 笔记本</li> 
 <li>数据库管理</li> 
 <li>Docker 优化</li> 
</ul> 
<h2>Python 3.11</h2> 
<p>PyCharm 2022.2 为 Python 3.11 的一些主要功能配备了代码洞察力，例如异常组和 except* 运算符 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpeps.python.org%2Fpep-0654%2F" target="_blank">PEP 654</a> )，以及单个 TypedDict 键的新符号 Required[] 和NotRequired[] 符号 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpeps.python.org%2Fpep-0655%2F" target="_blank">PEP 655</a> )。</p> 
<p><img alt height="420" src="https://oscimg.oschina.net/oscnet/up-8be4984f942804f2ef3078a8257bffbcb14.gif" width="700" referrerpolicy="no-referrer"></p> 
<h2>HTTP 客户端</h2> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>PyCharm 2022.2 支持 WebSocket 连接。使用此 API 可以向服务器发送消息并接收事件驱动的响应，而无需轮询服务器以获取回复。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><img alt height="420" src="https://oscimg.oschina.net/oscnet/up-4f1727de6dad076214b41acf94e4e291d30.gif" width="700" referrerpolicy="no-referrer"></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<h2><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>用于设置远程解释器的新 UI</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h2> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>PyCharm 2022.2 引入了一个新向导，用于在远程目标（例如 WSL、SSH、Docker、Docker Compose 或 Vagrant）上设置解释器，它使设置过程更加结构化且易于遵循。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<h2><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Run Current File 功能</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h2> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>新增 Run Current File 功能，用于在没有专用运行配置的情况下立即运行和调试单个文件，可从 Run/Debug 小部件获得。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><img alt height="420" src="https://oscimg.oschina.net/oscnet/up-c3672a43527eaf19201ecbc57659d3bce78.png" width="700" referrerpolicy="no-referrer"></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<h2><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>对 PyScript 的初始支持</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h2> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>PyScript是一个框架，用于使用 HTML 界面和 Pyodide、WASM 等 Web 技术在浏览器中创建丰富的 Python 应用程序。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><py-script>标签允许执行多行 Python 脚本并与页面交互。PyCharm 2022.2 可识别 Python 语法，包括 NumPy 和 Matplotlib 库。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><img alt height="421" src="https://oscimg.oschina.net/oscnet/up-fcca68f7c4ba9a783eaa0fa006ac510ebf0.gif" width="700" referrerpolicy="no-referrer"></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>更多内容可查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fpycharm%2F2022%2F07%2F2022-2%2F" target="_blank">更新博客</a>。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p>
                                        </div>
                                      
</div>
            
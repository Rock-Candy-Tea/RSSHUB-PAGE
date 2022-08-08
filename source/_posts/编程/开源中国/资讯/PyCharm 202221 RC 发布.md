
---
title: 'PyCharm 2022.2.1 RC 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1457'
author: 开源中国
comments: false
date: Mon, 08 Aug 2022 07:45:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1457'
---

<div>   
<div class="content">
                                                                                            <p>PyCharm 2022.2.1 RC 现已发布，这是 <span style="background-color:#ffffff; color:#27282c">PyCharm 2022.2 系列</span>第一个次要更新的候选版本。以下是主要修复内容：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>Docker：在 Linux 上使用 Docker 解释器时，控制台和调试器现在可以连接。[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FPY-55338" target="_blank">PY-55338</a> ]</li> 
 <li>Docker compose：端口配置现在适用于 docker-compose 解释器。[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FPY-54302" target="_blank">PY-54302</a> ]</li> 
 <li>在输出控制台选项中模拟终端不再导致控制台或调试器中出现意外缩进 [ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FPY-55322" target="_blank">PY-55322</a> ]</li> 
 <li>Debugger：调试多处理脚本不再导致 IDE 异常错误。[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FPY-55104" target="_blank">PY-55104</a> ]</li> 
 <li>Debugger：Python 控制台现在可以正确显示包含 ANSI 颜色序列的文本。[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FPY-54599" target="_blank">PY-54599</a> ]</li> 
 <li>Debugger：使用 Python 3.8 解释器调试 Django 项目现在可以顺利进行。[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FPY-40754" target="_blank">PY-40754</a> ]</li> 
 <li>PyCharm 现在可以识别非默认的 Flask 应用程序名称并相应地设置 Flask 运行配置。[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FPY-55347" target="_blank">PY-55347</a> ]</li> 
 <li>在 if 和 elif 语句中使用 __debug__不再导致无法访问的代码。[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FPY-29435" target="_blank">PY-29435</a> ]</li> 
</ul> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>此外，开发团队还正在修复：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>Docker：在调试 Docker 时，暴露的端口不起作用。[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FPY-55294%2FExposepublish-docker-port-doesnt-work" target="_blank">PY-55294</a> ]</li> 
 <li>远程解释器不支持自定义解释器路径。[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FPY-52925%2FCustom-interpreter-path-additions-not-supported-in-any-remote-interpreter-WSL-SSH" target="_blank">PY-52925</a> ]</li> 
 <li>Docker：PyCharm 无法启动项目的解释器。[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FPY-55423%2Fpython-cant-open-file-optprojectsamplepy-Errno-2-No-such-file-or-directory-using-docker-compose-interpreter-after-updating-to" target="_blank">PY-55423</a> ]</li> 
 <li>Debugger：PyCharm 在调试包含非 ASCII 编码的代码时会产生错误。[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FPY-55369" target="_blank">PY-55369</a> ]</li> 
 <li>Testing：Behave 运行配置不能只运行文件夹中的一个场景，它会运行目标目录中的所有可用文件。[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FPY-55434" target="_blank">PY-55434</a> ]</li> 
 <li>Django：尝试打开 manage.py 控制台时，使用 Docker-compose 解释器会导致错误。[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FPY-52610%2FTargets-API-Cannot-run-managepy-task-from-the-main-menu-with-Docker-interpreter" target="_blank">PY-52610</a> ]</li> 
</ul> 
<p>详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fpycharm%2F2022%2F08%2F2022-2-1-rc%2F" target="_blank">https://blog.jetbrains.com/pycharm/2022/08/2022-2-1-rc/</a></p>
                                        </div>
                                      
</div>
            
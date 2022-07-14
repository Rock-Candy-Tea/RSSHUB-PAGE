
---
title: 'FileZilla Server 1.5-rc1 发布，开源 FTP 服务器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=854'
author: 开源中国
comments: false
date: Thu, 14 Jul 2022 07:25:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=854'
---

<div>   
<div class="content">
                                                                    
                                                        <p>FileZilla Server 是一个免费开源的 FTP 和 FTPS 服务器，能够提供与服务器的安全加密连接。Filezilla Server 没有实现对 SFTP（SSH 文件传输协议）的支持。</p> 
<p>FileZilla Server 1.5-rc1 发布，更新内容如下：</p> 
<h3>新功能：</h3> 
<ul> 
 <li>Server：在失败次数过多的情况下，实现了登录尝试的限制</li> 
 <li>Server：欢迎信息中的版本号现在可以通过将配置文件中信息字段的 "has_version" 属性设置为 "false" 来手动隐藏</li> 
 <li>MSW：如果服务是在 SYSTEM 账户下运行，配置文件现在被放在 <code>%PROGRAMDATA%\\\\filezilla-server</code> 下。这是为了解决在进行 Windows 更新时，设置可能会被抹去的问题。仍然驻留在 <code>%LOCALAPPDATA%\\\\filezilla-server</code> 下的设置会自动迁移。</li> 
 <li>与模拟子进程的通信现在是异步的</li> 
 <li>Admin UI：配置对话框中的密码字段现在可以显示提示，告知用户如何保留现有的密码</li> 
</ul> 
<h3>错误修正和小改动</h3> 
<ul> 
 <li>Admin UI：修复了监听器编辑器中的崩溃</li> 
 <li>Admin UI（macOS）：为一些 wxWidgets 的错误实施了解决方法</li> 
 <li>Admin UI：system_user 的名字不能再被编辑了</li> 
 <li>不能被序列化的配置数据现在可以防止不完整的输出文件被写入磁盘</li> 
 <li>模拟进程的突然中断不再导致非预期的行为</li> 
 <li>修正了在某些情况下，由于意外的套接字事件导致的服务器崩溃问题</li> 
 <li>MSW：由于工具链的问题，使用线程本地变量的程序会在退出时崩溃。</li> 
 <li>可能的工作线程的数量已减少到最多 256 个</li> 
 <li>FTP Server：NLST 命令现在报告符合 RFC 1123 的路径</li> 
 <li>当使用命令行参数 <code>--config-version-check ignore</code> 时，如果检测到不匹配，现在会将预期的版本写入设置文件中</li> 
 <li>nix：标志图标不再被嵌入可执行文件中，而是被安装到适当的系统路径中</li> 
 <li>nix：增加了一个 <code>filezilla-server-gui.desktop</code> 文件，这样就可以通过桌面环境轻松打开 Admin UI</li> 
 <li>日志文件轮换的最大数量已经减少到一个更合理的数量，并且已经更换了更有效的轮换算法</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ffilezilla-project.org%2F" target="_blank">https://filezilla-project.org/</a></p>
                                        </div>
                                      
</div>
            
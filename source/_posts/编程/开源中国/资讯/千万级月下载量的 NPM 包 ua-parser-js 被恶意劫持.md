
---
title: '千万级月下载量的 NPM 包 ua-parser-js 被恶意劫持'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5399'
author: 开源中国
comments: false
date: Sun, 24 Oct 2021 01:46:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5399'
---

<div>   
<div class="content">
                                                                    
                                                        <p>2021 年<span style="background-color:#ffffff; color:#333333">10月22日，</span>Npm 官方仓库 ua-parser-js 被恶意劫持<span style="background-color:#ffffff; color:#333333">，多个版本被植入了挖矿脚本。</span></p> 
<h2><span style="color:#070707"><strong>什么是 </strong></span><span style="color:#333333"><strong>ua-parser-js</strong></span></h2> 
<p><span style="color:#333333">ua-parser-js 包是一个 JavaScript 库，用于 从User-Agent 中解析出浏览器、引擎、操作系统、CPU 和设备类型/模型等相关的设备信息，被广泛应用于JavaScript开发。这个</span>库非常受欢迎，每周下载数百万次，本月下载量超过 2400 万次，被用于一千多个项目，包括 Facebook、微软、亚马逊、Instagram、谷歌、Slack、Mozilla、Discord、Elastic、Intuit、Reddit 等公司的项目。</p> 
<h2><strong>攻击过程</strong></h2> 
<p><span style="color:#070707">10 月 22 日，攻击者劫持了 NPM 某位开发者的账号，并发布了恶意版本的 </span><span style="color:#333333">ua-parser-js</span><span style="color:#070707"> NPM 库，这个库会在 Linux 和 Windows 设备上自动安装矿工程序和盗取密码的木马。</span></p> 
<p><span style="color:#070707">受感染的软件包安装在用户的设备上时，preinstall.js 脚本会检查设备上使用的操作系统类型，然后启动 Linux shell 脚本或 Windows 批量处理文件。</span></p> 
<p><span style="color:#070707">如果软件包在 Linux 设备上，它将执行 preinstall.sh 脚本，来检查用户是不是在俄罗斯、乌克兰、白俄罗斯和哈萨克斯坦这几个地方，不在的话就从 </span><span style="color:#333333"><code>http://159.148.186.228/download/jsextension</code> </span><span style="color:#070707">下载 </span><strong>jsextension </strong>程序来挖矿。jsextension 是一个<span style="color:#3e3e3e">门罗币挖矿程序，为了避免被及时侦测到，它只会占用设备 </span><span style="color:#070707">50%</span><span style="color:#3e3e3e"> CPU。</span></p> 
<p><span style="color:#070707">如果软件包在 Windows 设备上，它也会自动下载 </span><strong>jsextension.exe ，除了这个自动挖矿工具，它还会下载 </strong><span style="color:#070707">sdd.dll 文件，这个文件会被命名为 create.dll 。这个 DLL 是一个盗号木马，会尝试偷取存储在设备上的密码，包括 FTP 客户端、VNC、聊天软件、电子邮件客户端和浏览器等等，DLL 还会执行 PowerShell 脚本从 Windows 证书管理器中窃取密码。</span></p> 
<h2><strong>如何预防/补救？</strong></h2> 
<p><span style="color:#070707">建议所有使用 </span><span style="color:#333333">ua-parser-js</span><span style="color:#070707"> 库的用户都检查一下自己的项目有没有被感染。</span></p> 
<ul> 
 <li style="text-align:justify">确认于2021 年 10 月 22 日 是否安装或更新过 ua-parser-js 包。</li> 
 <li style="text-align:justify">确认是否有相关组件依赖于 ua-parser-js 包。</li> 
 <li style="text-align:justify">检查设备里有没有 <strong>jsextension.exe</strong> (Windows) 或 <strong>jsextension</strong> (Linux)，并彻底删除。</li> 
 <li style="text-align:justify">Windows 用户请查找 <strong>create.dll </strong>文件并彻底删除。</li> 
</ul> 
<p><span style="color:#070707"><strong>已经受感染的 Linux 和 Windows 用户，所有在被感染设备登陆过的账号，都要更改密码！</strong></span></p>
                                        </div>
                                      
</div>
            
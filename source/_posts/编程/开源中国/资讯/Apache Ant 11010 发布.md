
---
title: 'Apache Ant 1.10.10 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2543'
author: 开源中国
comments: false
date: Tue, 20 Apr 2021 23:38:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2543'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Apache Ant 1.10.10 已发布。Apache Ant 是一个将软件编译、测试、部署等步骤联系在一起加以自动化的一个工具，大多用于 Java 环境中的软件开发。</p> 
<p>Apache Ant 团队目前维护着两条开发线，分别为 1.9.x 与 1.10.x，前者要求 Java 5，后者要求 Java 8。一般来说 1.9.x 主要是修改 bug，新增特性会体现在 1.10.x 中，目前建议使用的版本为 1.10.10，除非开发环境要求 Java 8。</p> 
<p>Apache Ant 1.10.10 主要更新内容是修复错误，以及部分功能增强。</p> 
<p>Bugfix</p> 
<ul> 
 <li>修复如果获取位于根目录下的文件，​SCP (with sftp=true) 任务会失败的问题</li> 
 <li>如果 javac 任务创建的参数文件（内部）没有引用 # 字符，则会创建失败，此错误现已被修复</li> 
 <li>确保 LegacyXmlResultFormatter 对 XML 中的非法字符进行编码，与 JUnit5 内置格式化器的方式相同</li> 
 <li>LegacyXmlResultFormatter 不再对 system-err 和 system-out 中的 <>& 进行双重编码</li> 
 <li>修复了 junitlauncher 任务 legacy-xml 格式化工具中的一个 bug，即代表 @Parameterized JUnit4 测试的测试案例没有在 XML 中被报告</li> 
 <li>修复发布到 Maven 中央仓库的 ant-testutil-sources.jar 不包含任何源文件的错误</li> 
 <li><http> 条件没有遵循从 http 到 https 的重定向</li> 
 <li>修复使用 legacy-xml reporter 时，junitlauncher 任务可能出现的死锁问题</li> 
</ul> 
<p>除了上述修复的错误，还有部分其他变化，<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmail-archives.apache.org%2Fmod_mbox%2Fwww-announce%2F202104.mbox%2F%253C9f001cf4-f562-2164-5662-a8ec9ca8ee4f%40apache.org%253E" target="_blank">详情点此查看</a>。</p> 
<p>源码和二进制文件下载</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fant.apache.org%2Fbindownload.cgi" target="_blank">https://ant.apache.org/bindownload.cgi</a><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fant.apache.org%2Fsrcdownload.cgi" target="_blank">https://ant.apache.org/srcdownload.cgi</a></p>
                                        </div>
                                      
</div>
            
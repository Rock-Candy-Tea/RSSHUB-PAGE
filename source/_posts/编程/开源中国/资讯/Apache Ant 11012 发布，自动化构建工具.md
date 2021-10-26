
---
title: 'Apache Ant 1.10.12 发布，自动化构建工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=279'
author: 开源中国
comments: false
date: Tue, 26 Oct 2021 07:07:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=279'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="margin-left:0px; margin-right:0px; text-align:start">Apache Ant 1.10.12 已发布。</p> 
<p style="margin-left:0px; margin-right:0px; text-align:start">目前 Apache Ant 团队正在维护两个分支，分别是 1.9.x 和 1.10.x。前者要求 Java 5 以上，后者要求 Java 8 以上。1.9.x 系列主要是修复 bug，1.10.x 会增加新功能，两个分支都基于 Ant 1.9.7。除非在构建过程中要求 Java 8 之前的版本，否则最好还是使用官方推荐的 1.10.x 分支。</p> 
<p>此次发布的 1.10.12 主要是修复 bug。</p> 
<p><strong>已修复的错误</strong></p> 
<ul> 
 <li>即便"followRedirects"属性被设置为"false"，http condition 也会跟随重定向。此问题现已修复。</li> 
 <li>确保将 build.compiler 设置为与 extJavac 或现代相对应的完全限定类名，与使用较短的别名具有相同的效果</li> 
 <li>防止 org.apache.tools.ant.IntrospectionHelper 中的潜在死锁</li> 
</ul> 
<p><strong>其他变更</strong></p> 
<ul> 
 <li>修改 AntClassLoader#findResources() 方法的实现，优化其潜在的性能问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.jenkins.io%2Fbrowse%2FJENKINS-22310%3FfocusedCommentId%3D197405%26page%3Dcom.atlassian.jira.plugin.system.issuetabpanels%3Acomment-tabpanel%23comment-197405" target="_blank">详情点此查看</a></li> 
 <li>AntClassLoader 已实现 ClassLoader#findResource(String) 方法</li> 
 <li>Ant 在可能的情况下会尽量避免文件名的规范化 (file name canonicalization)</li> 
 <li>当"failonwarning"设置为 true 时，javadoc task 会在 STDERR stream 中寻找警告信息</li> 
 <li>tar task 现已支持保留嵌套 tarfilesets 的符号链接</li> 
</ul> 
<p><strong>下载地址</strong></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fant.apache.org%2Fbindownload.cgi" target="_blank">https://ant.apache.org/bindownload.cgi</a>（二进制文件）<br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fant.apache.org%2Fbindownload.cgi" target="_blank">https://ant.apache.org/srcdownload.cgi</a>（源代码）</p>
                                        </div>
                                      
</div>
            
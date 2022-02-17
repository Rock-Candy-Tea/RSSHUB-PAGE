
---
title: 'Git LFS 3.1 发布，对大文件进行版本控制的 Git 扩展'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5682'
author: 开源中国
comments: false
date: Thu, 17 Feb 2022 07:20:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5682'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Git LFS 是一个命令行扩展，用于使用 Git 管理大文件。这个版本是一个功能更新版本，其中包括为 Debian 11 提供的新的 ARM64 软件包、新的本地化基础架构，以及改进的 netrc 支持，此外还有一些错误修复并解决了 v3.0.2 中引入的 git lfs 迁移导入的性能退步问题。具体更新内容如下：</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">功能：</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>从 Negotiate 退回到 Basic</li> 
 <li>增加对本地化的基本支持</li> 
 <li>增加对 ARM64 Debian 软件包的支持</li> 
 <li>netrc：考虑同一台机器可能有不同的登录名</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">错误修复</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>修复迁移过程中以执行文件模式合并 .gitattributes 的问题</li> 
 <li>修复 migrate 导入速度退步问题</li> 
 <li>修复错别字</li> 
 <li>将错误检查移至使用该值之前</li> 
 <li>migrate import：不允许使用 --above 的路径过滤器</li> 
 <li>避免在使用带有 --to 的 checkout 但没有路径的情况下出现 panic</li> 
 <li>creds：更好地处理缺乏 askpass 帮助器的问题</li> 
 <li>post-checkout：不要修改未跟踪的文件的权限</li> 
 <li>使用 gitattributes 文件路径匹配迁移过滤器选项</li> 
 <li>避免 git lfs env 中的错误</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">其他</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>构建缺失的手册页面并纠正 HTML 渲染</li> 
 <li>更新并标记要翻译的信息字符串</li> 
 <li>标记几乎所有的字符串以备翻译</li> 
 <li>.github/workflows：切换到 action/checkout@v2</li> 
 <li>脚本/packagecloud：为最新的发行版更新</li> 
 <li>filter-process：不在修复的版本上打印大文件警告</li> 
 <li>ssh：尽可能避免使用<span> </span><code>--</code></li> 
 <li>停止支持 Go 1.13 以下版本</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgit-lfs%2Fgit-lfs%2Fblob%2Fmain%2FCHANGELOG.md" target="_blank">https://github.com/git-lfs/git-lfs/blob/main/CHANGELOG.md</a></p>
                                        </div>
                                      
</div>
            
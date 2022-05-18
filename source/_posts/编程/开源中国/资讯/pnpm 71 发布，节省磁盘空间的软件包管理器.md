
---
title: 'pnpm 7.1 发布，节省磁盘空间的软件包管理器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8604'
author: 开源中国
comments: false
date: Wed, 18 May 2022 07:22:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8604'
---

<div>   
<div class="content">
                                                                    
                                                        <p>pnpm 是一个快速、节省磁盘空间的软件包管理器。它使用一个内容可寻址的文件系统来存储磁盘上所有模块目录的所有文件。当使用 npm 或 Yarn 时，如果你有 100 个使用 lodash 的项目，你将在磁盘上有 100 份 lodash 的拷贝，而使用 pnpm 时，lodash 将被存储在一个内容可寻址的存储器中。</p> 
<p>pnpm 7.1 正式发布，更新内容如下：</p> 
<ul> 
 <li>fix: 应该将有关安装的信息打印到 stderr <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpnpm%2Fpnpm%2Fpull%2F4696" target="_blank">#4696</a></li> 
 <li>fix: 之前 <code>pnpm setup</code>会破坏包含非 ASCII 字符的 %PATH%，现已修复 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpnpm%2Fpnpm%2Fpull%2F4699" target="_blank">#4699</a></li> 
 <li>fix(setup): 更新当前的 shell，而不是首选的 shell <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpnpm%2Fpnpm%2Fpull%2F4701" target="_blank">#4701</a></li> 
 <li>refactor: 使用 @yarnpkg/extensions 而不是 @yarnpkg/plugin-compat <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpnpm%2Fpnpm%2Fpull%2F4710" target="_blank">#4710</a></li> 
 <li>pnpm run -stream 应该以目录名作为前缀 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpnpm%2Fpnpm%2Fpull%2F4703" target="_blank">#4703</a></li> 
 <li>feat: 增加了对 package.json 中 libc 字段的支持 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpnpm%2Fpnpm%2Fpull%2F4605" target="_blank">#4605</a></li> 
 <li>fix: 让 pnpm setup 没有乱码 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpnpm%2Fpnpm%2Fpull%2F4712" target="_blank">#4712</a></li> 
 <li>fix(dlx): pnpm dlx 应该与 git-hosted 的软件包一起工作 #<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpnpm%2Fpnpm%2Fpull%2F4717" target="_blank">4717</a></li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpnpm%2Fpnpm%2Freleases%2Ftag%2Fv7.1.0" target="_blank">https://github.com/pnpm/pnpm/releases/tag/v7.1.0</a></p>
                                        </div>
                                      
</div>
            
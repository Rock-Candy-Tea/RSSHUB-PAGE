
---
title: 'pnpm 7.8 发布，节省磁盘空间的软件包管理器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1911'
author: 开源中国
comments: false
date: Wed, 03 Aug 2022 07:54:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1911'
---

<div>   
<div class="content">
                                                                                            <p>pnpm 是一个快速、节省磁盘空间的软件包管理器。它使用一个内容可寻址的文件系统来存储磁盘上所有模块目录的所有文件。当使用 npm 或 Yarn 时，如果你有 100 个使用 lodash 的项目，你将在磁盘上有 100 份 lodash 的拷贝，而使用 pnpm 时，lodash 将被存储在一个内容可寻址的存储器中。</p> 
<p>pnpm 7.8 正式发布，更新内容如下：</p> 
<h3>小改动</h3> 
<ul> 
 <li>当<code>publishConfig.directory</code>被设置时，只有当<code>publishConfig.linkDirectory</code>被设置为<code>true</code>时，才能将其与其他工作区项目进行符号链接。</li> 
</ul> 
<h3>补丁变化</h3> 
<ul> 
 <li>当软件包有 publishConfig.directory 字段时，不要错误地识别过期的 lockfile</li> 
 <li>当配置文件包含一个不存在的环境变量的设置时，不要崩溃</li> 
</ul> 
<h3>其他变化</h3> 
<ul> 
 <li>修复 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpnpm%2Fpnpm%2Fpull%2F5128" target="_blank">#5128</a> 中出现的错字</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpnpm%2Fpnpm%2Freleases%2Ftag%2Fv7.8.0" target="_blank">https://github.com/pnpm/pnpm/releases/tag/v7.8.0</a></p>
                                        </div>
                                      
</div>
            
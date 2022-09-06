
---
title: 'pnpm 7.10 发布，节省磁盘空间的软件包管理器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3220'
author: 开源中国
comments: false
date: Tue, 06 Sep 2022 07:15:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3220'
---

<div>   
<div class="content">
                                                                                            <p>pnpm 是一个快速、节省磁盘空间的软件包管理器。它使用一个内容可寻址的文件系统来存储磁盘上所有模块目录的所有文件。当使用 npm 或 Yarn 时，如果你有 100 个使用 lodash 的项目，你将在磁盘上有 100 份 lodash 的拷贝，而使用 pnpm 时，lodash 将被存储在一个内容可寻址的存储器中。</p> 
<p>pnpm 7.10 正式发布，更新内容如下：</p> 
<h3>改变：</h3> 
<ul> 
 <li> <p>支持新的基于时间的解析策略。</p> <p>当 <code>resolution-mode</code> 被设置为 <code>time-based</code> 的时候，pnpm 将以如下方式解析依赖关系：</p> 
  <ul> 
   <li>直接依赖关系将被解析为其最低版本。因此，如果依赖项中有 <code>foo@^1.1.0</code>，那么 <code>1.1.0</code> 将被安装。</li> 
   <li>子依赖关系将从最后一个直接依赖关系发布之前的版本中解析。</li> 
  </ul> <p>有了这种解析模式，使用热缓存的安装会更快。它也减少了子依赖劫持的机会，因为子依赖只有在直接依赖被更新时才会被更新。</p> <p>这种解析模式只对 npm 的完整元数据起作用。所以在某些情况下会比较慢。然而，如果你使用 Verdaccio v5.15.1 或更新的版本，你可以将 <code>registry-supports-time-field</code> 设置为 <code>true</code>，这样会非常快。</p> </li> 
 <li> <p>用 <code>remove</code> 命令增强 <code>pnpm env</code>。要删除由 pnpm 安装的 Node.js 版本，请运行： <code>pnpm env remove --global <node.js version></code></p> </li> 
</ul> 
<h3>补丁更改</h3> 
<ul> 
 <li><code>pnpm store prune</code> 应删除所有缓存的元数据</li> 
 <li>当注入的工作区项目在 prod 和 peer 依赖中具有相同的依赖性时，不要修改其 manifest</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpnpm%2Fpnpm%2Freleases%2Ftag%2Fv7.10.0" target="_blank">https://github.com/pnpm/pnpm/releases/tag/v7.10.0</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            
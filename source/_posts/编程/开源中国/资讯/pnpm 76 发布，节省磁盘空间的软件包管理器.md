
---
title: 'pnpm 7.6 发布，节省磁盘空间的软件包管理器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3095'
author: 开源中国
comments: false
date: Sat, 23 Jul 2022 07:40:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3095'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">pnpm 是一个快速、节省磁盘空间的软件包管理器。它使用一个内容可寻址的文件系统来存储磁盘上所有模块目录的所有文件。当使用 npm 或 Yarn 时，如果你有 100 个使用 lodash 的项目，你将在磁盘上有 100 份 lodash 的拷贝，而使用 pnpm 时，lodash 将被存储在一个内容可寻址的存储器中。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">pnpm 7.6 正式发布，更新内容如下：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><code>pnpm rebuild</code><span> </span>接受<span> </span><code>--store-dir</code></li> 
 <li>fix(deploy): 默认包含所有 deps</li> 
 <li>chore(deps): 升级 nock 到 v13</li> 
 <li>修复：记录 HTTP 错误的更多信息</li> 
 <li>修复：记录 -r 选项</li> 
 <li>chore(deps): 将 sinon 升级到 v14</li> 
 <li>fix(audit): 为 pnpm-audit 添加认证</li> 
 <li>支持的新设置：<span> </span><code>prefer-symlinked-executables</code></li> 
 <li>chore: 更新 pnpm-workspace.yaml</li> 
 <li>添加<span> </span><code>lockfile-include-tarball-url</code><span> </span>选项</li> 
 <li>修正：当<span> </span><code>auto-install-peers=true</code><span> </span>时，自动安装根对等程序</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpnpm%2Fpnpm%2Freleases%2Ftag%2Fv7.6.0" target="_blank">https://github.com/pnpm/pnpm/releases/tag/v7.6.0</a></p>
                                        </div>
                                      
</div>
            

---
title: 'pnpm 7.0 发布，节省磁盘空间的软件包管理器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3289'
author: 开源中国
comments: false
date: Sat, 07 May 2022 07:09:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3289'
---

<div>   
<div class="content">
                                                                                            <p>pnpm 是一个快速、节省磁盘空间的软件包管理器。它使用一个内容可寻址的文件系统来存储磁盘上所有模块目录的所有文件。当使用 npm 或 Yarn 时，如果你有 100 个使用 lodash 的项目，你将在磁盘上有 100 份 lodash 的拷贝，而使用 pnpm 时，lodash 将被存储在一个内容可寻址的存储器中。</p> 
<p>pnpm 7.0 正式发布，更新内容如下：</p> 
<h3>主要变化</h3> 
<ul> 
 <li>不支持 Node.js 12</li> 
 <li>运行 <code>pnpm -r exec|run|add</code> 时，默认排除了 root 包</li> 
 <li>默认情况下， <code>embed-readme</code> 设置为 <code>false</code></li> 
 <li>当使用 <code>pnpm run <script></code> 时，脚本名称后面的所有命令行参数现在都被传递到脚本的 argv 中，甚至包括 <code>-</code>。</li> 
 <li>默认情况下，Side effects 缓存是开启的。要关闭它，请使用 <code>side-effects-cache=false</code></li> 
 <li><code>npm_config_argv</code> 环境变量没有为脚本设置</li> 
 <li><code>pnpx</code> 现在只是 <code>pnpm dlx</code> 的一个别名</li> 
 <li><code>pnpm install -g pkg</code> 将只把全局命令添加到预定义的位置</li> 
 <li><code>pnpm pack</code> 只有在文件是 bin 或列在 <code>publishConfig.executableFiles</code> 数组中时，才会将其打包为可执行文件</li> 
 <li><code>W</code> 不再是 <code>-ignore-workspace-root-check</code> 的别名了</li> 
 <li>允许在一个与软件包名称不匹配的目录中执行生命周期脚本。以前只有在使用 <code>--unsafe-perm</code> CLI 选项时才允许这样做</li> 
 <li><code>strict-peer-dependencies</code> 默认为 <code>true</code></li> 
 <li>根工作区项目的依赖不用于解决其他工作区项目的 peer dependencies</li> 
 <li>不要默认将类型提升到 <code>node_modules</code> 的根目录</li> 
 <li>将全局存储的位置从 <code>~/.pnpm-store</code> 更改为 <code><pnpm home directory>/store</code> 
  <ul> 
   <li>在 Linux 上，默认是 <code>~/.local/share/pnpm/store</code></li> 
   <li>在 Windows 上： <code>%LOCALAPPDATA%/pnpm/store</code></li> 
   <li>在 macOS 上： <code>~/Library/pnpm/store</code></li> 
  </ul> </li> 
 <li>Lockfile 版本升级到了 5.4</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpnpm%2Fpnpm%2Freleases" target="_blank">https://github.com/pnpm/pnpm/releases</a></p>
                                        </div>
                                      
</div>
            
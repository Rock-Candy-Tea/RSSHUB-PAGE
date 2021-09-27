
---
title: 'Git LFS 3.0.0 发布，对大文件进行版本控制的 Git 扩展'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4101'
author: 开源中国
comments: false
date: Mon, 27 Sep 2021 07:30:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4101'
---

<div>   
<div class="content">
                                                                                            <p>Git LFS 是一个命令行扩展，用于使用 Git 管理大文件。Git LFS 3.0.0 版本是一个重要的新版本，引入了几个新特性，具体更新内容如下：</p> 
<h3>向后兼容的改动：</h3> 
<ul> 
 <li>对 NTLM 的支持已被完全删除</li> 
 <li>当使用 SSH URL（即以 <code>ssh://</code> 开头的语法）时，在调用 <code>git-lfs-authenticate</code> 或 <code>git-lfs-transfer</code> 时不会去掉前面的斜线。这与 Git 在通过 SSH 调用命令时的行为一致</li> 
 <li><code>git lfs fsck</code> 现在会额外检查指针是否符合规范，以及那些应该是 LFS 文件的文件是否符合规范。</li> 
 <li>模式匹配应该更加严格，应该与 <code>.gitattributes</code> 或 <code>.gitignore</code> 的行为相匹配</li> 
 <li>Git LFS 现在会将 Git LFS 仓库格式的版本写入仓库。这样做是为了允许将来在不兼容的情况下进行扩展。</li> 
 <li>……</li> 
</ul> 
<h3>功能：</h3> 
<ul> 
 <li>将软件包版本提升到 v3</li> 
 <li>更新 OS 版本</li> 
 <li>增加对 Debian 11 的支持</li> 
 <li>支持锁定和解锁多个文件</li> 
 <li>增加对 Windows ARM64 的支持</li> 
 <li>LFS 仓库格式版本</li> 
 <li>纯粹基于 SSH 的协议</li> 
 <li>让 fsck 能够检查无效的指针</li> 
 <li>在 migrate info 命令中增加 -fixup 选项</li> 
 <li>允许在 migrate info 命令中单独报告 LFS 指针的情况</li> 
 <li>为默认远程添加配置变量</li> 
 <li>让 lfshttp 包的构建更加便捷</li> 
 <li>……</li> 
</ul> 
<h3><strong>Bug 修复：</strong></h3> 
<ul> 
 <li>filepathfilter：总是使用与 Git 兼容的模式匹配</li> 
 <li>debian 和 rpm：向 <code>install</code> 和 <code>uninstall</code> 传递 <code>--skip-repo</code></li> 
 <li>修复 prune 中的挂起</li> 
 <li>在解析日志和锚点差异正则表达式时禁用 ANSI 色码</li> 
 <li>go.mod：将 gitobj 升级到 v2.0.2</li> 
 <li>修复多路径和绝对路径的锁定问题</li> 
 <li>migrate import：让 <code>--above</code> 只影响单个文件</li> 
 <li>fs：清理时不要太激进</li> 
 <li>让 blobSizeCutoff 的所有检查保持一致</li> 
 <li>修正对 "migrate info" 命令的 -top 选项的处理</li> 
 <li>像 Git 那样对 Windows 路径进行规范化处理</li> 
 <li>lfsapi：不对重复但相同的别名发出警告</li> 
 <li>……</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgit-lfs%2Fgit-lfs%2Fblob%2Fmain%2FCHANGELOG.md" target="_blank">https://github.com/git-lfs/git-lfs/blob/main/CHANGELOG.md</a></p>
                                        </div>
                                      
</div>
            

---
title: 'libgit2 v1.3.0 发布，跨平台、可链接的 Git 库实现'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5706'
author: 开源中国
comments: false
date: Wed, 29 Sep 2021 06:50:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5706'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">libgit2 是一个可以在应用程序中使用的跨平台、可链接的 Git 库实现。libgit2 1.3.0 版本正式发布，这个版本包括多个错误修复，仅有少量的新功能更新，有助于用户有序地过渡到 v2.0 版本。</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">新功能</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>支持自定义 git 扩展 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flibgit2%2Flibgit2%2Fpull%2F6031" target="_blank">#6031</a></li> 
 <li>引入 <code>git_email_create</code>; 弃用 <code>git_diff_format_email</code> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flibgit2%2Flibgit2%2Fpull%2F6061" target="_blank">#6061</a></li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">弃用的 API</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><code>git_oidarray_free</code> 已被弃用; 调用者应使用 <code>git_oidarray_dispose</code></li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">错误修正</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>在释放缓冲区前检查<span> </span><code>threadstate->error_t.message</code><span> </span>是否为<span> </span><code>git_buf__initbuf</code><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flibgit2%2Flibgit2%2Fpull%2F6029" target="_blank">#6029</a></li> 
 <li>将<span> </span><code>git_remote_name_is_valid</code><span> </span>标记为<span> </span><code>GIT_EXTERN</code><span> </span> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flibgit2%2Flibgit2%2Fpull%2F6032" target="_blank">#6032</a></li> 
 <li>修复多行的配置解析，其中包含多个引用的注释字符 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flibgit2%2Flibgit2%2Fpull%2F6043" target="_blank">#6043</a></li> 
 <li>索引器：避免每个<span> </span><code>git_indexer_append</code><span> </span>调用一个<span> </span><code>mmap(2)</code>/<span> </span><code>munmap(2)</code>对<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flibgit2%2Flibgit2%2Fpull%2F6039" target="_blank">#6039</a></li> 
 <li>合并：在解决重名时检查文件模式 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flibgit2%2Flibgit2%2Fpull%2F6060" target="_blank">#6060</a></li> 
 <li>允许在连接分离的远程仓库时使用代理选项 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flibgit2%2Flibgit2%2Fpull%2F6058" target="_blank">#6058</a></li> 
 <li>win32：允许空环境变量 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flibgit2%2Flibgit2%2Fpull%2F6063" target="_blank">#6063</a></li> 
 <li>修复已弃用的 API <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flibgit2%2Flibgit2%2Fpull%2F6066" target="_blank">#6066</a></li> 
 <li>在过滤器选项中使用<span> </span><code>git_oid</code>，而不是<span> </span><code>git_oid *</code> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flibgit2%2Flibgit2%2Fpull%2F6067" target="_blank">#6067</a></li> 
 <li>diff: 更新<span> </span><code>GIT_DIFF_IGNORE_BLANK_LINES</code><span> </span> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flibgit2%2Flibgit2%2Fpull%2F6068" target="_blank">#6068</a></li> 
 <li>属性查询总是在相对路径上进行 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flibgit2%2Flibgit2%2Fpull%2F6073" target="_blank">#6073</a></li> 
 <li>在查询属性时处理长路径 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flibgit2%2Flibgit2%2Fpull%2F6075" target="_blank">#6075</a></li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">代码清理</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>在内部使用缓冲区 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flibgit2%2Flibgit2%2Fpull%2F6047" target="_blank">#6047</a></li> 
 <li>修正指针的编码方式 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flibgit2%2Flibgit2%2Fpull%2F6045" target="_blank">#6045</a></li> 
 <li>使用 typeof GNUC 关键字以兼容 ISO C <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flibgit2%2Flibgit2%2Fpull%2F6041" target="_blank">#6041</a></li> 
 <li>……</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">CI 改进</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>ci: 从<span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.libssh2.org%2F" target="_blank">www.libssh2.org</a><span> </span>拉取 libssh2 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flibgit2%2Flibgit2%2Fpull%2F6064" target="_blank">#6064</a></li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">文档变化</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>更新<span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Freadme.md%2F" target="_blank">README.md</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flibgit2%2Flibgit2%2Fpull%2F6050" target="_blank">#6050</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flibgit2%2Flibgit2%2Freleases%2Ftag%2Fv1.3.0" target="_blank">https://github.com/libgit2/libgit2/releases/tag/v1.3.</a></p>
                                        </div>
                                      
</div>
            
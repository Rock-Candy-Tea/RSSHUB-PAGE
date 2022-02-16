
---
title: 'libgit2 v1.4.0 发布，跨平台、可链接的 Git 库实现'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=310'
author: 开源中国
comments: false
date: Wed, 16 Feb 2022 07:16:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=310'
---

<div>   
<div class="content">
                                                                                            <p>libgit2 是一个可以在应用程序中使用的跨平台、可链接的 Git 库实现。libgit2 1.4.0 版本正式发布，这个版本包括一些错误修复和功能更新，提高了与 git 的兼容性，并有助于用户有序地过渡到 v2.0 版本。</p> 
<h3>新功能</h3> 
<ul> 
 <li>diff: 更新重命名限制为 1000，以符合 git 的行为 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flibgit2%2Flibgit2%2Fpull%2F6092" target="_blank">#6092</a></li> 
 <li>odb: 支持在不刷新的情况下检查对象的存在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flibgit2%2Flibgit2%2Fpull%2F6107" target="_blank">#6107</a></li> 
 <li>object: 提供一个底层机制来验证原始对象是否有效 (<code>git_object_rawcontent_is_valid</code>) <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flibgit2%2Flibgit2%2Fpull%2F6128" target="_blank">#6128</a></li> 
 <li>blob: 提供一个识别二进制内容的函数 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flibgit2%2Flibgit2%2Fpull%2F6142" target="_blank">#6142</a></li> 
 <li>status: 在 <code>git_status_options</code> 中增加 <code>rename_threshold</code> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flibgit2%2Flibgit2%2Fpull%2F6158" target="_blank">#6158</a></li> 
 <li>remote: 支持 <code>http.followRedirects</code> ( <code>false</code> 和 <code>initial</code>)，并默认情况下遵循初始重定向 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flibgit2%2Flibgit2%2Fpull%2F6175" target="_blank">#6175</a></li> 
 <li>remote: 支持带有端口的 scp 样式路径 (<code>[git@github.com:22]:libgit2/libgit2</code>) <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flibgit2%2Flibgit2%2Fpull%2F6167" target="_blank">#6167</a></li> 
 <li>win32: 更新 git for windows 配置文件位置兼容性 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flibgit2%2Flibgit2%2Fpull%2F6180" target="_blank">#6180</a></li> 
 <li>merge: 支持 zdiff3 conflict 样式 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flibgit2%2Flibgit2%2Fpull%2F6195" target="_blank">#6195</a></li> 
 <li>remote: 支持通过对象 ID 获取 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flibgit2%2Flibgit2%2Fpull%2F6203" target="_blank">#6203</a></li> 
</ul> 
<h3>弃用的 API</h3> 
<ul> 
 <li><code>git_index_checksu</code>已弃用</li> 
 <li><code>git_indexer_hash</code>已弃用</li> 
 <li><code>git_packbuilder_hash</code>已弃用</li> 
</ul> 
<h3>错误修复</h3> 
<ul> 
 <li>修复了 src/threadstate.c 中的一个 gcc 11 警告 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flibgit2%2Flibgit2%2Fpull%2F6115" target="_blank">#6115</a></li> 
 <li>修复了 src/thread.h 中的一个 gcc 11 警告 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flibgit2%2Flibgit2%2Fpull%2F6116" target="_blank">#6116</a></li> 
 <li>cmake: 重新启用 WinHTTP <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flibgit2%2Flibgit2%2Fpull%2F6120" target="_blank">#6120</a></li> 
 <li>当模板目录不存在时，修复 repo init <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flibgit2%2Flibgit2%2Fpull%2F6106" target="_blank">#6106</a></li> 
 <li>cmake: 使用项目特定的 root 变量而不是 CMAKE_SOURCE_DIR <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flibgit2%2Flibgit2%2Fpull%2F6146" target="_blank">#6146</a></li> 
 <li>remotes: 修正 InsteadOf/pushInsteadOf 的处理 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flibgit2%2Flibgit2%2Fpull%2F6101" target="_blank">#6101</a></li> 
 <li>git_commit_summary: 忽略有空格的行 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flibgit2%2Flibgit2%2Fpull%2F6125" target="_blank">#6125</a></li> 
 <li>修复 git_status_list_new 不区分大小写的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flibgit2%2Flibgit2%2Fpull%2F6159" target="_blank">#6159</a></li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flibgit2%2Flibgit2%2Freleases%2Ftag%2Fv1.4.0" target="_blank">https://github.com/libgit2/libgit2/releases/tag/v1.4.0</a></p>
                                        </div>
                                      
</div>
            
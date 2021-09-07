
---
title: 'libgit2 v1.2.0 发布，跨平台、可链接的 Git 库实现'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3106'
author: 开源中国
comments: false
date: Tue, 07 Sep 2021 07:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3106'
---

<div>   
<div class="content">
                                                                                            <p>libgit2 是一个可以在应用程序中使用的跨平台、可链接的 Git 库实现。libgit2 1.2.0 版本包括许多新特性：特别是对 commit graphs、multi-pack-index 和 <code>core.longpaths</code> 的支持。</p> 
<p>v1.2.0 将是 v1 下的最后一个版本更新，下一个版本更新将会是 v2.0，届时将删除废弃的 API，并包括一些重大变化。</p> 
<h3>新功能：</h3> 
<ul> 
 <li>winhttp：支持可选的客户证书</li> 
 <li>增加对其他 SSH 主机密钥类型的支持</li> 
 <li>处理 ipv6 地址</li> 
 <li>zlib: 增加对 Chromium 的 zlib 实现构建的支持</li> 
 <li>commit-graph: 引入 commit-graph 文件解析器</li> 
 <li>patch：添加所有者访问器</li> 
 <li>commit-graph: 支持在 commit-graph 中查询条目</li> 
 <li>commit-graph: 引入 <code>git_commit_graph_needs_refresh()</code></li> 
 <li>工作目录路径验证</li> 
 <li>在 Windows 上支持 <code>core.longpaths</code></li> 
 <li>git_reference_create_matching: 将 all-zero 的 OID 视为 "必须不存在 "</li> 
 <li>diff: 增加忽略空白行修改的选项</li> 
 <li>commit-graph: 在 revwalks 中使用 commit-graph</li> 
 <li>commit-graph: 引入 <code>git_commit_list_generation_cmp</code></li> 
 <li>graph: 创建 <code>git_graph_reachable_from_any()</code></li> 
 <li>支持从特定的 commit 中读取属性</li> 
 <li>[Branch] 用格式化的上游分支</li> 
 <li>动态加载 OpenSSL（可选）</li> 
 <li>当指定分支时，将 refs/remotes/origin/HEAD 设为默认分支</li> 
 <li>midx: 增加编写 multi-pack-index 文件的方法</li> 
 <li>在认证失败时使用错误代码 <code>GIT_EAUTH</code></li> 
 <li>midx: 引入 <code>git_odb_write_multi_pack_index()</code></li> 
 <li>mbedTLS：修复设置证书目录</li> 
 <li>remote：引入 <code>remote_ready_cb</code>，废除 <code>resolve_url</code> 回调</li> 
 <li>引入 <code>create_commit_cb</code>，废除 <code>signing_cb</code></li> 
 <li>commit-graph：增加写 commit-graph 文件的方法</li> 
 <li>添加 NO_PROXY 环境支持</li> 
 <li>更新代理配置</li> 
</ul> 
<h3>废弃的 API</h3> 
<ul> 
 <li>revspec：将 git_revparse_mode_t 更名为 git_revspec_t</li> 
 <li>tree: 废弃 <code>git_treebuilder_write_with_buffer</code></li> 
 <li>废弃 <code>is_valid_name</code> 函数；用 <code>name_is_valid</code> 函数代替</li> 
 <li>停止将 git_buf 作为用户输入</li> 
 <li>remote：引入 remote_ready_cb，废弃 resolve_url 回调</li> 
 <li>引入 <code>create_commit_cb</code>，废弃 <code>signing_cb</code></li> 
 <li>buf：废弃公共的 git_buf 写入函数</li> 
</ul> 
<h3>文档改进</h3> 
<ul> 
 <li>更新 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Freadme.md" target="_blank">README.md</a> 以增加 Delphi 绑定</li> 
 <li>修复文档格式</li> 
 <li>文档：修复不正确的注释标记</li> 
 <li>修复 <code>git_index_find</code> 的误导性文档</li> 
 <li>文档：停止提及 libgit2 的 "master" 分支</li> 
 <li>docs: 修正一些缺失导致 Docurium 出错</li> 
</ul> 
<h3>依赖关系的更新</h3> 
<ul> 
 <li>ntlm: ntlmclient v0.9.1</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flibgit2%2Flibgit2%2Freleases%2Ftag%2Fv1.2.0" target="_blank">https://github.com/libgit2/libgit2/releases/tag/v1.2.0</a></p>
                                        </div>
                                      
</div>
            
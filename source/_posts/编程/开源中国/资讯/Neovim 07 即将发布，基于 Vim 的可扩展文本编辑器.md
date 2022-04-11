
---
title: 'Neovim 0.7 即将发布，基于 Vim 的可扩展文本编辑器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-a32e33b9d1d2c41533b4d62db520c42ffc9.png'
author: 开源中国
comments: false
date: Sun, 10 Apr 2022 23:40:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-a32e33b9d1d2c41533b4d62db520c42ffc9.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Neovim 0.7 目前正处于稳定化阶段，预计在 4 月 15 日发布。</p> 
<p><strong>主要变化</strong></p> 
<ul style="margin-left:1.25em; margin-right:0"> 
 <li>新增 lua 自动命令</li> 
 <li>新增 lua <span style="background-color:#ffffff; color:#222222">keymap API</span></li> 
 <li>新增 lua 命令 API</li> 
 <li>支持全局命名空间 lua 高亮（纯 lua 配色方案）</li> 
 <li>全局 <span style="background-color:#ffffff; color:#222222">statusline</span></li> 
 <li>支持通过<code>nvim_buf_set_extmark</code>设置 signs</li> 
 <li>提供在映射中从<code><Tab></code>区分<code><C-I></code>的能力</li> 
 <li><code>filetype.lua</code>（用于匹配<code>filetype</code>规则的单个自动命令的更快替代方案）</li> 
 <li><code>:lua =expr</code>， 尝试<code>:lua =&#123;test = true&#125;</code></li> 
</ul> 
<p style="text-align:start"><span><span style="color:#222222"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>其他更新内容是常见的错误修复、移植 Vim 补丁和改进性能。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<hr> 
<p style="text-align:start">Neovim 是 Vim 的一个分支，<span style="background-color:#ffffff; color:#333333">旨在改进代码库，允许更轻松地实现 API，改善用户体验和插件实现。Neovim 的源代码比 Vim 少 30%。</span></p> 
<p>其目标是：</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>重构代码以改善维护</li> 
 <li>实施新的高级功能</li> 
 <li>展示一个更好、更强大的插件系统</li> 
 <li>开放的开发模式，随时接受贡献，接受的标准也很明确。</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>特性：</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>现代图形用户界面</li> 
 <li>从任何语言访问API，包括C/C++, C#, Clojure, D, Elixir, Go, Haskell, Java, JavaScript/Node.js, Julia, Lisp, Lua, Perl, Python, Racket, Ruby, Rust</li> 
 <li>嵌入式、可编写脚本的终端仿真器</li> 
 <li>异步作业控制</li> 
 <li>多个编辑器实例之间的共享数据（shada）。</li> 
 <li>支持XDG基础目录</li> 
 <li>与大多数Vim插件兼容，包括Ruby和Python插件</li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-a32e33b9d1d2c41533b4d62db520c42ffc9.png" referrerpolicy="no-referrer"></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-61df5897f6ea52d7cca37699b8cc7854962.png" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            
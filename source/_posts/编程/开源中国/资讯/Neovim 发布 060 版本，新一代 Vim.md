
---
title: 'Neovim 发布 0.6.0 版本，新一代 Vim'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=123'
author: 开源中国
comments: false
date: Thu, 02 Dec 2021 07:51:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=123'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="margin-left:0px"><span style="color:#333333">Neovim 是专注于可扩展性和可用性的新一代 Vim，Neovim 0.6.0 版本已发布，此版本带来以下内容：</span></p> 
<h2 style="margin-left:0px"><strong>对比 0.5.0 版本的重大变化</strong></h2> 
<ul> 
 <li>不再提供 32 位 Windows 版本。</li> 
 <li><strong>build deps</strong>：在 WIN32 上使用 libuv 1.42.0 上游 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fpull%2F15889" target="_blank">#15889</a> ) ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fcommit%2Ff6c0a37b021cebe7fda730f2116c763b6464203d" target="_blank">f6c0a37</a> )，关闭 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fissues%2F15889" target="_blank">#15889</a> 
  <ul> 
   <li>删除对 Windows 7 的支持</li> 
   <li>在 Windows 8 和 8.1 的 TUI 中删除对鼠标和备用缓冲区的支持</li> 
  </ul> </li> 
 <li><strong>lsp/diagnostic：</strong>突出显示 LSP 诊断的组和标志重命名（例如 <code>LspDiagnosticsDefaultWarning</code> 到<code>DiagnosticWarn</code>）（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fpull%2F15585%2Fcommits%2Fa5bbb932f9094098bd656d3f6be3c58344576709" target="_blank">a5bbb93</a>）</li> 
 <li><strong>诊断：</strong>使 DiagnosticChanged 成为一流的 autocmd ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fpull%2F16098" target="_blank">#16098</a> ) ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fcommit%2F150a5922aae3ed02c9f4eee7e5f162454c42231c" target="_blank">150a592</a> )，关闭 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fissues%2F16098" target="_blank">#16098</a> 
  <ul> 
   <li><code>au User LspDiagnosticsChanged</code> 不支持自动命令。请改用新的一流 DiagnosticChanged 事件。</li> 
  </ul> </li> 
 <li><strong>lua</strong>：<code>register_keystroke_callback</code> => <code>on_key</code>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fpull%2F15460" target="_blank"># </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fpull%2F15460%2Fcommits%2F69fe427df408bc404b17d13759b2e925819c8cf7" target="_blank">15460</a>）（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fpull%2F15460%2Fcommits%2F69fe427df408bc404b17d13759b2e925819c8cf7" target="_blank">69fe427</a>） 
  <ul> 
   <li><strong>注意</strong>：此重大更改已包含在 0.5.1 中</li> 
  </ul> </li> 
</ul> 
<h3>特性</h3> 
<ul> 
 <li><span style="color:#2e3033"><strong>:source, nvim_exec：</strong>推迟脚本项创建，直到 s:var 访问 </span><span style="color:#24292f">( </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fcommit%2Fda9b0abc67a936021a4ecf7634395db860edcab1" target="_blank">da9b0ab</a> <span style="color:#24292f">)</span></li> 
 <li><strong>:source, nvim_exec：</strong>支持脚本本地变量 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fcommit%2Fd4ed51eb4492d4358eb4ab0c939802f2a5fdc636" target="_blank">d4ed51e</a> )</li> 
 <li><strong>lua：</strong>将trimempty 可选参数添加到 vim.split ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fcommit%2F5fa26e2c2fcc208ca31187de4338d5b6f746f2e1" target="_blank">5fa26e2</a> )</li> 
 <li><strong>lua：</strong>添加 vim.str_utf_&#123;start,end&#125;  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fissues%2F16129" target="_blank">#16129</a> </li> 
 <li><strong>lua：</strong>添加 vim.str_utf_pos 函数 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fcommit%2Fd752cbc4d2ef67686acb4bbe06e8cdfa79aa23f8" target="_blank">d752cbc</a> )</li> 
 <li><strong>lsp：</strong>来自所有客户端的聚合代码操作  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fissues%2F15121" target="_blank">#</a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fcommit%2Fc36df20aef22288f47e19084d2671327f7cd878c" target="_blank">15121</a></li> 
 <li><strong>api：</strong>为 xdiff 添加 lua C 绑定  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fissues%2F14536" target="_blank">#14536</a></li> 
 <li><strong>api：</strong>评估状态行字符串  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fissues%2F16020" target="_blank">#</a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fcommit%2F9086938f7bd6d6ccb7f4a30fb78aeaf0d84e4471" target="_blank">16020</a></li> 
 <li><strong>api：</strong>命名标记设置、获取、删除  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fissues%2F15346" target="_blank">#15346</a> </li> 
 <li><strong>api：</strong> nvim_get_chan_info: 为作业包含“argv”  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fissues%2F15537" target="_blank">#15537</a> </li> 
 <li><strong>api：</strong> win_viewport 也发送 line_count  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fissues%2F15613" target="_blank">#15613</a></li> 
 <li><strong>api：</strong>支持 lua 中的终端输入回调（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fcommit%2F9e41e82481753cf13171ab9402bf6f761afc1b66" target="_blank">9e41e82</a>）</li> 
 <li><strong>ci：</strong>添加向后移植 PR 操作  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fissues%2F14766" target="_blank">#14766</a></li> 
 <li><strong>decorations：</strong>在 virt_text 中允许多个堆叠的高光  ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fcommit%2F1495d36d63305862da3c4106455667d51b578707" target="_blank">1495d36</a> )</li> 
 <li><strong>decorations：</strong>支持虚拟线（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fcommit%2F392c658d4d0f9457f143748adf98ecd4cdc8dc85" target="_blank">392c658</a>）</li> 
 <li><strong>decorations：</strong>将 vim.lsp.diagnostic 移至 vim.diagostic 并支持其他来源（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fpull%2F15585%2Fcommits%2Fa5bbb932f9094098bd656d3f6be3c58344576709" target="_blank">a5bbb93</a>）</li> 
 <li><strong>decorations：</strong>向 open_float 添加“前缀”选项（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fissues%2F16321" target="_blank">#16321</a>）</li> 
 <li><strong>decorations：</strong>添加选项以包含诊断源（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fcommit%2Fd43151ea0bb194f7463cc8762919cd38546973c2" target="_blank">d43151e</a>）</li> 
 <li><strong>decorations：</strong>允许“前缀”选项返回突出显示（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fcommit%2Fcc488376221e3792a2c69d1507bdfe405eaebc73" target="_blank">cc48837</a>）</li> 
 <li><strong>decorations：</strong>允许自定义诊断消息（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fissues%2F15742" target="_blank">#15742</a>）</li> 
 <li><strong>decorations：</strong>匹配（），tolist（），fromlist（）（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fissues%2F15704" target="_blank">＃15704）</a></li> 
 <li><strong>decorations：</strong>更新 goto_next/prev 上的跳转列表 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fissues%2F15942" target="_blank">#15942</a> ) </li> 
 <li><strong>decorations：</strong>支持severity_sort（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fcommit%2F32c0631183a64925d38a13819db9557f8da02738" target="_blank">32c0631</a>）</li> 
 <li><strong>lsp：</strong>向 open_floating_preview 添加“焦点”选项（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fissues%2F16465" target="_blank">#16465</a>）</li> 
 <li><strong>lsp：</strong>为客户端代码操作命令添加注册表 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fcommit%2F6c03601e3adb4c3c4d47f148df8df20401b88677" target="_blank">6c03601</a> )</li> 
 <li><strong>lsp：</strong>向 codelens 添加客户端命令支持 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fissues%2F15820" target="_blank">#15820</a> )</li> 
 <li><strong>lsp：</strong>添加 codeAction/resolve 支持 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fissues%2F15818" target="_blank">#15818</a> ) </li> 
 <li><strong>lsp：</strong>添加 exit_timeout 标志（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fissues%2F16070" target="_blank">#16070</a>）</li> 
 <li><strong>lsp：</strong>添加 formatexpr ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fissues%2F16186" target="_blank">#16186</a> )</li> 
 <li><strong>lsp：</strong>添加 lsp 健康检查 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fcommit%2Fe26802650dd3f660f909a3abde8126cee7db1ab0" target="_blank">e268026</a> )</li> 
</ul> 
<p style="margin-left:40px"><strong>......</strong></p> 
<h3><strong>变化</strong></h3> 
<ul> 
 <li><strong>defaults:</strong> <span style="color:#2e3033">自动创建备份目录</span> (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fcommit%2F460019366e58e1bcd42959f76494e38bd895e762" target="_blank">4600193</a>)</li> 
 <li><strong>defaults:</strong> inccommand = nosplit <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fissues%2F15395" target="_blank">#15395</a></li> 
 <li><strong>defaults:</strong> set undo points in and (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fissues%2F15400" target="_blank">#15400</a>)</li> 
 <li><strong>defaults:</strong> <span style="color:#2e3033">限制 CmdwinEnter的语法开销</span> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fissues%2F15401" target="_blank">#15401</a> </li> 
 <li><strong>defaults:</strong> <span style="color:#24292f">将 CTRL-L 映射到搜索亮点，更新差异</span> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fissues%2F15385" target="_blank">#15385</a> </li> 
 <li><strong>defaults:</strong> 将 Y 映射到 y$ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fissues%2F13268" target="_blank">#13268</a></li> 
 <li><strong>defaults:</strong> 从 viewoptions 中删除 'options' <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fissues%2F15397" target="_blank">#15397</a></li> 
 <li><strong>defaults:</strong> 默认值设为隐藏 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fcommit%2Ff6c72b745cfbaaba80555de9a5d4b25f30f17ab2" target="_blank">f6c72b7</a>)</li> 
 <li><strong>defaults:</strong> 设置 nojoinspaces (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fcommit%2Fd417e67e595a9eb19797866e91bb80b4fe299a94" target="_blank">d417e67</a>)</li> 
 <li><strong>defaults:</strong>switchbuf = uselast  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fissues%2F15394" target="_blank">#15394</a></li> 
 <li><strong>runtime:</strong> 将包作为<code>"/pack/*/start/*"</code>模式添加到 &rtp ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fcommit%2F9df7e022b498cb74ffbf5b8fd2ddc4dd5c04d127" target="_blank">9df7e02</a> )</li> 
 <li><strong>startup:</strong> 用 --clean <span style="color:#2e3033">加载内置插件</span> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fissues%2F15893" target="_blank">#15893</a></li> 
 <li><strong>terminal:</strong> 在终端模式下设置 cursorlineopt=number ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fissues%2F15493" target="_blank">#15493</a> ) </li> 
 <li><strong>window:</strong> 跳过不可聚焦的浮动：windo（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fissues%2F15378" target="_blank">#15378</a>）</li> 
</ul> 
<h3><strong>性能改进</strong></h3> 
<ul> 
 <li><strong>api：</strong>在转换小对象时避免虚假分配（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fcommit%2F705e8f10ac83f32dea5bfa0569aba12a692fe522" target="_blank">705e8f1</a>）</li> 
 <li><strong>highlight：</strong>使用哈希表时突出显示组名称（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fcommit%2Fbb4b4d79a8dd0eb60aa37f0b889558c4ae8e9317" target="_blank">bb4b4d7</a>）</li> 
 <li><strong>lua：</strong>优化 vim.deep_equal <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fissues%2F15236" target="_blank">#15236</a> </li> 
 <li><strong>lua：</strong>不要在 lua require'mod' 中使用正则表达式</li> 
 <li><strong>lsp：</strong>提高 json 反序列化性能 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fissues%2F15854" target="_blank"># </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fcommit%2F912a6e5a9c58fce74134f9f8c2801373928e8289" target="_blank">15854</a> ) </li> 
 <li><strong>map：</strong>将双指针间接减少为单指针间接（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fcommit%2F9e651a9d097c5715c0f025555814fa0ad18ca8cd" target="_blank">9e651a9</a>）</li> 
 <li><strong>treesitter：</strong><span style="color:#2e3033">避免在热循环中查找高亮显示名称的字符串</span>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fcommit%2F2460f0a7028550ea2d87492a4e8b95914fdba7b1" target="_blank">2460f0a</a>）</li> 
</ul> 
<p>0.6.0 是一个大版本更新，除了上述新功能和特性以外<strong>还包含大量 Bug 修复</strong>，详细信息可在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Freleases%2Ftag%2Fv0.6.0" target="_blank">官方公告</a>查看。</p> 
<p> </p> 
<p> </p>
                                        </div>
                                      
</div>
            
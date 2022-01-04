
---
title: 'Neovim 0.6.1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2907'
author: 开源中国
comments: false
date: Tue, 04 Jan 2022 07:20:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2907'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Neovim 是 Vim 的一个分支，旨在改进代码库，允许更轻松地实现 API，改善用户体验和插件实现。Neovim 的源代码比 Vim 少 30%。</p> 
<p>Neovim 0.6.1 发布，更新内容如下：</p> 
<h3>错误修复：</h3> 
<ul> 
 <li>api: 允许 nvim_buf_set_extmark 接受 end_row 键 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fissues%2F16686" target="_blank">#16686</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fcommit%2F1b54344c113a506f88a435fbf44ad0c7aa506020" target="_blank">1b54344</a>)</li> 
 <li>diagnostic：断言诊断具有行号和列 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fissues%2F16687" target="_blank">#16687</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fcommit%2F9dae939b1fd4254da22ce1c81a4f0551f21b1de3" target="_blank">9dae939</a>)</li> 
 <li>diagnostic：转义文件名中的特殊字符 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fissues%2F16588" target="_blank">#16588</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fcommit%2Fbeac24d6f3afa8da992e9fdda2ce1d3235f45113" target="_blank">beac24d</a>)</li> 
 <li>diagnostic：尊重 virtual text 的 "if_many" 源选项 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fissues%2F16697" target="_blank">#16697</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fcommit%2F060eeaa14c67d53dc751ccb399b1977f099b736c" target="_blank">060eeaa</a>)</li> 
 <li>diagnostic：为 DiagnosticChanged autocmd 设置有效的缓冲区编号(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fissues%2F16485" target="_blank">#16485</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fcommit%2F84784a83913d12009b19649a7238369f7eca4c04" target="_blank">84784a8</a>)</li> 
 <li>lsp：避免附加到未加载的缓冲区 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fissues%2F16726" target="_blank">#16726</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fcommit%2F00889948ddabcf1bb488665d6afe52c50506a34c" target="_blank">0088994</a>)</li> 
 <li>lsp：在清除 context 之前调用 config on_exit 处理程序 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fissues%2F16781" target="_blank">#16781</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fcommit%2F571609fb8960755a6f0f9416ef0a28acc52830c0" target="_blank">571609f</a>)</li> 
 <li>lsp：修复 <code>_str_*index_enc_</code> 方法中 UTF-8 的 <code>nil</code> 索引行为 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fissues%2F16785" target="_blank">#16785</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fcommit%2F03bd9147f00ebabe28b3b522cefb35bf5efb06a1" target="_blank">03bd914</a>)</li> 
 <li>lsp：处理偏移编码 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fissues%2F16783" target="_blank">#16783</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fcommit%2F7b60ec79eab9e4973c168bdb4b985683e5411282" target="_blank">7b60ec7</a>)</li> 
 <li>lsp：进度处理程序出错时应返回 vim.NIL (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fissues%2F16476" target="_blank">#16476</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fcommit%2Ffb11ef0aad30f99783ccc8459d569447a680a019" target="_blank">fb11ef0</a>)</li> 
 <li>options：不允许空的 "fdc" 和 "scl” (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fissues%2F16776" target="_blank">#16776</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fcommit%2F37a00be7c0bff9c33c2c679561e6bf53c648c271" target="_blank">37a00be</a>)</li> 
 <li>screenpos, float：增加顶部和左侧的边界调整 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fcommit%2F8f68548384780e9200b8471bd21b6a000d2cd705" target="_blank">8f68548</a>)</li> 
 <li><strong>terminal</strong>：修复调整大小时的崩溃 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fissues%2F16665" target="_blank">#16665</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fcommit%2Fae249d81fb9acf68590b932f4714188a93f40935" target="_blank">ae249d8</a>)</li> 
 <li>ui：在 BufLeave 事件上关闭浮动窗口 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fissues%2F16664" target="_blank">#16664</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fcommit%2F785baceaeecf83f894de90c3e6b444e01be187f0" target="_blank">785bace</a>)</li> 
 <li>uri：更改方案模式以不包含逗号字符 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fissues%2F16798" target="_blank">#16798</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fcommit%2F0e96f7d04c1fedb5ed29e21ef4121e2ce3661673" target="_blank">0e96f7d</a>)</li> 
</ul> 
<h3>功能：</h3> 
<ul> 
 <li>lsp,diagnostic: 执行跳转相关函数后打开光标下的折叠 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fissues%2F16784" target="_blank">#16784</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fcommit%2Fee9e3420fdf4beec1a84d45acb434a79e4f816d2" target="_blank">ee9e342</a>)</li> 
 <li>lsp: 增加 buf_detach_client (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fissues%2F16741" target="_blank">#16741</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fcommit%2Fec101b9fd9f3fb5991615a8f4f0f4b4c4602f309" target="_blank">ec101b9</a>)</li> 
 <li>lsp: 使用 <code>vim.ui.select</code> 来选择 lsp 客户端 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fissues%2F16782" target="_blank">#16782</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fcommit%2F14357c83c5e9f1065b445cb9c93611fb6bdc2679" target="_blank">14357c8</a>)</li> 
 <li>运行时：新的 checkhealth 文件类型 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fissues%2F16708" target="_blank">#16708</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Fcommit%2F09306f07c4a4efbc20711ade36a19ce4ba96bb25" target="_blank">09306f0</a>)</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fneovim%2Fneovim%2Freleases%2Ftag%2Fv0.6.1" target="_blank">https://github.com/neovim/neovim/releases/tag/v0.6.1</a></p>
                                        </div>
                                      
</div>
            
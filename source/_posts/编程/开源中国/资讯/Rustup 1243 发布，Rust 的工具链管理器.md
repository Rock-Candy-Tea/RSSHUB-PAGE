
---
title: 'Rustup 1.24.3 发布，Rust 的工具链管理器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=165'
author: 开源中国
comments: false
date: Tue, 08 Jun 2021 23:27:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=165'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Rustup 1.24.3 现已发布。Rustup 是一个命令行应用，能够下载并在不同版本的 Rust 工具链中进行切换。</p> 
<p><strong>主要更新内容</strong></p> 
<ul> 
 <li>增加了配置自动自我更新功能。当用户在测试未发布的 Rustup 版本时，不必一直使用 --no-self-update 运行，也能保证不会意外地丢失测试版本。</li> 
 <li>不再删除 $RUSTUP_HOME/tmp 和 $RUSTUP_HOME/download 的顶层，这意味着用户可以将这些设置为另一个地方的符号链接，或绑定挂载等。</li> 
 <li>使用 unpack-RAM 更优雅地处理异常情况，减少 panic，将设置限制在可行范围内并发出警告。</li> 
 <li>修复了一个与解包板块分配器中数据块的释放相关的问题，该问题会导致安装程序挂起。</li> 
 <li>修复了早期的 Rust 版本（1.0 到 1.7）在已经安装的情况下仍反复被取走校验和的问题。</li> 
 <li>改进了开始警告正在安装的工具链可能无法在给定主机上工作的方法，以降低误报率。</li> 
</ul> 
<p>详情请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.rust-lang.org%2F2021%2F06%2F08%2FRustup-1.24.3.html" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            
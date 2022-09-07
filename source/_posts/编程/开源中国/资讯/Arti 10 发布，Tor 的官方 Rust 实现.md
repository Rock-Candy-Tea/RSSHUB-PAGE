
---
title: 'Arti 1.0 发布，Tor 的官方 Rust 实现'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9876'
author: 开源中国
comments: false
date: Wed, 07 Sep 2022 07:27:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9876'
---

<div>   
<div class="content">
                                                                                            <p>当在 2001 年开始研究 Tor 时，C 是一个合理的选择，但也一直受到它的限制，C 语言的开发速度一直比 Tor 官方希望的要慢。更重要的是，现有的 C 语言实现经过多年的发展，已经有了一个不那么模块化的设计。几乎所有的东西都与其他东西相连，这使得分析代码和进行安全改进变得更加困难。</p> 
<p>因此从 2020 年起，Tor 官方就开始尝试以 Rust 编程语言对 Tor 进行新的实现。而现在，随着最新版本的发布，Arti 已经达到了 1.0.0 的里程碑。</p> 
<h3>重大变化</h3> 
<ul> 
 <li><code>arti</code> crate 中的大部分 API，现在都隐藏在 <code>experimental-api</code> 功能的后面，以标明它们是不稳定的和不支持的。</li> 
 <li><code>default_config_file</code> 函数已被替换为 <code>default_config_files</code>，因为现在有一个默认目录和一个默认文件使用了上述名称</li> 
</ul> 
<h3>低级 crate 中的重大变化</h3> 
<ul> 
 <li>在 <code>NetDirProvider</code> 特性中新增了 <code>params()</code> 方法，以暴露最新的参数，即使没有一个完整的目录</li> 
 <li>对代表一个中继的身份集的特征进行了大规模的重构</li> 
 <li>要求我们的 <code>TcpStream</code> 类型实现 <code>Send</code></li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgitlab.torproject.org%2Ftpo%2Fcore%2Farti%2F-%2Fblob%2Fmain%2FCHANGELOG.md" target="_blank">https://gitlab.torproject.org/tpo/core/arti/-/blob/main/CHANGELOG.md</a></p>
                                        </div>
                                      
</div>
            
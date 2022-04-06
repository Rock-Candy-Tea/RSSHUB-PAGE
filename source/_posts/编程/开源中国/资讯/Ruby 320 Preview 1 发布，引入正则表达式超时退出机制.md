
---
title: 'Ruby 3.2.0 Preview 1 发布，引入正则表达式超时退出机制'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-d7ef587486f22e8a6e4d6d93836e6b3a702.png'
author: 开源中国
comments: false
date: Wed, 06 Apr 2022 07:11:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-d7ef587486f22e8a6e4d6d93836e6b3a702.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Ruby 3.2.0 Preview 1 已发布。此版本增加了许多新特性，以及优化性能。</p> 
<p><strong>基于 WASI 的 WebAssembly 支持</strong></p> 
<p>这是基于 WASI 的 WebAssembly 支持的初始移植。此项特性使得 CRuby 二进制文件可在 Web 浏览器、Serverless Edge 环境和其他 WebAssembly/WASI 嵌入器上使用。目前，此移植可在不使用 Thread API 的前提下通过基本和引导测试套件的测试。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-d7ef587486f22e8a6e4d6d93836e6b3a702.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0px; margin-right:0px; text-align:left"><strong>正则表达式超时退出机制</strong></p> 
<p style="margin-left:0px; margin-right:0px; text-align:left">此版本引入了正则表达式超时退出机制。</p> 
<pre><code>Regexp.timeout = 1.0

/^a*b?a*$/ =~ "a" * 50000 + "x"
#=> Regexp::TimeoutError is raised in one second</code></pre> 
<p style="margin-left:0px; margin-right:0px; text-align:left">由于正则表达式匹配会耗费不少时间，当代码试图向不受信任的输入匹配低效的正则表达式时，攻击者可能会利用它进行 DoS 攻击（即正则表达式 DoS，或称作 ReDoS）。</p> 
<p><code class="language-plaintext">Regexp.timeout</code>根据 Ruby 应用程序的要求进行配置，可以防止或显着降低 DoS 的风险。请注意，<code class="language-plaintext">Regexp.timeout</code>是全局配置项，如果希望对某些特殊的正则表达式使用不同的超时设置，需要使用<code class="language-plaintext">timeout</code>关键字<code class="language-plaintext">Regexp.new</code>。</p> 
<pre><code>Regexp.timeout = 1.0

# This regexp has no timeout
long_time_re = Regexp.new("^a*b?a*$", timeout: nil)

long_time_re =~ "a" * 50000 + "x" # never interrupted</code></pre> 
<p>此项特性的最初提案：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.ruby-lang.org%2Fissues%2F17837" target="_blank">https://bugs.ruby-lang.org/issues/17837</a></p> 
<p>其他更新内容包括优化性能，更新标准库等，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.ruby-lang.org%2Fen%2Fnews%2F2022%2F04%2F03%2Fruby-3-2-0-preview1-released%2F" target="_blank">详情查看发布公告</a>。</p>
                                        </div>
                                      
</div>
            
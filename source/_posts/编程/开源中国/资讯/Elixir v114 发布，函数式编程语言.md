
---
title: 'Elixir v1.14 发布，函数式编程语言'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3600'
author: 开源中国
comments: false
date: Tue, 06 Sep 2022 07:30:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3600'
---

<div>   
<div class="content">
                                                                                            <p>Elixir v1.14 已发布。此版本为 Elixir 的调试体验和数据类型检查带来了许多改进。此外还添加了一个新的抽象，以方便进程的分区，称为<code>PartitionSupervisor</code>，以及优化编译时间和错误信息。</p> 
<p>另外，Elixir v1.14 是支持 Erlang/OTP 23 的最后一个版本。建议开发者考虑升级到 Erlang/OTP 24 或 Erlang/OTP 25。    </p> 
<p><strong><code>dbg</code></strong></p> 
<p><code>Kernel.dbg/2</code>是一个新的宏，有点类似于<code>IO.inspect/2</code>，专门为<strong>调试</strong>而定制。</p> 
<p>调用该宏时，它会打印传递给它的任何值，以及已调试代码本身及其位置。</p> 
<p>下面这段代码：</p> 
<pre><code># In my_file.exs
feature = %&#123;name: :dbg, inspiration: "Rust"&#125;
dbg(feature)
dbg(Map.put(feature, :in_version, "1.14.0"))</code></pre> 
<p>会打印出：</p> 
<pre><code>$ elixir my_file.exs
[my_file.exs:2: (file)]
feature #=> %&#123;inspiration: "Rust", name: :dbg&#125;

[my_file.exs:3: (file)]
Map.put(feature, :in_version, "1.14.0") #=> %&#123;in_version: "1.14.0", inspiration: "Rust", name: :dbg&#125;</code></pre> 
<p><code>dbg/2</code>能完成更多任务。它是一个宏，所以可以理解 Elixir 代码_。当开发者将一系列<code>|></code>管道传递给它时，<code>dbg/2</code>将打印管道每一步的值。</p> 
<p>下面这段代码：</p> 
<pre><code># In dbg_pipes.exs
__ENV__.file
|> String.split("/", trim: true)
|> List.last()
|> File.exists?()
|> dbg()</code></pre> 
<p>会打印出：</p> 
<pre><code>$ elixir dbg_pipes.exs
[dbg_pipes.exs:5: (file)]
__ENV__.file #=> "/home/myuser/dbg_pipes.exs"
|> String.split("/", trim: true) #=> ["home", "myuser", "dbg_pipes.exs"]
|> List.last() #=> "dbg_pipes.exs"
|> File.exists?() #=> true</code></pre> 
<p><strong>PartitionSupervisor</strong></p> 
<p><code>PartitionSupervisor</code>是一个新模块，实现了新的 supervisor 类型。<span style="background-color:#ffffff; color:#24292f">partition supervisor</span> 旨在帮助处理成为瓶颈的单个受监督进程的情况。如果该进程的状态可以轻松分区，那么可以使用<code>PartitionSupervisor</code>来监督该进程同​​时运行的多个隔离副本，每个副本都分配了自己的分区。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felixir-lang%2Felixir%2Freleases%2Ftag%2Fv1.14.0" target="_blank">详情查看 release note</a>。</p>
                                        </div>
                                      
</div>
            
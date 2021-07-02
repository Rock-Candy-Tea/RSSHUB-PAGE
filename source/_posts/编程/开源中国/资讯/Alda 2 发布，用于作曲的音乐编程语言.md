
---
title: 'Alda 2 发布，用于作曲的音乐编程语言'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://cors.zfour.workers.dev/?http://static.oschina.net/uploads/space/2015/0907/112300_aZmw_2306979.png'
author: 开源中国
comments: false
date: Fri, 02 Jul 2021 08:08:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://static.oschina.net/uploads/space/2015/0907/112300_aZmw_2306979.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Alda 2.0.0 已正式发布。发布公告写道：“新版本的 Alda 从 2018 年底就开始了彻底的重写。虽然版本号由 1 变为了 2，但在语言层面上，Alda 2 几乎与 Alda 1 完全一样。”</p> 
<p>Alda 是用于音乐创作的基于文本的编程语言，它可以通过在编辑框里输入代码来谱写不同种类的曲子，并且能把这些曲子编译成音乐。简单来说，通过 Alda 使用者只需文本编辑器和命令行即可编写和播放音乐。</p> 
<pre><code>piano:
  o3
  g8 a b > c d e f+ g | a b > c d e f+ g4
  g8 f+ e d c < b a g | f+ e d c < b a g4
  << g1/>g/>g/b/>d/g</code></pre> 
<p><img alt="112300_aZmw_2306979.png" src="https://cors.zfour.workers.dev/?http://static.oschina.net/uploads/space/2015/0907/112300_aZmw_2306979.png" referrerpolicy="no-referrer"></p> 
<p>值得关注的变化包括：</p> 
<ul> 
 <li>使用 Go 代替 Clojure 来编写新版本，因此现在的 Alda 是一个原生的 Go 应用，其发行版适用于 Linux、Windows 和 macOS 平台。</li> 
 <li>新增小的后台<code>alda-player</code>进程，其采用 Kotlin 编写。Alda 会在后台启动这些进程来播放乐谱。</li> 
 <li>由于应用已迁移至本地，且大部分工作现在在<code>alda</code>客户端进程（而不是在 worker 进程中）完成，因此在解析和评估分数方面，Alda 2 明显比 Alda 1 快。</li> 
 <li>无需启动服务器才能使用 Alda（不再需要运行<code>alda up</code>）。安装 Alda 2 后，可以立即使用<code>alda play</code>命令并聆听基于文本的音乐创作。</li> 
 <li>支持使用动态标记来指定音量。例如，可以使用<code>(mp)</code> 属性用于安静的<em>中音钢琴</em>，或<code>(ffffff)</code>用于最响亮的动态属性。这些动态属性等同于音量属性，如<code>(vol 46)</code>和 <code>(vol 100)</code>。</li> 
 <li>……</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.djy.io%2Fannouncing-alda-2%2F" target="_blank">详情查看发布公告</a>。</p>
                                        </div>
                                      
</div>
            
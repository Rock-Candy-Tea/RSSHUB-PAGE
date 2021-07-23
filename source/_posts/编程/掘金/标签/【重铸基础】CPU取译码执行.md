
---
title: '【重铸基础】CPU取译码执行'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7cf1bd0741274efc900c783f41353c1f~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 21 Jul 2021 19:59:33 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7cf1bd0741274efc900c783f41353c1f~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><h2 data-id="heading-0">往期文章</h2>
<blockquote>
<p><a href="https://juejin.cn/post/6969457808378953735" target="_blank" title="https://juejin.cn/post/6969457808378953735">寻找IOS相册中相似图片</a> <br><a href="https://juejin.cn/post/6966865296632053790" target="_blank" title="https://juejin.cn/post/6966865296632053790">NSNotification与类对象,实例对象</a><br><a href="https://juejin.cn/post/6971996422149406756" target="_blank" title="https://juejin.cn/post/6971996422149406756">iCloud-Documents存储</a><br><a href="https://juejin.cn/post/6974586785741422628" target="_blank" title="https://juejin.cn/post/6974586785741422628">CocoaPods私有源搭建</a><br><a href="https://juejin.cn/post/6977241628297658398" target="_blank" title="https://juejin.cn/post/6977241628297658398">Swarm区块链分布式存储使用</a><br><a href="https://juejin.cn/editor/drafts/6979762500661149727" target="_blank" title="https://juejin.cn/editor/drafts/6979762500661149727">MacOS流编辑器sed</a><br><a href="https://juejin.cn/post/6985068459541397534" target="_blank" title="https://juejin.cn/post/6985068459541397534">IOS使用Flutter模块</a></p>
</blockquote>
<h1 data-id="heading-1">开始</h1>
<p>我们通过一个简单的CPU的架构图，来简单了解下CPU取译码执行过程。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7cf1bd0741274efc900c783f41353c1f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
现在我们来简单介绍下图片中的各种名词</p>









































<table><thead><tr><th>名称</th><th>用途</th></tr></thead><tbody><tr><td>A B C D E F</td><td>代表6个通用寄存器，用于需要暂存数据</td></tr><tr><td>ALU</td><td>算术逻辑单元是专门执行算术和逻辑运算的地方</td></tr><tr><td>PC</td><td>程序计数器用于存放下一条指令的地方</td></tr><tr><td>MAR</td><td>地址寄存器</td></tr><tr><td>BR</td><td>全称buffer register 缓冲寄存器</td></tr><tr><td>IR</td><td>存放CPU指令集的地方</td></tr><tr><td>Decoder</td><td>译码器</td></tr><tr><td>CU</td><td>控制单元,CPU执行指令的地方</td></tr></tbody></table>
<h1 data-id="heading-2">获取一条指令</h1>
<h2 data-id="heading-3">汇编语言简介</h2>
<p>大多数情况下我们的用C++或者java或者其他高级语言生成的代码首先被编译成汇编语言。汇编语言可以生成CPU对应的指令集，而指令集是由一堆二进制代码组成的机器语言，能够直接被CPU识别和执行。</p>
<p><strong>简单的指令介绍</strong><br>
0000 代表 加载（LOAD）<br>
0001 代表 存储（STORE）</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6ec95f53730c4ee79606cc627cabb84e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">使用汇编语言生成一条CPU指令</h2>
<p>下面来看一条汇编代码</p>
<pre><code class="copyable">INC A
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这条汇编代码的意思是让寄存器A自增一次。</p>
<p>这条汇编代码会生成一条CPU指令，其二进制形式如下</p>
<pre><code class="copyable">00111100
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通常为了方便我们记忆我会使用其16进制形式</p>
<pre><code class="copyable">3C
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">CPU选中指令的内存地址</h2>
<p>我们将3C这条让寄存器A自增的指令，放在内存中其地址为AE00，如下图所示</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/630e4cb494744ec5995c5c93a68d8474~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>接来下CPU将这条指令的地址AE00从内存加载到PC程序计数器中，这里我们假设寄存器其A中已经有一个数据了00000000，为了方便记忆我们还是使用其十六进制形式00H</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a7655868231c448ea2f74ef77eb6deca~tplv-k3u1fbpfcp-watermark.image" alt="CPU.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>程序计数器在获取到3C指令之后，将这条指令放入MAR(Memory address register) 地址寄存器中,然后PC程序计数器+1,这样程序计数器PC 就可以加载下一个内存地址(这样就可以取下一个指令或者操作)</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c6af4fc5232848ce9ff7476f12b5a9ea~tplv-k3u1fbpfcp-watermark.image" alt="CPU1.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在地址寄存器中的AE00地址，通过地址总线，来到内存中选中当前CPU操作的地址AE00</p>
<h2 data-id="heading-6">取地址中的指令</h2>
<p>在选中操作地址之后，控制单元发送读取内存地址数据操作。然后被选中的地址AE00，将自身保存的数据通过数据总线传递到CPU中的BR缓冲寄存器中。然后从BR缓冲寄存器中拷贝到IR 指令寄存器中。然后IR指令寄存器将指令3C 放入decoder解码器中。待解码器解码完成以后。解码后的指令进入控制单元CU，执行流程如下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/795c2b4ebb9a4eaeb2e66285d6bd0426~tplv-k3u1fbpfcp-watermark.image" alt="CPU3.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">执行指令</h2>
<p>当INC A指令(3C)进入CU控制单元之后，CU控制单元执行指令，将A通用寄存器中暂存的数据00H，放入ALU算术与逻辑单元之中，在ALU中完成自增。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3203aa99b58e4fed8d0930f62b8b99d4~tplv-k3u1fbpfcp-watermark.image" alt="CPU4.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>以上就是一次完整的取译码过程。</p>
<h1 data-id="heading-8">结语</h1>
<p>做图有点粗糙，请各位多多包涵，以上文章有什么错误之处，可以在下面评论，我会及时改正</p></div>  
</div>
            
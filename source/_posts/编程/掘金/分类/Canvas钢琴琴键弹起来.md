
---
title: 'Canvas钢琴琴键弹起来'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ebe780068fef4aff98b4531970f2760b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 27 Aug 2021 04:49:20 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ebe780068fef4aff98b4531970f2760b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p><strong>这是我参与8月更文挑战的第27天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h2 data-id="heading-0">前情回顾</h2>
<p>在之前曾经写过<a href="https://juejin.cn/post/7000389929842769956" target="_blank" title="https://juejin.cn/post/7000389929842769956">《canvas 制作钢琴琴键》</a>一文，在那篇文章当中，已经使用<code>canvas</code>绘制出来了钢琴的琴键，并且能够通过鼠标点击白键来改变白键的颜色。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ebe780068fef4aff98b4531970f2760b~tplv-k3u1fbpfcp-watermark.image" alt="1.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>不过光是点击白键还不够，钢琴也是需要点击黑键的，并且最重要的是钢琴怎么能够<strong>没有声音</strong>呢！</p>
<p><strong>项目Gitee的地址</strong>：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Fwzckongchengji%2Fnode_study%2Ftree%2Fmaster%2FpianoDemo" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/wzckongchengji/node_study/tree/master/pianoDemo" ref="nofollow noopener noreferrer">gitee.com/wzckongchen…</a></p>
<hr>
<br>
<h2 data-id="heading-1">再起</h2>
<p>因为之前已经写过白键的点击方法，所以本次就用只需要稍作改变，即可完成黑键的点击。</p>
<p>首先对鼠标点击位置的(x, y)进行判断，下面由于代码过长，就不准备粘贴了。大家如果想看可以去上面Gitee上<strong>main.ts</strong>中查看</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/67faa527dfe64c0da5d4a2c9552abca1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>因为是在<code>TypeScript</code>中编写的，所以会有类型定义，xy是之前定义的<strong>坐标类型</strong></p>
<pre><code class="hljs language-js copyable" lang="js">type xy = &#123;
    <span class="hljs-attr">x</span>: number,
    <span class="hljs-attr">y</span>: number
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过这一步，能够做到不同类别的按键判断。</p>
<p>其中的<code>whiteKeyClick</code>是白键按下的方法，白键和黑键按下在类中都有<code>pressDown</code>按下事件，各自会重写一下此方法</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4a8b75a8e750491ca28626f42d284cd1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当前的效果是鼠标点击黑键和白键都会变色</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/66240938f5704ff9b1c68b4a0f9b4922~tplv-k3u1fbpfcp-watermark.image" alt="80901.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<br>
<h2 data-id="heading-2">钢琴音效</h2>
<p>钢琴如果没有琴键的声音又怎么能称为钢琴呢，所以每一个按键都要有对应的声音，一共88个琴键，就要有88中音效。</p>
<p>说实话，找这些音效资源花费了我很久的时间......</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4aea09463d9a41699c6dcc2c554b196f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>最后经过一系列的寻找，还是被我找到了</p>
<blockquote>
<p>地址就在上面的项目中， <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Fwzckongchengji%2Fnode_study%2Ftree%2Fmaster%2FnodeDemoIO%2Fmusic" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/wzckongchengji/node_study/tree/master/nodeDemoIO/music" ref="nofollow noopener noreferrer">gitee.com/wzckongchen…</a></p>
</blockquote>
<p><strong>注意：</strong> 我使用audio标签去播放音乐，由于音频的资源比较大，所以我就不存放在前端项目中了，把这些音频资源放在我平时练习的node里，使用node来给出url去调用音频。</p>
<p>node运行命令： <code>nodemon IO.js</code></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/85d8e98d572a4c4ba45eb65ba35aa851~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这样测试一下，在网页中输入URL： <a href="https://link.juejin.cn/?target=http%3A%2F%2Flocalhost%3A3001%2Fmusic%2F8A.mp3" target="_blank" rel="nofollow noopener noreferrer" title="http://localhost:3001/music/8A.mp3" ref="nofollow noopener noreferrer">http://localhost:3001/music/8A.mp3</a> 。 发现能够访问到音频了</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6152344bda5d44cba2827130b78f4b41~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>之后就可以在钢琴按下事件中调用音频调用方法了，注意这里需要根据不同的index去判断调用不同琴键的音效。</p>
<p>下面是白键的音调判断方法：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fdc25c70385b429cb07283bfcef5d727~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>黑键判断：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4b21352abc294c878609659b5267f030~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<p>当然了，这些判断需要对钢琴有一定了解，钢琴中是存在不同分区的。下图很重要，这也是我在编写时的重要依据：</p>
<blockquote>
<p>可以看出，钢琴琴键排布具有如下特点。</p>
<ul>
<li>1、共有52个白键和36个黑键。</li>
<li>2、黑键的长度和宽度均小于白键。</li>
<li>3、每个黑键都位于两个白键中间（但不一定是正中间）。</li>
<li>4、琴键分为若干组，每组有12个琴键（7个白键和5个黑键）。</li>
<li>5、最左边的组只有3个琴键（2个白键和1个黑键），最后边的组只有1个琴键（1个白键），这两个组都是不完整的组。</li>
</ul>
<p>每组的这12个琴键中，7个白键从左向右依次为do、re、mi、fa、sol、la、si，5个黑键从左向右依次为升do（降re）、升re（降mi）、升fa（降sol）、升sol（降la）、升la（降si）。</p>
</blockquote>
<p>图中的那些汉字是每组的名称（从左向右依次为大字二组、大字一组、大字组、小字组、小字一组、小字二组、小字三组、小字四组、小字五组，其中大字二组和小字五组是不完全音组）</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f24107d74cbe4459be995b8721a3f741~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>经过这一系列的操作之后，点击琴键就能发出不同的音效声音了。</p>
<hr>
<br>
<h2 data-id="heading-3">键盘绑定</h2>
<p>做到这里，突然觉得还是有些美中不足。 光是使用鼠标点击好像有些过于单调了，那么让<strong>打键盘变成弹钢琴</strong>吧</p>
<p>将键盘上的按键对应钢琴的琴键匹配绑定起来。</p>
<p>这里的内容我主要写在<code>keyWord.ts</code>当中了，使用export抛出</p>
<p>使用<strong>Map</strong>定义的<code>keyWord</code>来存放对应的联系</p>
<pre><code class="hljs language-js copyable" lang="js">interface keyObj &#123;
    <span class="hljs-attr">keyname</span>: string;
    type: number;  <span class="hljs-comment">// 0：白键  1：黑键</span>
    index: number;   <span class="hljs-comment">// 对应的黑键和白键index</span>
    represent: string
&#125;
<span class="hljs-keyword">let</span> keyWord:<span class="hljs-built_in">Map</span><string|number, keyObj> = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>keyWord中的内容：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/007a8e5211ea4a7e9e1726e9baa3cba3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过回调函数来设置电脑键盘的按下与抬起事件对应的操作：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 监听键盘点击</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">keyWordDown</span>(<span class="hljs-params">callback:<span class="hljs-built_in">Function</span>, callback2:<span class="hljs-built_in">Function</span></span>) </span>&#123;    
    <span class="hljs-built_in">document</span>.onkeydown = <span class="hljs-function">(<span class="hljs-params">event</span>)=></span>&#123; 
        <span class="hljs-keyword">let</span> e = event || <span class="hljs-built_in">window</span>.event;
        callback(e.keyCode)
    &#125;    
    <span class="hljs-built_in">document</span>.onkeyup = <span class="hljs-function">()=></span>&#123; 
        callback2();
    &#125;   
&#125;

<span class="hljs-keyword">export</span> &#123; keyWord, keyWordDown, keyObj &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>之后回到<code>main.ts</code>对应的回调方法写入即可。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0d9cd3c70223461c96395bbaff4da9ce~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<br>
<h2 data-id="heading-4">完成</h2>
<p>当然下面的GIF中是没有声音的，挺可惜的，毕竟重点就本文在于钢琴能响了</p>
<p>键盘弹奏：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6166415795b2432abcae6baa4e804d1d~tplv-k3u1fbpfcp-watermark.image" alt="80901.gif" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            
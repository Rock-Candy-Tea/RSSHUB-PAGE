
---
title: 'Redis 帝国的神秘使者，竟然想改造 C 语言！'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e0072707dc2a4c9a88066996e0d193e8~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 25 Jul 2021 17:34:26 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e0072707dc2a4c9a88066996e0d193e8~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文已参与好文召集令活动，点击查看：<a href="https://juejin.cn/post/6978685539985653767" target="_blank" title="https://juejin.cn/post/6978685539985653767">后端、大前端双赛道投稿，2万元奖池等你挑战！</a></p>
<p>你好，我是悟空。</p>
<h2 data-id="heading-0">迎接使者大人</h2>
<p>“吁····”</p>
<p>这声音从一辆豪华马车中传出，拉车的两匹马儿听到后，立马停在了路边。</p>
<p>“先生，可有什么不对劲？”车夫谨慎地问道。</p>
<p>车中的一位年轻帅小伙拉开了车门前的帘布，说道：“前方有一只百人军队正在赶来，想必是 C 语言帝国的皇家护卫军。”</p>
<p>一小会的功夫，前方百人军队正骑着马来到了马车前。</p>
<p>一名身材魁梧，八尺高，手持一柄长枪的士兵从马背上下来了。</p>
<p>“我是 C 语言帝国的皇家护卫队队长，恭闻使者大人远道而来出使我国，国王特派我前来迎接。” 这位队长笑盈盈说道。</p>
<h2 data-id="heading-1">C 语言帝国大殿</h2>
<p>“使者大人，前面就是我国的宫殿了，请小心殿堂内的<code>字符串大臣</code>。”护卫队队长说道。</p>
<p>先生心生疑惑地走进了殿堂中，大家的目光都汇聚到了这位年轻人的身上。他在大殿上给国王行了一个礼。</p>
<p>国王说道：“这是 Redis 帝国派来的使者，他给我们带了一个新的数据结构，叫做<code>简单动态字符串</code>，他还有个英文名字，叫做 <code>SDS</code>，全称 Simple Dynamic String”。</p>
<p>在大殿一旁的字符串大臣，脸色显得略微有点难看。</p>
<p>国王继续说道：“SDS 先生，你一路辛苦了，可以介绍下贵国的 SDS 数据结构吗？”</p>
<p>SDS 使者说：“我和 C 语言大国的字符串不一样，我们先来回顾下贵国的字符串表示方式。C 语言字符串是由<code>字符数组</code>组成的，最后一个元素总是空字符 <code>\0</code>。” 使者向殿内大臣展示了一张示意图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e0072707dc2a4c9a88066996e0d193e8~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>“比如现在中文<code>悟空</code>的拼音 <code>wukong</code> 被放到数组一个长度为 7 的字符数组中，最后一个元素是空字符'\0'。” 使者继续解释道。</p>
<p>旁边的数组大臣和字符串大臣专注地聆听着，好像随时准备发问似的。</p>
<p>SDS 使者说：“我们 Redis 帝国的字符串是用 SDS 表示的，这是在字符数组上进行了增强，是一种新的结构体”</p>
<p>随后使者拿出了一卷羊皮纸，上面写着一份代码：</p>
<pre><code class="hljs language-c copyable" lang="c"> <span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">sdshdr</span> &#123;</span>
    <span class="hljs-comment">// 字符数组，用于保存字符串</span>
    <span class="hljs-comment">// 和 C 语言中保存字符串的字符数组一样。</span>
    <span class="hljs-keyword">char</span> buf[];
     
    <span class="hljs-comment">// 记录 buf 数组中已使用字节的数量，等于 SDS 锁保存字符串的长度。 </span>
 <span class="hljs-keyword">int</span> len;
     
    <span class="hljs-comment">// 记录 buf 数组中未使用字节的数量</span>
 <span class="hljs-keyword">int</span> <span class="hljs-built_in">free</span>;
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>随后 SDS 使者拿出来了一张准备好的示例图解释道：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f09fbf74c9d4499b0f733a271b632af~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>简单动态字符串 SDS 结构是由三部分组成的：</p>
<ul>
<li><strong>buf</strong> 数组属性和 C 语言帝国一样，都用了 7 个字节来保存 <code>wukong</code>，最后一个元素是空字符。</li>
<li><strong>len</strong> 属性这个值为 6，代表这个 SDS 保存了一个 6 字节长的字符串（最后一个空字符不计算 len 属性中）。</li>
<li><strong>free</strong> 属性的值为 0，代表这个 SDS 没有其他剩余空间来存放字符了。</li>
</ul>
<blockquote>
<p>注意：数组中的空字符是自动加到字符串末尾的，由 SDS 的函数自动完成。为什么要和 C 语言的字符串的空字符结尾保持一致呢？是因为这样可以重用一部分 C 字符串函数库里面的函数。</p>
</blockquote>
<p>旁边的字符串大臣按捺不住地问道：“你这样做，我看不到什么好处呢？反而增加了空间来保存 free 和 len 属性。”</p>
<p>众人听完字符串大臣的话，都若有所思。</p>
<p>“大家不要着急，且听使者解释。”国王看着众人疑惑的脸说道。</p>
<p>“因为我用 len 属性记录了字符串的总长度，所以要是有程序想要访问 SDS 的 len 属性，就可以立即知道保存的字符串长度，简单来说就是复杂度为 O(1)。比如我刚刚举的例子，可以立即知道 SDS 的长度为 6 字节。” 使者不紧不慢地说道。</p>
<p>国王将目光投向了字符串大臣，然后说道：“字符串爱卿，我们的 C 字符串计算长度需要多久？”</p>
<p>“尊敬的国王大人，我们计算 C 字符串的长度需要遍历整个字符串，对遇到的每个字符进行计数，直到遇到代表字符串结尾的空字符为止。上面的例子，我们要记 6 次，也就是复杂度为 O(N)。” 字符串大臣连忙回答。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0f46f4f2ae4e4e52832eb3c8c574658b~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>“那我们也太慢了吧...” 国王小声嘀咕着。</p>
<h2 data-id="heading-2">内存分配的天赋</h2>
<h3 data-id="heading-3">杜绝缓冲区溢出</h3>
<p>“听说 SDS 在内存分配上有很大的天赋，可以给我们说说看吗？”C 语言帝国的内存大臣提到。</p>
<p>“首先我可以杜绝缓冲区溢出。” SDS 使者自豪地说道。</p>
<blockquote>
<p><strong>提示</strong>：缓冲区是对原始磁盘块的临时存储，用来缓存将要写入磁盘的数据。这样，内核就可以把分散的写集中起来，统一优化磁盘写入。</p>
</blockquote>
<p>“快给我说说，我发现总是有缓冲区溢出的异常出现，就是因为 C 字符串的一些不正规操作导致的。”内存大臣说完瞥了一眼字符串大臣。</p>
<p>“这可不管我的事，都是那些程序员不正规操作造成的。”字符串赶紧向内存大臣解释。</p>
<p>“这还跟程序员有关？”国王追问着。</p>
<p>“国王大人，情况是这样的，假设内存中有<code>紧邻</code>的 C 字符串 S1 和 S2，S1 保存了字符串 <code>WuKong</code>（悟空），而 S2 字符串保存了字符串<code>ZiXia</code>（紫霞），给您看个示意图。”SDS 使者拿出了一张早已准备好的原理图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dfa5031c72014c2baf3cee4a96222e9a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>“如果某个程序员执行了如下拼接字符串命令，又没有提前为 S1 分配足够的空间，那就悲剧了。”字符串大臣继续说道。</p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-built_in">strcat</span>(s1, <span class="hljs-string">" QuJing"</span>) <span class="hljs-comment">// 取经</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>“因为 S1 没有分配足够的空间，所以在 strcat 函数执行之后，S1 d的数据将会溢出到 S2 所在的空间中，导致 S2 保存的内容被意外地修改，这就是缓冲区溢出。但这个跟我无关啊，是程序员干的。”字符串大臣一脸无辜地说道。</p>
<p>“对对对，就是这样，害得我好惨。”内存大臣嘀咕道。</p>
<p>“请问使者有什么高见？”国王大人毕恭毕敬地说道。</p>
<p>“和 C 字符串相比，SDS 的空间分配策略就杜绝了这种情况发生。”SDS 使者平静地说道。</p>
<p>“当 SDS API，比如拼接的 API，需要对 SDS 进行修改时，API 会先检查 SDS 的空间是否满足修改所需的要求，不满足的话，则会自动扩容。” SDS 解释道。</p>
<p>“妙啊！对于 C 字符串来说，每次修改字符串长度都要进行内存重分配的操作，涉及到了复杂的算法，还可能需要执行系统调用，非常耗时。” 内存大臣大声感叹道。</p>
<p>“那你们的自动扩容是每次修改字符串时都需要么？” 字符串大臣疑惑道。</p>
<p>“当然不是，我们扩容的时候不仅会为 SDS 分配修改所必须要的空间，而且还会为 SDS 分配额外的未使用空间。”</p>
<p>“快给我们讲讲吧。”国王急不可待的说道。</p>
<h3 data-id="heading-4">空间预分配</h3>
<p>“我这个功能叫做空间预分配。分配的规则如下。”使者义正言辞地解释道。</p>
<ul>
<li>如果对 SDS 进行修改之后，SDS 的长度（len 属性决定），还是小于 1 MB 的话，那么将会分配和 len 属性相同大小的未使用空间，那么 SDS len 属性的值将 free 属性的值相同。比如说当前 SDS 的 len = 6，加上 7 个字符后，len 的值变为了 13，还是小于 1 MB 的，然后 SDS 会被分配 13 字节的<code>未使用空间</code>。那么 SDS 的实际长度就是 13 + 13 + 1 = 27 字节（额外的字节用于保存空字符）。</li>
<li>如果对 SDS 进行修改之后，SDS 的长度大于等于 1 MB，那么会分配 1 MB 的额外空间。也就是说 SDS 长度等于必须存放的空间的长度 + 1MB 的未使用空间的长度。比如说 SDS 修改之后，变成了 10 MB，那么会分配 1 MB 的未使用空间，最后 buf 数组的实际长度等于 30 MB + 1 MB + 1 byte。</li>
</ul>
<p>听完使者说完，国王还是有点懵，但是身边的字符串大臣和内存大臣已经听懂了，不亏是 C 语言帝国的两大支柱，这点扩容知识还是很容易理解的。</p>
<p>“可否举个例子呀，寡人实在无法理解。”国王摇摇头的说道。</p>
<p>“好的，国王。我还是用<code>悟空取经</code>来说明。”使者答应道。</p>
<p>“首先 SDS 存放的是悟空的英文 <code>WuKong</code>，然后追加一个取经的英文<code> QuJing</code>，我们来看看怎么扩容的。”使者继续说道。</p>
<blockquote>
<p><strong>提示</strong>：SDS 的 API 中其实也有一个用于执行拼接操作的 sdscat 函数，他可以将一个 C 字符串拼接到 SDS 所保存的字符串后面，但是在执行拼接操作之前，sdscat API 会先检查给定 SDS 的空间是否足够，如果不够的话， sdscat 会先扩展 SDS 的空间，然后才执行拼接操作。</p>
<pre><code class="hljs language-c copyable" lang="c">s = <span class="hljs-string">"WuKong"</span>;
sdscat(<span class="hljs-string">"s"</span>, <span class="hljs-string">" QuJing"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
</blockquote>
<p><code>WuKong</code>总共占了 6 个字符，<code> QuJing</code> 占了 7 个字符（包含前面的空格）。最后拼接的结果就是：<code>WuKong Qujing</code>。我还是来画个图给大家看下吧。”</p>
<p>最开始 SDS 长这样：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aae62f628bb24cc182580aea4f74481d~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>后来拼接了 " QuJing" 的时候，free = 0，不足以存放，所以开始扩容，首先会增加 7 个字符的空间，len = 6 + 7 = 13，然后再分配额外的未使用空间，空间大小等于 len 的值，也是 13，所以 free = len = 13。</p>
<p>拼接后 SDS 长下面这样：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/def99e7114644076b8be00cd8c428ef6~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果还想再拼接一个字符串在后面，比如字符串 <code>GuiLai</code>（中文：归来，占 6 个字符），那是不用再扩容，因为未使用的 13 个字符串空间足以容纳这 6 个字符。通过简单的计算也可以得出这个结果：Total = 13 + 13 = 26，6 + 7 + 7 = 20 < 26。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1b9be6c47b964317a756400f8cd7f5c6~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>众人听完使者的解释后，都赞叹不已。</p>
<p>突然大殿之中传来一个声音：“那假设每次拼接的字符串都超过了未分配空间，是不是每次都得扩容？”众人将目光转向了声音的方向，字符串大臣那里。</p>
<p>“的确如此，不过通过这种预分配的扩容方式，SDS 将必定 N 次扩容降低为最多 N 次。”使者微笑道。</p>
<p>“那缩短字符串的时候，会立即回收多余的空间吗？”字符串大臣追问道。</p>
<p>“我们有<code>惰性空间释放</code>的功能，不会立即释放多出来的字节，而是等待将来使用。而且当有需要的时候，会有专门的 API 来真正地释放 SDS 的空间。”使者解释道。</p>
<p>众人纷纷点头，国王总结道：“<strong>通过 SDS 的预分配和惰性空间释放的方式，确实减少了分配空间的次数，难怪 Redis 会这么快的。</strong>”</p>
<p>字符串大臣静静地听着国王的总结，生怕国王一声令下要改造 C 语言帝国的字符串形式。</p>
<p>“你去公众号<strong>悟空聊架构</strong>回复下 <code>SDS</code> 吧，听说那里可以下载 Redis SDS 的源码。研究下，后面可能改造下我们的字符串。”国王对着字符串大臣说道。</p>
<p>巨人的肩膀：</p>
<p>Redis 设计与实现</p></div>  
</div>
            
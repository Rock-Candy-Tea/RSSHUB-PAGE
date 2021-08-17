
---
title: 'MethodSwizzing方法交换的坑｜伤敌一千自损八百'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb085e4328d4432dbddda9552efa81c6~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 08 Aug 2021 00:49:19 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb085e4328d4432dbddda9552efa81c6~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p><strong>这是我参与8月更文挑战的第8天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h2 data-id="heading-0">Hi 👋</h2>
<ul>
<li>Wechat: RyukieW</li>
<li>📦 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fryukiedev.gitbook.io%2Fwiki%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://ryukiedev.gitbook.io/wiki/" ref="nofollow noopener noreferrer">技术文章归档</a></li>
<li>🐙 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FRyukieSama" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/RyukieSama" ref="nofollow noopener noreferrer">Github</a></li>
</ul>




















<table><thead><tr><th align="center">我的个人项目</th><th align="center">扫雷Elic 无尽天梯</th><th align="center">梦见账本</th></tr></thead><tbody><tr><td align="center">类型</td><td align="center">游戏</td><td align="center">财务</td></tr><tr><td align="center"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fapps.apple.com%2Fcn%2Fdeveloper%2Frongqing-wang%2Fid1264542103" target="_blank" rel="nofollow noopener noreferrer" title="https://apps.apple.com/cn/developer/rongqing-wang/id1264542103" ref="nofollow noopener noreferrer">AppStore</a></td><td align="center"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fapps.apple.com%2Fcn%2Fapp%2Fid1488204246" target="_blank" rel="nofollow noopener noreferrer" title="https://apps.apple.com/cn/app/id1488204246" ref="nofollow noopener noreferrer">Elic</a></td><td align="center"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fapps.apple.com%2Fcn%2Fapp%2Fid1498426607" target="_blank" rel="nofollow noopener noreferrer" title="https://apps.apple.com/cn/app/id1498426607" ref="nofollow noopener noreferrer">Umemi</a></td></tr></tbody></table>
<h2 data-id="heading-1">前言</h2>
<p><code>MethodSwizzing</code> 方法交换是比较常用的所谓 <code>黑魔法</code>。但正如武侠小说中的绝世武功一般，也存在使用不恰当发生 <code>伤敌一千，自损八百</code> 的情况。</p>
<p>本文就带你来探索一下其中的坑，避免走火入魔。</p>
<h2 data-id="heading-2">一、 MethodSwizzingTool</h2>
<p>为了方便，我们封装一下常规的方法交换逻辑</p>
<pre><code class="hljs language-Objc copyable" lang="Objc"><span class="hljs-class"><span class="hljs-keyword">@implementation</span> <span class="hljs-title">MethodSwizzingTool</span></span>

+ (<span class="hljs-keyword">void</span>)swizzingClass:(Class)cls oldSEL:(SEL)oldSel toNewSel:(SEL)newSel &#123;
    <span class="hljs-keyword">if</span> (!cls) &#123; <span class="hljs-keyword">return</span>; &#125;
    Method oldM = class_getInstanceMethod(cls, oldSel);
    Method newM = class_getInstanceMethod(cls, newSel);
    method_exchangeImplementations(oldM, newM);
&#125;

<span class="hljs-keyword">@end</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">1.1 验证是否有效</h3>
<pre><code class="hljs language-Objc copyable" lang="Objc"><span class="hljs-class"><span class="hljs-keyword">@implementation</span> <span class="hljs-title">RYModel</span></span>

+(<span class="hljs-keyword">void</span>)load &#123;
    <span class="hljs-keyword">static</span> <span class="hljs-built_in">dispatch_once_t</span> onceToken;
    <span class="hljs-built_in">dispatch_once</span>(&onceToken, ^&#123;
        [MethodSwizzingTool swizzingClass:<span class="hljs-keyword">self</span> oldSEL:<span class="hljs-keyword">@selector</span>(functionA) toNewSel:<span class="hljs-keyword">@selector</span>(functionB)];
    &#125;);
&#125;

- (<span class="hljs-keyword">void</span>)functionA &#123;
    <span class="hljs-built_in">NSLog</span>(<span class="hljs-string">@"%s"</span>, __func__);
&#125;

- (<span class="hljs-keyword">void</span>)functionB &#123;
    <span class="hljs-built_in">NSLog</span>(<span class="hljs-string">@"%s"</span>, __func__);
    [<span class="hljs-keyword">self</span> functionB];
&#125;

<span class="hljs-keyword">@end</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em><strong>调用：</strong></em></p>
<pre><code class="hljs language-Objc copyable" lang="Objc">RYModel *ry = [[RYModel alloc] init];
[ry functionA];
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em><strong>输出：</strong></em></p>
<pre><code class="copyable">2021-08-07 17:01:53.954201+0800 MethodSwizzing[72309:15057493] -[RYModel functionB]
2021-08-07 17:01:53.954534+0800 MethodSwizzing[72309:15057493] -[RYModel functionA]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>嗯～感觉封装的没问题。</p>
<h2 data-id="heading-4">二、 子类的坑</h2>
<h3 data-id="heading-5">2.1 用子类方法替换父类方法，会怎样？</h3>
<p><em><strong>思考：</strong></em></p>
<blockquote>
<p>在子类 <code>RYSubModel</code> 中用 <code>子类</code> 的 <code>subFunctionA</code> 替换 <code>父类</code> 的 <code>functionA</code> ，<code>子类实例</code>和<code>父类实例</code>分别调用 <code>functionA</code> 会是什么样的结果呢？（父类中未做交换）</p>
</blockquote>
<p><em><strong>子类代码如下：</strong></em></p>
<pre><code class="hljs language-Objc copyable" lang="Objc"><span class="hljs-class"><span class="hljs-keyword">@implementation</span> <span class="hljs-title">RYSubModel</span></span>

+ (<span class="hljs-keyword">void</span>)load &#123;
    <span class="hljs-keyword">static</span> <span class="hljs-built_in">dispatch_once_t</span> onceToken;
    <span class="hljs-built_in">dispatch_once</span>(&onceToken, ^&#123;
        [MethodSwizzingTool swizzingClass:<span class="hljs-keyword">self</span> oldSEL:<span class="hljs-keyword">@selector</span>(functionA) toNewSel:<span class="hljs-keyword">@selector</span>(subFunctionA)];
    &#125;);
&#125;

- (<span class="hljs-keyword">void</span>)subFunctionA &#123;
    <span class="hljs-built_in">NSLog</span>(<span class="hljs-string">@"%s"</span>, __func__);
&#125;

<span class="hljs-keyword">@end</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em><strong>调用：</strong></em></p>
<pre><code class="hljs language-Objc copyable" lang="Objc">RYModel *ry = [[RYModel alloc] init];
[ry functionA];

RYSubModel *sub = [[RYSubModel alloc] init];
[sub functionA];
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em><strong>输出：</strong></em></p>
<pre><code class="copyable">2021-08-07 17:10:37.990097+0800 MethodSwizzing[72705:15063434] -[RYSubModel subFunctionA]
2021-08-07 17:10:37.990530+0800 MethodSwizzing[72705:15063434] -[RYSubModel subFunctionA]
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em><strong>分析</strong></em></p>
<p>用子类中的方法 <code>subFunctionA</code> 替换父类中的方法 <code>functionA</code>， <code>functionA</code> 的实现变成了 <code>subFunctionA</code>。</p>
<h3 data-id="heading-6">2.2 调用原实现</h3>
<p>一般我们交换方法后想要继续调用原本的实现一般会如<a href="https://juejin.cn/post/6993975469724925959#11-%E9%AA%8C%E8%AF%81%E6%98%AF%E5%90%A6%E6%9C%89%E6%95%88" target="_blank" title="#11-%E9%AA%8C%E8%AF%81%E6%98%AF%E5%90%A6%E6%9C%89%E6%95%88">上文中functionB</a>那样调用一下自己。</p>
<p>那么我们在用子类中的方法 <code>subFunctionA</code> 替换了父类中的方法 <code>functionA</code> 后想要继续调用 <code>functionA</code> 同理应该这么写：</p>
<pre><code class="hljs language-Objc copyable" lang="Objc">- (<span class="hljs-keyword">void</span>)subFunctionA &#123;
    [<span class="hljs-keyword">self</span> subFunctionA];
    <span class="hljs-built_in">NSLog</span>(<span class="hljs-string">@"%s"</span>, __func__);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em><strong>调用：</strong></em></p>
<pre><code class="hljs language-Objc copyable" lang="Objc">RYModel *ry = [[RYModel alloc] init];
[ry functionA];

RYSubModel *sub = [[RYSubModel alloc] init];
[sub functionA];
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em><strong>输出：</strong></em></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb085e4328d4432dbddda9552efa81c6~tplv-k3u1fbpfcp-watermark.image" alt="19-01.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>为什么呢？居然找不到了</p>
</blockquote>
<h4 data-id="heading-7">分析</h4>
<p>我们在用子类中的方法 <code>subFunctionA</code> 替换了父类中的方法 <code>functionA</code> 后</p>
<p><em><strong>父类中：</strong></em></p>
<p><code>functionA</code> 调用 <code>subFunctionA</code></p>
<p>但是父类本身方法列表中并没有 <code>subFunctionA</code> ，所以父类就报了 <code>unrecognized selector</code> 的错误。</p>
<h4 data-id="heading-8">修改调用</h4>
<p><em><strong>如果我们只调用子类：</strong></em></p>
<pre><code class="hljs language-Objc copyable" lang="Objc">RYSubModel *sub = [[RYSubModel alloc] init];
[sub functionA];
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em><strong>输出：</strong></em></p>
<pre><code class="copyable">2021-08-07 17:33:28.874108+0800 MethodSwizzing[73690:15075457] -[RYModel functionA]
2021-08-07 17:33:28.874564+0800 MethodSwizzing[73690:15075457] -[RYSubModel subFunctionA]
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>这里就是正常的</p>
</blockquote>
<h2 data-id="heading-9">三、 优化 MethodSwizzingTool</h2>
<p>我们能不能优化 <code>MethodSwizzingTool</code> 来防止这样的问题出现呢？</p>
<p><em><strong>可以！</strong></em></p>
<h3 data-id="heading-10">3.1 优化思路</h3>
<ul>
<li>出现上面找不到方法的原因是：<em><strong>子类用自己的实现直接替换了父类的方法</strong></em></li>
<li>那么我们能不能为子类动态添加一个和父类一样的方法呢？子类中进行替换的时候就不会影响父类了</li>
</ul>
<h3 data-id="heading-11">3.2 编写优化代码</h3>
<pre><code class="hljs language-Objc copyable" lang="Objc">+ (<span class="hljs-keyword">void</span>)swizzingClassB:(Class)cls oldSEL:(SEL)oldSel toNewSel:(SEL)newSel &#123;
    <span class="hljs-keyword">if</span> (!cls) &#123; <span class="hljs-keyword">return</span>; &#125;
    Method oldM = class_getInstanceMethod(cls, oldSel);
    Method newM = class_getInstanceMethod(cls, newSel);
    
    <span class="hljs-comment">// 先尝试给 cls 添加方法（SEL: oldSel  IMP: newM），防止子类直接替换父类中的方法</span>
    <span class="hljs-built_in">BOOL</span> addSuccess = class_addMethod(cls, oldSel, method_getImplementation(newM), method_getTypeEncoding(oldM));
    
    <span class="hljs-keyword">if</span> (addSuccess) &#123; <span class="hljs-comment">// 添加成功即：原本没有 oldSel，成功为子类添加了一个 oldSel - newM 的方法</span>
        <span class="hljs-comment">// 这里将原 newSel的imp替换为 oldM 的 IMP</span>
        class_replaceMethod(cls, newSel, method_getImplementation(oldM), method_getTypeEncoding(oldM));
    &#125;
    <span class="hljs-keyword">else</span> &#123;
        method_exchangeImplementations(oldM, newM);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">3.3 优化代码流程分析</h3>
<p>本案例子类调用流程分析：</p>
<ul>
<li>调用方法，准备用子类中的方法 <code>subFunctionA</code> 替换的方法 <code>functionA</code></li>
<li><code>Method oldM</code> 是从父类获取到的方法 <code>（SEL: functionA, IMP: functionA）</code></li>
<li><code>Method newM</code> 是从子类自己获取到的方法 <code>（SEL: subFunctionA, IMP: subFunctionA）</code></li>
<li>是否可以成功添加方法：<code>（SEL: functionA, IMP: subFunctionA）</code>
<ul>
<li>否：已存在 <code>SEL: functionA</code> 的方法</li>
<li>是：不存在 <code>SEL: functionA</code> 的方法
<ul>
<li>将子类的 <code>（SEL: subFunctionA, IMP: subFunctionA）</code> 替换为 <code>（SEL: subFunctionA, IMP: functionA）</code></li>
</ul>
</li>
</ul>
</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e2d6f1d5ecc04d6782656c86cb0fb862~tplv-k3u1fbpfcp-watermark.image" alt="19-02.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>父类实例
<ul>
<li><code>[ry functionA]</code></li>
<li>调用没有受子类方法交换的影响</li>
</ul>
</li>
<li>子类实例
<ul>
<li><code>[sub functionA]</code></li>
<li>没有出现父类调用找不到方法的情况</li>
</ul>
</li>
</ul>
<h2 data-id="heading-13">四、 如果父类的 functionA 没有实现呢？</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/149646bc2adf4961a51ac9228ebce9e9~tplv-k3u1fbpfcp-watermark.image" alt="19-03.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-14">4.1 分析</h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6ee150cd69ec4184b1568ae961718450~tplv-k3u1fbpfcp-watermark.image" alt="19-04.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>由于并不存在 <code>functionA</code> 的实现，所以这里的替换方法并没有成功。 <code>subFunctionA</code> 的调用就直接递归死循环了。</p>
<h3 data-id="heading-15">4.2 再优化</h3>
<p>通过设置默认实现的方式来避免死循环，新实现也为空的情景可以类似处理，这里就不赘述了。</p>
<pre><code class="hljs language-Objc copyable" lang="Objc">+ (<span class="hljs-keyword">void</span>)swizzingClassB:(Class)cls oldSEL:(SEL)oldSel toNewSel:(SEL)newSel &#123;
    <span class="hljs-keyword">if</span> (!cls) &#123; <span class="hljs-keyword">return</span>; &#125;
    Method oldM = class_getInstanceMethod(cls, oldSel);
    Method newM = class_getInstanceMethod(cls, newSel);
    
    <span class="hljs-keyword">if</span> (!oldM) &#123;
        <span class="hljs-comment">// 先用新的实现来，临时添加一个（这里忽略新实现也为空的情况，可以类似的处理）</span>
        class_addMethod(cls, oldSel, method_getImplementation(newM), method_getTypeEncoding(newM));
        <span class="hljs-comment">// 对 oldM 变量重新赋值</span>
        oldM = class_getInstanceMethod(cls, oldSel);
        <span class="hljs-comment">// 创建默认实现，可以进行一些日志收集之类的</span>
        IMP defaultIMP = imp_implementationWithBlock(^(<span class="hljs-keyword">id</span> <span class="hljs-keyword">self</span>, SEL _cmd)&#123;
            <span class="hljs-built_in">NSLog</span>(<span class="hljs-string">@"一些处理"</span>);
        &#125;);
        <span class="hljs-comment">// 为 oldM 设置 IMP</span>
        method_setImplementation(oldM, defaultIMP);
    &#125;
    
    <span class="hljs-comment">// 先尝试给 cls 添加方法（SEL: oldSel  IMP: newM），防止子类直接替换父类中的方法</span>
    <span class="hljs-built_in">BOOL</span> addSuccess = class_addMethod(cls, oldSel, method_getImplementation(newM), method_getTypeEncoding(oldM));
    
    <span class="hljs-keyword">if</span> (addSuccess) &#123; <span class="hljs-comment">// 添加成功即：原本没有 oldSel，成功为子类添加了一个 oldSel - newM 的方法</span>
        <span class="hljs-comment">// 这里将原 newSel的imp替换为 oldM 的 IMP</span>
        class_replaceMethod(cls, newSel, method_getImplementation(oldM), method_getTypeEncoding(oldM));
    &#125;
    <span class="hljs-keyword">else</span> &#123;
        method_exchangeImplementations(oldM, newM);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e2bd3adbe0943719ea2efb307443a8e~tplv-k3u1fbpfcp-watermark.image" alt="19-05.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-16">总结</h2>
<p>黑魔法虽好，使用也得倍加小心！</p>
<p>尤其要对方法的本质以及方法调用的流程烂熟于心才能随心所欲，内功到家，进阶武功才不会伤及自身。</p>
<p>👋欢迎点赞收藏关注♥️</p>
<p><em><strong>拓展阅读：</strong></em></p>
<ul>
<li><a href="https://juejin.cn/post/6979935428920999967" target="_blank" title="https://juejin.cn/post/6979935428920999967">objc_msgSend源码调试解读</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fryukiedev.gitbook.io%2Fwiki%2Fios%2Fqi-ios-di-ceng-zhi-shi-shu-li" target="_blank" rel="nofollow noopener noreferrer" title="https://ryukiedev.gitbook.io/wiki/ios/qi-ios-di-ceng-zhi-shi-shu-li" ref="nofollow noopener noreferrer">iOS底层知识梳理</a></li>
</ul></div>  
</div>
            
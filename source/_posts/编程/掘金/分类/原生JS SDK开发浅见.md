
---
title: '原生JS SDK开发浅见'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6144'
author: 掘金
comments: false
date: Sun, 25 Jul 2021 08:42:14 GMT
thumbnail: 'https://picsum.photos/400/300?random=6144'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>「本文已参与好文召集令活动，点击查看：<a href="https://juejin.cn/post/6978685539985653767" title="https://juejin.cn/post/6978685539985653767" target="_blank">后端、大前端双赛道投稿，2万元奖池等你挑战！</a>」</p>
<h2 data-id="heading-0">前言</h2>
<p>在开发JS SDK时，『原生 or 框架』不同人不同场景都有不同的选择。本文源于实际项目场景，阐述一些在原生环境下『不顺手』问题的处理。</p>
<h2 data-id="heading-1">1. 模块化开发</h2>
<pre><code class="copyable">// index.js
// 加入一个入口按钮
// 按钮点击增加侧边栏
// 点击空白隐藏侧边栏
// 侧边栏点击出现弹窗
// ...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如此写下去想想都头秃，像一篇流水账作文。</p>
<ul>
<li>为了让读者快速定位到寻找的代码段，可以使用<strong>模块化</strong>（利用 webpack ， gulp 等构建工具）。</li>
<li>为了弱化组织逻辑的时间顺序，可以使用<strong>面向对象</strong>，比如拆分 Class （拆分的粒度可以借鉴对框架中组件的使用）。</li>
</ul>
<pre><code class="copyable">//index.js
Class Entry &#123;&#125; // 入口按钮

// dropdown.js
Class Dropdown &#123; // 为指定dom绑定侧边栏
    show() &#123;&#125; // 显示侧边栏
    hidden() &#123;&#125; // 隐藏侧边栏
    select() &#123;&#125; // 选中打开弹框
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里将组件开发的经验活用在了原生环境，代码结构更清晰了。</p>
<h2 data-id="heading-2">2. 维护 innerHTML 的秩序</h2>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"list"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span>1<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span>2<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span>3<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>用 JS 动态生成上面一段 dom 可能是这样的。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> ul = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'ul'</span>);
ul.className = <span class="hljs-string">'list'</span>;
ul.innerHTML = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>].map(<span class="hljs-function"><span class="hljs-params">i</span> =></span> <span class="hljs-string">`<li><span class="hljs-subst">$&#123;i&#125;</span></li>`</span>).join(<span class="hljs-string">''</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>innerHTML 接受 HTML 序列化片段，因此我们可以使用模板字符串动态生成 dom 。不过这种方法存在局限性：</p>
<ol>
<li>需要一个已有节点作为容器，<strong>无法在插入容器前操作 dom</strong>；</li>
<li><strong>容器节点的属性设置仍然需要手动添加</strong>（比如class）；</li>
</ol>
<p>通过封装innerHTML可以克服上述局限性脱离容器生成一段 dom。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">const</span> wrap = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'div'</span>);
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> template2dom = <span class="xml"><span class="hljs-tag"><<span class="hljs-name">T</span> <span class="hljs-attr">extends</span> <span class="hljs-attr">HTMLElement</span>></span>(template: string): T => &#123;
    wrap.innerHTML = template;
    return wrap.children[0] as T;
&#125;;

const ul = template2dom(`
<span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"list"</span>></span>$&#123;
    [1, 2, 3].map(i => `<span class="hljs-tag"><<span class="hljs-name">li</span>></span>$&#123;i&#125;<span class="hljs-tag"></<span class="hljs-name">li</span>></span>`).join('')
&#125;<span class="hljs-tag"></<span class="hljs-name">ul</span>></span>`);
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>结合模块拆分可以将 dom 操作分为<strong>初始化渲染</strong>和<strong>动态修改</strong>。使用封装的 template2dom 可以得到模块的根节点，在根节点下 querySelector 可获取动态修改的节点，使用原生 dom API操作。</p>
<h2 data-id="heading-3">3. 清除事件</h2>
<p>使用框架时，我们可以不必关心自己监听的事件是不是该移除了，通常框架会替我们解决。现在需要我们来解决：</p>
<ul>
<li>当 dom 离开文档时，移除在其中绑定的事件；</li>
<li>当 dom 内有频繁更且需要绑定事件的节点，使用<strong>事件委托</strong>；</li>
</ul>
<p>知易行难，<strong>移除事件的位置通常与注册事件不在一起</strong>，为了获取监听函数和 dom 增加了很多在 class 中共享的属性；<strong>由于疏忽很可能遗漏某个 removeEventlistener</strong> 。封装一个事件管理类作为一个基类可以很好解决。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">abstract</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">EventCleaner</span> </span>&#123;
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">readonly</span> eventMap = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span> <HTMLElement, <span class="hljs-built_in">Set</span><&#123;
        <span class="hljs-attr">name</span>: keyof HTMLElementEventMap;
        cb(e: HTMLElementEventMap[keyof HTMLElementEventMap]): unknown;
    &#125;>>();
    addEventListener<T <span class="hljs-keyword">extends</span> keyof HTMLElementEventMap>(
        el: HTMLElement,
        <span class="hljs-attr">name</span>: T,
        <span class="hljs-attr">cb</span>: <span class="hljs-function">(<span class="hljs-params">e: HTMLElementEventMap[T]</span>) =></span> unknown
    ): <span class="hljs-built_in">void</span> &#123;
        el.addEventListener(name, cb);
        <span class="hljs-keyword">const</span> events = <span class="hljs-built_in">this</span>.eventMap.get(el);
        <span class="hljs-keyword">if</span> (events) &#123;
            events.add(&#123;name, cb&#125;);
        &#125;
        <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-built_in">this</span>.eventMap.set(el, <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>([&#123;name, cb&#125;]));
        &#125;
    &#125;
    cleanEvent(): <span class="hljs-built_in">void</span> &#123;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> [dom, events] <span class="hljs-keyword">of</span> <span class="hljs-built_in">Array</span>.from(<span class="hljs-built_in">this</span>.eventMap)) &#123;
            <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> &#123;name, cb&#125; <span class="hljs-keyword">of</span> events) &#123;
                dom.removeEventListener(name, cb);
            &#125;
        &#125;
        <span class="hljs-built_in">this</span>.eventMap.clear();
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样只需要在每个派生类写入一个卸载方法，调用 <code>cleanEvent</code> ,即可清除该实例内监听的所有事件。</p>
<h2 data-id="heading-4">4. 样式隔离</h2>
<p>样式隔离是 SDK 绕不开的问题。CSS Module 可在构建时修改 id 和 class 的形式，使得样式不会造成意外污染。</p>
<ul>
<li>hash：CSS Module 默认class，<strong>丢失语义性</strong>且<strong>随样式修改</strong> <em>（不利于下游覆盖样式）</em>；</li>
<li>local + name[md5]：兼顾语义性、唯一性且不会随样式修改。</li>
</ul>
<p><code>local + name\[md5\]</code> 并不是 css-loader 支持的形式，需要在构建时提供 hash</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> md5 = <span class="hljs-built_in">require</span>(<span class="hljs-string">'md5'</span>);
<span class="hljs-keyword">var</span> affix = md5(path.parse(packageName)).slice(<span class="hljs-number">0</span>, <span class="hljs-number">5</span>); <span class="hljs-comment">// 将包名md5作为CssModule的后缀</span>

<span class="hljs-comment">// webpack 配置</span>
&#123;
    <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/i</span>,
    use: [
        <span class="hljs-string">'style-loader'</span>,
        &#123;
            <span class="hljs-attr">loader</span>: <span class="hljs-string">'css-loader'</span>,
            <span class="hljs-attr">options</span>: &#123;
                <span class="hljs-attr">modules</span>: &#123;
                    <span class="hljs-attr">localIdentName</span>: <span class="hljs-string">`[local]_<span class="hljs-subst">$&#123;affix&#125;</span>`</span>,
                &#125;
            &#125;
        &#125;
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<p>以上是本人使用原生 JS 开发 SDK 的一些思考。其实主要围绕着梳理代码的秩序，原生API已足够强大不需要我扩展什么功能。前端框架给开发者更低的成本来养成逻辑清晰的习惯，也带来了一些思维惯性。<strong>希望能够取其精华弃其糟粕，无畏向前！</strong></p>
<p>源码参考：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fanyblue%2Fblue-feedback" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/anyblue/blue-feedback" ref="nofollow noopener noreferrer">github.com/anyblue/blu…</a></p></div>  
</div>
            
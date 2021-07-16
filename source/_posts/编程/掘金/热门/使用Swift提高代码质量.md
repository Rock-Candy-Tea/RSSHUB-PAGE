
---
title: '使用Swift提高代码质量'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f8f0f4ff0424a3e8415ae77e0d38a88~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 14 Jul 2021 05:11:31 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f8f0f4ff0424a3e8415ae77e0d38a88~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><h1 data-id="heading-0">前言</h1>
<p><code>京喜APP</code>最早在2019年引入了<code>Swift</code>，使用<code>Swift</code>完成了第一个订单模块的开发。之后一年多我们持续在团队/公司内部推广和普及<code>Swift</code>，目前<code>Swift</code>已经支撑了<code>70%+</code>以上的业务。通过使用<code>Swift</code>提高了团队内同学的开发效率，同时也带来了质量的提升，目前来自<code>Swift</code>的Crash的占比不到<code>1%</code>。在这过程中不断的学习/实践，团队内的<code>Code Review</code>，也对如何使用<code>Swift</code>来提高代码质量有更深的理解。</p>
<h1 data-id="heading-1">Swift特性</h1>
<p>在讨论如何使用<code>Swift</code>提高代码质量之前，我们先来看看<code>Swift</code>本身相比<code>ObjC</code>或其他编程语言有什么优势。<code>Swift</code>有三个重要的特性分别是<code>富有表现力</code>/<code>安全性</code>/<code>快速</code>，接下来我们分别从这三个特性简单介绍一下：</p>
<h3 data-id="heading-2">富有表现力</h3>
<p><code>Swift</code>提供更多的<code>编程范式</code>和<code>特性</code>支持，可以编写更少的代码，而且易于阅读和维护。</p>
<ul>
<li><code>基础类型</code> - 元组、Enum<code>关联类型</code></li>
<li><code>方法</code> - <code>方法重载</code></li>
<li><code>protocol</code> - 不限制只支持<code>class</code>、协议<code>默认</code>实现、<code>类</code>专属协议</li>
<li><code>泛型</code> - <code>protocol</code>关联类型、<code>where</code>实现类型约束、泛型扩展</li>
<li><code>可选值</code> - 可选值申明、可选链、隐式可选值</li>
<li><code>属性</code> - let、lazy、计算属性`、willset/didset、Property Wrappers</li>
<li><code>函数式编程</code> - 集合<code>filter/map/reduce</code>方法，提供更多标准库方法</li>
<li><code>并发</code> - async/await、actor</li>
<li><code>标准库框架</code> - <code>Combine</code>响应式框架、<code>SwiftUI</code>申明式UI框架、<code>Codable</code>JSON模型转换</li>
<li><code>Result builder</code> - 描述实现<code>DSL</code>的能力</li>
<li><code>动态性</code> - dynamicCallable、dynamicMemberLookup</li>
<li><code>其他</code> - 扩展、subscript、操作符重写、嵌套类型、区间</li>
<li><code>Swift Package Manager</code> - 基于Swift的包管理工具，可以直接用<code>Xcode</code>进行管理更方便</li>
<li><code>struct</code> - 初始化方法自动补齐</li>
<li><code>类型推断</code> - 通过编译器强大的<code>类型推断</code>编写代码时可以减少很多类型申明</li>
</ul>
<blockquote>
<p>提示：类型推断同时也会增加一定的编译<code>耗时</code>，不过<code>Swift</code>团队也在不断的改善编译速度。</p>
</blockquote>
<h3 data-id="heading-3">安全性</h3>
<h4 data-id="heading-4">代码安全</h4>
<ul>
<li><code>let属性</code> - 使用<code>let</code>申明常量避免被修改。</li>
<li><code>值类型</code> - 值类型可以避免在方法调用等<code>参数传递</code>过程中状态被修改。</li>
<li><code>访问控制</code> - 通过<code>public</code>和<code>final</code>限制模块外使用<code>class</code>不能被<code>继承</code>和<code>重写</code>。</li>
<li><code>强制异常处理</code> - 方法需要抛出异常时，需要申明为<code>throw</code>方法。当调用可能会<code>throw</code>异常的方法，需要强制捕获异常避免将异常暴露到上层。</li>
<li><code>模式匹配</code> - 通过模式匹配检测<code>switch</code>中未处理的case。</li>
</ul>
<h4 data-id="heading-5">类型安全</h4>
<ul>
<li><code>强制类型转换</code> - 禁止<code>隐式类型转换</code>避免转换中带来的异常问题。同时类型转换不会带来<code>额外</code>的运行时消耗。。</li>
</ul>
<blockquote>
<p>提示：编写<code>ObjC</code>代码时，我们通常会在编码时添加类型检查避免运行时崩溃导致<code>Crash</code>。</p>
</blockquote>
<ul>
<li><code>KeyPath</code> - <code>KeyPath</code>相比使用<code>字符串</code>可以提供属性名和类型信息，可以利用编译器检查。</li>
<li><code>泛型</code> - 提供<code>泛型</code>和协议<code>关联类型</code>，可以编写出类型安全的代码。相比<code>Any</code>可以更多利用编译时检查发现类型问题。</li>
<li><code>Enum关联类型</code> - 通过给特定枚举指定类型避免使用<code>Any</code>。</li>
</ul>
<h4 data-id="heading-6">内存安全</h4>
<ul>
<li><code>空安全</code> - 通过标识可选值避免<code>空指针</code>带来的异常问题</li>
<li><code>ARC</code> - 使用<code>自动</code>内存管理避免<code>手动</code>管理内存带来的各种内存问题</li>
<li><code>强制初始化</code> - 变量使用前必须<code>初始化</code></li>
<li><code>内存独占访问</code> - 通过编译器检查发现潜在的内存冲突问题</li>
</ul>
<h4 data-id="heading-7">线程安全</h4>
<ul>
<li><code>值类型</code> - 更多使用值类型减少在多线程中遇到的<code>数据竞争</code>问题</li>
<li><code>async/await</code> - 提供<code>async</code>函数使我们可以用结构化的方式编写并发操作。避免基于<code>闭包</code>的异步方式带来的内存<code>循环引用</code>和无法抛出异常的问题</li>
<li><code>Actor</code> - 提供<code>Actor</code>模型避免多线程开发中进行数据共享时发生的数据竞争问题，同时避免在使用锁时带来的死锁等问题</li>
</ul>
<h3 data-id="heading-8">快速</h3>
<ul>
<li><code>值类型</code> - 相比<code>class</code>不需要额外的<code>堆内存</code>分配/释放和更少的内存消耗</li>
<li><code>方法静态派发</code> - 方法调用支持<code>静态</code>调用相比原有ObjC<code>消息转发</code>调用性能更好</li>
<li><code>编译器优化</code> - Swift的<code>静态性</code>可以使编译器做更多优化。例如<code>Tree Shaking</code>相关优化移除未使用的类/方法等减少二进制文件大小。使用<code>静态派发</code>/<code>方法内联优化</code>/<code>泛型特化</code>/<code>写时复制</code>等优化提高运行时性能</li>
</ul>
<blockquote>
<p>提示：<code>ObjC</code>动态派发同时会导致编译器无法进行移除无用方法/类的优化，编译器并不知道是否可能被用到。</p>
</blockquote>
<ul>
<li><code>ARC优化</code> - 虽然和<code>ObjC</code>一样都是使用<code>ARC</code>，<code>Swift</code>通过编译器优化，可以进行更快的内存回收和更少的内存引用计数管理</li>
</ul>
<blockquote>
<p>提示： 相比<code>ObjC</code>，Swift内部不需要使用<code>autorelease</code>进行管理。</p>
</blockquote>
<h1 data-id="heading-9">代码质量指标</h1>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f8f0f4ff0424a3e8415ae77e0d38a88~tplv-k3u1fbpfcp-watermark.image" alt="代码质量指标" loading="lazy" referrerpolicy="no-referrer">
以上是一些常见的代码质量指标。我们的目标是如何更好的使用<code>Swift</code>编写出符合代码质量指标要求的代码。</p>
<blockquote>
<p>提示：本文不涉及设计模式/架构，更多关注如何通过合理使用<code>Swift</code>特性做部分代码段的重构。</p>
</blockquote>
<h2 data-id="heading-10">一些不错的实践</h2>
<h3 data-id="heading-11">利用编译检查</h3>
<h4 data-id="heading-12">减少使用<code>Any/AnyObject</code></h4>
<p>因为<code>Any/AnyObject</code>缺少明确的类型信息，编译器无法进行类型检查，会带来一些问题：</p>
<ul>
<li>编译器无法检查类型是否正确保证类型安全</li>
<li>代码中大量的<code>as?</code>转换</li>
<li>类型的缺失导致编译器无法做一些潜在的<code>编译优化</code></li>
</ul>
<h4 data-id="heading-13">使用<code>自定义类型</code>代替<code>Dictionary</code></h4>
<p>代码中大量<code>Dictionary</code>数据结构会降低代码可维护性，同时带来潜在的<code>bug</code>：</p>
<ul>
<li><code>key</code>需要字符串硬编码，编译时无法检查</li>
<li><code>value</code>没有类型限制。<code>修改</code>时类型无法限制，读取时需要重复类型转换和解包操作</li>
<li>无法利用<code>空安全</code>特性，指定某个属性必须有值</li>
</ul>
<h5 data-id="heading-14">不推荐</h5>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">let</span> dic: [<span class="hljs-type">String</span>: <span class="hljs-keyword">Any</span>]
<span class="hljs-keyword">let</span> num <span class="hljs-operator">=</span> dic[<span class="hljs-string">"value"</span>] <span class="hljs-keyword">as?</span> <span class="hljs-type">Int</span>
dic[<span class="hljs-string">"name"</span>] <span class="hljs-operator">=</span> <span class="hljs-string">"name"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-15">推荐</h5>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">Data</span> </span>&#123;
  <span class="hljs-keyword">let</span> num: <span class="hljs-type">Int</span>
  <span class="hljs-keyword">var</span> name: <span class="hljs-type">String</span>?
&#125;
<span class="hljs-keyword">let</span> num <span class="hljs-operator">=</span> data.num
data.name <span class="hljs-operator">=</span> <span class="hljs-string">"name"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>提示：部分场景可以考虑使用<code>Dictionary</code>。1.数据并不<code>读取</code>只是用来传递。2.数据太过于动态性没有明确的类型。</p>
</blockquote>
<h4 data-id="heading-16">使用<code>枚举关联值</code>代替<code>Any</code></h4>
<p>例如使用枚举改造<code>NSAttributedString</code>API，原有API<code>value</code>为<code>Any</code>类型无法限制特定的类型。</p>
<h5 data-id="heading-17">优化前</h5>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">let</span> string <span class="hljs-operator">=</span> <span class="hljs-type">NSMutableAttributedString</span>()
string.addAttribute(.foregroundColor, value: <span class="hljs-type">UIColor</span>.red, range: range)
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-18">改造后</h5>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">enum</span> <span class="hljs-title">NSAttributedStringKey</span> </span>&#123;
  <span class="hljs-keyword">case</span> foregroundColor(<span class="hljs-type">UIColor</span>)
&#125;
<span class="hljs-keyword">let</span> string <span class="hljs-operator">=</span> <span class="hljs-type">NSMutableAttributedString</span>()
string.addAttribute(.foregroundColor(<span class="hljs-type">UIColor</span>.red), range: range) <span class="hljs-comment">// 不传递Color会报错</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-19">使用<code>泛型</code>/<code>协议关联类型</code>代替<code>Any</code></h4>
<p>使用<code>泛型</code>或<code>协议关联类型</code>代替<code>Any</code>，通过<code>泛型类型约束</code>来使编译器进行更多的类型检查。</p>
<h4 data-id="heading-20">使用<code>枚举</code>/<code>常量</code>代替<code>硬编码</code></h4>
<p>代码中存在重复的<code>硬编码</code>字符串/数字，在修改时可能会因为不同步引发<code>bug</code>。尽可能减少<code>硬编码</code>字符串/数字，使用<code>枚举</code>或<code>常量</code>代替。</p>
<h4 data-id="heading-21">使用<code>KeyPath</code>代替<code>字符串</code>硬编码</h4>
<p><code>KeyPath</code>包含属性名和类型信息，可以避免<code>硬编码</code>字符串，同时当属性名或类型改变时编译器会进行检查。</p>
<h5 data-id="heading-22">不推荐</h5>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">SomeClass</span>: <span class="hljs-title">NSObject</span> </span>&#123;
    <span class="hljs-keyword">@objc</span> <span class="hljs-keyword">dynamic</span> <span class="hljs-keyword">var</span> someProperty: <span class="hljs-type">Int</span>
    <span class="hljs-function"><span class="hljs-keyword">init</span>(<span class="hljs-params">someProperty</span>: <span class="hljs-type">Int</span>)</span> &#123;
        <span class="hljs-keyword">self</span>.someProperty <span class="hljs-operator">=</span> someProperty
    &#125;
&#125;
<span class="hljs-keyword">let</span> object <span class="hljs-operator">=</span> <span class="hljs-type">SomeClass</span>(someProperty: <span class="hljs-number">10</span>)
object.observeValue(forKeyPath: <span class="hljs-string">""</span>, of: <span class="hljs-literal">nil</span>, change: <span class="hljs-literal">nil</span>, context: <span class="hljs-literal">nil</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-23">推荐</h5>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">let</span> object <span class="hljs-operator">=</span> <span class="hljs-type">SomeClass</span>(someProperty: <span class="hljs-number">10</span>)
object.observe(\.someProperty) &#123; object, change <span class="hljs-keyword">in</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-24">内存安全</h3>
<h4 data-id="heading-25">减少使用<code>!</code>属性</h4>
<p><code>!</code>属性会在读取时隐式<code>强解包</code>，当值不存在时产生运行时异常导致Crash。</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ViewController</span>: <span class="hljs-title">UIViewController</span> </span>&#123;
    <span class="hljs-keyword">@IBOutlet</span> <span class="hljs-keyword">private</span> <span class="hljs-keyword">var</span> label: <span class="hljs-type">UILabel</span>! <span class="hljs-comment">// @IBOutlet需要使用!</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-26">减少使用<code>!</code>进行强解包</h4>
<p>使用<code>!</code>强解包会在值不存在时产生运行时异常导致Crash。</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">var</span> num: <span class="hljs-type">Int</span>?
<span class="hljs-keyword">let</span> num2 <span class="hljs-operator">=</span> num<span class="hljs-operator">!</span> <span class="hljs-comment">// 错误</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>提示：建议只在小范围的局部代码段使用<code>!</code>强解包。</p>
</blockquote>
<h4 data-id="heading-27">避免使用<code>try!</code>进行错误处理</h4>
<p>使用<code>try!</code>会在方法抛出异常时产生运行时异常导致Crash。</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">try!</span> method()
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-28">使用<code>weak</code>/<code>unowned</code>避免循环引用</h4>
<pre><code class="hljs language-swift copyable" lang="swift">resource.request().onComplete &#123; [<span class="hljs-keyword">weak</span> <span class="hljs-keyword">self</span>] response <span class="hljs-keyword">in</span>
  <span class="hljs-keyword">guard</span> <span class="hljs-keyword">let</span> <span class="hljs-keyword">self</span> <span class="hljs-operator">=</span> <span class="hljs-keyword">self</span> <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">return</span>
  &#125;
  <span class="hljs-keyword">let</span> model <span class="hljs-operator">=</span> <span class="hljs-keyword">self</span>.updateModel(response)
  <span class="hljs-keyword">self</span>.updateUI(model)
&#125;

resource.request().onComplete &#123; [<span class="hljs-keyword">unowned</span> <span class="hljs-keyword">self</span>] response <span class="hljs-keyword">in</span>
  <span class="hljs-keyword">let</span> model <span class="hljs-operator">=</span> <span class="hljs-keyword">self</span>.updateModel(response)
  <span class="hljs-keyword">self</span>.updateUI(model)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-29">减少使用<code>unowned</code></h4>
<p><code>unowned</code>在值不存在时会产生运行时异常导致Crash，只有在确定<code>self</code>一定会存在时才使用<code>unowned</code>。</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Class</span> </span>&#123;
    <span class="hljs-keyword">@objc</span> <span class="hljs-keyword">unowned</span> <span class="hljs-keyword">var</span> object: <span class="hljs-type">Object</span>
    <span class="hljs-keyword">@objc</span> <span class="hljs-keyword">weak</span> <span class="hljs-keyword">var</span> object: <span class="hljs-type">Object</span>?
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>unowned</code>/<code>weak</code>区别：</p>
<ul>
<li><code>weak</code> - 必须设置为可选值，会进行弱引用处理性能更差。会自动设置为<code>nil</code></li>
<li><code>unowned</code> - 可以不设置为可选值，不会进行弱引用处理性能更好。但是不会自动设置为<code>nil</code>, 如果<code>self</code>已释放会触发错误.</li>
</ul>
<h3 data-id="heading-30">错误处理方式</h3>
<ul>
<li><code>可选值</code> - 调用方并不关注内部可能会发生错误，当发生错误时返回<code>nil</code></li>
<li><code>try/catch</code> - 明确提示调用方需要处理异常，需要实现<code>Error</code>协议定义明确的错误类型</li>
<li><code>assert</code> - 断言。只能在<code>Debug</code>模式下生效</li>
<li><code>precondition</code> - 和<code>assert</code>类似，可以再<code>Debug</code>/<code>Release</code>模式下生效</li>
<li><code>fatalError</code> - 产生运行时崩溃会导致Crash，应避免使用</li>
<li><code>Result</code> - 通常用于<code>闭包</code>异步回调返回值</li>
</ul>
<h3 data-id="heading-31">减少使用可选值</h3>
<p><code>可选值</code>的价值在于通过明确标识值可能会为<code>nil</code>并且编译器强制对值进行<code>nil</code>判断。但是不应该随意的定义可选值，可选值不能用<code>let</code>定义，并且使用时必须进行<code>解包</code>操作相对比较繁琐。在代码设计时应考虑<code>这个值是否有可能为nil</code>，只在合适的场景使用可选值。</p>
<h4 data-id="heading-32">使用<code>init</code>注入代替<code>可选值</code>属性</h4>
<h5 data-id="heading-33">不推荐</h5>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Object</span> </span>&#123;
  <span class="hljs-keyword">var</span> num: <span class="hljs-type">Int</span>?
&#125;
<span class="hljs-keyword">let</span> object <span class="hljs-operator">=</span> <span class="hljs-type">Object</span>()
object.num <span class="hljs-operator">=</span> <span class="hljs-number">1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-34">推荐</h5>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Object</span> </span>&#123;
  <span class="hljs-keyword">let</span> num: <span class="hljs-type">Int</span>

  <span class="hljs-function"><span class="hljs-keyword">init</span>(<span class="hljs-params">num</span>: <span class="hljs-type">Int</span>)</span> &#123;
    <span class="hljs-keyword">self</span>.num <span class="hljs-operator">=</span> num
  &#125;
&#125;
<span class="hljs-keyword">let</span> object <span class="hljs-operator">=</span> <span class="hljs-type">Object</span>(num: <span class="hljs-number">1</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-35">避免随意给予可选值默认值</h4>
<p>在使用可选值时，通常我们需要在可选值为<code>nil</code>时进行异常处理。有时候我们会通过给予可选值<code>默认值</code>的方式来处理。但是这里应考虑在什么场景下可以给予默认值。在不能给予默认值的场景应当及时使用<code>return</code>或<code>抛出异常</code>，避免错误的值被传递到更多的业务流程。</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">confirmOrder</span>(<span class="hljs-params">id</span>: <span class="hljs-type">String</span>)</span> &#123;&#125;

confirmOrder(id: orderId <span class="hljs-operator">??</span> <span class="hljs-string">""</span>) <span class="hljs-comment">// 随意给予默认值，可能会导致后面业务流程发现错误</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>提示：通常强业务相关的值不能给予默认值：例如<code>商品/订单id</code>或是<code>价格</code>。在可以使用兜底逻辑的场景使用默认值，例如<code>默认文字/文字颜色</code>。</p>
</blockquote>
<h4 data-id="heading-36">使用枚举优化可选值</h4>
<p><code>Object</code>结构同时只会有一个值存在：</p>
<h5 data-id="heading-37">优化前</h5>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Object</span> </span>&#123;
    <span class="hljs-keyword">var</span> name: <span class="hljs-type">Int</span>?
    <span class="hljs-keyword">var</span> num: <span class="hljs-type">Int</span>?
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-38">优化后</h5>
<ul>
<li><code>降低内存占用</code> - <code>枚举关联类型</code>的大小取决于最大的关联类型大小</li>
<li><code>逻辑更清晰</code> - 使用<code>enum</code>相比大量使用<code>if/else</code>逻辑更清晰</li>
</ul>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">enum</span> <span class="hljs-title">CustomType</span> </span>&#123;
    <span class="hljs-keyword">case</span> name(<span class="hljs-type">String</span>)
    <span class="hljs-keyword">case</span> num(<span class="hljs-type">Int</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-39">减少<code>var</code>属性</h3>
<h4 data-id="heading-40">使用计算属性</h4>
<p>使用<code>计算属性</code>可以减少多个变量同步带来的潜在bug。</p>
<h5 data-id="heading-41">不推荐</h5>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">model</span> </span>&#123;
  <span class="hljs-keyword">var</span> data: <span class="hljs-type">Object</span>?
  <span class="hljs-keyword">var</span> loaded: <span class="hljs-type">Bool</span>
&#125;
model.data <span class="hljs-operator">=</span> <span class="hljs-type">Object</span>()
loaded <span class="hljs-operator">=</span> <span class="hljs-literal">false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-42">推荐</h5>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">model</span> </span>&#123;
  <span class="hljs-keyword">var</span> data: <span class="hljs-type">Object</span>?
  <span class="hljs-keyword">var</span> loaded: <span class="hljs-type">Bool</span> &#123;
    <span class="hljs-keyword">return</span> data <span class="hljs-operator">!=</span> <span class="hljs-literal">nil</span>
  &#125;
&#125;
model.data <span class="hljs-operator">=</span> <span class="hljs-type">Object</span>()
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>提示：计算属性因为每次都会重复计算，所以计算过程需要轻量避免带来性能问题。</p>
</blockquote>
<h3 data-id="heading-43">控制流</h3>
<h4 data-id="heading-44">使用<code>filter/reduce/map</code>代替<code>for</code>循环</h4>
<p>使用<code>filter/reduce/map</code>可以带来很多好处，包括更少的局部变量，减少模板代码，代码更加清晰，可读性更高。</p>
<h5 data-id="heading-45">不推荐</h5>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">let</span> nums <span class="hljs-operator">=</span> [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>]
<span class="hljs-keyword">var</span> result <span class="hljs-operator">=</span> []
<span class="hljs-keyword">for</span> num <span class="hljs-keyword">in</span> nums &#123;
    <span class="hljs-keyword">if</span> num <span class="hljs-operator"><</span> <span class="hljs-number">3</span> &#123;
        result.append(<span class="hljs-type">String</span>(num))
    &#125;
&#125;
<span class="hljs-comment">// result = ["1", "2"]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-46">推荐</h5>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">let</span> nums <span class="hljs-operator">=</span> [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>]
<span class="hljs-keyword">let</span> result <span class="hljs-operator">=</span> nums.filter &#123; <span class="hljs-variable">$0</span> <span class="hljs-operator"><</span> <span class="hljs-number">3</span> &#125;.map &#123; <span class="hljs-type">String</span>(<span class="hljs-variable">$0</span>) &#125;
<span class="hljs-comment">// result = ["1", "2"]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-47">使用<code>guard</code>进行提前返回</h4>
<h5 data-id="heading-48">推荐</h5>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">guard</span> <span class="hljs-operator">!</span>a <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">return</span>
&#125;
<span class="hljs-keyword">guard</span> <span class="hljs-operator">!</span>b <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">return</span>
&#125;
<span class="hljs-comment">// do</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-49">不推荐</h5>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">if</span> a &#123;
    <span class="hljs-keyword">if</span> b &#123;
        <span class="hljs-comment">// do</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-50">使用三元运算符<code>?:</code></h4>
<h6 data-id="heading-51">推荐</h6>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">let</span> b <span class="hljs-operator">=</span> <span class="hljs-literal">true</span>
<span class="hljs-keyword">let</span> a <span class="hljs-operator">=</span> b <span class="hljs-operator">?</span> <span class="hljs-number">1</span> : <span class="hljs-number">2</span>

<span class="hljs-keyword">let</span> c: <span class="hljs-type">Int</span>?
<span class="hljs-keyword">let</span> b <span class="hljs-operator">=</span> c <span class="hljs-operator">??</span> <span class="hljs-number">1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-52">不推荐</h6>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">var</span> a: <span class="hljs-type">Int</span>?
<span class="hljs-keyword">if</span> b &#123;
    a <span class="hljs-operator">=</span> <span class="hljs-number">1</span>
&#125; <span class="hljs-keyword">else</span> &#123;
    a <span class="hljs-operator">=</span> <span class="hljs-number">2</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-53">使用<code>for where</code>优化循环</h4>
<p><code>for</code>循环添加<code>where</code>语句，只有当<code>where</code>条件满足时才会进入循环</p>
<h5 data-id="heading-54">不推荐</h5>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">for</span> item <span class="hljs-keyword">in</span> collection &#123;
  <span class="hljs-keyword">if</span> item.hasProperty &#123;
    <span class="hljs-comment">// ...</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-55">推荐</h5>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">for</span> item <span class="hljs-keyword">in</span> collection <span class="hljs-keyword">where</span> item.hasProperty &#123;
  <span class="hljs-comment">// item.hasProperty == true，才会进入循环</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-56">使用<code>defer</code></h4>
<p><code>defer</code>可以保证在函数退出前一定会执行。可以使用<code>defer</code>中实现退出时一定会执行的操作例如<code>资源释放</code>等避免遗漏。</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">method</span>()</span> &#123;
    <span class="hljs-keyword">defer</span> &#123;
        <span class="hljs-comment">// 会在method作用域结束的时候调用</span>
    &#125;
    <span class="hljs-comment">// do</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-57">字符串</h3>
<h4 data-id="heading-58">使用<code>"""</code></h4>
<p>在定义<code>复杂</code>字符串时，使用<code>多行字符串字面量</code>可以保持原有字符串的换行符号/引号等特殊字符，不需要使用<code>\</code>进行转义。</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">let</span> quotation <span class="hljs-operator">=</span> <span class="hljs-string">"""
The White Rabbit put on his spectacles.  "Where shall I begin,
please your Majesty?" he asked.

"Begin at the beginning," the King said gravely, "and go on
till you come to the end; then stop."
"""</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>提示：上面字符串中的<code>""</code>和换行可以自动保留。</p>
</blockquote>
<h4 data-id="heading-59">使用字符串插值</h4>
<p>使用字符串插值可以提高代码可读性。</p>
<h5 data-id="heading-60">不推荐</h5>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">let</span> multiplier <span class="hljs-operator">=</span> <span class="hljs-number">3</span>
<span class="hljs-keyword">let</span> message <span class="hljs-operator">=</span> <span class="hljs-type">String</span>(multiplier) <span class="hljs-operator">+</span> <span class="hljs-string">"times 2.5 is"</span> <span class="hljs-operator">+</span> <span class="hljs-type">String</span>((<span class="hljs-type">Double</span>(multiplier) <span class="hljs-operator">*</span> <span class="hljs-number">2.5</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-61">推荐</h5>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">let</span> multiplier <span class="hljs-operator">=</span> <span class="hljs-number">3</span>
<span class="hljs-keyword">let</span> message <span class="hljs-operator">=</span> <span class="hljs-string">"<span class="hljs-subst">\(multiplier)</span> times 2.5 is <span class="hljs-subst">\(Double(multiplier) <span class="hljs-operator">*</span> <span class="hljs-number">2.5</span>)</span>"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-62">集合</h3>
<h4 data-id="heading-63">使用标准库提供的高阶函数</h4>
<h5 data-id="heading-64">不推荐</h5>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">var</span> nums <span class="hljs-operator">=</span> []
nums.count <span class="hljs-operator">==</span> <span class="hljs-number">0</span>
nums[<span class="hljs-number">0</span>]
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-65">推荐</h5>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">var</span> nums <span class="hljs-operator">=</span> []
nums.isEmpty
nums.first
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-66">访问控制</h3>
<p><code>Swift</code>中默认访问控制级别为<code>internal</code>。编码中应当尽可能减小<code>属性</code>/<code>方法</code>/<code>类型</code>的访问控制级别隐藏内部实现。</p>
<blockquote>
<p>提示：同时也有利于编译器进行优化。</p>
</blockquote>
<h4 data-id="heading-67">使用<code>private</code>/<code>fileprivate</code>修饰私有<code>属性</code>和<code>方法</code></h4>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">private</span> <span class="hljs-keyword">let</span> num <span class="hljs-operator">=</span> <span class="hljs-number">1</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyClass</span> </span>&#123;
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">var</span> num: <span class="hljs-type">Int</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-68">使用<code>private(set)</code>修饰外部只读/内部可读写属性</h4>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyClass</span> </span>&#123;
    <span class="hljs-keyword">private(set)</span> <span class="hljs-keyword">var</span> num <span class="hljs-operator">=</span> <span class="hljs-number">1</span>
&#125;
<span class="hljs-keyword">let</span> num <span class="hljs-operator">=</span> <span class="hljs-type">MyClass</span>().num
<span class="hljs-type">MyClass</span>().num <span class="hljs-operator">=</span> <span class="hljs-number">2</span> <span class="hljs-comment">// 会编译报错</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-69">函数</h3>
<h4 data-id="heading-70">使用参数默认值</h4>
<p>使用参数<code>默认值</code>，可以使调用方传递<code>更少</code>的参数。</p>
<h5 data-id="heading-71">不推荐</h5>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">test</span>(<span class="hljs-params">a</span>: <span class="hljs-type">Int</span>, <span class="hljs-params">b</span>: <span class="hljs-type">String</span>?, <span class="hljs-params">c</span>: <span class="hljs-type">Int</span>?)</span> &#123;
&#125;
test(<span class="hljs-number">1</span>, <span class="hljs-literal">nil</span>, <span class="hljs-literal">nil</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-72">推荐</h5>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">test</span>(<span class="hljs-params">a</span>: <span class="hljs-type">Int</span>, <span class="hljs-params">b</span>: <span class="hljs-type">String</span>? <span class="hljs-operator">=</span> <span class="hljs-literal">nil</span>, <span class="hljs-params">c</span>: <span class="hljs-type">Int</span>? <span class="hljs-operator">=</span> <span class="hljs-literal">nil</span>)</span> &#123;
&#125;
test(<span class="hljs-number">1</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>提示：相比<code>ObjC</code>，<code>参数默认值</code>也可以让我们定义更少的方法。</p>
</blockquote>
<h4 data-id="heading-73">限制参数数量</h4>
<p>当方法参数过多时考虑使用<code>自定义类型</code>代替。</p>
<h5 data-id="heading-74">不推荐</h5>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">f</span>(<span class="hljs-params">a</span>: <span class="hljs-type">Int</span>, <span class="hljs-params">b</span>: <span class="hljs-type">Int</span>, <span class="hljs-params">c</span>: <span class="hljs-type">Int</span>, <span class="hljs-params">d</span>: <span class="hljs-type">Int</span>, <span class="hljs-params">e</span>: <span class="hljs-type">Int</span>, <span class="hljs-params">f</span>: <span class="hljs-type">Int</span>)</span> &#123;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-75">推荐</h5>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">Params</span> </span>&#123;
    <span class="hljs-keyword">let</span> a, b, c, d, e, f: <span class="hljs-type">Int</span>
&#125;
<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">f</span>(<span class="hljs-params">params</span>: <span class="hljs-type">Params</span>)</span> &#123;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-76">使用<code>@discardableResult</code></h4>
<p>某些方法使用方并不一定会处理返回值，可以考虑添加<code>@discardableResult</code>标识提示<code>Xcode</code>允许不处理返回值不进行<code>warning</code>提示。</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-comment">// 上报方法使用方不关心是否成功</span>
<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">report</span>(<span class="hljs-params">id</span>: <span class="hljs-type">String</span>)</span> -> <span class="hljs-type">Bool</span> &#123;&#125; 

<span class="hljs-keyword">@discardableResult</span> <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">report2</span>(<span class="hljs-params">id</span>: <span class="hljs-type">String</span>)</span> -> <span class="hljs-type">Bool</span> &#123;&#125;

report(<span class="hljs-string">"1"</span>) <span class="hljs-comment">// 编译器会警告</span>
report2(<span class="hljs-string">"1"</span>) <span class="hljs-comment">// 不处理返回值编译器不会警告</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-77">元组</h3>
<h4 data-id="heading-78">避免过长的元组</h4>
<p>元组虽然具有类型信息，但是并不包含变量名信息，使用方并不清晰知道变量的含义。所以当元组数量过多时考虑使用<code>自定义类型</code>代替。</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">test</span>()</span> -> (<span class="hljs-type">Int</span>, <span class="hljs-type">Int</span>, <span class="hljs-type">Int</span>) &#123;

&#125;

<span class="hljs-keyword">let</span> (a, b, c) <span class="hljs-operator">=</span> test()
<span class="hljs-comment">// a，b，c类型一致，没有命名信息不清楚每个变量的含义</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-79">系统库</h3>
<h4 data-id="heading-80"><code>KVO</code>/<code>Notification</code> 使用 <code>block</code> API</h4>
<p><code>block</code> API的优势：</p>
<ul>
<li><code>KVO</code> 可以支持 <code>KeyPath</code></li>
<li>不需要主动移除监听，<code>observer</code>释放时自动移除监听</li>
</ul>
<h5 data-id="heading-81">不推荐</h5>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Object</span>: <span class="hljs-title">NSObject</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-keyword">init</span>()</span> &#123;
    <span class="hljs-keyword">super</span>.<span class="hljs-keyword">init</span>()
    addObserver(<span class="hljs-keyword">self</span>, forKeyPath: <span class="hljs-string">"value"</span>, options: .new, context: <span class="hljs-literal">nil</span>)
    <span class="hljs-type">NotificationCenter</span>.default.addObserver(<span class="hljs-keyword">self</span>, selector: #selector(test), name: <span class="hljs-type">NSNotification</span>.<span class="hljs-type">Name</span>(rawValue: <span class="hljs-string">""</span>), object: <span class="hljs-literal">nil</span>)
  &#125;

  <span class="hljs-keyword">override</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">func</span> <span class="hljs-title">observeValue</span>(<span class="hljs-title">forKeyPath</span> <span class="hljs-title">keyPath</span>: <span class="hljs-title">String</span>?, <span class="hljs-title">of</span> <span class="hljs-title">object</span>: <span class="hljs-title">Any</span>?, <span class="hljs-title">change</span>: [<span class="hljs-title">NSKeyValueChangeKey</span> : <span class="hljs-title">Any</span>]?, <span class="hljs-title">context</span>: <span class="hljs-title">UnsafeMutableRawPointer</span>?) </span>&#123;
  &#125;

  <span class="hljs-keyword">@objc</span> <span class="hljs-keyword">private</span> <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">test</span>()</span> &#123;
  &#125;

  <span class="hljs-keyword">deinit</span> &#123;
    removeObserver(<span class="hljs-keyword">self</span>, forKeyPath: <span class="hljs-string">"value"</span>)
    <span class="hljs-type">NotificationCenter</span>.default.removeObserver(<span class="hljs-keyword">self</span>)
  &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-82">推荐</h5>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Object</span>: <span class="hljs-title">NSObject</span> </span>&#123;

  <span class="hljs-keyword">private</span> <span class="hljs-keyword">var</span> observer: <span class="hljs-type">AnyObserver</span>?
  <span class="hljs-keyword">private</span> <span class="hljs-keyword">var</span> kvoObserver: <span class="hljs-type">NSKeyValueObservation</span>?

  <span class="hljs-function"><span class="hljs-keyword">init</span>()</span> &#123;
    <span class="hljs-keyword">super</span>.<span class="hljs-keyword">init</span>()
    observer <span class="hljs-operator">=</span> <span class="hljs-type">NotificationCenter</span>.default.addObserver(forName: <span class="hljs-type">NSNotification</span>.<span class="hljs-type">Name</span>(rawValue: <span class="hljs-string">""</span>), object: <span class="hljs-literal">nil</span>, queue: <span class="hljs-literal">nil</span>) &#123; (<span class="hljs-keyword">_</span>) <span class="hljs-keyword">in</span> 
    &#125;
    kvoObserver <span class="hljs-operator">=</span> foo.observe(\.value, options: [.new]) &#123; (foo, change) <span class="hljs-keyword">in</span>
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-83">Protocol</h3>
<h4 data-id="heading-84">使用<code>protocol</code>代替继承</h4>
<p><code>Swift</code>中针对<code>protocol</code>提供了很多新特性，例如<code>默认实现</code>，<code>关联类型</code>，支持值类型。在代码设计时可以优先考虑使用<code>protocol</code>来避免臃肿的父类同时更多使用值类型。</p>
<blockquote>
<p>提示：一些无法用<code>protocol</code>替代<code>继承</code>的场景：1.需要继承NSObject子类。2.需要调用<code>super</code>方法。3.实现<code>抽象类</code>的能力。</p>
</blockquote>
<h3 data-id="heading-85">Extension</h3>
<h4 data-id="heading-86">使用<code>extension</code>组织代码</h4>
<p>使用<code>extension</code>将<code>私有方法</code>/<code>父类方法</code>/<code>协议方法</code>等不同功能代码进行分离更加清晰/易维护。</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyViewController</span>: <span class="hljs-title">UIViewController</span> </span>&#123;
  <span class="hljs-comment">// class stuff here</span>
&#125;
<span class="hljs-comment">// MARK: - Private</span>
<span class="hljs-class"><span class="hljs-keyword">extension</span>: <span class="hljs-title">MyViewController</span> </span>&#123;
    <span class="hljs-keyword">private</span> <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">method</span>()</span> &#123;&#125;
&#125;
<span class="hljs-comment">// MARK: - UITableViewDataSource</span>
<span class="hljs-class"><span class="hljs-keyword">extension</span> <span class="hljs-title">MyViewController</span>: <span class="hljs-title">UITableViewDataSource</span> </span>&#123;
  <span class="hljs-comment">// table view data source methods</span>
&#125;
<span class="hljs-comment">// MARK: - UIScrollViewDelegate</span>
<span class="hljs-class"><span class="hljs-keyword">extension</span> <span class="hljs-title">MyViewController</span>: <span class="hljs-title">UIScrollViewDelegate</span> </span>&#123;
  <span class="hljs-comment">// scroll view delegate methods</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-87">代码风格</h3>
<p>良好的代码风格可以提高代码的<code>可读性</code>，统一的代码风格可以降低团队内相互<code>理解成本</code>。对于<code>Swift</code>的代码<code>格式化</code>建议使用自动格式化工具实现，将自动格式化添加到代码提交流程，通过定义Lint<code>规则</code>统一团队内代码风格。考虑使用<code>SwiftFormat</code>和<code>SwiftLint</code>。</p>
<blockquote>
<p>提示：<code>SwiftFormat</code>主要关注代码样式的格式化，<code>SwiftLint</code>可以使用<code>autocorrect</code>自动修复部分不规范的代码。</p>
</blockquote>
<h5 data-id="heading-88">常见的自动格式化修正</h5>
<ul>
<li>移除多余的<code>;</code></li>
<li>最多只保留一行换行</li>
<li>自动对齐<code>空格</code></li>
<li>限制每行的宽度<code>自动换行</code></li>
</ul>
<h2 data-id="heading-89">性能优化</h2>
<p>性能优化上主要关注提高<code>运行时性能</code>和降低<code>二进制体积</code>。需要考虑如何更好的使用<code>Swift</code>特性，同时提供更多信息给<code>编译器</code>进行优化。</p>
<h3 data-id="heading-90">使用<code>Whole Module Optimization</code></h3>
<p>当<code>Xcode</code>开启<code>WMO</code>优化时，编译器可以将整个程序编译为一个文件进行更多的优化。例如通过<code>推断final</code>/<code>函数内联</code>/<code>泛型特化</code>更多使用静态派发，并且可以<code>移除</code>部分未使用的代码。</p>
<h3 data-id="heading-91">使用<code>源代码</code>打包</h3>
<p>当我们使用<code>组件化</code>时，为了提高<code>编译速度</code>和<code>打包效率</code>，通常单个组件独立编译生成<code>静态库</code>，最后多个组件直接使用<code>静态库</code>进行打包。这种场景下<code>WMO</code>仅针对<code>internal</code>以内作用域生效，对于<code>public/open</code>缺少外部使用信息所以无法进行优化。所以对于大量使用<code>Swift</code>的项目，使用<code>全量代码打包</code>更有利于编译器做更多优化。</p>
<h3 data-id="heading-92">减少方法<code>动态</code>派发</h3>
<ul>
<li><code>使用final</code> - <code>class</code>/<code>方法</code>/<code>属性</code>申明为<code>final</code>，编译器可以优化为静态派发</li>
<li><code>使用private</code> - <code>方法</code>/<code>属性</code>申明为<code>private</code>，编译器可以优化为静态派发</li>
<li><code>避免使用dynamic</code> - <code>dynamic</code>会使方法通过ObjC<code>消息转发</code>的方式派发</li>
<li><code>使用WMO</code> - 编译器可以自动分析推断出<code>final</code>优化为静态派发</li>
</ul>
<h3 data-id="heading-93">使用<code>Slice</code>共享内存优化性能</h3>
<p>在使用<code>Array</code>/<code>String</code>时，可以使用<code>Slice</code>切片获取一部分数据。<code>Slice</code>保存对原始<code>Array</code>/<code>String</code>的引用共享内存数据，不需要重新分配空间进行存储。</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">let</span> midpoint <span class="hljs-operator">=</span> absences.count <span class="hljs-operator">/</span> <span class="hljs-number">2</span>

<span class="hljs-keyword">let</span> firstHalf <span class="hljs-operator">=</span> absences[<span class="hljs-operator">..<</span>midpoint]
<span class="hljs-keyword">let</span> secondHalf <span class="hljs-operator">=</span> absences[midpoint<span class="hljs-operator">...</span>]
<span class="hljs-comment">// firstHalf/secondHalf并不会复制和占用更多内存</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>提示：应<code>避免</code>一直持有<code>Slice</code>，<code>Slice</code>会延长原始<code>Array</code>/<code>String</code>的生命周期导致无法被释放造成<code>内存泄漏</code>。</p>
</blockquote>
<h3 data-id="heading-94"><code>protocol</code>添加<code>AnyObject</code></h3>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">protocol</span> <span class="hljs-title">AnyProtocol</span> </span>&#123;&#125;

<span class="hljs-class"><span class="hljs-keyword">protocol</span> <span class="hljs-title">ObjectProtocol</span>: <span class="hljs-title">AnyObject</span> </span>&#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当<code>protocol</code>仅限制为<code>class</code>使用时，继承<code>AnyObject</code>协议可以使编译器不需要考虑<code>值类型</code>实现，提高运行时性能。</p>
<h3 data-id="heading-95">属性</h3>
<h4 data-id="heading-96">使用<code>lazy</code>延时初始化属性</h4>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">View</span> </span>&#123;
    <span class="hljs-keyword">var</span> <span class="hljs-keyword">lazy</span> label: <span class="hljs-type">UILabel</span> <span class="hljs-operator">=</span> &#123;
        <span class="hljs-keyword">let</span> label <span class="hljs-operator">=</span> <span class="hljs-type">UILabel</span>()
        <span class="hljs-keyword">self</span>.addSubView(label)
        <span class="hljs-keyword">return</span> label
    &#125;()
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>lazy</code>属性初始化会<code>延迟</code>到第一次使用时，常见的使用场景：</p>
<ul>
<li>初始化比较耗时</li>
<li>可能不会被使用到</li>
<li>初始化过程需要使用<code>self</code></li>
</ul>
<blockquote>
<p>提示：<code>lazy</code>属性不能保证线程安全</p>
</blockquote>
<h4 data-id="heading-97">避免使用<code>private let</code>属性</h4>
<p><code>private let</code>属性会增加每个<code>class</code>对象的内存大小。同时会增加<code>包大小</code>，因为需要为属性生成相关的信息。可以考虑使用文件级<code>private let</code>申明或<code>static</code>常量代替。</p>
<h5 data-id="heading-98">不推荐</h5>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Object</span> </span>&#123;
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">let</span> title <span class="hljs-operator">=</span> <span class="hljs-string">"12345"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-99">推荐</h5>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">private</span> <span class="hljs-keyword">let</span> title <span class="hljs-operator">=</span> <span class="hljs-string">"12345"</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Object</span> </span>&#123;
    <span class="hljs-keyword">static</span> <span class="hljs-keyword">let</span> title <span class="hljs-operator">=</span> <span class="hljs-string">""</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>提示：这里并不包括通过<code>init</code>初始化注入的属性。</p>
</blockquote>
<h4 data-id="heading-100">使用<code>didSet</code>/<code>willSet</code>时进行<code>Diff</code></h4>
<p>某些场景需要使用<code>didSet</code>/<code>willSet</code>属性检查器监控属性变化，做一些额外的计算。但是由于<code>didSet</code>/<code>willSet</code>并不会检查<code>新/旧</code>值是否相同，可以考虑添加<code>新/旧</code>值判断，只有当值真的改变时才进行运算提高性能。</p>
<h5 data-id="heading-101">优化前</h5>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Object</span> </span>&#123;
    <span class="hljs-keyword">var</span> orderId: <span class="hljs-type">String</span>? &#123;
        <span class="hljs-keyword">didSet</span> &#123;
            <span class="hljs-comment">// 拉取接口等操作</span>
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>例如上面的例子，当每一次<code>orderId</code>变更时需要重新拉取当前订单的数据，但是当orderId值一样时，拉取订单数据是无效执行。</p>
<h5 data-id="heading-102">优化后</h5>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Object</span> </span>&#123;
    <span class="hljs-keyword">var</span> orderId: <span class="hljs-type">String</span>? &#123;
        <span class="hljs-keyword">didSet</span> &#123;
            <span class="hljs-comment">// 判断新旧值是否相等</span>
            <span class="hljs-keyword">guard</span> oldValue <span class="hljs-operator">!=</span> orderId <span class="hljs-keyword">else</span> &#123;
                <span class="hljs-keyword">return</span>
            &#125;
            <span class="hljs-comment">// 拉取接口等操作</span>
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-103">集合</h3>
<h4 data-id="heading-104">集合使用<code>lazy</code>延迟序列</h4>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">var</span> nums <span class="hljs-operator">=</span> [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>]
<span class="hljs-keyword">var</span> result <span class="hljs-operator">=</span> nums.lazy.map &#123; <span class="hljs-type">String</span>(<span class="hljs-variable">$0</span>) &#125;
result[<span class="hljs-number">0</span>] <span class="hljs-comment">// 对1进行map操作</span>
result[<span class="hljs-number">1</span>] <span class="hljs-comment">// 对2进行map操作</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在集合操作时使用<code>lazy</code>，可以将数组运算操作<code>推迟</code>到第一次使用时，避免一次性全部计算。</p>
<blockquote>
<p>提示：例如长列表，我们需要创建每个<code>cell</code>对应的<code>视图模型</code>，一次性创建太耗费时间。</p>
</blockquote>
<h4 data-id="heading-105">使用合适的集合方法优化性能</h4>
<h5 data-id="heading-106">不推荐</h5>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">var</span> items <span class="hljs-operator">=</span> [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>]
items.filter(&#123; <span class="hljs-variable">$0</span> <span class="hljs-operator">></span> <span class="hljs-number">1</span> &#125;).first <span class="hljs-comment">// 查找出所有大于1的元素，之后找出第一个</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-107">推荐</h5>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">var</span> items <span class="hljs-operator">=</span> [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>]
items.first(where: &#123; <span class="hljs-variable">$0</span> <span class="hljs-operator">></span> <span class="hljs-number">1</span> &#125;) <span class="hljs-comment">// 查找出第一个大于1的元素直接返回</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-108">使用值类型</h3>
<p><code>Swift</code>中的值类型主要是<code>结构体</code>/<code>枚举</code>/<code>元组</code>。</p>
<ul>
<li><code>启动性能</code> - <code>APP启动</code>时值类型没有额外的消耗，<code>class</code>有一定额外的消耗。</li>
<li><code>运行时性能</code>- 值类型不需要在堆上分配空间/额外的引用计数管理。更少的内存占用和更快的性能。</li>
<li><code>包大小</code> - 相比<code>class</code>，值类型不需要创建<code>ObjC</code>类对应的<code>ro_data_t</code>数据结构。</li>
</ul>
<blockquote>
<p>提示：<code>class</code>即使没有继承<code>NSObject</code>也会生成<code>ro_data_t</code>，里面包含了<code>ivars</code>属性信息，包括@objc方法。</p>
</blockquote>
<blockquote>
<p>提示：<code>struct</code>无法代替<code>class</code>的一些场景：1.你需要使用<code>继承</code>。2.需要使用引用类型。3.需要使用<code>deinit</code>。4.需要在运行时动态转换一个实例的类型。</p>
</blockquote>
<h4 data-id="heading-109">集合元素使用值类型</h4>
<p>集合元素使用值类型。因为<code>NSArray</code>并不支持值类型，编译器不需要处理可能需要桥接到<code>NSArray</code>的场景，可以移除部分消耗。</p>
<h4 data-id="heading-110">纯静态类型避免使用<code>class</code></h4>
<p>当<code>class</code>只包含<code>静态方法/属性</code>时，考虑使用<code>enum</code>代替<code>class</code>，因为<code>class</code>会生成更多的二进制代码。</p>
<h5 data-id="heading-111">不推荐</h5>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Object</span> </span>&#123;
    <span class="hljs-keyword">static</span> <span class="hljs-keyword">var</span> num: <span class="hljs-type">Int</span>
    <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">test</span>()</span> &#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-112">推荐</h5>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">enum</span> <span class="hljs-title">Object</span> </span>&#123;
    <span class="hljs-keyword">static</span> <span class="hljs-keyword">var</span> num: <span class="hljs-type">Int</span>
    <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">test</span>()</span> &#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>提示：为什么用<code>enum</code>而不是<code>struct</code>，因为<code>struct</code>会额外生成<code>init</code>方法。</p>
</blockquote>
<h3 data-id="heading-113">值类型性能优化</h3>
<h4 data-id="heading-114">考虑使用引用类型</h4>
<p>值类型为了维持<code>值语义</code>，会在每次<code>赋值</code>/<code>参数传递</code>/<code>修改</code>时进行复制。虽然编译器本身会做一些优化，例如<code>写时复制优化</code>，在<code>修改</code>时减少复制频率，但是这仅针对于标准库提供的<code>集合</code>和<code>String</code>结构有效，对于<code>自定义结构</code>需要自己实现。对于<code>参数传递</code>编译器在一些场景会优化为直接<code>传递引用</code>的方式避免复制行为。</p>
<p>但是对于一些数据特别大的结构，同时需要频繁变更修改时也可以考虑使用<code>引用类型</code>实现。</p>
<h4 data-id="heading-115">使用<code>inout</code>传递参数减少复制</h4>
<p>虽然编译器本身会进行<code>写时复制</code>的优化，但是部分场景编译器无法处理。</p>
<h5 data-id="heading-116">不推荐</h5>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">append_one</span>(<span class="hljs-keyword">_</span> <span class="hljs-params">a</span>: [<span class="hljs-type">Int</span>])</span> -> [<span class="hljs-type">Int</span>] &#123;
  <span class="hljs-keyword">var</span> a <span class="hljs-operator">=</span> a
  a.append(<span class="hljs-number">1</span>) <span class="hljs-comment">// 无法被编译器优化，因为这时候有2个引用持有数组</span>
  <span class="hljs-keyword">return</span> a
&#125;

<span class="hljs-keyword">var</span> a <span class="hljs-operator">=</span> [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>]
a <span class="hljs-operator">=</span> append_one(a)
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-117">推荐</h5>
<p>直接使用<code>inout</code>传递参数</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">append_one_in_place</span>(<span class="hljs-params">a</span>: <span class="hljs-keyword">inout</span> [<span class="hljs-type">Int</span>])</span> &#123;
  a.append(<span class="hljs-number">1</span>)
&#125;

<span class="hljs-keyword">var</span> a <span class="hljs-operator">=</span> [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>]
append_one_in_place(<span class="hljs-operator">&</span>a)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-118">使用<code>isKnownUniquelyReferenced</code>实现<code>写时复制</code></h4>
<p>默认情况下结构体中包含<code>引用类型</code>，在修改时只会重新拷贝引用。但是我们希望<code>CustomData</code>具备值类型的特性，所以当修改时需要重新复制<code>NSMutableData</code>避免复用。但是<code>复制</code>操作本身是耗时操作，我们希望可以减少一些不必要的复制。</p>
<h5 data-id="heading-119">优化前</h5>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">CustomData</span> </span>&#123;
    <span class="hljs-keyword">fileprivate</span> <span class="hljs-keyword">var</span> _data: <span class="hljs-type">NSMutableData</span>
    <span class="hljs-keyword">var</span> _dataForWriting: <span class="hljs-type">NSMutableData</span> &#123;
        <span class="hljs-keyword">mutating</span> <span class="hljs-keyword">get</span> &#123;
            _data <span class="hljs-operator">=</span> _data.mutableCopy() <span class="hljs-keyword">as!</span> <span class="hljs-type">NSMutableData</span>
            <span class="hljs-keyword">return</span> _data
        &#125;
    &#125;
    <span class="hljs-function"><span class="hljs-keyword">init</span>(<span class="hljs-keyword">_</span> <span class="hljs-params">data</span>: <span class="hljs-type">NSData</span>)</span> &#123;
        <span class="hljs-keyword">self</span>._data <span class="hljs-operator">=</span> data.mutableCopy() <span class="hljs-keyword">as!</span> <span class="hljs-type">NSMutableData</span>
    &#125;

    <span class="hljs-keyword">mutating</span> <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">append</span>(<span class="hljs-keyword">_</span> <span class="hljs-params">other</span>: <span class="hljs-type">MyData</span>)</span> &#123;
        _dataForWriting.append(other._data <span class="hljs-keyword">as</span> <span class="hljs-type">Data</span>)
    &#125;
&#125;

<span class="hljs-keyword">var</span> buffer <span class="hljs-operator">=</span> <span class="hljs-type">CustomData</span>(<span class="hljs-type">NSData</span>())
<span class="hljs-keyword">for</span> <span class="hljs-keyword">_</span> <span class="hljs-keyword">in</span> <span class="hljs-number">0</span><span class="hljs-operator">..<</span><span class="hljs-number">5</span> &#123;
    buffer.append(x) <span class="hljs-comment">// 每一次调用都会复制</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-120">优化后</h5>
<p>使用<code>isKnownUniquelyReferenced</code>检查如果是<code>唯一引用</code>不进行复制。</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">final</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Box</span><<span class="hljs-title">A</span>> </span>&#123;
    <span class="hljs-keyword">var</span> unbox: <span class="hljs-type">A</span>
    <span class="hljs-function"><span class="hljs-keyword">init</span>(<span class="hljs-keyword">_</span> <span class="hljs-params">value</span>: <span class="hljs-type">A</span>)</span> &#123; <span class="hljs-keyword">self</span>.unbox <span class="hljs-operator">=</span> value &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">CustomData</span> </span>&#123;
    <span class="hljs-keyword">fileprivate</span> <span class="hljs-keyword">var</span> _data: <span class="hljs-type">Box</span><<span class="hljs-type">NSMutableData</span>>
    <span class="hljs-keyword">var</span> _dataForWriting: <span class="hljs-type">NSMutableData</span> &#123;
        <span class="hljs-keyword">mutating</span> <span class="hljs-keyword">get</span> &#123;
            <span class="hljs-comment">// 检查引用是否唯一</span>
            <span class="hljs-keyword">if</span> <span class="hljs-operator">!</span><span class="hljs-built_in">isKnownUniquelyReferenced</span>(<span class="hljs-operator">&</span>_data) &#123;
                _data <span class="hljs-operator">=</span> <span class="hljs-type">Box</span>(_data.unbox.mutableCopy() <span class="hljs-keyword">as!</span> <span class="hljs-type">NSMutableData</span>)
            &#125;
            <span class="hljs-keyword">return</span> _data.unbox
        &#125;
    &#125;
    <span class="hljs-function"><span class="hljs-keyword">init</span>(<span class="hljs-keyword">_</span> <span class="hljs-params">data</span>: <span class="hljs-type">NSData</span>)</span> &#123;
        <span class="hljs-keyword">self</span>._data <span class="hljs-operator">=</span> <span class="hljs-type">Box</span>(data.mutableCopy() <span class="hljs-keyword">as!</span> <span class="hljs-type">NSMutableData</span>)
    &#125;
&#125;

<span class="hljs-keyword">var</span> buffer <span class="hljs-operator">=</span> <span class="hljs-type">CustomData</span>(<span class="hljs-type">NSData</span>())
<span class="hljs-keyword">for</span> <span class="hljs-keyword">_</span> <span class="hljs-keyword">in</span> <span class="hljs-number">0</span><span class="hljs-operator">..<</span><span class="hljs-number">5</span> &#123;
    buffer.append(x) <span class="hljs-comment">// 只会在第一次调用时进行复制</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>提示：对于<code>ObjC</code>类型<code>isKnownUniquelyReferenced</code>会直接返回<code>false</code>。</p>
</blockquote>
<h3 data-id="heading-121">减少使用<code>Objc</code>特性</h3>
<h4 data-id="heading-122">避免使用<code>Objc</code>类型</h4>
<p>尽可能避免在<code>Swift</code>中使用<code>NSString</code>/<code>NSArray</code>/<code>NSDictionary</code>等<code>ObjC</code>基础类型。以<code>Dictionary</code>为例，虽然<code>Swift Runtime</code>可以在<code>NSArray</code>和<code>Array</code>之间进行隐式桥接需要<code>O(1)</code>的时间。但是字典当<code>Key</code>和<code>Value</code>既不是类也不是<code>@objc</code>协议时，需要对<code>每个值</code>进行桥接，可能会导致消耗<code>O(n)</code>时间。</p>
<h3 data-id="heading-123">减少添加<code>@objc</code>标识</h3>
<p><code>@objc</code>标识虽然不会强制使用<code>消息转发</code>的方式来调用<code>方法/属性</code>，但是他会默认<code>ObjC</code>是可见的会生成和<code>ObjC</code>一样的<code>ro_data_t</code>结构。</p>
<h4 data-id="heading-124">避免使用<code>@objcMembers</code></h4>
<p>使用<code>@objcMembers</code>修饰的类，默认会为<code>类</code>/<code>属性</code>/<code>方法</code>/<code>扩展</code>都加上<code>@objc</code>标识。</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">@objc</span>Members <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Object</span>: <span class="hljs-title">NSObject</span> </span>&#123;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>提示：你也可以使用<code>@nonobjc</code>取消支持<code>ObjC</code>。</p>
</blockquote>
<h4 data-id="heading-125">避免继承<code>NSObject</code></h4>
<p>你只需要在需要使用<code>NSObject</code>特性时才需要继承，例如需要实现<code>UITableViewDataSource</code>相关协议。</p>
<h3 data-id="heading-126">使用<code>let</code>变量/属性</h3>
<h5 data-id="heading-127">优化集合创建</h5>
<p>集合不需要修改时，使用<code>let</code>修饰，编译器会优化创建集合的性能。例如针对<code>let</code>集合，<code>编译器</code>在创建时可以分配更小的<code>内存大小</code>。</p>
<h5 data-id="heading-128">优化逃逸闭包</h5>
<p>在<code>Swift</code>中，当捕获<code>var</code>变量时编译器需要生成一个在堆上的<code>Box</code>保存变量用于之后对于变量的<code>读/写</code>，同时需要额外的内存管理操作。如果是<code>let</code>变量，编译器可以保存<code>值复制或引用</code>，避免使用<code>Box</code>。</p>
<h1 data-id="heading-129">总结</h1>
<p>个人从<code>Swift</code>3.0开始将<code>Swift</code>作为第一语言使用。编写<code>Swift</code>代码并不只是简单对于<code>ObjC</code>代码的翻译/重写，需要对于<code>Swift</code>特性更多的理解才能更好的利用这些特性带来更多的收益。同时我们需要关注每个版本<code>Swift</code>的优化/改进和新特性。在这过程中也会提高我们的编码能力，加深对于一些通用编程概念/思想的理解，包括可选址、值类型、协程、不共享数据的Actor并发模型、函数式编程、面向协议编程、内存所有权等。对于新的现代编程语言例如<code>Swift</code>/<code>Dart</code>/<code>TS</code>/<code>Kotlin</code>/<code>Rust</code>等，很多特性/思想都是相互借鉴，当我们理解这些概念/思想以后对于理解其他语言也会更容易。</p>
<p>这里推荐有兴趣可以关注<a href="https://link.juejin.cn/?target=https%3A%2F%2Fapple.github.io%2Fswift-evolution%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://apple.github.io/swift-evolution/" ref="nofollow noopener noreferrer">Swift Evolution</a>，每个特性加入都会有一个提案，里面会详细介绍<code>动机</code>/<code>使用场景</code>/<code>实现方式</code>/<code>未来方向</code>。</p>
<h1 data-id="heading-130">扩展链接</h1>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.swift.org%2Fswift-book%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.swift.org/swift-book/" ref="nofollow noopener noreferrer">The Swift Programming Language</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fobjccn.io%2Fproducts%2Fadvanced-swift%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://objccn.io/products/advanced-swift/" ref="nofollow noopener noreferrer">Swift 进阶</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Frealm.github.io%2FSwiftLint%2Frule-directory.html" target="_blank" rel="nofollow noopener noreferrer" title="https://realm.github.io/SwiftLint/rule-directory.html" ref="nofollow noopener noreferrer">SwiftLint Rules</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fapple%2Fswift%2Fblob%2Fmain%2Fdocs%2FOptimizationTips.rst" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/apple/swift/blob/main/docs/OptimizationTips.rst" ref="nofollow noopener noreferrer">OptimizationTips</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Ftech.meituan.com%2F2018%2F11%2F01%2Fswift-compile-performance-optimization.html" target="_blank" rel="nofollow noopener noreferrer" title="https://tech.meituan.com/2018/11/01/swift-compile-performance-optimization.html" ref="nofollow noopener noreferrer">深入剖析Swift性能优化</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgoogle.github.io%2Fswift%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://google.github.io/swift/" ref="nofollow noopener noreferrer">Google Swift Style Guide</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fapple.github.io%2Fswift-evolution%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://apple.github.io/swift-evolution/" ref="nofollow noopener noreferrer">Swift Evolution</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Fswift%2Fdictionary" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/swift/dictionary" ref="nofollow noopener noreferrer">Dictionary</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Fswift%2Fdictionary" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/swift/dictionary" ref="nofollow noopener noreferrer">Array</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Fswift%2Fdictionary" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/swift/dictionary" ref="nofollow noopener noreferrer">String</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Fswift%2Fchoosing_between_structures_and_classes" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/swift/choosing_between_structures_and_classes" ref="nofollow noopener noreferrer">struct</a></li>
</ul>
<h4 data-id="heading-131">最后发个招聘广告</h4>
<p>团队招新：京东京喜，base深圳，有兴趣的同学可以私信我简历</p></div>  
</div>
            
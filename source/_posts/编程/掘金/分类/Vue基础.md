
---
title: 'Vue基础'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/be28eb4df69045c8ab97e72f932859cc~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 18 Jul 2021 22:27:29 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/be28eb4df69045c8ab97e72f932859cc~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">一、 Vue基础</h1>
<h1 data-id="heading-1">一、  模板语法</h1>
<h2 data-id="heading-2">1.1数据绑定</h2>
<h3 data-id="heading-3">1.1.1文本，v-text、&#123;&#123;&#125;&#125;</h3>
<blockquote>
<p>在mustache语法中，是可以使用加减乘除运算符的</p>
</blockquote>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span>></span>
&#123;&#123;uage *2&#125;&#125;
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-text</span>=<span class="hljs-string">"uage"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><script>
<span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
<span class="hljs-attr">el</span>:<span class="hljs-string">'#app'</span>,
<span class="hljs-attr">data</span>:&#123;
<span class="hljs-attr">uage</span>:<span class="hljs-number">10</span>
&#125;
&#125;)
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">1.1.2 v-once：</h3>
<p>只将数值绑定一次</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-once</span>></span>
&#123;&#123;uage&#125;&#125;
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">1.1.3v-pre:</h3>
<p>将标签内的内容不编译进行渲染</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-pre</span>></span>
&#123;&#123;uage *2&#125;&#125;
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">1.1.4v-cloak:</h3>
<p>使数据加载之后才渲染页面</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-cloak</span>></span>
&#123;&#123;uage *2&#125;&#125;
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>原理：在vue数据加载之前，标签中有v-cloak这个属性，阻止元素的显示，数据加载之后，驱动页面渲染，元素上就没有v-cloak这个属性了</p>
</blockquote>
<h3 data-id="heading-7">1.1.5 v-html</h3>
<p>插入带html的字符</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-html</span> =<span class="hljs-string">'url'</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><script>
<span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
<span class="hljs-attr">el</span>:<span class="hljs-string">'#app'</span>,
<span class="hljs-attr">data</span>:&#123;
<span class="hljs-attr">uage</span>:<span class="hljs-number">10</span>,
<span class="hljs-attr">url</span>:<span class="hljs-string">'<a href="http://www.baidu.com">ddd</a>'</span>
&#125;
&#125;)
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">1.1.6v-bind：</h3>
<p>动态绑定属性值</p>
<p>语法糖：<code>:</code></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">v-bind:href</span>= <span class="hljs-string">"url"</span>></span>
我是百度
<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><script>
<span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
<span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
<span class="hljs-attr">data</span>: &#123;
<span class="hljs-attr">uage</span>: <span class="hljs-number">10</span>,
<span class="hljs-attr">url</span>: <span class="hljs-string">'http://www.baidu.com'</span>
&#125;
&#125;)
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>==<strong>扩展使用:绑定class</strong>==</p>
<blockquote>
<p>文件css</p>
</blockquote>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.active</span> &#123;
<span class="hljs-attribute">color</span>: red;
&#125;

<span class="hljs-selector-class">.uncheck</span> &#123;
<span class="hljs-attribute">color</span>: yellow;
&#125;
<span class="hljs-selector-class">.green</span>&#123;
<span class="hljs-attribute">color</span>: green;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>文件js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><script>
<span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
<span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
<span class="hljs-attr">data</span>: &#123;
<span class="hljs-attr">isActive</span>: <span class="hljs-literal">true</span>,
<span class="hljs-attr">isUncheck</span>: <span class="hljs-literal">false</span>

&#125;,
<span class="hljs-attr">methods</span>: &#123;
<span class="hljs-attr">btnClick</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-built_in">this</span>.isActive = !<span class="hljs-built_in">this</span>.isActive,
<span class="hljs-built_in">this</span>.isUncheck = !<span class="hljs-built_in">this</span>.isUncheck

&#125;,
<span class="hljs-attr">getClass</span>:<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
<span class="hljs-keyword">return</span>  &#123;<span class="hljs-attr">active</span>:<span class="hljs-built_in">this</span>.isActive,<span class="hljs-attr">uncheck</span>:<span class="hljs-built_in">this</span>.isUncheck&#125;
&#125;
&#125;
&#125;)
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>用法一：直接使用&#123;&#125;绑定一个class</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">:class</span>=<span class="hljs-string">&#123;active:true&#125;</span>></span>
我是直接绑定的样式
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>用法二:使用变量传入boolean类型控制多个class是否生效</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"btnClick"</span> <span class="hljs-attr">:class</span>=<span class="hljs-string">"&#123;active:isActive,uncheck:isUncheck&#125;"</span> ></span>
我要变色了
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>用法三：与其他class共同使用，样式冲突的情况下以到单独写的class为主</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"btnClick"</span> <span class="hljs-attr">:class</span>=<span class="hljs-string">"&#123;active:isActive,uncheck:isUncheck&#125;"</span><span class="hljs-attr">class</span>=<span class="hljs-string">"green"</span> ></span>
我要变色了
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>用法四：如果过于复杂，可以放在一个methods或者computed中</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><div @click=<span class="hljs-string">"btnClick"</span> v-bind:<span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"getClass()"</span> >
我要变色了
</div>
<span class="hljs-comment">//调用方法的时候可以选择不加括号 </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用数组绑定class：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">:class</span>= <span class="hljs-string">"['green','fontClass']"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"active"</span> ></span>
我绑定了好几个class哦~
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样驻足绑定的方法可以使用data中的变量，也不与单独写的class冲突
但是在渲染的时候，是优先渲染内联class，所以如果有样式重叠，绑定的样式会覆盖掉内联class，截图如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/be28eb4df69045c8ab97e72f932859cc~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<ul>
<li>
<h2 data-id="heading-9"><strong>v-bind绑定style</strong></h2>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">:style</span>=<span class="hljs-string">"&#123;fontSize:'30px'&#125;"</span>></span>我绑定了style<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">:style</span>=<span class="hljs-string">"&#123;color:color,fontSize:fontSize+'px'&#125;"</span>></span>我也绑定了style<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript">data: &#123;
<span class="hljs-attr">color</span>: <span class="hljs-string">"red"</span>,
<span class="hljs-attr">fontSize</span>:<span class="hljs-number">30</span>

&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意事项：</p>
<ol>
<li>格式为<code>：style= "&#123;属性名:属性值&#125;"</code></li>
<li>如果属性值是类似font-size带有<code>-</code>的属性值都要转换为fontSize，否则会报错</li>
<li>属性值如果直接写数值要加<code>''</code>，如果是变量则不用加</li>
</ol>
</blockquote>
</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">        computed: &#123;
            <span class="hljs-attr">fullName</span>:<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
                <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.firstName + <span class="hljs-string">' '</span> + <span class="hljs-built_in">this</span>.lastName;
            &#125;
        &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">1.1.7v-model</h3>
<p>在表单上创建<strong>双向绑定</strong>，v-model会忽略所有表单元素的value，checked，selected属性 初始值，而选定Vue实例数据为具体值。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">v-model</span> = <span class="hljs-string">"userName"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;&#123;userName&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
        <span class="hljs-attr">el</span>:<span class="hljs-string">"#app"</span>,
        <span class="hljs-attr">data</span>:&#123;
            <span class="hljs-attr">userName</span>:<span class="hljs-string">"hong"</span>
        &#125;
    &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>v-model的相关使用：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
        <span class="hljs-comment"><!-- v-model与radio的配合使用 --></span>

        <span class="hljs-tag"><<span class="hljs-name">label</span> <span class="hljs-attr">for</span>=<span class="hljs-string">"male"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"male"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"radio"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"sex"</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"sex"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"男"</span>></span>男
        <span class="hljs-tag"></<span class="hljs-name">label</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">label</span> <span class="hljs-attr">for</span>=<span class="hljs-string">"female"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"female"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"radio"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"sex"</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"sex"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"女"</span>></span>女
        <span class="hljs-tag"></<span class="hljs-name">label</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">p</span>></span>选中的性别是：&#123;&#123;sex&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
        <span class="hljs-comment"><!-- v-model与checkBox的配合使用 --></span>
        <span class="hljs-comment"><!-- <input type="checkbox" value="篮球" v-model="checked">篮球
        <input type="checkbox" value="足球" v-model="checked">足球
        <input type="checkbox" value="乒乓球" v-model="checked">乒乓球
        <input type="checkbox" value="羽毛球" v-model="checked">羽毛球
        <input type="checkbox" value="橄榄球" v-model="checked">橄榄球
        <input type="checkbox" value="高尔夫" v-model="checked">高尔夫 --></span>
        <span class="hljs-tag"><<span class="hljs-name">label</span> <span class="hljs-attr">v-for</span>= <span class="hljs-string">"item in hobbies"</span> <span class="hljs-attr">:for</span>=<span class="hljs-string">"item"</span> ></span>
            <span class="hljs-comment"><!-- 注意label的for与input的id都需要动态绑定，input的value也是需要动态绑定的 --></span>
            <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"checkbox"</span> <span class="hljs-attr">:value</span>=<span class="hljs-string">"item"</span> <span class="hljs-attr">:id</span>=<span class="hljs-string">"item"</span> <span class="hljs-attr">v-model</span>= <span class="hljs-string">"checked"</span> ></span>&#123;&#123;item&#125;&#125;
        <span class="hljs-tag"></<span class="hljs-name">label</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">p</span>></span>我选中了&#123;&#123;checked&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
        <span class="hljs-comment"><!-- v-model与select配合使用 --></span>
        <span class="hljs-tag"><<span class="hljs-name">select</span>  <span class="hljs-attr">name</span>=<span class="hljs-string">""</span> <span class="hljs-attr">id</span>=<span class="hljs-string">""</span> <span class="hljs-attr">v-model</span>= <span class="hljs-string">"checkBooks"</span> <span class="hljs-attr">multiple</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">option</span> <span class="hljs-attr">v-for</span> = <span class="hljs-string">"item in books"</span> <span class="hljs-attr">:value</span>=<span class="hljs-string">"item"</span>></span>&#123;&#123;item&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">option</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">select</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">p</span>></span>我选中了：&#123;&#123;checkBooks&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../js/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    Vue.component(<span class="hljs-string">'cpn'</span>, cpnC)
    <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
        <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
        <span class="hljs-attr">data</span>: &#123;
            <span class="hljs-comment">// 给单选框一个默认值“男”</span>
            <span class="hljs-attr">sex</span>: <span class="hljs-string">'男'</span>,<span class="hljs-comment">//单选</span>
            <span class="hljs-attr">checked</span>: [],<span class="hljs-comment">//多选</span>
            <span class="hljs-attr">hobbies</span>:[<span class="hljs-string">"足球"</span>,<span class="hljs-string">"乒乓球"</span>,<span class="hljs-string">"羽毛球"</span>,<span class="hljs-string">"橄榄球"</span>,<span class="hljs-string">"高尔夫"</span>],
            <span class="hljs-attr">books</span>:[<span class="hljs-string">"钢铁是怎样炼成的"</span>,<span class="hljs-string">"啊"</span>,<span class="hljs-string">"Linux该怎么学"</span>,<span class="hljs-string">"前端好难"</span>,<span class="hljs-string">"努力学习"</span>],
            <span class="hljs-attr">checkBooks</span>:[]
        &#125;,
    &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">1.1.7.1model修饰符</h4>
<ol>
<li>
<p>.lazy</p>
<p>默认情况下v-model是实时同步输入框的值和数据，加上<code>.lazy</code>后变为触发change时间后再同步（即相当于修改后要按下回车，或点击其他位置后才触发数据同步）</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">v-model.lazy</span> = <span class="hljs-string">"userName"</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>.number</p>
<p>将用户输入的内容转化成数值类型，转化规则与js的Number()的规则相同</p>
<p>详见<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.w3school.com.cn%2Fjs%2Fjs_type_conversion.asp" target="_blank" rel="nofollow noopener noreferrer" title="https://www.w3school.com.cn/js/js_type_conversion.asp" ref="nofollow noopener noreferrer">w3shool的JS数据类型转换</a></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">v-model.number</span> = <span class="hljs-string">"userName"</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>.trim</p>
<p>过滤掉输入框的首位空格</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">v-model.trim</span> = <span class="hljs-string">"userName"</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<h2 data-id="heading-12">1.2事件绑定</h2>
<h3 data-id="heading-13">1.2.1 v-on</h3>
<p>作用：绑定事件监听器</p>
<p>语法糖：@</p>
<p>参数：event</p>
<h4 data-id="heading-14">1.2.1.1基本使用</h4>
<p>使用v-on绑定事件</p>
<ul>
<li>一个元素上可以绑定多个不同的事件</li>
<li>事件的绑定也可以通过methods中定义函数的方法来实现绑定</li>
<li>当定义的事件没有参数，所以我们在调用方法的时候不需要添加()</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;&#123;total&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
        <span class="hljs-comment"><!-- 一个元素上可以绑定多个不同的事件 --></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"div1"</span> @<span class="hljs-attr">mouseout</span> = <span class="hljs-string">"total++"</span> @<span class="hljs-attr">click</span> = <span class="hljs-string">"total--"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-comment"><!-- 事件的绑定也可以通过methods中定义函数的方法来实现绑定 --></span>
        <span class="hljs-comment"><!-- 因为现在定义的事件没有参数，所以我们在调用方法的时候不需要添加() --></span>
        <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">v-on:click</span> = <span class="hljs-string">"reduce"</span>></span>-<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">v-on:click</span> = <span class="hljs-string">"increase"</span>></span>+<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
        <span class="hljs-attr">el</span>:<span class="hljs-string">"#app"</span>,
        <span class="hljs-attr">data</span>:&#123;
            <span class="hljs-attr">total</span>:<span class="hljs-number">1</span>
        &#125;,
        <span class="hljs-attr">methods</span>:&#123;
            <span class="hljs-comment">// 定义total增加的函数</span>
            <span class="hljs-function"><span class="hljs-title">increase</span>(<span class="hljs-params"></span>)</span>&#123;
                <span class="hljs-built_in">this</span>.total++;
            &#125;,
            <span class="hljs-comment">// 定义total减少的函数</span>
            <span class="hljs-function"><span class="hljs-title">reduce</span>(<span class="hljs-params"></span>)</span>&#123;
                <span class="hljs-built_in">this</span>.total--;
            &#125;

        &#125;
    &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-15">1.2.1.2事件监听传参</h4>
<ul>
<li>当方法需要参数但未传递实参，会将event对象当成默认参数返回</li>
<li>正常传递参数</li>
<li>当需要传递其他参数和event的时候，需要借助<code>$event</code>实现​</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
        <span class="hljs-comment"><!-- 省略参数，会将event事件当成默认的参数返回 --></span>
        <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span> = <span class="hljs-string">"clickBtn"</span>></span>按钮<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
        <span class="hljs-comment"><!-- 传递所需参数 --></span>
        <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span> = <span class="hljs-string">"clickBtn1('sss')"</span>></span>按钮<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
        <span class="hljs-comment"><!-- 同时传递需要的参数和event，使用vue封装的$event进行传参 --></span>
        <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span> = <span class="hljs-string">"clickBtn2(123,$event)"</span>></span>按钮<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
        
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
        <span class="hljs-attr">el</span>:<span class="hljs-string">"#app"</span>,
        <span class="hljs-attr">data</span>:&#123;

        &#125;,
        <span class="hljs-attr">methods</span>:&#123;
            <span class="hljs-function"><span class="hljs-title">clickBtn</span>(<span class="hljs-params"></span>)</span>&#123;
                <span class="hljs-built_in">console</span>.log(event);
            &#125;,
            <span class="hljs-function"><span class="hljs-title">clickBtn1</span>(<span class="hljs-params">a</span>)</span>&#123;
                <span class="hljs-built_in">console</span>.log(a);
            &#125;,
            <span class="hljs-function"><span class="hljs-title">clickBtn2</span>(<span class="hljs-params">a,event</span>)</span>&#123;
                <span class="hljs-built_in">console</span>.log(a,event);
            &#125;

        &#125;
    &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">1.2.2 v-on的修饰符</h3>
<ul>
<li>.stop调用了event。stopPropagation()</li>
<li>.prevent调用event.preventDefault()</li>
<li>.&#123;keyCode|keyAlias&#125;是事件只从特定按键触发时才触发回调</li>
<li>.native  监听组件根元素的原生事件</li>
<li>.once 只触发一次回调</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html">        <span class="hljs-comment"><!-- 阻止冒泡 --></span>
        <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click.stop</span> = <span class="hljs-string">"clickBtn"</span>></span>按钮<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
        <span class="hljs-comment"><!-- 阻止默认行为 --></span>
        <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click.prevent</span> = <span class="hljs-string">"clickBtn"</span>></span>按钮<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
        <span class="hljs-comment"><!-- 阻止默认行为，没有表达式 --></span>
        <span class="hljs-tag"><<span class="hljs-name">form</span> @<span class="hljs-attr">submit.prevent</span>></span><span class="hljs-tag"></<span class="hljs-name">form</span>></span>
        <span class="hljs-comment"><!-- 串联修饰符 --></span>
        <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click.stop</span>,<span class="hljs-attr">prevent</span> = <span class="hljs-string">"clickBtn"</span>></span>按钮<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
        <span class="hljs-comment"><!-- 按键别名，键盘上的名称 --></span>
        <span class="hljs-tag"><<span class="hljs-name">input</span> @<span class="hljs-attr">keydown.</span>+ = <span class="hljs-string">"onEnter"</span>></span>
        <span class="hljs-comment"><!-- 按键代码，按键对应的代码数字 --></span>
        <span class="hljs-tag"><<span class="hljs-name">input</span> @<span class="hljs-attr">keydown.13</span> = <span class="hljs-string">"onEnter"</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">1.2.2 v-if、v-else、v-else-if</h3>
<h4 data-id="heading-18">1..2.2.1 v-if、v-else</h4>
<p>v-if与js的if用法相同，是通过v-if = ""引号中的Boolen值去进行判断，如果为false就隐藏元素是true就显示</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"isShow"</span>></span>true<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-else</span>></span>false<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"changeClick"</span>></span>切换<span class="hljs-tag"></<span class="hljs-name">button</span>></span>

    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
        <span class="hljs-attr">el</span>: <span class="hljs-string">"#app"</span>,
        <span class="hljs-attr">data</span>: &#123;
            <span class="hljs-attr">isShow</span>: <span class="hljs-literal">true</span>
        &#125;,
        <span class="hljs-attr">methods</span>: &#123;
            <span class="hljs-function"><span class="hljs-title">changeClick</span>(<span class="hljs-params"></span>)</span> &#123;
                <span class="hljs-built_in">this</span>.isShow = !<span class="hljs-built_in">this</span>.isShow;
            &#125;
        &#125;
    &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-19">1.2.2.2v-else-if</h4>
<p>用处不多，不赘余</p>
<pre><code class="hljs language-html copyable" lang="html">    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"score >90 "</span>></span>优秀<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-else-if</span>=<span class="hljs-string">"score >80 "</span>></span>良好<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-else-if</span>=<span class="hljs-string">"score > 60"</span>></span>及格<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-else</span>></span>不及格<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-20">1.3 v-for循环遍历</h2>
<p>用法与for…in相同，详见<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.w3school.com.cn%2Fjs%2Fjs_loop_for_in.asp" target="_blank" rel="nofollow noopener noreferrer" title="https://www.w3school.com.cn/js/js_loop_for_in.asp" ref="nofollow noopener noreferrer">w3school的for…in介绍</a></p>
<h3 data-id="heading-21">1.3.1循环数组</h3>
<h4 data-id="heading-22">1.3.1.1无索引循环</h4>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">v-for</span> = <span class="hljs-string">"item in names"</span> <span class="hljs-attr">v-block</span>></span>&#123;&#123;item&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
        <span class="hljs-attr">el</span>: <span class="hljs-string">"#app"</span>,
        <span class="hljs-attr">data</span>: &#123;
            <span class="hljs-attr">names</span>:[<span class="hljs-string">"h"</span>,<span class="hljs-string">"w"</span>,<span class="hljs-string">"l"</span>,<span class="hljs-string">"g"</span>,<span class="hljs-string">"z"</span>]
        &#125;,
        <span class="hljs-attr">methods</span>: &#123;
        &#125;
    &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-23">1.3.1.2 有索引循环</h4>
<ul>
<li>加一个小括号，里面加上item和index</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html">        <span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">v-for</span> = <span class="hljs-string">"(item,index) in names"</span> <span class="hljs-attr">v-block</span>></span>&#123;&#123;index&#125;&#125;----&#123;&#123;item&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-24">1.3.2对象循环遍历</h3>
<h4 data-id="heading-25">1.3.2.1无key无索引遍历</h4>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">v-for</span> = <span class="hljs-string">"item in names"</span> <span class="hljs-attr">v-block</span>></span>&#123;&#123;item&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
        <span class="hljs-attr">el</span>: <span class="hljs-string">"#app"</span>,
        <span class="hljs-attr">data</span>: &#123;
            <span class="hljs-attr">names</span>:&#123;
                <span class="hljs-attr">name</span>:<span class="hljs-string">"hong"</span>,
                <span class="hljs-attr">age</span>:<span class="hljs-number">18</span>,
                <span class="hljs-attr">sex</span>:<span class="hljs-string">"男"</span>
            &#125;
        &#125;,
        <span class="hljs-attr">methods</span>: &#123;
        &#125;
    &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-26">1.3.2.2有key无索引遍历</h4>
<pre><code class="hljs language-html copyable" lang="html">        <span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">v-for</span> = <span class="hljs-string">"(item,key) in names"</span> <span class="hljs-attr">v-block</span>></span>&#123;&#123;key&#125;&#125;------&#123;&#123;item&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-27">1.3.2.2有key有索引遍历</h4>
<pre><code class="hljs language-html copyable" lang="html"> <span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">v-for</span> = <span class="hljs-string">"(item,key，index) in names"</span> <span class="hljs-attr">v-block</span>></span>&#123;&#123;key&#125;&#125;------&#123;&#123;item&#125;&#125;-----&#123;&#123;index&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-28">1.4(了解)如何正确使用key</h2>
<ol>
<li>
<p>v-for使用时，为了能够更好的复用，我们在使用v-for的时候，需要搭配key属性的使用</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fsegmentfault.com%2Fa%2F1190000013810844" target="_blank" rel="nofollow noopener noreferrer" title="https://segmentfault.com/a/1190000013810844" ref="nofollow noopener noreferrer"></a></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">v-for</span> = <span class="hljs-string">"item in names"</span> <span class="hljs-attr">key</span> = <span class="hljs-string">"item"</span>></span>&#123;&#123;item&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">v-for</span> = <span class="hljs-string">"item in user"</span> <span class="hljs-attr">key</span> = <span class="hljs-string">"item"</span>></span>&#123;&#123;item&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
        <span class="hljs-attr">el</span>: <span class="hljs-string">"#app"</span>,
        <span class="hljs-attr">data</span>: &#123;
            <span class="hljs-attr">names</span>:&#123;
                <span class="hljs-attr">name</span>:<span class="hljs-string">"hong"</span>,
                <span class="hljs-attr">age</span>:<span class="hljs-number">18</span>,
                <span class="hljs-attr">sex</span>:<span class="hljs-string">"男"</span>
            &#125;,
            <span class="hljs-attr">user</span>:[<span class="hljs-string">"s"</span>,<span class="hljs-string">"d"</span>,<span class="hljs-string">"f"</span>,<span class="hljs-string">"j"</span>]
        &#125;,
        <span class="hljs-attr">methods</span>: &#123;
        &#125;
    &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<h2 data-id="heading-29">二、计算属性</h2>
<h3 data-id="heading-30">2.1基本使用</h3>
<pre><code class="hljs language-html copyable" lang="html">    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;&#123;fullName&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript">        data: &#123;
            <span class="hljs-attr">firstName</span>: <span class="hljs-string">'zhang'</span>,
            <span class="hljs-attr">lastName</span>: <span class="hljs-string">'san'</span>
        &#125;,
        <span class="hljs-attr">computed</span>: &#123;
            <span class="hljs-attr">fullName</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
                <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.firstName + <span class="hljs-string">' '</span> + <span class="hljs-built_in">this</span>.lastName;
            &#125;
        &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-31">三、ES6语法</h2>
<ol>
<li>
<p>对象的增强语法</p>
<p>ES5的创建方法</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> a = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Object</span>();
a.sname = <span class="hljs-string">"hong"</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">var</span> a = &#123;
    sname = <span class="hljs-string">"hong"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>ES6语法</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> sname =  <span class="hljs-string">"hong"</span>;
<span class="hljs-keyword">var</span> a = &#123;
    sname,
&#125;
<span class="hljs-comment">//在es6的语法中，上面写法会吧sname当成key，将变量sname的值赋值给它</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<h2 data-id="heading-32">四、组件</h2>
<h3 data-id="heading-33">4.1 全局组件与局部组件</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><body>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
        <span class="hljs-comment"><!-- 全局组件在哪里都可以调用 --></span>
        <span class="hljs-tag"><<span class="hljs-name">global-c</span>></span><span class="hljs-tag"></<span class="hljs-name">global-c</span>></span>
        <span class="hljs-comment"><!-- 局部组件只有在注册的组件内才能调用 --></span>
        <span class="hljs-tag"><<span class="hljs-name">cpn</span>></span><span class="hljs-tag"></<span class="hljs-name">cpn</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app2"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">global-c</span>></span><span class="hljs-tag"></<span class="hljs-name">global-c</span>></span>
        <span class="hljs-comment"><!-- <cpn></cpn> --></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>

</body>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../js/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-comment">// 定义组件</span>
    <span class="hljs-keyword">const</span> cpnC = Vue.extend(&#123;
        <span class="hljs-attr">template</span>: <span class="hljs-string">`        
        <div>
            <span>hhh</span>
            <input type="text">
        </div>
        `</span>
    &#125;)
    <span class="hljs-comment">// 全局组件注册</span>
    Vue.component(<span class="hljs-string">'globalCi'</span>, cpnC)
    <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
        <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
        <span class="hljs-attr">data</span>: &#123;

        &#125;,
        <span class="hljs-comment">// 局部组件注册</span>
        <span class="hljs-attr">components</span>: &#123;
            <span class="hljs-attr">cpn</span>: cpnC
        &#125;
    &#125;)
    <span class="hljs-keyword">const</span> app2 = <span class="hljs-keyword">new</span> Vue(&#123;
        <span class="hljs-attr">el</span>: <span class="hljs-string">"#app2"</span>,
    &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
</span><span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>提示：组件命名的时候是允许驼峰命名的，但是在使用的时候，要将大写字母转小写，前面加一个中划线<code>-</code></p>
<p>如Vue.component('globalComponent',***)在使用时就要</p>
</blockquote>
<h3 data-id="heading-34">4.2父子组件</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><body>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">cpn</span>></span><span class="hljs-tag"></<span class="hljs-name">cpn</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</body>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../js/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="handlebars"><span class="xml">
    // 定义组件1
    const cpnC = Vue.extend(&#123;
        template: `        
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            我是组件1
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>  
        `
    &#125;)
    const cpnC2 = Vue.extend(&#123;
        template: `
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            我是组件2
            <span class="hljs-comment"><!-- 将注册好的组件在父组件中调用--></span>
            <span class="hljs-tag"><<span class="hljs-name">sonCpn</span>></span><span class="hljs-tag"></<span class="hljs-name">sonCpn</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        `,
        components:&#123;
            // 将组件1注册到组件2，此时组件1为字子组件，组件2为父组件
            sonCpn:cpnC
        &#125;
    &#125;)
    const app = new Vue(&#123;
        el: '#app',
        data: &#123;

        &#125;,
        // 在root根组件中注册组件2，在使用组件
        components: &#123;
            cpn: cpnC2
        &#125;
    &#125;)
    const app2 = new Vue(&#123;
        el: "#app2",
    &#125;)
</span></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>在调用组件的时候，Vue对象会先在自己的组件中去找，是否注册了这个组件，如果没有，去全局组件中查找，如果都没有，将报错</p>
</blockquote>
<h4 data-id="heading-35">4.2.1父子组件语法糖</h4>
<p>旧写法</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-comment">// 定义组件</span>
    <span class="hljs-keyword">const</span> cpnC = Vue.extend(&#123;
        <span class="hljs-attr">template</span>: <span class="hljs-string">`        
        <div>
            我是组件1
        </div>
        `</span>
    &#125;)
    <span class="hljs-comment">// 全局组件注册</span>
    Vue.component(<span class="hljs-string">'globalCi'</span>, cpnC)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>新写法</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    Vue.component(<span class="hljs-string">"ss"</span>,&#123;
        <span class="hljs-attr">template</span>: <span class="hljs-string">`        
        <div>
            我是组件1
        </div>  
        `</span>
    &#125;)
<span class="hljs-comment">//------------------------------------------</span>
        <span class="hljs-attr">components</span>: &#123;
            <span class="hljs-attr">cpn</span>: &#123;
      <span class="hljs-attr">template</span>: <span class="hljs-string">`        
        <div>
            我是组件1
        </div>  
        `</span>
            &#125;
        &#125;
<span class="hljs-comment">//-----------------------------------------------</span>
<span class="hljs-keyword">const</span> cpn = &#123;
     <span class="hljs-attr">template</span>: <span class="hljs-string">`        
        <div>
            我是组件1
        </div>  
        `</span>
&#125;
<span class="hljs-comment">//在vue组件中定义</span>
    <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
        <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
        <span class="hljs-attr">components</span>: &#123;
            <span class="hljs-comment">//ES6语法，key与value相同时，直接写一个就可以了</span>
            cpn
        &#125;
    &#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-36">4.2.2将template抽离出来</h4>
<h5 data-id="heading-37">4.2.2.1使用script标签</h5>
<p>使用<code><script type="text/x-template"></script></code>标签将html代码包裹，并赋以ID值，实现html代码的剥离</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><body>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">cpn</span>></span><span class="hljs-tag"></<span class="hljs-name">cpn</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">cpn1</span>></span><span class="hljs-tag"></<span class="hljs-name">cpn1</span>></span>
        <span class="hljs-comment"><!-- <cpn2></cpn2> --></span>

    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/x-template"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"test"</span>></span><span class="handlebars"><span class="xml">
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            我是组件，但代码抽离了哦~
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    </span></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>


</body>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../js/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-comment">// 下面是注册全局组件的方式</span>
    Vue.component(<span class="hljs-string">'cpn'</span>, &#123;
        <span class="hljs-attr">template</span>: <span class="hljs-string">"#test"</span>
    &#125;)

    <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
        <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
        <span class="hljs-comment">// 下面是注册局部组件的方式</span>
        <span class="hljs-attr">components</span>: &#123;
            <span class="hljs-attr">cpn1</span>: &#123;
                <span class="hljs-attr">template</span>: <span class="hljs-string">"#test"</span>
            &#125;

        &#125;
    &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/227d15ca998545028a6a0cedd3308b7c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-38">4.2.2.2使用template标签</h5>
<p>使用<code><template></template></code>标签将html代码包裹，并赋以ID值，实现html代码的剥离</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <template id=<span class="hljs-string">"test02"</span>>
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            hi~我是用template标签实现的
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    </template>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实现方法与上面相同只是标签使用方法不同</p>
<p>:low_brightness:注意，在组件中使用变量是可以的但是data要使用<strong>data()&#123;&#125;方法</strong>，用==return返回一个对象==的方式实现，如下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-comment">// 下面是注册全局组件的方式</span>
    Vue.component(<span class="hljs-string">'cpn1'</span>,&#123;
        <span class="hljs-attr">template</span>:<span class="hljs-string">"#test02"</span>,
        <span class="hljs-comment">//data必须使用方法，然后return返回</span>
        <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-keyword">return</span> &#123;
                <span class="hljs-attr">title</span>:<span class="hljs-string">"我是标题"</span>
            &#125;
        &#125;
    &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>因为我们使用方法再ruturn的情况下，每次调用都相当于在不同的地址生成对象，在复用的时候，会同步更改，所以设计者尤大大规定组件中必须使用data()&#123;reutrn &#123;&#125; &#125;的方式</p>
<p>理论同下，帮助理解</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">a</span> (<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">sname</span>:<span class="hljs-string">"hong"</span>,
        <span class="hljs-attr">sage</span>:<span class="hljs-number">18</span>
    &#125;
&#125;
<span class="hljs-keyword">let</span> b = a();
<span class="hljs-keyword">let</span> c = a();
<span class="hljs-keyword">let</span> d = a();
<span class="hljs-comment">//上面的b,c,d并不是相同的物理地址</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</blockquote>
<h4 data-id="heading-39">4.2.3 父子组件传值</h4>
<h5 data-id="heading-40">4.2.3.1父传子</h5>
<ul>
<li>
<p>通过<code>props</code>属性进行传值</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">cpn</span> <span class="hljs-attr">:cmovies</span>=<span class="hljs-string">"movies"</span>></span><span class="hljs-tag"></<span class="hljs-name">cpn</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-comment"><!-- 下面的是子组件的html --></span>
    <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"ccpn"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            &#123;&#123;cmovies&#125;&#125;
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../js/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-comment">// 下面是子组件</span>
    <span class="hljs-keyword">const</span> cpn = &#123;
        <span class="hljs-attr">template</span>: <span class="hljs-string">'#ccpn'</span>,
        <span class="hljs-attr">props</span>: [<span class="hljs-string">'cmovies'</span>],
        <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
            <span class="hljs-keyword">return</span>&#123;
            &#125;
        &#125;
    &#125;
    <span class="hljs-comment">// 下面是根组件也是父组件</span>
    <span class="hljs-keyword">const</span> App = <span class="hljs-keyword">new</span> Vue(&#123;
        <span class="hljs-attr">el</span>: <span class="hljs-string">"#app"</span>,
        <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
            <span class="hljs-keyword">return</span> &#123;
                <span class="hljs-attr">movies</span>: [<span class="hljs-string">'海王'</span>, <span class="hljs-string">'海贼'</span>]
            &#125;
        &#125;,
        <span class="hljs-attr">components</span>: &#123;
            cpn,
        &#125;

    &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>通过上面的方法，我们借助<code>props</code>属性来将父组件的数据传递给子组件，在调用子组件的时候通过<code>v-bind</code>属性来绑定子组件的变量和父组件中的变量</p>
</blockquote>
<blockquote>
<ul>
<li><code>compnents</code>属性不止可以使用<code>[]</code>也可以使用<code>&#123;&#125;</code>,在使用对象语法的时候，我们可以验证传过来的数据类型，基本语法如下</li>
</ul>
</blockquote>
</li>
</ul>
<h6 data-id="heading-41">4.2.3.1.1 porps属性的使用</h6>
<ul>
<li>
<p>动态props</p>
<p>上面的代码就是动态的props</p>
</li>
<li>
<p>静态props</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
        <span class="hljs-comment"><!-- props静态的赋值 --></span>
        <span class="hljs-tag"><<span class="hljs-name">cpn</span> <span class="hljs-attr">cmovies</span>=<span class="hljs-string">"sss"</span>></span><span class="hljs-tag"></<span class="hljs-name">cpn</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"ccpn"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            &#123;&#123;cmovies&#125;&#125;
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意点:</p>
<ul>
<li>props的变量前面不需要加<code>：</code>,不加<code>:</code>的情况下，后面赋值就不会被认为是变量</li>
</ul>
</blockquote>
</li>
<li>
<p>props验证</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> props: &#123; 
                    <span class="hljs-comment">// 基础类型检测, null意味着任何类型都行</span>
                    <span class="hljs-attr">propA</span>: <span class="hljs-built_in">Number</span>,
                     <span class="hljs-comment">// 多种类型</span>
                    <span class="hljs-attr">propB</span>: [<span class="hljs-built_in">String</span>, <span class="hljs-built_in">Number</span>],
                     <span class="hljs-comment">// 必传且是String</span>
                    <span class="hljs-attr">propC</span>: &#123;
                        <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
                        <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>
                    &#125;,
                     <span class="hljs-comment">// 数字有默认值</span>
                    <span class="hljs-attr">propD</span>: &#123;
                        <span class="hljs-attr">type</span>: <span class="hljs-built_in">Number</span>,
                        <span class="hljs-attr">default</span>: <span class="hljs-number">101</span>
                    &#125;,
                     <span class="hljs-comment">// 数组、默认值是一个工厂函数返回对象</span>
                    <span class="hljs-attr">propE</span>: &#123;
                        <span class="hljs-attr">type</span>: <span class="hljs-built_in">Object</span>,
                        <span class="hljs-attr">default</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
                            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"propE default invoked."</span>);
                            <span class="hljs-keyword">return</span> &#123;
                                <span class="hljs-attr">message</span>: <span class="hljs-string">"I am from propE."</span>
                            &#125;;
                        &#125;
                    &#125;, 
                    <span class="hljs-comment">// 自定义验证函数</span>
                    <span class="hljs-attr">propF</span>: &#123;
                        <span class="hljs-attr">isValid</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">value</span>) </span>&#123;
                            <span class="hljs-keyword">return</span> value > <span class="hljs-number">100</span>;
                        &#125;
                    &#125;
                &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>可检测的类型有：</p>
<ul>
<li>String</li>
<li>Number</li>
<li>Boolean</li>
<li>Function</li>
<li>Object</li>
<li>Array</li>
<li>Symbol</li>
</ul>
</blockquote>
<h2 data-id="heading-42">单向数据流</h2>
<p>props 是单向绑定的：当父组件的属性变化时，将传导给子组件，但是不会反过来。这是为了防止子组件五一修改父组件的状态。</p>
<p>所以不应该在子组件中修改 props 中的值，Vue 会报出警告。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> childNode = &#123;
  <span class="hljs-attr">template</span>: <span class="hljs-string">`
          <div class="child">
            <div>
              <span>子组件数据</span>
              <input v-model="forChildMsg"/>
            </div>
            <p>&#123;&#123;forChildMsg&#125;&#125;</p>
          </div>`</span>,
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-string">"for-child-msg"</span>: <span class="hljs-built_in">String</span>
  &#125;
&#125;;
<span class="hljs-keyword">let</span> parentNode = &#123;
  <span class="hljs-attr">template</span>: <span class="hljs-string">`
          <div class="parent">
            <div>
              <span>父组件数据</span>
              <input v-model="msg"/>
            </div>
            <p>&#123;&#123;msg&#125;&#125;</p>
            <child :for-child-msg="msg"></child>
          </div>
        `</span>,
  <span class="hljs-attr">components</span>: &#123;
    <span class="hljs-attr">child</span>: childNode
  &#125;,
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">msg</span>: <span class="hljs-string">"default string."</span>
    &#125;;
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里我们给父组件和子组件都有一个输入框，并且显示出父组件数据和子组件的数据。当我们在父组件的输入框输入新数据时，同步的子组件数据也被修改了；这就是 props 的向子组件传递数据。而当我们修改子组件的输入框时，浏览器的控制台则报出错误警告</p>
<blockquote>
<p>[Vue warn]: Avoid mutating a prop directly since the value will be overwritten whenever the parent component re-renders. Instead, use a data or computed property based on the prop's value. Prop being mutated: "forChildMsg"</p>
</blockquote>
</li>
<li>
<p>修改 props 数据</p>
<ul>
<li>通常有两种原因：</li>
<li>prop 作为初始值传入后，子组件想把它当做局部数据来用</li>
<li>prop 作为初始值传入后，由子组件处理成其他数据输出</li>
</ul>
<p>应对办法是:</p>
<ul>
<li>定义一个局部变量，并用 prop 的值初始化它</li>
</ul>
<p>但是由于定义的 ownChildMsg 只能接受 forChildMsg 的初始值，当父组件要传递的值变化发生时，ownChildMsg 无法收到更新。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> childNode = &#123;
  <span class="hljs-attr">template</span>: <span class="hljs-string">`
          <div class="child">
            <div>
              <span>子组件数据</span>
              <input v-model="forChildMsg"/>
            </div>
            <p>&#123;&#123;forChildMsg&#125;&#125;</p>
            <p>ownChildMsg : &#123;&#123;ownChildMsg&#125;&#125;</p>
          </div>`</span>,
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-string">"for-child-msg"</span>: <span class="hljs-built_in">String</span>
  &#125;,
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123; <span class="hljs-attr">ownChildMsg</span>: <span class="hljs-built_in">this</span>.forChildMsg &#125;;
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里我们加了一个</p><p>用于查看 ownChildMsg 数据是否变化，结果发现只有默认值传递给了 ownChildMsg，父组件改变只会变化到 forChildMsg，不会修改 ownChildMsg。</p>
<ul>
<li>
<p>定义一个计算属性，处理 prop 的值并返回</p>
<p>由于是计算属性，所以只能显示值，不能设置值。我们这里设置的是一旦从父组件修改了 forChildMsg 数据，我们就把 forChildMsg 加上一个字符串"---ownChildMsg"，然后显示在屏幕上。这时是可以每当父组件修改了新数据，都会更新 ownChildMsg 数据的。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> childNode = &#123;
  <span class="hljs-attr">template</span>: <span class="hljs-string">`
          <div class="child">
            <div>
              <span>子组件数据</span>
              <input v-model="forChildMsg"/>
            </div>
            <p>&#123;&#123;forChildMsg&#125;&#125;</p>
            <p>ownChildMsg : &#123;&#123;ownChildMsg&#125;&#125;</p>
          </div>`</span>,
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-string">"for-child-msg"</span>: <span class="hljs-built_in">String</span>
  &#125;,
  <span class="hljs-attr">computed</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">ownChildMsg</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.forChildMsg + <span class="hljs-string">"---ownChildMsg"</span>;
    &#125;
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>更加妥帖的方式是使用变量存储 prop 的初始值，并用 watch 来观察 prop 值得变化。发生变化时，更新变量的值。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> childNode = &#123;
  <span class="hljs-attr">template</span>: <span class="hljs-string">`
          <div class="child">
            <div>
              <span>子组件数据</span>
              <input v-model="forChildMsg"/>
            </div>
            <p>&#123;&#123;forChildMsg&#125;&#125;</p>
            <p>ownChildMsg : &#123;&#123;ownChildMsg&#125;&#125;</p>
          </div>`</span>,
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-string">"for-child-msg"</span>: <span class="hljs-built_in">String</span>
  &#125;,
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">ownChildMsg</span>: <span class="hljs-built_in">this</span>.forChildMsg
    &#125;;
  &#125;,
  <span class="hljs-attr">watch</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">forChildMsg</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">this</span>.ownChildMsg = <span class="hljs-built_in">this</span>.forChildMsg;
    &#125;
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>单向数据流</p>
</li>
</ul>
<p>props 是单向绑定的：当父组件的属性变化时，将传导给子组件，但是不会反过来。这是为了防止子组件五一修改父组件的状态。</p>
<p>所以不应该在子组件中修改 props 中的值，Vue 会报出警告。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> childNode = &#123;
  <span class="hljs-attr">template</span>: <span class="hljs-string">`
          <div class="child">
            <div>
              <span>子组件数据</span>
              <input v-model="forChildMsg"/>
            </div>
            <p>&#123;&#123;forChildMsg&#125;&#125;</p>
          </div>`</span>,
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-string">"for-child-msg"</span>: <span class="hljs-built_in">String</span>
  &#125;
&#125;;
<span class="hljs-keyword">let</span> parentNode = &#123;
  <span class="hljs-attr">template</span>: <span class="hljs-string">`
          <div class="parent">
            <div>
              <span>父组件数据</span>
              <input v-model="msg"/>
            </div>
            <p>&#123;&#123;msg&#125;&#125;</p>
            <child :for-child-msg="msg"></child>
          </div>
        `</span>,
  <span class="hljs-attr">components</span>: &#123;
    <span class="hljs-attr">child</span>: childNode
  &#125;,
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">msg</span>: <span class="hljs-string">"default string."</span>
    &#125;;
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里我们给父组件和子组件都有一个输入框，并且显示出父组件数据和子组件的数据。当我们在父组件的输入框输入新数据时，同步的子组件数据也被修改了；这就是 props 的向子组件传递数据。而当我们修改子组件的输入框时，浏览器的控制台则报出错误警告</p>
<blockquote>
<p>[Vue warn]: Avoid mutating a prop directly since the value will be overwritten whenever the parent component re-renders. Instead, use a data or computed property based on the prop's value. Prop being mutated: "forChildMsg"</p>
</blockquote>
</li>
<li>
<p>修改 props 数据</p>
<p>通常有两种原因：</p>
<ul>
<li>
<p>prop 作为初始值传入后，子组件想把它当做局部数据来用</p>
</li>
<li>
<p>prop 作为初始值传入后，由子组件处理成其他数据输出</p>
</li>
</ul>
<p>应对办法是</p>
<ul>
<li>
<p>定义一个局部变量，并用 prop 的值初始化它</p>
<p>但是由于定义的 ownChildMsg 只能接受 forChildMsg 的初始值，当父组件要传递的值变化发生时，ownChildMsg 无法收到更新。</p>
</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-keyword">let</span> childNode = &#123;
      <span class="hljs-attr">template</span>: <span class="hljs-string">`
              <div class="child">
                <div>
                  <span>子组件数据</span>
                  <input v-model="forChildMsg"/>
                </div>
                <p>&#123;&#123;forChildMsg&#125;&#125;</p>
                <p>ownChildMsg : &#123;&#123;ownChildMsg&#125;&#125;</p>
              </div>`</span>,
      <span class="hljs-attr">props</span>: &#123;
        <span class="hljs-string">"for-child-msg"</span>: <span class="hljs-built_in">String</span>
      &#125;,
      <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> &#123; <span class="hljs-attr">ownChildMsg</span>: <span class="hljs-built_in">this</span>.forChildMsg &#125;;
      &#125;
    &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里我们加了一个</p><p>用于查看 ownChildMsg 数据是否变化，结果发现只有默认值传递给了 ownChildMsg，父组件改变只会变化到 forChildMsg，不会修改 ownChildMsg。</p>
<ul>
<li>
<p>定义一个计算属性，处理 prop 的值并返回</p>
<p>由于是计算属性，所以只能显示值，不能设置值。我们这里设置的是一旦从父组件修改了 forChildMsg 数据，我们就把 forChildMsg 加上一个字符串"---ownChildMsg"，然后显示在屏幕上。这时是可以每当父组件修改了新数据，都会更新 ownChildMsg 数据的。</p>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> childNode = &#123;
  <span class="hljs-attr">template</span>: <span class="hljs-string">`
          <div class="child">
            <div>
              <span>子组件数据</span>
              <input v-model="forChildMsg"/>
            </div>
            <p>&#123;&#123;forChildMsg&#125;&#125;</p>
            <p>ownChildMsg : &#123;&#123;ownChildMsg&#125;&#125;</p>
          </div>`</span>,
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-string">"for-child-msg"</span>: <span class="hljs-built_in">String</span>
  &#125;,
  <span class="hljs-attr">computed</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">ownChildMsg</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.forChildMsg + <span class="hljs-string">"---ownChildMsg"</span>;
    &#125;
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>更加妥帖的方式是使用变量存储 prop 的初始值，并用 watch 来观察 prop 值得变化。发生变化时，更新变量的值。</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> childNode = &#123;
  <span class="hljs-attr">template</span>: <span class="hljs-string">`
          <div class="child">
            <div>
              <span>子组件数据</span>
              <input v-model="forChildMsg"/>
            </div>
            <p>&#123;&#123;forChildMsg&#125;&#125;</p>
            <p>ownChildMsg : &#123;&#123;ownChildMsg&#125;&#125;</p>
          </div>`</span>,
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-string">"for-child-msg"</span>: <span class="hljs-built_in">String</span>
  &#125;,
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">ownChildMsg</span>: <span class="hljs-built_in">this</span>.forChildMsg
    &#125;;
  &#125;,
  <span class="hljs-attr">watch</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">forChildMsg</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">this</span>.ownChildMsg = <span class="hljs-built_in">this</span>.forChildMsg;
    &#125;
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>上面部分代码借鉴<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jianshu.com%2Fp%2F89bd18e44e73" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jianshu.com/p/89bd18e44e73" ref="nofollow noopener noreferrer">www.jianshu.com/p/89bd18e44…</a></p>
</blockquote>
</li>
</ul>
<h5 data-id="heading-43">4.2.3.2 子传父</h5>
<ul>
<li>
<p>在子组件中通过<code>$emit()</code>来触发事件。</p>
</li>
<li>
<p>在父组件中通过<code>v-on</code>来监听子组件事件</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-comment"><!-- 父组件模板 --></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
        <span class="hljs-comment"><!-- 调用childMessage方法的时候如果省略参数，系统将会自动接收子组件方法传递过来的值 --></span>
        <span class="hljs-tag"><<span class="hljs-name">cpn</span> @<span class="hljs-attr">btn-click</span> = <span class="hljs-string">childMessage</span>></span><span class="hljs-tag"></<span class="hljs-name">cpn</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    
<span class="hljs-comment"><!-- 子组件模板 --></span>
    <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"cpn"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span> = <span class="hljs-string">"logClick(item)"</span> <span class="hljs-attr">v-for</span> = <span class="hljs-string">"item in categories"</span>></span>&#123;&#123;item.wname&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../js/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-comment">// 子组件</span>
    <span class="hljs-keyword">const</span> cpn =&#123;
        <span class="hljs-attr">template</span>:<span class="hljs-string">"#cpn"</span>,
        <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-keyword">return</span> &#123;
                <span class="hljs-attr">categories</span>:[
                    &#123;
                        <span class="hljs-attr">id</span>:<span class="hljs-number">1</span>,
                        <span class="hljs-attr">wname</span>:<span class="hljs-string">'篮球'</span>
                    &#125;,&#123;
                        <span class="hljs-attr">id</span>:<span class="hljs-number">2</span>,
                        <span class="hljs-attr">wname</span>:<span class="hljs-string">'乒乓球'</span>
                    &#125;,
                    &#123;
                        <span class="hljs-attr">id</span>:<span class="hljs-number">3</span>,
                        <span class="hljs-attr">wname</span>:<span class="hljs-string">'羽毛球'</span>
                    &#125;,
                ]
            &#125;
        &#125;,
        <span class="hljs-attr">methods</span>:&#123;
            <span class="hljs-function"><span class="hljs-title">logClick</span>(<span class="hljs-params">item</span>)</span>&#123;
                <span class="hljs-comment">// 这个输出是在子组件本身内完成的</span>
                <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"我点击了"</span>,item.wname);
                <span class="hljs-comment">// 下面是将数据传递给父组件</span>
                <span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">'btn-click'</span>,item.wname,)
            &#125;
        &#125;
    &#125;
    <span class="hljs-comment">// 父组件</span>
    <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
        <span class="hljs-attr">el</span>:<span class="hljs-string">'#app'</span>,
        <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-keyword">return</span>&#123;
            <span class="hljs-attr">message</span>:<span class="hljs-string">'hello'</span>

            &#125;
        &#125;,
        <span class="hljs-attr">methods</span>:&#123;
            <span class="hljs-function"><span class="hljs-title">childMessage</span>(<span class="hljs-params">arg</span>)</span>&#123;
                <span class="hljs-built_in">console</span>.log(arg);
            &#125;
        &#125;,
        <span class="hljs-attr">components</span>:&#123;
            cpn
        &#125;
    &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h4 data-id="heading-44">父子组间访问</h4>
<h5 data-id="heading-45">4.3.4.1 父访问子</h5>
<ul>
<li>
<p><code>$children</code></p>
<blockquote>
<p><code>$children</code>是一个数组，打印之后显示VueComponent，VueComponent里面包含了很多数据，其中就有自组件中的属性或者方法。</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8bffda07391d4be78f9840a6404f5902~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>整体代码：</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>

<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../js/vue.js"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/javascript"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"btnClick"</span>></span>按钮<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">Cpn</span>></span><span class="hljs-tag"></<span class="hljs-name">Cpn</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"cpn"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span>我是子组件<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-comment">//下面是子组件</span>
    <span class="hljs-keyword">const</span> Cpn = &#123;
        <span class="hljs-attr">template</span>: <span class="hljs-string">'#cpn'</span>,
        <span class="hljs-comment">// 子组件的data必须使用方法的形式</span>
        <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-keyword">return</span>&#123;
                <span class="hljs-attr">msg</span>:<span class="hljs-string">"我是一条在子组件的消息"</span>
            &#125;
        &#125;,
        <span class="hljs-attr">methods</span>: &#123;
            <span class="hljs-function"><span class="hljs-title">showMessage</span>(<span class="hljs-params"></span>)</span> &#123;
                <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"sss"</span>);
                <span class="hljs-keyword">return</span>  <span class="hljs-string">"我是返回的内容"</span>
            &#125;
        &#125;
    &#125;;
  <span class="hljs-comment">//下面是父组件  </span>
    <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
        <span class="hljs-attr">el</span>: <span class="hljs-string">"#app"</span>,
        <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
            <span class="hljs-keyword">return</span> &#123;
               
            &#125;
        &#125;,
        <span class="hljs-attr">methods</span>: &#123;
            <span class="hljs-function"><span class="hljs-title">btnClick</span>(<span class="hljs-params"></span>)</span> &#123;
                <span class="hljs-comment">// 获取$children</span>
                <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.$children);
                <span class="hljs-comment">// 获取子组件中的方法并调用</span>
                <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.$children[<span class="hljs-number">0</span>].showMessage());
                <span class="hljs-comment">// 获取子组件data中的变量</span>
                <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.$children[<span class="hljs-number">0</span>].msg)
            &#125;,
        &#125;,
        <span class="hljs-attr">components</span>: &#123;
            Cpn
        &#125;
    &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>关键代码：</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"> methods: &#123;
            <span class="hljs-function"><span class="hljs-title">btnClick</span>(<span class="hljs-params"></span>)</span> &#123;
                <span class="hljs-comment">// 获取$children</span>
                <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.$children);
                <span class="hljs-comment">// 获取子组件中的方法并调用</span>
                <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.$children[<span class="hljs-number">0</span>].showMessage());
                <span class="hljs-comment">// 获取子组件data中的变量</span>
                <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.$children[<span class="hljs-number">0</span>].msg)
            &#125;,
        &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>但是不推荐这种，因为如果后期dom树更改的时候，就会对这个方法造成影响。</p>
</blockquote>
</li>
<li>
<p><code>$refs</code></p>
<blockquote>
<p>refs是一个对象，默认是个空对象，里面包含了被选中的子组件的所有元素</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1923a9340c624f6599d2f291b4c97af8~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<ul>
<li>
<p>在需要使用的子集上通过属性<code>ref</code>添加属性名</p>
</li>
<li>
<p>在父级使用<code>$refs.属性名</code>来获取自组件中的数据</p>
</li>
<li>
<p>整体代码</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>

<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../js/vue.js"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/javascript"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"btnClick"</span>></span>按钮<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">Cpn</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"son"</span> ></span><span class="hljs-tag"></<span class="hljs-name">Cpn</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"cpn"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span>我是子组件<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">const</span> Cpn = &#123;
        <span class="hljs-attr">template</span>: <span class="hljs-string">'#cpn'</span>,
        <span class="hljs-comment">// 子组件的data必须使用方法的形式</span>
        <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-keyword">return</span>&#123;
                <span class="hljs-attr">msg</span>:<span class="hljs-string">"我是一条在子组件的消息"</span>
            &#125;
        &#125;,
        <span class="hljs-attr">methods</span>: &#123;
            <span class="hljs-function"><span class="hljs-title">showMessage</span>(<span class="hljs-params"></span>)</span> &#123;
                <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"sss"</span>);
                <span class="hljs-keyword">return</span>  <span class="hljs-string">"我是返回的内容"</span>
            &#125;
        &#125;
    &#125;;
    <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
        <span class="hljs-attr">el</span>: <span class="hljs-string">"#app"</span>,
        <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
            <span class="hljs-keyword">return</span> &#123;
               
            &#125;
        &#125;,
        <span class="hljs-attr">methods</span>: &#123;
            <span class="hljs-function"><span class="hljs-title">btnClick</span>(<span class="hljs-params"></span>)</span> &#123;
                <span class="hljs-comment">// // 获取$children</span>
                <span class="hljs-comment">// console.log(this.$children);</span>
                <span class="hljs-comment">// // 获取子组件中的方法并调用</span>
                <span class="hljs-comment">// console.log(this.$children[0].showMessage());</span>
                <span class="hljs-comment">// // 获取子组件data中的变量</span>
                <span class="hljs-comment">// console.log(this.$children[0].msg)</span>

                <span class="hljs-comment">// 打印$refs</span>
                <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.$refs);
                <span class="hljs-comment">// 获取aaa的msg变量</span>
                <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.$refs.son.msg);
                <span class="hljs-comment">// 获取aaa的方法</span>
                <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.$refs.son.showMessage());
            &#125;,
        &#125;,
        <span class="hljs-attr">components</span>: &#123;
            Cpn
        &#125;
    &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>关键代码;</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-function"><span class="hljs-title">btnClick</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-comment">// 打印$refs</span>
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.$refs);
        <span class="hljs-comment">// 获取aaa的msg变量</span>
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.$refs.son.msg);
        <span class="hljs-comment">// 获取aaa的方法</span>
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.$refs.son.showMessage());
    &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
</li>
<li>
<p>子访问父（理解）</p>
<ul>
<li>
<p><code>$parent</code></p>
<blockquote>
<p>可以访问到子组件的直系父级（但因为这样的原因，开发时一个组件可能有多个父级，但并不是所有父级都有你所要的属性，那么就会返回<code>undefined</code>，所以开<strong>发时一般不用</strong>）。</p>
</blockquote>
<ul>
<li>
<p>完整代码</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>

<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../js/vue.js"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/javascript"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">cpn</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"son"</span>></span><span class="hljs-tag"></<span class="hljs-name">cpn</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-comment"><!-- 下面是cpn子组件 --></span>
    <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"cpn"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span>

            <span class="hljs-tag"><<span class="hljs-name">div</span>></span>我是cpn组件<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">ccpn</span>></span><span class="hljs-tag"></<span class="hljs-name">ccpn</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>



    <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
    <span class="hljs-comment"><!-- 下面是ccpn组件 --></span>
    <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"ccpn"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span>></span>我是ccpn组件<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"checkParent"</span>></span>按钮<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-comment">// 下面是cpn的子组件</span>
    <span class="hljs-keyword">const</span> ccpn = &#123;
        <span class="hljs-attr">template</span>: <span class="hljs-string">"#ccpn"</span>,
        <span class="hljs-attr">methods</span>: &#123;
            <span class="hljs-function"><span class="hljs-title">checkParent</span>(<span class="hljs-params"></span>)</span> &#123;
                <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.$parent.msg);
            &#125;

        &#125;

    &#125;
    <span class="hljs-comment">// 下面是第一个子组件</span>
    <span class="hljs-keyword">const</span> cpn = &#123;
        <span class="hljs-attr">template</span>: <span class="hljs-string">'#cpn'</span>,
        <span class="hljs-comment">// 注册ccpn组件</span>
        <span class="hljs-attr">components</span>: &#123;
            ccpn
        &#125;,
        <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
            <span class="hljs-keyword">return</span> &#123;
                <span class="hljs-attr">msg</span>: <span class="hljs-string">"我是cpn组件中的一条消息"</span>
            &#125;
        &#125;,
        <span class="hljs-attr">methods</span>: &#123;&#125;
    &#125;;

    <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
        <span class="hljs-attr">el</span>: <span class="hljs-string">"#app"</span>,
        <span class="hljs-attr">components</span>: &#123;
            cpn,
        &#125;
    &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>关键代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    methods: &#123;
        <span class="hljs-function"><span class="hljs-title">checkParent</span>(<span class="hljs-params"></span>)</span> &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.$parent.msg);
        &#125;

    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
</li>
<li>
<p><code>$root</code></p>
<blockquote>
<p>无论在哪的组件，可以直接获取到根组件的属性：</p>
</blockquote>
<ul>
<li>
<p>完整代码</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>

<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../js/vue.js"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/javascript"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">cpn</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"son"</span>></span><span class="hljs-tag"></<span class="hljs-name">cpn</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-comment"><!-- 下面是cpn子组件 --></span>
    <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"cpn"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span>

            <span class="hljs-tag"><<span class="hljs-name">div</span>></span>我是cpn组件<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">ccpn</span>></span><span class="hljs-tag"></<span class="hljs-name">ccpn</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>



    <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
    <span class="hljs-comment"><!-- 下面是ccpn组件 --></span>
    <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"ccpn"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span>></span>我是ccpn组件<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"checkParent"</span>></span>按钮<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-comment">// 下面是cpn的子组件</span>
    <span class="hljs-keyword">const</span> ccpn = &#123;
        <span class="hljs-attr">template</span>: <span class="hljs-string">"#ccpn"</span>,
        <span class="hljs-attr">methods</span>: &#123;
            <span class="hljs-function"><span class="hljs-title">checkParent</span>(<span class="hljs-params"></span>)</span> &#123;
                <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.$root.msg);
            &#125;

        &#125;

    &#125;
    <span class="hljs-comment">// 下面是第一个子组件</span>
    <span class="hljs-keyword">const</span> cpn = &#123;
        <span class="hljs-attr">template</span>: <span class="hljs-string">'#cpn'</span>,
        <span class="hljs-comment">// 注册ccpn组件</span>
        <span class="hljs-attr">components</span>: &#123;
            ccpn
        &#125;,
        <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
            <span class="hljs-keyword">return</span> &#123;
                <span class="hljs-attr">msg</span>: <span class="hljs-string">"我是cpn组件中的一条消息"</span>
            &#125;
        &#125;,
        <span class="hljs-attr">methods</span>: &#123;&#125;
    &#125;;

    <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
        <span class="hljs-attr">el</span>: <span class="hljs-string">"#app"</span>,
        <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-keyword">return</span>&#123;
                <span class="hljs-attr">msg</span>:<span class="hljs-string">"我是根组件的一条消息"</span>
            &#125;
        &#125;,
        <span class="hljs-attr">components</span>: &#123;
            cpn,
        &#125;
    &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>关键代码</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">        methods: &#123;
            <span class="hljs-function"><span class="hljs-title">checkParent</span>(<span class="hljs-params"></span>)</span> &#123;
                <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.$root.msg);
            &#125;

        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c4594ba9e38e4dabb8c6e7255a016d57~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<h2 data-id="heading-46">五、插槽</h2>
<h3 data-id="heading-47">5.1普通插槽的使用</h3>
<ul>
<li>
<p>首先在子组件中需要改变的地方写上插槽(<code><slot></slot></code>)</p>
</li>
<li>
<p>在父级调用组件的标签内写这里需要显示的内容（<strong>调用就必须使用双标签</strong>）</p>
</li>
<li>
<p>整体代码：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>

<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../js/vue.js"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/javascript"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
        <span class="hljs-selector-tag">img</span> &#123;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
        &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
        <span class="hljs-comment"><!-- 第一个插槽显示按钮 --></span>
        <span class="hljs-tag"><<span class="hljs-name">cpn</span>></span> <span class="hljs-tag"><<span class="hljs-name">button</span>></span>按钮<span class="hljs-tag"></<span class="hljs-name">button</span>></span><span class="hljs-tag"></<span class="hljs-name">cpn</span>></span>
        <span class="hljs-comment"><!-- 第二个插槽显示图片 --></span>
        <span class="hljs-tag"><<span class="hljs-name">cpn</span>></span> <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../img/01.png"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">"个人logo"</span>></span><span class="hljs-tag"></<span class="hljs-name">cpn</span>></span>
        <span class="hljs-comment"><!-- 第三个插槽显示文字 --></span>
        <span class="hljs-tag"><<span class="hljs-name">cpn</span>></span> <span class="hljs-tag"><<span class="hljs-name">span</span>></span>我就是一段文字<span class="hljs-tag"></<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">cpn</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-comment"><!-- 下面是子组件 --></span>
    <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"cpn"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>我是一个子组件<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
            <span class="hljs-comment"><!-- 定义一个插槽 --></span>
            <span class="hljs-tag"><<span class="hljs-name">slot</span>></span><span class="hljs-tag"></<span class="hljs-name">slot</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
    
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">const</span> cpn = &#123;
        <span class="hljs-attr">template</span>: <span class="hljs-string">"#cpn"</span>,
    &#125;;
    <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
        <span class="hljs-attr">el</span>: <span class="hljs-string">"#app"</span>,
        <span class="hljs-attr">components</span>: &#123;
            cpn
        &#125;
    &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>关键代码：</p>
<pre><code class="hljs language-html copyable" lang="html">    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
        <span class="hljs-comment"><!-- 第一个插槽显示按钮 --></span>
        <span class="hljs-tag"><<span class="hljs-name">cpn</span>></span> <span class="hljs-tag"><<span class="hljs-name">button</span>></span>按钮<span class="hljs-tag"></<span class="hljs-name">button</span>></span><span class="hljs-tag"></<span class="hljs-name">cpn</span>></span>
        <span class="hljs-comment"><!-- 第二个插槽显示图片 --></span>
        <span class="hljs-tag"><<span class="hljs-name">cpn</span>></span> <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../img/01.png"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">"个人logo"</span>></span><span class="hljs-tag"></<span class="hljs-name">cpn</span>></span>
        <span class="hljs-comment"><!-- 第三个插槽显示文字 --></span>
        <span class="hljs-tag"><<span class="hljs-name">cpn</span>></span> <span class="hljs-tag"><<span class="hljs-name">span</span>></span>我就是一段文字<span class="hljs-tag"></<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">cpn</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-comment"><!-- 下面是子组件 --></span>
    <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"cpn"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>我是一个子组件<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
            <span class="hljs-comment"><!-- 定义一个插槽 --></span>
            <span class="hljs-tag"><<span class="hljs-name">slot</span>></span><span class="hljs-tag"></<span class="hljs-name">slot</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c04f9b2f99e4df381e14504e257b723~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</li>
</ul>
<h3 data-id="heading-48">5.2默认插槽值</h3>
<ul>
<li>
<p>使用过程与上面一样，不同的是在子组件中直接给<code><solt></slot></code>一个默认值</p>
</li>
<li>
<p>在调用的时候，如果没有指定插槽内容，就会显示默认的插槽内容</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
        <span class="hljs-comment"><!-- 第一个插槽显示按钮 --></span>
        <span class="hljs-tag"><<span class="hljs-name">cpn</span>></span> <span class="hljs-tag"><<span class="hljs-name">button</span>></span>我是另一个按钮<span class="hljs-tag"></<span class="hljs-name">button</span>></span><span class="hljs-tag"></<span class="hljs-name">cpn</span>></span>
        <span class="hljs-comment"><!-- 第二个插槽默认内容 --></span>
        <span class="hljs-tag"><<span class="hljs-name">cpn</span>></span><span class="hljs-tag"></<span class="hljs-name">cpn</span>></span>
        <span class="hljs-comment"><!-- 第三个插槽显示文字 --></span>
        <span class="hljs-tag"><<span class="hljs-name">cpn</span>></span> <span class="hljs-tag"><<span class="hljs-name">span</span>></span>我就是一段文字<span class="hljs-tag"></<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">cpn</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-comment"><!-- 下面是子组件 --></span>
    <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"cpn"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>我是一个子组件<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
            <span class="hljs-comment"><!-- 给插槽一个默认值 --></span>
            <span class="hljs-tag"><<span class="hljs-name">slot</span>></span><span class="hljs-tag"><<span class="hljs-name">button</span>></span>按钮<span class="hljs-tag"></<span class="hljs-name">button</span>></span><span class="hljs-tag"></<span class="hljs-name">slot</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2c20a76bbf6343a0845a1048642e15b7~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</li>
</ul>
<h3 data-id="heading-49">5.3具名插槽</h3>
<ul>
<li>
<p>使用<code>name</code>属性给插槽一个标识</p>
</li>
<li>
<p>在调用的时候使用属性<code>slot</code>来确定给哪个插槽替换</p>
</li>
<li>
<p>如果没有用名称来确定的标识的内容，就会去寻找未具名的插槽，将其替换</p>
</li>
<li>
<p>如果没有未具名的插槽，未指定<code>name</code>的内容将不会显示</p>
</li>
<li>
<p>整体代码</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>

<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../js/vue.js"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/javascript"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
        <span class="hljs-selector-tag">img</span> &#123;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
        &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">cpn</span>></span>
            <span class="hljs-comment"><!-- 将第一个插槽替换为按钮 --></span>
            <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"first"</span>></span><span class="hljs-symbol">&lt;</span><span class="hljs-tag"></<span class="hljs-name">button</span>></span>
            <span class="hljs-comment"><!-- 将第二个插槽替换为文本+输入框 --></span>
            <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"second"</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">span</span>></span>搜索<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">placeholder</span>=<span class="hljs-string">"搜索"</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">span</span>></span>
            <span class="hljs-comment"><!-- 第三个插槽变空 --></span>
            <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"third"</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
            <span class="hljs-comment"><!-- 替换没有名称的插槽 --></span>
            <span class="hljs-tag"><<span class="hljs-name">span</span>></span>淦<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">span</span>></span>淦<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">cpn</span>></span>

    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-comment"><!-- 下面是子组件 --></span>
    <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"cpn"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">slot</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"first"</span>></span>我是第一个插槽<span class="hljs-tag"></<span class="hljs-name">slot</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">slot</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"second"</span>></span>我是第二个插槽<span class="hljs-tag"></<span class="hljs-name">slot</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">slot</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"third"</span>></span>我是第三个插槽<span class="hljs-tag"></<span class="hljs-name">slot</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">slot</span>></span><span class="hljs-tag"></<span class="hljs-name">slot</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">const</span> cpn = &#123;
        <span class="hljs-attr">template</span>: <span class="hljs-string">"#cpn"</span>,
    &#125;;
    <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
        <span class="hljs-attr">el</span>: <span class="hljs-string">"#app"</span>,
        <span class="hljs-attr">components</span>: &#123;
            cpn
        &#125;
    &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>关键代码</p>
<pre><code class="hljs language-html copyable" lang="html">   <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">cpn</span>></span>
            <span class="hljs-comment"><!-- 将第一个插槽替换为按钮 --></span>
            <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"first"</span>></span><span class="hljs-symbol">&lt;</span><span class="hljs-tag"></<span class="hljs-name">button</span>></span>
            <span class="hljs-comment"><!-- 将第二个插槽替换为文本+输入框 --></span>
            <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"second"</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">span</span>></span>搜索<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">placeholder</span>=<span class="hljs-string">"搜索"</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">span</span>></span>
            <span class="hljs-comment"><!-- 第三个插槽变空 --></span>
            <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"third"</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
            <span class="hljs-comment"><!-- 替换没有名称的插槽 --></span>
            <span class="hljs-tag"><<span class="hljs-name">span</span>></span>淦<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">span</span>></span>嘿<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">cpn</span>></span>

    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-comment"><!-- 下面是子组件 --></span>
    <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"cpn"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">slot</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"first"</span>></span>我是第一个插槽<span class="hljs-tag"></<span class="hljs-name">slot</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">slot</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"second"</span>></span>我是第二个插槽<span class="hljs-tag"></<span class="hljs-name">slot</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">slot</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"third"</span>></span>我是第三个插槽<span class="hljs-tag"></<span class="hljs-name">slot</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">slot</span>></span><span class="hljs-tag"></<span class="hljs-name">slot</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79af52f6f4564639876654b1a65692fd~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>如果我们在子组件中将最后的那个未具名的插槽删除，那么上面的文字将不会显示：</p>
</blockquote>
<pre><code class="hljs language-html copyable" lang="html">    <span class="hljs-comment"><!-- 下面是子组件 --></span>
    <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"cpn"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">slot</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"first"</span>></span>我是第一个插槽<span class="hljs-tag"></<span class="hljs-name">slot</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">slot</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"second"</span>></span>我是第二个插槽<span class="hljs-tag"></<span class="hljs-name">slot</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">slot</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"third"</span>></span>我是第三个插槽<span class="hljs-tag"></<span class="hljs-name">slot</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e620991fc18f41d985e0e15c850308aa~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</li>
</ul>
<h3 data-id="heading-50">5.4作用域插槽</h3>
<ul>
<li>
<p>在子组件中的<strong>插槽上</strong>通过<code>:</code>来绑定一个属性名与属性值，语法为<code><slot :list = "Arr"> 内容 </slot></code>。<strong>属性名不能包含大写字母</strong></p>
</li>
<li>
<p>父级在调用的时候需要在组件内写一个<code><template slot-scope="slot">内容</template></code>(低版本必须用template，高版本可以不用)</p>
</li>
<li>
<p>整体代码</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>

<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../js/vue.js"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/javascript"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
        <span class="hljs-selector-tag">img</span> &#123;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
        &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">cpn</span>></span><span class="hljs-tag"></<span class="hljs-name">cpn</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">cpn</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">slot-scope</span>=<span class="hljs-string">"slot"</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"item in slot.list"</span>></span>&#123;&#123;item&#125;&#125;-<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">cpn</span>></span>

    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-comment"><!-- 下面是子组件 --></span>
    <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"cpn"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>我是子组件<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">slot</span> <span class="hljs-attr">:list</span>=<span class="hljs-string">"Arr"</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
                    <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"item in Arr"</span>></span>
                        &#123;&#123;item&#125;&#125;
                    <span class="hljs-tag"></<span class="hljs-name">li</span>></span>
                <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">slot</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">const</span> cpn = &#123;
        <span class="hljs-attr">template</span>: <span class="hljs-string">"#cpn"</span>,
        <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
            <span class="hljs-keyword">return</span> &#123;
                <span class="hljs-attr">Arr</span>: [<span class="hljs-string">"xiaoming"</span>, <span class="hljs-string">"xiaohong"</span>, <span class="hljs-string">"xiaoguang"</span>]
            &#125;
        &#125;
    &#125;;
    <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
        <span class="hljs-attr">el</span>: <span class="hljs-string">"#app"</span>,


        <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
            <span class="hljs-keyword">return</span> &#123;

            &#125;
        &#125;,
        <span class="hljs-attr">methods</span>: &#123;&#125;,
        <span class="hljs-attr">components</span>: &#123;
            cpn
        &#125;
    &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>关键代码:</p>
<pre><code class="hljs language-html copyable" lang="html">    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">cpn</span>></span><span class="hljs-tag"></<span class="hljs-name">cpn</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">cpn</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">slot-scope</span>=<span class="hljs-string">"slot"</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"item in slot.list"</span>></span>&#123;&#123;item&#125;&#125;*<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">cpn</span>></span>

    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-comment"><!-- 下面是子组件 --></span>
    <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"cpn"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>我是子组件<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">slot</span> <span class="hljs-attr">:list</span>=<span class="hljs-string">"Arr"</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
                    <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"item in Arr"</span>></span>
                        &#123;&#123;item&#125;&#125;
                    <span class="hljs-tag"></<span class="hljs-name">li</span>></span>
                <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">slot</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1f93dbf331174fc9b69835b91de598bd~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</li>
</ul>
<h2 data-id="heading-51">六、webpack</h2></div>  
</div>
            
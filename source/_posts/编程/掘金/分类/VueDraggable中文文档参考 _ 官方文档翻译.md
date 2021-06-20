
---
title: 'Vue.Draggable中文文档参考 _ 官方文档翻译'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://raw.githubusercontent.com/SortableJS/Vue.Draggable/master/example.gif'
author: 掘金
comments: false
date: Fri, 18 Jun 2021 07:22:10 GMT
thumbnail: 'https://raw.githubusercontent.com/SortableJS/Vue.Draggable/master/example.gif'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第18天，活动详情查看：<a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<blockquote>
<p>文档来源于<a href="https://github.com/SortableJS/Vue.Draggable" target="_blank" rel="nofollow noopener noreferrer">官方文档</a>,  因为官网文档为英文文档, 看的吃力, 而且在网上也并未查询到相关中文文档，所以本人使用翻译工具与查阅相关资料进行逐行翻译, 如有不足请指正~</p>
<p>谨作学习使用。</p>
<p>中文翻译的的Github地址: <a href="https://github.com/itmier/Vue.Draggable" target="_blank" rel="nofollow noopener noreferrer">github.com/itmier/Vue.…</a></p>
</blockquote>
<p>Vue组件（Vue.js 2.0）或指令（Vue.js 1.0）允许拖放并与视图模型阵列同步。</p>
<p>基于并提供 <a href="https://github.com/RubaXa/Sortable" target="_blank" rel="nofollow noopener noreferrer">Sortable.js</a> 的所有功能</p>
<h2 data-id="heading-0">适用于Vue 3</h2>
<p>​见  <a href="https://github.com/SortableJS/vue.draggable.next" target="_blank" rel="nofollow noopener noreferrer">vue.draggable.next</a></p>
<h2 data-id="heading-1">示例</h2>
<p><img src="https://raw.githubusercontent.com/SortableJS/Vue.Draggable/master/example.gif" alt="demo gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">浏览Demo</h2>
<p><a href="https://sortablejs.github.io/Vue.Draggable/" target="_blank" rel="nofollow noopener noreferrer">sortablejs.github.io/Vue.Draggab…</a></p>
<p><a href="https://david-desmaisons.github.io/draggable-example/" target="_blank" rel="nofollow noopener noreferrer">david-desmaisons.github.io/draggable-e…</a></p>
<h2 data-id="heading-3">特点</h2>
<ul>
<li>完全支持 Sortable.js 的功能
<ul>
<li>支持触摸设备</li>
<li>支持拖动手柄和可选文本 [选择器???]</li>
<li>智能自动滚动</li>
<li>支持在不同列表之间拖放</li>
<li>没有 JQuery 依赖关系</li>
</ul>
</li>
<li>使HTML与视图模型列表保持同步 [ HTML结构与数据保持同步 ]</li>
<li>兼容 Vue.js 2.0 的 transition-group</li>
<li>支持撤销功能</li>
<li>当需要全面控制时, 报告任何变化的事件 [ 拖放从鼠标按下开始拖拽到鼠标松开拖动结束都有完整的事件监听,可以添加自己的处理 ]</li>
<li>重用现有的UI组件库,如:<a href="https://vuetifyjs.com/" target="_blank" rel="nofollow noopener noreferrer">vuetify</a>, <a href="http://element.eleme.io/" target="_blank" rel="nofollow noopener noreferrer">element</a>, or <a href="https://vuematerial.io/" target="_blank" rel="nofollow noopener noreferrer">vue material</a> 等等, 使用 <code>tag</code> 或者 <code>componentData</code> 属性选项来使他们可以拖动</li>
</ul>
<h2 data-id="heading-4">支持者</h2>
 <a href="https://flatlogic.com/admin-dashboards" target="_blank" rel="nofollow noopener noreferrer">
 <img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f7d169bb5aac4899afa7b53127ff2563~tplv-k3u1fbpfcp-zoom-1.image" loading="lazy" referrerpolicy="no-referrer">
 </a>
<p>Admin Dashboard Templates made with Vue, React and Angular.</p>
<h2 data-id="heading-5">捐赠</h2>
<p>觉得项目有用吗? 你可以请我:coffee: or a :beer:</p>
<p><a href="https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=GYAEKQZJ4FQT2&currency_code=USD&source=url" target="_blank" rel="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2befb85b2af7460cab78b6973d19f9c3~tplv-k3u1fbpfcp-zoom-1.image" alt="paypal" loading="lazy" referrerpolicy="no-referrer"></a></p>
<h2 data-id="heading-6">安装</h2>
<h3 data-id="heading-7">使用 npm 或者 yarn</h3>
<pre><code class="hljs language-bash copyable" lang="bash">yarn add vuedraggable

npm i -S vuedraggable
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注意它是针对Vue 2.0的vuedraggable，而不是针对1.0版本的vue-draggable</strong></p>
<h3 data-id="heading-8">直链</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"//cdnjs.cloudflare.com/ajax/libs/vue/2.5.2/vue.min.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-comment"><!-- CDNJS :: Sortable (https://cdnjs.com/) --></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"//cdn.jsdelivr.net/npm/sortablejs@1.8.4/Sortable.min.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-comment"><!-- CDNJS :: Vue.Draggable (https://cdnjs.com/) --></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"//cdnjs.cloudflare.com/ajax/libs/Vue.Draggable/2.20.0/vuedraggable.umd.min.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://github.com/SortableJS/Vue.Draggable/tree/master/example" target="_blank" rel="nofollow noopener noreferrer">参照实例部分</a></p>
<h2 data-id="heading-9">适用于 Vue.js 2.0</h2>
<p>使用 draggable 组件:</p>
<h3 data-id="heading-10">典型使用:</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">draggable</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"myArray"</span> <span class="hljs-attr">group</span>=<span class="hljs-string">"people"</span> @<span class="hljs-attr">start</span>=<span class="hljs-string">"drag=true"</span> @<span class="hljs-attr">end</span>=<span class="hljs-string">"drag=false"</span>></span>
   <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"element in myArray"</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">"element.id"</span>></span>&#123;&#123;element.name&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">draggable</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>.vue 文件:</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">import</span> draggable <span class="hljs-keyword">from</span> <span class="hljs-string">'vuedraggable'</span>
  ...
  <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
        <span class="hljs-attr">components</span>: &#123;
            draggable,
        &#125;,
  ...
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">使用 <code>transition-group</code>:</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">draggable</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"myArray"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">transition-group</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"element in myArray"</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">"element.id"</span>></span>
            &#123;&#123;element.name&#125;&#125;
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">transition-group</span>></span>
<span class="hljs-tag"></<span class="hljs-name">draggable</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Draggable 组件应该直接包裹 draggable 元素, 或者包裹包含 draggable 元素的 <code>transition-group</code></p>
<h3 data-id="heading-12">使用 footer slot:</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">draggable</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"myArray"</span> <span class="hljs-attr">draggable</span>=<span class="hljs-string">".item"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"element in myArray"</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">"element.id"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>
        &#123;&#123;element.name&#125;&#125;
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"footer"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"addPeople"</span>></span>Add<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"></<span class="hljs-name">draggable</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">使用 header slot:</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">draggable</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"myArray"</span> <span class="hljs-attr">draggable</span>=<span class="hljs-string">".item"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"element in myArray"</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">"element.id"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>
        &#123;&#123;element.name&#125;&#125;
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"header"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"addPeople"</span>></span>Add<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"></<span class="hljs-name">draggable</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">使用 Vuex:</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">draggable</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">'myList'</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript">computed: &#123;
    <span class="hljs-attr">myList</span>: &#123;
        <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span> &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.$store.state.myList
        &#125;,
        <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">value</span>)</span> &#123;
            <span class="hljs-built_in">this</span>.$store.commit(<span class="hljs-string">'updateList'</span>, value)
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">接收属性 Props</h3>
<h4 data-id="heading-16">value</h4>
<p>Type: <code>Array</code><br>
Required: <code>false</code><br>
Default: <code>null</code></p>
<p>draggable component 的输入数组。通常与内部元素 v-for 指令引用的数组相同。<br>这是使用 Vue.draggable 的首选方式，因为它与 Vuex 兼容 。<br>它不应该直接使用， 但可以通过 <code>v-model</code> 指令使用：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">draggable</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"myArray"</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-17">list</h4>
<p>Type: <code>Array</code><br>
Required: <code>false</code><br>
Default: <code>null</code></p>
<p>Alternative to the <code>value</code> prop, list is an array to be synchronized with drag-and-drop.<br></p>
<p>作为 <code>value</code> 属性的替代, list 是一个可以与拖放同步的数组</p>
<p>主要区别在于: <code>list</code> 属性是 draggable component 使用 splice 方法更新的，而 <code>value</code> 是不可变的。</p>
<p><strong>不用与 value prop 同时使用</strong></p>
<h4 data-id="heading-18">All sortable options(所有的 sortable 选项)</h4>
<p>2.19版的新内容</p>
<p>从2.19版开始, Sortable 的选项可直接设置为 vue.draggable 的 属性</p>
<p>这意味着所有的  <a href="https://github.com/RubaXa/Sortable#options" target="_blank" rel="nofollow noopener noreferrer">sortable option</a> 都是有效的 sortable props, 但是有明显的例外:所有以 "on" 开头的方法。因为 draggable component 通过事件暴露了相同的API</p>
<p>支持 kebab-case 属性: 例如 <code>ghost-class</code> 属性将会被转换名为 <code>ghostClass</code> 的 sortable option。</p>
<p>例如设置 handle,sortable 和 group的选项:</p>
<pre><code class="hljs language-HTML copyable" lang="HTML"><span class="hljs-tag"><<span class="hljs-name">draggable</span>
        <span class="hljs-attr">v-model</span>=<span class="hljs-string">"list"</span>
        <span class="hljs-attr">handle</span>=<span class="hljs-string">".handle"</span>
        <span class="hljs-attr">:group</span>=<span class="hljs-string">"&#123; name: 'people', pull: 'clone', put: false &#125;"</span>
        <span class="hljs-attr">ghost-class</span>=<span class="hljs-string">"ghost"</span>
        <span class="hljs-attr">:sort</span>=<span class="hljs-string">"false"</span>
        @<span class="hljs-attr">change</span>=<span class="hljs-string">"log"</span>
      ></span>
      <span class="hljs-comment"><!-- --></span>
<span class="hljs-tag"></<span class="hljs-name">draggable</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-19">tag</h4>
<p>Type: <code>String</code><br>
Default: <code>'div'</code></p>
<p>draggable component 作为包含slot的外部元素创建的HTML节点类型<br></p>
<p>也可以将Vue组件的name作为元素传递,在这种情况下, draggable的属性将被传递给创建组件<br></p>
<p>如果你需要为创建的组件设置props或者event, 请参考 <a href="https://juejin.cn/post/6975153687056351263#componentdata">componentData</a></p>
<h4 data-id="heading-20">clone</h4>
<p>Type: <code>Function</code><br>
Required: <code>false</code><br>
Default: <code>(original) => &#123; return original;&#125;</code><br></p>
<p>当 clone 选项为true时, 在源组件上调用函数来克隆元素。唯一的参数是要克隆的viewModel元素, 返回值是它的克隆版本。<br></p>
<p>默认情况下, vue.draggable 复用了 viewModel元素(的数据), 所有如果你想要去克隆或者深度克隆它,你必须使用这个hook。</p>
<h4 data-id="heading-21">move</h4>
<p>Type: <code>Function</code><br>
Required: <code>false</code><br>
Default: <code>null</code><br></p>
<p>If not null this function will be called in a similar way as <a href="https://github.com/RubaXa/Sortable#move-event-object" target="_blank" rel="nofollow noopener noreferrer">Sortable onMove callback</a>.</p>
<p>如果不为null的话, 那此函数的调用方式与  <a href="https://github.com/RubaXa/Sortable#move-event-object" target="_blank" rel="nofollow noopener noreferrer">Sortable onMove callback</a> 类似。</p>
<p>返回false将取消拖动操作。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">onMoveCallback</span>(<span class="hljs-params">evt, originalEvent</span>)</span>&#123;
   ...
    <span class="hljs-comment">// return false; — for cancel</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>evt 对象有三个与 <a href="https://github.com/RubaXa/Sortable#move-event-object" target="_blank" rel="nofollow noopener noreferrer">Sortable onMove event</a> 相同的属性以及3个附加属性:</p>
<ul>
<li><code>draggedContext</code>:  与被拖动元素相关的上下文
<ul>
<li><code>index</code>: 被拖动元素的索引</li>
<li><code>element</code>: dragged element underlying view model element 被拖动元素的底层视图模型元素 [ 被拖动元素的数据 ]</li>
<li><code>futureIndex</code>:  如果接受(鼠标)放下的操作, (则为)被拖动元素的潜在(未来)索引值</li>
</ul>
</li>
<li><code>relatedContext</code>: 与当前拖动操作相关的上下文
<ul>
<li><code>index</code>: 目标元素的索引</li>
<li><code>element</code>: 目标元素的视图模型元素 [ 目标元素的数据 ]</li>
<li><code>list</code>: 目标(所在的)列表</li>
<li><code>component</code>: target VueComponent    [ Vue组件目标??? ]</li>
</ul>
</li>
</ul>
<p>HTML:</p>
<pre><code class="hljs language-HTML copyable" lang="HTML"><span class="hljs-tag"><<span class="hljs-name">draggable</span> <span class="hljs-attr">:list</span>=<span class="hljs-string">"list"</span> <span class="hljs-attr">:move</span>=<span class="hljs-string">"checkMove"</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>javascript:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">checkMove: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">evt</span>)</span>&#123;
    <span class="hljs-keyword">return</span> (evt.draggedContext.element.name!==<span class="hljs-string">'apple'</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>查看完整演示:  <a href="https://github.com/SortableJS/Vue.Draggable/blob/master/examples/Cancel.html" target="_blank" rel="nofollow noopener noreferrer">Cancel.html</a>, <a href="https://github.com/SortableJS/Vue.Draggable/blob/master/examples/script/cancel.js" target="_blank" rel="nofollow noopener noreferrer">cancel.js</a></p>
<h4 data-id="heading-22">componentData</h4>
<p>Type: <code>Object</code><br>
Required: <code>false</code><br>
Default: <code>null</code><br></p>
<p>这个prop属性用来向被 <a href="https://juejin.cn/post/6975153687056351263#tag">tag props</a> 所声明的子组件传递额外信息<br>
Value:</p>
<ul>
<li><code>props</code>: 传递给子组件的 props</li>
<li><code>attrs</code>: 传递给子组件的 attrs</li>
<li><code>on</code>: 要在子组件中订阅的事件</li>
</ul>
<p>Example(使用 <a href="http://element.eleme.io/#/en-US" target="_blank" rel="nofollow noopener noreferrer">element UI library</a> ):</p>
<pre><code class="hljs language-HTML copyable" lang="HTML"><span class="hljs-tag"><<span class="hljs-name">draggable</span> <span class="hljs-attr">tag</span>=<span class="hljs-string">"el-collapse"</span> <span class="hljs-attr">:list</span>=<span class="hljs-string">"list"</span> <span class="hljs-attr">:component-data</span>=<span class="hljs-string">"getComponentData()"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">el-collapse-item</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"e in list"</span> <span class="hljs-attr">:title</span>=<span class="hljs-string">"e.title"</span> <span class="hljs-attr">:name</span>=<span class="hljs-string">"e.name"</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">"e.name"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;&#123;e.description&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
     <span class="hljs-tag"></<span class="hljs-name">el-collapse-item</span>></span>
<span class="hljs-tag"></<span class="hljs-name">draggable</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript">methods: &#123;
    <span class="hljs-function"><span class="hljs-title">handleChange</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'changed'</span>);
    &#125;,
    <span class="hljs-function"><span class="hljs-title">inputChanged</span>(<span class="hljs-params">value</span>)</span> &#123;
      <span class="hljs-built_in">this</span>.activeNames = value;
    &#125;,
    <span class="hljs-function"><span class="hljs-title">getComponentData</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">on</span>: &#123;
          <span class="hljs-attr">change</span>: <span class="hljs-built_in">this</span>.handleChange,
          <span class="hljs-attr">input</span>: <span class="hljs-built_in">this</span>.inputChanged
        &#125;,
        <span class="hljs-attr">attrs</span>:&#123;
          <span class="hljs-attr">wrap</span>: <span class="hljs-literal">true</span>
        &#125;,
        <span class="hljs-attr">props</span>: &#123;
          <span class="hljs-attr">value</span>: <span class="hljs-built_in">this</span>.activeNames
        &#125;
      &#125;;
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-23">Events</h3>
<ul>
<li>
<p>支持 Sortable 事件:</p>
<p><code>start</code>, <code>add</code>, <code>remove</code>, <code>update</code>, <code>end</code>, <code>choose</code>, <code>unchoose</code>, <code>sort</code>, <code>filter</code>, <code>clone</code><br></p>
<p>由 Sortable.js 使用相同的参数触发 onStart, onAdd, onRemove, onUpdate, onEnd, onChoose, onUnchoose, onSort, onClone 时, 就会调用这些事件。</p>
<p><a href="https://github.com/RubaXa/Sortable#event-object-demo" target="_blank" rel="nofollow noopener noreferrer">阅读此处以供参考</a></p>
<p>Note that SortableJS OnMove callback is mapped with the <a href="https://github.com/SortableJS/Vue.Draggable/blob/master/README.md#move" target="_blank" rel="nofollow noopener noreferrer">move prop</a></p>
<p>注意： SortableJS 的 OnMove 回调是由 <a href="https://juejin.cn/post/6975153687056351263#move">move prop</a> 映射的。</p>
</li>
</ul>
<p>HTML:</p>
<pre><code class="hljs language-HTML copyable" lang="HTML"><span class="hljs-tag"><<span class="hljs-name">draggable</span> <span class="hljs-attr">:list</span>=<span class="hljs-string">"list"</span> @<span class="hljs-attr">end</span>=<span class="hljs-string">"onEnd"</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>change event</p>
<p><code>change</code> event is triggered when list prop is not null and the corresponding array is altered due to drag-and-drop operation.<br></p>
<p>当 list 属性不为 null 并且由于拖放操作而更改了对应的数组, 就会触发 <code>change</code> 事件。</p>
<p>This event is called with one argument containing one of the following properties:</p>
<p>可以使用包含以下属性之一的参数来调用事件：</p>
<ul>
<li><code>added</code>:  包含添加到数组中的元素的信息
<ul>
<li><code>newIndex</code>: 所添加的元素的索引</li>
<li><code>element</code>: 增加的元素</li>
</ul>
</li>
<li><code>removed</code>:  包含从数组中移除的元素的信息
<ul>
<li><code>oldIndex</code>: 移除前元素的索引</li>
<li><code>element</code>: 移除的元素</li>
</ul>
</li>
<li><code>moved</code>:  包含在数组中移动的元素的信息
<ul>
<li><code>newIndex</code>: 被移动元素的当前索引</li>
<li><code>oldIndex</code>: 被移动元素的旧索引</li>
<li><code>element</code>: 被移动的元素</li>
</ul>
</li>
</ul>
</li>
</ul>
<h3 data-id="heading-24">Slots</h3>
<p>限制: header slot 和 footer slot 都不能与 transition-group 一起使用</p>
<h4 data-id="heading-25">Header</h4>
<p>使用 <code>header</code> slot 来向 vuedraggable 组件内添加  none-draggable 元素</p>
<p>重要提示: 它应该与 draggable 选项一起使用来标记 draggable 元素</p>
<p>请注意: header slot 不论它在模板中什么位置, 它都会被加入到默认插槽之前。
Ex:</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">draggable</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"myArray"</span> <span class="hljs-attr">draggable</span>=<span class="hljs-string">".item"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"element in myArray"</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">"element.id"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>
        &#123;&#123;element.name&#125;&#125;
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"header"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"addPeople"</span>></span>Add<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"></<span class="hljs-name">draggable</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-26">Footer</h4>
<p>使用 <code>footer</code> slot 来向vuedraggable 组件内添加 none-draggable 元素</p>
<p>重要提示: 它应该和 draggable 选项一起使用来标记 draggable 元素
请注意: footer slot 不论它在模板中什么位置, 它都会被加入到默认插槽之后。
Ex:</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">draggable</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"myArray"</span> <span class="hljs-attr">draggable</span>=<span class="hljs-string">".item"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"element in myArray"</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">"element.id"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>
        &#123;&#123;element.name&#125;&#125;
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"footer"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"addPeople"</span>></span>Add<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"></<span class="hljs-name">draggable</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-27">Gotchas</h3>
<ul>
<li>Vue.draggable children 应使用 v-for 指令来映射 list 或者 value 属性
<ul>
<li>你可以使用 <a href="https://github.com/SortableJS/Vue.Draggable#header" target="_blank" rel="nofollow noopener noreferrer">header</a> 或者 <a href="https://github.com/SortableJS/Vue.Draggable#footer" target="_blank" rel="nofollow noopener noreferrer">footer</a> slot 来绕过这一限制</li>
</ul>
</li>
<li>v-for中的子元素应该像Vue.js中的任何元素一样被标记. 特别需要注意的是要提供有意义的key值
<ul>
<li>通常情况下提供数组索引值来作为 key 值是不通的, 因为key应该与 items content 相关联</li>
<li>cloned elements should provide updated keys, it is doable using the <a href="https://juejin.cn/post/6975153687056351263#clone">clone props</a> for example</li>
<li>克隆的元素应该提供更新后的key, 例如使用 <a href="https://juejin.cn/post/6975153687056351263#clone">clone props</a> 是能做到的。</li>
</ul>
</li>
</ul>
<h3 data-id="heading-28">Example</h3>
<ul>
<li><a href="https://sortablejs.github.io/Vue.Draggable/#/custom-clone" target="_blank" rel="nofollow noopener noreferrer">Clone</a></li>
<li><a href="https://sortablejs.github.io/Vue.Draggable/#/handle" target="_blank" rel="nofollow noopener noreferrer">Handle</a></li>
<li><a href="https://sortablejs.github.io/Vue.Draggable/#/transition-example-2" target="_blank" rel="nofollow noopener noreferrer">Transition</a></li>
<li><a href="https://sortablejs.github.io/Vue.Draggable/#/nested-example" target="_blank" rel="nofollow noopener noreferrer">Nested</a></li>
<li><a href="https://sortablejs.github.io/Vue.Draggable/#/table-example" target="_blank" rel="nofollow noopener noreferrer">Table</a></li>
</ul>
<h3 data-id="heading-29">Full demo example</h3>
<p><a href="https://github.com/David-Desmaisons/draggable-example" target="_blank" rel="nofollow noopener noreferrer">draggable-example</a></p>
<h2 data-id="heading-30">For Vue.js 1.0</h2>
<p><a href="https://juejin.cn/post/documentation/Vue.draggable.for.ReadME.md">See here</a></p></div>  
</div>
            
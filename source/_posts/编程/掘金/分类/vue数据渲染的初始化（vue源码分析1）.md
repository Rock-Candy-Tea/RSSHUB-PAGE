
---
title: 'vue数据渲染的初始化（vue源码分析1）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5f5ec8bcacb243b588821f4f7cf6edf0~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 30 Aug 2021 18:29:25 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5f5ec8bcacb243b588821f4f7cf6edf0~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>以下代码和分析过程需要结合vue.js源码查看，通过打断点逐一比对。</p>
</blockquote>
<h2 data-id="heading-0">一. 代码</h2>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Title<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
        <span class="hljs-comment"><!--this is comment--></span> &#123;&#123; message &#125;&#125;
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app1"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            <span class="hljs-comment"><!--count=&#123;&#123;count&#125;&#125;--></span>
            <span class="hljs-comment"><!--reversedCount=&#123;&#123;reversedCount&#125;&#125;--></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>

    <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
        <span class="hljs-keyword">debugger</span>;
        <span class="hljs-keyword">var</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
            <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
            <span class="hljs-function"><span class="hljs-title">beforeCreate</span>(<span class="hljs-params"></span>)</span> &#123;&#125;,
            <span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span> &#123;&#125;,
            <span class="hljs-function"><span class="hljs-title">beforeMount</span>(<span class="hljs-params"></span>)</span> &#123;&#125;,
            <span class="hljs-attr">mounted</span>: <span class="hljs-function">() =></span> &#123; <span class="hljs-comment">//挂载元素，获取到DOM节点</span>
                <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
                    <span class="hljs-comment">//this.count+=1;</span>
                    <span class="hljs-comment">//console.log('this.count='+this.count)</span>
                &#125;, <span class="hljs-number">1000</span>)
            &#125;,
            <span class="hljs-function"><span class="hljs-title">beforeUpdate</span>(<span class="hljs-params"></span>)</span> &#123;&#125;,
            <span class="hljs-function"><span class="hljs-title">updated</span>(<span class="hljs-params"></span>)</span> &#123;&#125;,<span class="hljs-comment">//挂载元素，获取到DOM节点</span>
            <span class="hljs-function"><span class="hljs-title">beforeDestroy</span>(<span class="hljs-params"></span>)</span> &#123;&#125;,
            <span class="hljs-function"><span class="hljs-title">destroyed</span>(<span class="hljs-params"></span>)</span> &#123;&#125;,
            <span class="hljs-attr">data</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
                <span class="hljs-keyword">return</span> &#123;
                    <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>,
                    <span class="hljs-attr">message</span>: <span class="hljs-string">'Hello Vue!1111111'</span>
                &#125;
            &#125;,
        &#125;)
        &#125;)
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>

<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">二.执行步骤</h2>
<h3 data-id="heading-2">1. initMixin，初始化vue，挂载_init方法</h3>
<p>执行<code>initMixin(Vue)</code> Vue是一个构造函数。</p>
<p>在Vue原型上挂载一个_init方法，这一步只是挂载方法，并没有执行。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5f5ec8bcacb243b588821f4f7cf6edf0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">2. stateMixin，数据绑定，$watch方法</h3>
<h4 data-id="heading-4">2-1. 执行<code>stateMixin(Vue)</code> Vue是一个构造函数。</h4>
<p>在Vue原型上挂载一个_init方法，这一步只是挂载方法，并没有执行。</p>
<p>定义一个<code>data</code>对象，一个<code>props</code>对象，并分别给这个2个对象添加get和set方法属性.</p>
<h4 data-id="heading-5">2-2. 然后执行<code>Object.defineProperty</code>，通过设定对象属性的 set/get 方法来监听数据的变化，</h4>
<p>通过get进行依赖收集，而每个set方法就是一个观察者，在数据变更的时候通知订阅者更新视图。</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-built_in">Object</span>.defineProperty(Vue.prototype, <span class="hljs-string">'$data'</span>, dataDef); 
 <span class="hljs-built_in">Object</span>.defineProperty(Vue.prototype, <span class="hljs-string">'$props'</span>, propsDef);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时Vue.prototype上只有刚挂载的_init方法</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a515a4cb8d00423dba888a206b263542~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>此时dataDef只有get和set方法</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/807a52de303045688b5db01f7e561522~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Object.defineProperty执行完以后，这时候再看，这时候已经在Vue上挂载了get，set方法和<code>$data和$props</code>属性。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f75a7bcac78409d825f623f48687aa3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-6">2-3 然后执行</h4>
<pre><code class="copyable">  Vue.prototype.$set = set;
  Vue.prototype.$delete = del;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>后面调用的时候我们再看下set和del方法的定义。</p>
<h4 data-id="heading-7">2-4 然后挂载<code>$watch</code></h4>
<p>这个方法我们也后面分析，ok，现在看下Vue挂载了哪些方法：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d3a3d92f0c14c92b0aecbe58d77051e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>stateMixin执行完毕</p>
<h3 data-id="heading-8">3 eventsMixin，初始化事件绑定方法</h3>
<h4 data-id="heading-9">3-1. 依次挂载<code>$on，$once，$off，$emit</code>，方法属性</h4>
<p>这几个方法只是挂载，我们也后面分析</p>
<p>此时Vue挂载了这些属性：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3be9a5d2c00b408aaf50b9421eab1327~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-10">4 lifecycleMixin，初始化  更新 销毁 函数</h3>
<h4 data-id="heading-11">4-1. 依次挂载<code>_update，$forceUpdate，$$destroy</code>，方法属性</h4>
<p>这几个方法只是挂载，我们也后面分析</p>
<ul>
<li>_update在【14. 定义指令章节】</li>
</ul>
<p>此时Vue挂载了这些属性：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0c047797d6b147338bf0c6d6212c6bda~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-12">5 renderMixin，初始化vue 需要渲染的函数</h3>
<h4 data-id="heading-13">5-1. 首先执行 installRenderHelpers</h4>
<pre><code class="copyable">//在Vue的原型上挂载渲染相关的工具函数
installRenderHelpers(Vue.prototype)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>函数的入参就是vue的原型，如图：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/67d35832076540278a1e01c102d438c8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>installRenderHelpers函数执行完后，这时候Vue的原型上多了渲染工具方法属性</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/21a8f9af8ddd42cebdb297638bf527b1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-14">5-1. 接着挂载<code>$nextTick</code>和<code>_render</code></h4>
<ul>
<li>nextTick 延迟回调</li>
<li>_render渲染函数</li>
</ul>
<h3 data-id="heading-15">6 声明一些变量</h3>
<ul>
<li>patternTypes  //类型数组</li>
<li>KeepAlive  //以组件的格式定义内置组件的属性</li>
<li>builtInComponents // 内置保存状态的组件</li>
</ul>
<h3 data-id="heading-16">7 initGlobalAPI(Vue), 初始化全局api 并且暴露 一些静态方法</h3>
<h4 data-id="heading-17">7-1 挂载基础属性</h4>
<p>给配置对象configDef挂载一个get属性，它是一个函数，返回前面的定义的config对象，此时只是挂载，并没执行，因此只有一个get方法。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1224214385574f98a97cb00088de620f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>接着挂载个set方法，提示一些警告。</p>
<p>然后执行</p>
<pre><code class="copyable">/**
 * 在这里，为Vue的构造函数添加一个要通过Object.defineProperty监听的属性config，
 * 将configDef中的set和get方法关联到config上。
 * 获取的时候，拿到的是上面描述的那个config对象，如果对这个config对象直接做变更，
 * 就会提示“不要替换vue.config对象，而是设置单个字段”，说明，
 * vue不希望我们直接去替换和变更整个config对象，如果有需要，希望去直接修改我们需要修改的值
*/
Object.defineProperty(Vue, 'config', configDef);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>接着在<code>Vue构造函数</code>上挂载util，set，delete，nextTick方法，挂载一个空的options。</p>
</li>
<li>
<p>然后遍历指令集合，在<code>Vue.options</code>挂载相应指令，然后设置_base属性值为Vue</p>
</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f33c90dd98384ca18f0d96638d0527fd~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>合并KeepAlive组件到components中</p>
<pre><code class="copyable">extend(Vue.options.components, builtInComponents)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0558870033204e2e9a9814a19df690e4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-18">7-2 initUse</h4>
<blockquote>
<p>初始化vue 安装插件函数</p>
</blockquote>
<p>在Vue上挂载一个use方法。</p>
<h4 data-id="heading-19">7-3 initMixin$1</h4>
<blockquote>
<p>initMixin$1(Vue);  //初始化vue mixin 函数</p>
</blockquote>
<p>在Vue上挂载一个mixin方法, 将传入的mixin（执行时传入的）覆盖到options项上。</p>
<p>在Vue上挂载一个use方法。</p>
<h4 data-id="heading-20">7-4 initExtend</h4>
<blockquote>
<p>initExtend  //初始化vue extend 函数</p>
</blockquote>
<p>在Vue上挂载一个extend方法,</p>
<h4 data-id="heading-21">7-5 initAssetRegisters</h4>
<blockquote>
<p>initAssetRegisters  //为vue 添加 静态方法component，directive，filter</p>
</blockquote>
<p><strong>到此，initGlobalAPI方法执行完毕。</strong></p>
<h3 data-id="heading-22">8. Object.defineProperty响应式一些属性</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//监听是否是服务器环境</span>
    <span class="hljs-built_in">Object</span>.defineProperty(Vue.prototype, <span class="hljs-string">'$isServer'</span>, &#123;
        <span class="hljs-attr">get</span>: isServerRendering <span class="hljs-comment">//判断是不是node 服务器环境</span>
    &#125;);
    <span class="hljs-comment">// 获取$ssrContext</span>
    <span class="hljs-built_in">Object</span>.defineProperty(Vue.prototype, <span class="hljs-string">'$ssrContext'</span>, &#123;
        <span class="hljs-attr">get</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">get</span>(<span class="hljs-params"></span>) </span>&#123;
            <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.$vnode && <span class="hljs-built_in">this</span>.$vnode.ssrContext
        &#125;
    &#125;);

    <span class="hljs-comment">//为ssr运行时帮助程序安装公开FunctionalRenderContext 创建 虚拟dom vonde 渲染 slots插槽</span>
    <span class="hljs-built_in">Object</span>.defineProperty(Vue, <span class="hljs-string">'FunctionalRenderContext'</span>, &#123;
        <span class="hljs-attr">value</span>: FunctionalRenderContext
    &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时观察Vue.prototype：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6ca0ebd68be2416d9b057c01dbed3e31~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-23">9. 设置版本号</h3>
<pre><code class="copyable">Vue.version = '2.5.16'; //版本号
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-24">10. 定义判断属性相关函数</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 以下都是通过makeMap函数返回一个函数，去查找map中是否存在val，存在返回true,否则返回false</span>
isReservedAttr <span class="hljs-comment">// 判断'style,class'</span>
acceptValue    <span class="hljs-comment">// 判断'input,textarea,option,select,progress'</span>
mustUseProp    <span class="hljs-comment">// 判断属性和标签是否匹配</span>
isEnumeratedAttr    <span class="hljs-comment">// 判断'contenteditable（编辑）,draggable（拖动）,spellcheck（拼写）'</span>
isBooleanAttr  <span class="hljs-comment">// 检查是否是html中的布尔值属性（属性值只有 true 和 false）</span>
isXlink        <span class="hljs-comment">// 判断是否是xmlns 属性</span>
getXlinkProp   <span class="hljs-comment">// 获取xml link的属性</span>
isFalsyAttrValue   <span class="hljs-comment">// 判断val 是否是 null 或者 false</span>
<span class="hljs-keyword">var</span> namespaceMap = &#123;
     <span class="hljs-attr">svg</span>: <span class="hljs-string">'http://www.w3.org/2000/svg'</span>, <span class="hljs-comment">//svg标签命名xmlns属性</span>
      <span class="hljs-attr">math</span>: <span class="hljs-string">'http://www.w3.org/1998/Math/MathML'</span> <span class="hljs-comment">//math 中的xmlns属性声明 XHTML 文件</span>
&#125;;
isFalsyAttrValue   <span class="hljs-comment">// 判断val 是否是 html中的原始标签</span>
isSVG              <span class="hljs-comment">// 判断svg 标签 以及 svg子元素标签</span>
isPreTag           <span class="hljs-comment">// 判断标签是否是pre</span>
isReservedTag      <span class="hljs-comment">// 判断是不是 html 原生的标签 或者svg标签</span>
getTagNamespace    <span class="hljs-comment">// 判断 是否是svg 或者 math 标签</span>
unknownElementCache    <span class="hljs-comment">// 判断 是否是svg 或者 math 标签</span>
isTextInputType    <span class="hljs-comment">// 判断 是否是文本输入框 判断属性：text,number,password,search,email,tel,url</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-25">11. nodeOps冻结节点</h3>
<blockquote>
<p>Object.freeze() 方法可以冻结一个对象。</p>
</blockquote>
<ul>
<li>一个被冻结的对象再也不能被修改；</li>
<li>冻结了一个对象则不能向这个对象添加新的属性</li>
<li>不能删除已有属性</li>
<li>不能修改该对象已有属性的可枚举性、可配置性、可写性</li>
<li>以及不能修改已有属性的值。</li>
<li>此外，冻结一个对象后该对象的原型也不能被修改。</li>
<li>freeze() 返回和传入的参数相同的对象。</li>
</ul>
<pre><code class="copyable">var nodeOps = Object.freeze(&#123;
        createElement: createElement$1, //创建一个真实的dom
        createElementNS: createElementNS, //创建一个真实的dom svg方式
        createTextNode: createTextNode, // 创建文本节点
        createComment: createComment,  // 创建一个注释节点
        insertBefore: insertBefore,  //插入节点 在xxx  dom 前面插入一个节点
        removeChild: removeChild,   //删除子节点
        appendChild: appendChild,  //添加子节点 尾部
        parentNode: parentNode,  //获取父亲子节点dom
        nextSibling: nextSibling,     //获取下一个兄弟节点
        tagName: tagName,   //获取dom标签名称
        setTextContent: setTextContent, //  //设置dom 文本
        setStyleScope: setStyleScope  //设置组建样式的作用域
    &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/083dcdefb3ee4faa81a9bc32d727ffab~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>下面逐个分析 对象的每一项</p>
<h4 data-id="heading-26">11-1 createElement$1</h4>
<blockquote>
<p>创建一个真实的dom</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createElement$1</span>(<span class="hljs-params">tagName, vnode</span>) </span>&#123;
        <span class="hljs-comment">//创建一个真实的dom</span>
        <span class="hljs-keyword">var</span> elm = <span class="hljs-built_in">document</span>.createElement(tagName);
        <span class="hljs-comment">//如果不是select标签则返回dom出去, 退出函数</span>
        <span class="hljs-keyword">if</span> (tagName !== <span class="hljs-string">'select'</span>) &#123; 
            <span class="hljs-keyword">return</span> elm
        &#125;
        <span class="hljs-comment">// false or null will remove the attribute but undefined will not</span>
        <span class="hljs-comment">// false或null将删除属性，但undefined不会</span>
        <span class="hljs-comment">// 否则，如果是select标签 判断是否设置了multiple属性。如果设置就重置</span>
        <span class="hljs-keyword">if</span> (vnode.data && vnode.data.attrs && vnode.data.attrs.multiple !== <span class="hljs-literal">undefined</span>) &#123;
            elm.setAttribute(<span class="hljs-string">'multiple'</span>, <span class="hljs-string">'multiple'</span>);
        &#125;
        <span class="hljs-keyword">return</span> elm
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-27">11-2 createElementNS</h4>
<blockquote>
<p>创建一个真实的dom svg方式，<code>document.createElementNS</code>方法可创建带有指定<code>命名空间</code>的元素节点。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-comment">//创建一个真实的dom svg方式</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createElementNS</span>(<span class="hljs-params">namespace, tagName</span>) </span>&#123;
        <span class="hljs-comment">/**  namespaceMap，前面定义值为 &#123;
             svg: 'http://www.w3.org/2000/svg',
             math: 'http://www.w3.org/1998/Math/MathML'
            &#125;;
            例如：document.createElementNS('http://www.w3.org/2000/svg','svg');
        */</span> 
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">document</span>.createElementNS(namespaceMap[namespace], tagName)
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>document.createElementNS用法：</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> c=<span class="hljs-built_in">document</span>.createElementNS(<span class="hljs-string">'http://www.w3.org/2000/svg'</span>,<span class="hljs-string">'svg'</span>) <span class="hljs-comment">//创建svg节点</span>
<span class="hljs-built_in">document</span>.body.appendChild(c);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到这dom中插入了一对svg标签</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4bf1af7ba63f432e97f6c889c79c6490~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-28">11-3 createTextNode</h4>
<blockquote>
<p>创建文本节点</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createTextNode</span>(<span class="hljs-params">text</span>) </span>&#123;
   <span class="hljs-keyword">return</span> <span class="hljs-built_in">document</span>.createTextNode(text)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-29">11-4 createComment</h4>
<blockquote>
<p>创建注释节点</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createTextNode</span>(<span class="hljs-params">text</span>) </span>&#123;
   <span class="hljs-keyword">return</span> <span class="hljs-built_in">document</span>.createTextNode(text)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>document.createComment用法：</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> c=<span class="hljs-built_in">document</span>.createComment(<span class="hljs-string">"My personal comments"</span>); <span class="hljs-comment">// 创建注释</span>
<span class="hljs-built_in">document</span>.body.appendChild(c); <span class="hljs-comment">//插入节点</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到这dom中插入了一条注释</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6a52060cfaf84f078ff37695824617aa~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-30">11-5 insertBefore</h4>
<blockquote>
<p>在父节点的某个子节点前插入一个新的节点</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">insertBefore</span>(<span class="hljs-params">parentNode, newNode, referenceNode</span>) </span>&#123;
        parentNode.insertBefore(newNode, referenceNode);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>insertBefore用法：</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
node.insertBefore(newnode,existingnode) 方法可在已有的子节点前插入一个新的子节点。
node: 被插入的父节点。
newnode: 必须。要插入的节点对象
existingnode必须。要添加新的节点前的子节点。
例如：
*/</span>
<ul id=<span class="hljs-string">"List"</span>>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">li</span>></span>上海<span class="hljs-tag"></<span class="hljs-name">li</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">li</span>></span>深圳<span class="hljs-tag"></<span class="hljs-name">li</span>></span></span>
</ul>
<span class="hljs-keyword">var</span> newCity = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">"li"</span>)  <span class="hljs-comment">//创建元素</span>
<span class="hljs-keyword">var</span> textnode = <span class="hljs-built_in">document</span>.createTextNode(<span class="hljs-string">"北京"</span>) <span class="hljs-comment">// 创建元素</span>
newCity.appendChild(textnode)  <span class="hljs-comment">// 添加文本</span>
<span class="hljs-keyword">var</span> list = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"List"</span>)
<span class="hljs-comment">// 在父节点ul的第一个节点li前添加一个newCity节点</span>
list.insertBefore(newCity,list.childNodes[<span class="hljs-number">0</span>]);

执行完后：
<ul id=<span class="hljs-string">"List"</span>>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">li</span>></span>北京<span class="hljs-tag"></<span class="hljs-name">li</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">li</span>></span>上海<span class="hljs-tag"></<span class="hljs-name">li</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">li</span>></span>深圳<span class="hljs-tag"></<span class="hljs-name">li</span>></span></span>
</ul>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-31">11-6 其它节点操作</h4>
<p>剩下的比较简单，就放一起讲了</p>
<pre><code class="copyable">    //删除子节点
    function removeChild(node, child) &#123;
        node.removeChild(child);
    &#125;

    //添加子节点 尾部
    function appendChild(node, child) &#123;
        node.appendChild(child);
    &#125;

    //获取父亲子节点dom
    function parentNode(node) &#123;
        return node.parentNode
    &#125;

    //获取下一个兄弟节点
    function nextSibling(node) &#123;
        return node.nextSibling
    &#125;

    //获取dom标签名称
    function tagName(node) &#123;
        return node.tagName
    &#125;

    //设置dom 文本
    function setTextContent(node, text) &#123;
        node.textContent = text;
    &#125;


    //设置组建样式的作用域,设置后只在当前组件生效
    function setStyleScope(node, scopeId) &#123;
        node.setAttribute(scopeId, '');
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到这里，nodeOps冻结节点就讲完了</p>
<h3 data-id="heading-32">12. 定义ref 创建 更新 和 销毁 事件</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> ref = &#123;
        <span class="hljs-attr">create</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">create</span>(<span class="hljs-params">_, vnode</span>) </span>&#123;
            <span class="hljs-comment">//创建注册一个ref</span>
            registerRef(vnode);
        &#125;,
        <span class="hljs-attr">update</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">update</span>(<span class="hljs-params">oldVnode, vnode</span>) </span>&#123;
            <span class="hljs-comment">//更新ref</span>
            <span class="hljs-keyword">if</span> (oldVnode.data.ref !== vnode.data.ref) &#123;

                registerRef(oldVnode, <span class="hljs-literal">true</span>); <span class="hljs-comment">//先删除</span>
                registerRef(vnode);  <span class="hljs-comment">//在添加</span>
            &#125;
        &#125;,
        <span class="hljs-attr">destroy</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">destroy</span>(<span class="hljs-params">vnode</span>) </span>&#123;
            registerRef(vnode, <span class="hljs-literal">true</span>); <span class="hljs-comment">//删除销毁ref</span>
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-33">12-1. create</h4>
<blockquote>
<p>ref 被用来给<code>元素或子组件</code>注册引用信息。引用信息将会注册在<code>父组件</code>的 <code>$refs</code> 对象上。如果在普通的 DOM 元素上使用，引用指向的就是 DOM 元素；如果用在子组件上，引用就指向组件实例。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
     * 注册ref或者删除ref。比如标签上面设置了ref='abc' 
     * 那么该函数就是为this.$refs.abc 注册ref 把真实的dom存进去
     */</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">registerRef</span>(<span class="hljs-params">
        vnode, <span class="hljs-comment">// 虚拟dom对象</span>
        isRemoval <span class="hljs-comment">// 是否销毁ref</span>
    </span>) </span>&#123;
        <span class="hljs-keyword">debugger</span>
        <span class="hljs-keyword">var</span> key = vnode.data.ref;  <span class="hljs-comment">//获取vnode ref的字符串</span>
        <span class="hljs-keyword">if</span> (!isDef(key)) &#123;  <span class="hljs-comment">//没有定义则退出函数,可以看下面的解析</span>
            <span class="hljs-keyword">return</span>
        &#125;
        <span class="hljs-keyword">var</span> vm = vnode.context; <span class="hljs-comment">//context 上下文</span>
        <span class="hljs-comment">//优先获取vonde的组件实例(对于组件来说)，或者el(该Vnode对应的DOM节点，非组件来说)</span>
        <span class="hljs-keyword">var</span> ref = vnode.componentInstance || vnode.elm; 
        <span class="hljs-keyword">var</span> refs = vm.$refs;
        <span class="hljs-comment">// 如果需要销毁ref</span>
        <span class="hljs-keyword">if</span> (isRemoval) &#123;
            <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(refs[key])) &#123;
                remove(refs[key], ref); 
            &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (refs[key] === ref) &#123; 
                refs[key] = <span class="hljs-literal">undefined</span>;  
            &#125;
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-keyword">if</span> (vnode.data.refInFor) &#123;  <span class="hljs-comment">//当在v-for之内时，则保存为数组形式</span>
                <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">Array</span>.isArray(refs[key])) &#123; <span class="hljs-comment">//refs[key] 不是数组 则变成一个数组</span>
                    refs[key] = [ref];
                &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (refs[key].indexOf(ref) < <span class="hljs-number">0</span>) &#123; <span class="hljs-comment">//如果ref 不存在 refs的时候则添加进去</span>
                    <span class="hljs-comment">// $flow-disable-line</span>
                    refs[key].push(ref);
                &#125;
            &#125; <span class="hljs-keyword">else</span> &#123;
                refs[key] = ref; <span class="hljs-comment">//如果是单个直接赋值</span>
            &#125;
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>isDef:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//判断数据是否定义（注意！值为0或者false也是定义过了的）</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isDef</span>(<span class="hljs-params">v</span>) </span>&#123;
    <span class="hljs-keyword">return</span> v !== <span class="hljs-literal">undefined</span> && v !== <span class="hljs-literal">null</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-34">12-2. update</h4>
<pre><code class="hljs language-js copyable" lang="js">update: <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">update</span>(<span class="hljs-params">oldVnode, vnode</span>) </span>&#123;
            <span class="hljs-comment">//如果新旧ref不一致，执行更新ref的操作</span>
            <span class="hljs-keyword">if</span> (oldVnode.data.ref !== vnode.data.ref) &#123;
                registerRef(oldVnode, <span class="hljs-literal">true</span>); <span class="hljs-comment">//先删除</span>
                registerRef(vnode);  <span class="hljs-comment">//在添加</span>
            &#125;
        &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-35">12-3. destroy</h4>
<pre><code class="hljs language-js copyable" lang="js">destroy: <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">destroy</span>(<span class="hljs-params">vnode</span>) </span>&#123;
            <span class="hljs-comment">//删除销毁ref</span>
            registerRef(vnode, <span class="hljs-literal">true</span>); 
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-36">13. 定义空vnode(emptyNode)和hooks</h3>
<p>先看下vnode有哪些属性：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/536704fb7a564399a11fc6f5237dfbb5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">// 定义一些声明周期相关的hooks
var hooks = ['create', 'activate', 'update', 'remove', 'destroy'];
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-37">14. 定义指令</h3>
<pre><code class="copyable">var directives = &#123;
        create: updateDirectives, //创建指令
        update: updateDirectives,  //更新指令
        destroy: function unbindDirectives(vnode) &#123;  //销毁指令
            updateDirectives(vnode, emptyNode);
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这三个属性其实用到的是同一个函数，updateDirectives</p>
<pre><code class="copyable">//更新指令
    function updateDirectives(
        oldVnode, //oldVnode 老数据
        vnode     //vnode 新数据 
        ) &#123;
        // 只要新旧指令存在，就更新
        if (oldVnode.data.directives || vnode.data.directives) &#123;
            _update(oldVnode, vnode);
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着分析<code>_update</code>函数，这个函数比较长，我们细细分析</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-comment">/**
     * 更新指令 比较oldVnode和vnode，根据oldVnode和vnode的情况 
     * 触发指令钩子函数bind，update，inserted，insert，componentUpdated，unbind钩子函数
     */</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_update</span>(<span class="hljs-params">
        oldVnode, <span class="hljs-comment">//oldVnode 老数据</span>
        vnode     <span class="hljs-comment">//vnode 新数据 </span>
    </span>) </span>&#123;
        <span class="hljs-comment">// 如果旧节点是空节点，就表示当前操作为创建,首次创建</span>
        <span class="hljs-keyword">var</span> isCreate = oldVnode === emptyNode;
        <span class="hljs-comment">//如果新节点是空节点，就表示当前操作为销毁</span>
        <span class="hljs-keyword">var</span> isDestroy = vnode === emptyNode;
        <span class="hljs-comment">//规范化的指令，为指令属性修正变成规范的指令数据。返回指令数据集合</span>
        <span class="hljs-comment">// 这个方法请看下面的解析</span>
        <span class="hljs-keyword">var</span> oldDirs = normalizeDirectives$<span class="hljs-number">1</span>(
            oldVnode.data.directives, <span class="hljs-comment">//vonde指令对象集合</span>
            oldVnode.context <span class="hljs-comment">//vm vne实例化对象，或者是组件实例化的对象</span>
        );
        <span class="hljs-comment">//规范化的指令，为指令属性修正变成规范的指令数据。返回指令数据集合</span>
        <span class="hljs-keyword">var</span> newDirs = normalizeDirectives$<span class="hljs-number">1</span>(
            vnode.data.directives, <span class="hljs-comment">//vonde指令对象集合</span>
            vnode.context <span class="hljs-comment">//vm vne实例化对象，或者是组件实例化的对象</span>
        );

        <span class="hljs-keyword">var</span> dirsWithInsert = []; <span class="hljs-comment">// 触发inserted指令钩子函数的指令列表。</span>
        <span class="hljs-keyword">var</span> dirsWithPostpatch = []; <span class="hljs-comment">// 触发componentUpdated钩子函数的指令列表。</span>

        <span class="hljs-keyword">var</span> key, oldDir, dir;
        <span class="hljs-keyword">for</span> (key <span class="hljs-keyword">in</span> newDirs) &#123;      <span class="hljs-comment">//循环新的指令集合</span>
            oldDir = oldDirs[key];  <span class="hljs-comment">//获取旧的单个指令值</span>
            dir = newDirs[key];     <span class="hljs-comment">//获取新的单个指令值</span>

            <span class="hljs-keyword">if</span> (!oldDir) &#123; <span class="hljs-comment">//新增指令，触发bind</span>
                <span class="hljs-comment">// new directive, bind 新指令,绑定</span>
                callHook$<span class="hljs-number">1</span>(  <span class="hljs-comment">//例：v-focus指令的bind函数</span>
                    dir, <span class="hljs-comment">//新的指令值</span>
                    <span class="hljs-string">'bind'</span>, <span class="hljs-comment">//触发bind钩子函数</span>
                    vnode,<span class="hljs-comment">//新的vonde</span>
                    oldVnode <span class="hljs-comment">//旧的vonde</span>
                );
                <span class="hljs-keyword">if</span> (dir.def && dir.def.inserted) &#123;
                    <span class="hljs-comment">// 如果有插入指令，加入列表</span>
                    dirsWithInsert.push(dir); 
                &#125;
            &#125; <span class="hljs-keyword">else</span> &#123;
                <span class="hljs-comment">// 指令已存在触发update</span>
                <span class="hljs-comment">// existing directive, update 现有的指令,更新</span>
                <span class="hljs-comment">// 如有指令 <div v-hello='123'></div> value=123. 如果更新了123 就是更新值</span>
                dir.oldValue = oldDir.value; 
                callHook$<span class="hljs-number">1</span>(
                    dir,
                    <span class="hljs-string">'update'</span>,  <span class="hljs-comment">//触发更新钩子函数</span>
                    vnode,
                    oldVnode
                );
                 <span class="hljs-comment">// 如果有更新指令，加入列表</span>
                <span class="hljs-keyword">if</span> (dir.def && dir.def.componentUpdated) &#123; 
                    dirsWithPostpatch.push(dir);
                &#125;
            &#125;
        &#125;

        <span class="hljs-comment">// 此时完成bind和update钩子函数，列表更新完成</span>

        <span class="hljs-keyword">if</span> (dirsWithInsert.length) &#123;
            <span class="hljs-comment">// 定义一个函数，该函数会执行dirsWithInsert里的每个函数</span>
            <span class="hljs-keyword">var</span> callInsert = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
                <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < dirsWithInsert.length; i++) &#123;
                    callHook$<span class="hljs-number">1</span>(
                        dirsWithInsert[i], <span class="hljs-comment">//新的指令值 也就是上面的dir（新的单个指令值）</span>
                        <span class="hljs-string">'inserted'</span>, <span class="hljs-comment">//触发inserted钩子函数</span>
                        vnode, <span class="hljs-comment">//新的vonde</span>
                        oldVnode <span class="hljs-comment">//旧的vonde</span>
                    );
                &#125;
            &#125;;
            <span class="hljs-keyword">if</span> (isCreate) &#123;
                <span class="hljs-comment">//如果是初始化  </span>
                mergeVNodeHook(
                    vnode,
                    <span class="hljs-string">'insert'</span>,<span class="hljs-comment">//合并钩子函数</span>
                    callInsert
                );
            &#125; <span class="hljs-keyword">else</span> &#123;
                callInsert();
            &#125;
        &#125;

        <span class="hljs-keyword">if</span> (dirsWithPostpatch.length) &#123;
            mergeVNodeHook(vnode,
                <span class="hljs-string">'postpatch'</span>,
                <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
                    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < dirsWithPostpatch.length; i++) &#123;
                        callHook$<span class="hljs-number">1</span>(
                            dirsWithPostpatch[i],
                            <span class="hljs-string">'componentUpdated'</span>,
                            vnode, oldVnode);
                    &#125;
                &#125;);
        &#125;

        <span class="hljs-keyword">if</span> (!isCreate) &#123;
            <span class="hljs-keyword">for</span> (key <span class="hljs-keyword">in</span> oldDirs) &#123;
                <span class="hljs-keyword">if</span> (!newDirs[key]) &#123; <span class="hljs-comment">//新的vonde 中没有了指令</span>
                    <span class="hljs-comment">// no longer present, unbind 不再存在，解除束缚</span>
                    callHook$<span class="hljs-number">1</span>(
                        oldDirs[key],
                        <span class="hljs-string">'unbind'</span>, <span class="hljs-comment">//触发unbind 钩子</span>
                        oldVnode,
                        oldVnode,
                    );
                &#125;
            &#125;
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着分析<code>normalizeDirectives$1</code>，它修正指令属性变成规范的指令数据，返回指令数据集合</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">normalizeDirectives$1</span>(<span class="hljs-params">
        dirs, <span class="hljs-comment">//vonde 指令集合</span>
        vm <span class="hljs-comment">//vm vne实例化对象，或者是组件实例化的对象</span>
    </span>) </span>&#123;
        <span class="hljs-comment">//创建一个空的对象</span>
        <span class="hljs-keyword">var</span> res = <span class="hljs-built_in">Object</span>.create(<span class="hljs-literal">null</span>);
        <span class="hljs-comment">//如果 指令 名称dirs 不存在 则返回一个空的对象</span>
        <span class="hljs-keyword">if</span> (!dirs) &#123;
            <span class="hljs-comment">// $flow-disable-line</span>
            <span class="hljs-keyword">return</span> res
        &#125;

        <span class="hljs-keyword">var</span> i, dir;
        <span class="hljs-keyword">for</span> (i = <span class="hljs-number">0</span>; i < dirs.length; i++) &#123; <span class="hljs-comment">//循环遍历指令集合</span>
            dir = dirs[i];
            <span class="hljs-keyword">if</span> (!dir.modifiers) &#123; <span class="hljs-comment">//判断是否有修饰符</span>
                <span class="hljs-comment">// $flow-disable-line</span>
                dir.modifiers = emptyModifiers; <span class="hljs-comment">//空对象</span>
            &#125;
            <span class="hljs-comment">//返回指令名称 或者属性name名称+修饰符</span>
            res[getRawDirName(dir)] = dir;
            <span class="hljs-comment">/**
            *给当前指令挂载自定义指令属性，该属性由用户自定义如 
            *bind，inserted，update，componentUpdated，unbind这些
            */</span>
            dir.def = resolveAsset(vm.$options, <span class="hljs-string">'directives'</span>, dir.name, <span class="hljs-literal">true</span>);
        &#125;
        <span class="hljs-comment">// $flow-disable-line</span>
        <span class="hljs-keyword">return</span> res
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着看getRawDirName函数，返回指令名称 或者属性name名称+修饰符</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getRawDirName</span>(<span class="hljs-params">dir</span>) </span>&#123;
        <span class="hljs-comment">//rawName 视图中的 指令如 <div v-hello></div>  就是v-hello</span>
        <span class="hljs-comment">//name 视图中的 指令如 <div v-hello></div>  就是hello</span>
        <span class="hljs-comment">//name 视图中的 指令如有修饰符 <div v-hello.native></div>  就是hello.native</span>
        <span class="hljs-comment">//modifiers 修饰符</span>
        <span class="hljs-keyword">return</span> dir.rawName || ((dir.name) + <span class="hljs-string">"."</span> + (<span class="hljs-built_in">Object</span>.keys(dir.modifiers || &#123;&#125;).join(<span class="hljs-string">'.'</span>)))
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时<code>res[getRawDirName(dir)] = dir</code>，已经将指令名作为res的属性了，并且将指令作为属性值。</p>
<p>接着检测指令是否在 组件对象上面 ,返回注册指令或者组建的对象</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">resolveAsset</span>(<span class="hljs-params">
        options, <span class="hljs-comment">//参数 例：vm.$options</span>
        type, <span class="hljs-comment">// 类型 例：'directives' ， 'filters' ，'components'</span>
        id,   <span class="hljs-comment">// 指令，组件的key 属性  例：dir.name</span>
        warnMissing <span class="hljs-comment">//开启警告的信息 例：true</span>
    </span>) </span>&#123;
        <span class="hljs-comment">/* istanbul ignore if  如果id不是字符串，退出函数 */</span>
        <span class="hljs-comment">// 返回逻辑【1】</span>
        <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> id !== <span class="hljs-string">'string'</span>) &#123;
            <span class="hljs-keyword">return</span>
        &#125;
        <span class="hljs-keyword">var</span> assets = options[type]; <span class="hljs-comment">// 例： vm.$options['components']</span>
        <span class="hljs-comment">// check local registration variations first</span>
        <span class="hljs-comment">/**
         * 首先检查本地注册的变化 判断id(组件等的name)是否是assets自有属性
         * 否则判断将id驼峰后的key，是否是assets自有属性
         * 否则判断将id驼峰后，再首字母变大写的key，是否是assets自有属性
         */</span>
        <span class="hljs-comment">// 例：判断v-modal 指令，在不在options['directives']中</span>
        <span class="hljs-comment">// 例：判断my-header 组件，在不在options['components']中</span>
        <span class="hljs-comment">/**
         * 所以，我们在Vue引入某个组件时候,我们可以在template写组件标签用驼峰的方式，
         * 也可以是首字母大写，或是直接用组件名来当作组件的标签，就是因为这里做了这样的扩展处理
         */</span>

        <span class="hljs-comment">// 执行返回逻辑【2】</span>
        <span class="hljs-keyword">if</span> (hasOwn(assets, id)) &#123;
            <span class="hljs-keyword">return</span> assets[id]
        &#125;

        <span class="hljs-comment">//  可以让这样的的属性 v-model 变成 vModel  变成驼峰</span>
        <span class="hljs-keyword">var</span> camelizedId = camelize(id);
        <span class="hljs-comment">// 执行返回逻辑【3】</span>
        <span class="hljs-keyword">if</span> (hasOwn(assets, camelizedId)) &#123;
            <span class="hljs-keyword">return</span> assets[camelizedId]
        &#125;

        <span class="hljs-comment">// 将首字母变成大写 即 vModel 变成 VModel</span>
        <span class="hljs-keyword">var</span> PascalCaseId = capitalize(camelizedId);
        <span class="hljs-comment">// 执行返回逻辑【4】</span>
        <span class="hljs-keyword">if</span> (hasOwn(assets, PascalCaseId)) &#123;
            <span class="hljs-keyword">return</span> assets[PascalCaseId]
        &#125;

        <span class="hljs-comment">// fallback to prototype chain  回到原型链</span>
        <span class="hljs-keyword">var</span> res = assets[id] || assets[camelizedId] || assets[PascalCaseId];
        <span class="hljs-comment">// 如果以上都不成立且是开发环境则警告</span>
        <span class="hljs-keyword">if</span> (<span class="hljs-string">"development"</span> !== <span class="hljs-string">'production'</span> && warnMissing && !res) &#123;
            warn(
                <span class="hljs-string">'Failed to resolve '</span> + type.slice(<span class="hljs-number">0</span>, -<span class="hljs-number">1</span>) + <span class="hljs-string">': '</span> + id,
                options
            );
        &#125;
        <span class="hljs-comment">//返回注册指令或者组建的对象(原型上的)</span>
        <span class="hljs-keyword">return</span> res
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里有到工具函数hasOwn:</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-comment">/**
     * Check whether the object has the property.
     *检查对象属性是在自身上还是原型上，在自身上返回true
     */</span>
    <span class="hljs-keyword">var</span> hasOwnProperty = <span class="hljs-built_in">Object</span>.prototype.hasOwnProperty;

    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">hasOwn</span>(<span class="hljs-params">obj, key</span>) </span>&#123;
        <span class="hljs-keyword">return</span> hasOwnProperty.call(obj, key)
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着将我们的指令name变成驼峰的写法,camelize:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
     把横线-的转换成驼峰写法
     这个正则可以让这样的的属性 v-model 变成 vModel
     把名称格式为“xx-xx”的变为“xxXx”，这里接收的是当前的props属性值，一个字符串
     */</span>
    <span class="hljs-keyword">var</span> camelizeRE = <span class="hljs-regexp">/-(\w)/g</span>;
    <span class="hljs-keyword">var</span> camelize = cached(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">str</span>) </span>&#123;
        <span class="hljs-keyword">return</span> str.replace(camelizeRE, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">_, c</span>) </span>&#123;
            <span class="hljs-comment">/**
             * var str="Hello World!"
               str.toUpperCase() //HELLO WORLD! 将小写转为大写
             */</span>
            <span class="hljs-keyword">return</span> c ? c.toUpperCase() : <span class="hljs-string">''</span>;
        &#125;)
    &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着看下cached函数:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 它将我们需要调用的一些函数给封装到一个对象里面，需要的时候就去对象取</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">cached</span>(<span class="hljs-params">fn</span>) </span>&#123;
        <span class="hljs-keyword">var</span> cache = <span class="hljs-built_in">Object</span>.create(<span class="hljs-literal">null</span>); <span class="hljs-comment">//这样创建的没有原型的空对象 </span>
        <span class="hljs-keyword">return</span> (<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">cachedFn</span>(<span class="hljs-params">str</span>) </span>&#123;
            <span class="hljs-keyword">var</span> hit = cache[str];
            <span class="hljs-keyword">return</span> hit || (cache[str] = fn(str))
        &#125;)
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为了更直接观的查看<code>camelize</code>函数，我们就将<code>cached</code>引入过来，再回到我们前面的<code>camelizeRE</code>函数，是不是清晰了很多：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> camelizeRE = <span class="hljs-regexp">/-(\w)/g</span>;
    <span class="hljs-keyword">var</span> camelize = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">var</span> cache = <span class="hljs-built_in">Object</span>.create(<span class="hljs-literal">null</span>); <span class="hljs-comment">//这样创建的没有原型的空对象 </span>
        <span class="hljs-comment">// 这个str就是某些属性的key，如id，v-modal</span>
        <span class="hljs-comment">// 也就是说，会先去缓存对象cache中判断有没有存在，id属性对应的函数，有就返回，没有的就设置</span>
        <span class="hljs-keyword">return</span> (<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">cachedFn</span>(<span class="hljs-params">str</span>) </span>&#123;
            <span class="hljs-keyword">var</span> hit = cache[str];
            <span class="hljs-keyword">return</span> hit
            || (cache[str] =  str.replace(camelizeRE, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">_, c</span>) </span>&#123; <span class="hljs-comment">//后面这一块就是cached的入参fn</span>
                <span class="hljs-keyword">return</span> c ? c.toUpperCase() : <span class="hljs-string">''</span>;
            &#125;)(str))
        &#125;)
        
    &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ok，此时我们已经分析完<code>camelize</code>函数了，现在<code>resolveAsset</code>已经分析完了，拿到了指令集合。<code>normalizeDirectives$1</code>也执行完了，指令属性修正变成规范的指令数据.</p>
<p>接着回到我们的<code>_update</code>函数,新旧的指令集合我们都拿到了：</p>
<p>这时，我们遍历新旧指令集合，这里面又涉及到几个工具函数，我们依次分析</p>
<p><strong>_update->callHook$1</strong></p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-comment">//触发指令钩子函数</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">callHook$1</span>(<span class="hljs-params">
        dir,  <span class="hljs-comment">//新的指令值</span>
        hook, <span class="hljs-comment">//钩子函数 例：bind</span>
        vnode, <span class="hljs-comment">//新的vnode</span>
        oldVnode, <span class="hljs-comment">//旧的vnode</span>
        isDestroy  <span class="hljs-comment">// 是否销毁  例：true</span>
    </span>) </span>&#123;
        <span class="hljs-keyword">var</span> fn = dir.def && dir.def[hook]; <span class="hljs-comment">//获取属性上面的钩子函数</span>
        <span class="hljs-keyword">if</span> (fn) &#123;
            <span class="hljs-keyword">try</span> &#123;
                fn(
                    vnode.elm, <span class="hljs-comment">//真实dom</span>
                    dir, <span class="hljs-comment">//新的指令值</span>
                    vnode, <span class="hljs-comment">//新的vond</span>
                    oldVnode, <span class="hljs-comment">//旧的vonde</span>
                    isDestroy <span class="hljs-comment">//是否要销毁标记</span>
                );
            &#125; <span class="hljs-keyword">catch</span> (e) &#123;
                handleError(e, vnode.context, (<span class="hljs-string">"directive "</span> + (dir.name) + <span class="hljs-string">" "</span> + hook + <span class="hljs-string">" hook"</span>));
            &#125;
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>_update->mergeVNodeHook</strong>，合并vue vnode 钩子函数</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-comment">/*
     *  钩子函数的作用是把insert作为一个hooks属性保存到对应的Vnode的data上面，
        当该Vnode插入到父节点后会调用该hooks
     *  def[hookKey] = invoker; //把钩子函数用对象存起来
     * */</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mergeVNodeHook</span>(<span class="hljs-params">
        def,  <span class="hljs-comment">// vnode</span>
        hookKey,  <span class="hljs-comment">// 函数指令 例: 'insert'</span>
        hook <span class="hljs-comment">// 回调函数 例：callInsert()</span>
        </span>) </span>&#123;
        <span class="hljs-comment">// 则将它重置为VNode.data.hook，如果VNode.data.hook不存在</span>
        <span class="hljs-comment">// 则初始化为一个空对象 注:普通节点VNode.data.hook是不存在的。</span>
        <span class="hljs-keyword">if</span> (def <span class="hljs-keyword">instanceof</span> VNode) &#123;
            def = def.data.hook || (def.data.hook = &#123;&#125;);
        &#125;

        <span class="hljs-keyword">var</span> invoker;
        <span class="hljs-comment">//获取旧的oldHook 钩子</span>
        <span class="hljs-keyword">var</span> oldHook = def[hookKey];

        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">wrappedHook</span>(<span class="hljs-params"></span>) </span>&#123;
            <span class="hljs-comment">//回调，执行钩子函数</span>
            hook.apply(<span class="hljs-built_in">this</span>, <span class="hljs-built_in">arguments</span>);
            <span class="hljs-comment">// important: remove merged hook to ensure it's called only once</span>
            <span class="hljs-comment">// and prevent memory leak</span>
            <span class="hljs-comment">// 重要：删除合并钩子以确保只调用一次</span>
            <span class="hljs-comment">// 和防止内存泄漏</span>
            <span class="hljs-comment">// 这个函数不解析了，太简单，删除invoker.fns数组中的wrappedHook项</span>
            remove(invoker.fns, wrappedHook);
        &#125;

        <span class="hljs-comment">//如果旧的钩子函数没有 为空的时候，则创建一个钩子函数</span>
        <span class="hljs-keyword">if</span> (isUndef(oldHook)) &#123; 
            <span class="hljs-comment">// no existing hook</span>
            invoker = createFnInvoker([wrappedHook]);
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-comment">// istanbul ignore if  </span>
            <span class="hljs-comment">// 如果有老的钩子函数，并且fns钩子函数存在 并且已经合并过</span>
            <span class="hljs-keyword">if</span> (isDef(oldHook.fns) && isTrue(oldHook.merged)) &#123;
                <span class="hljs-comment">// already a merged invoker 已合并的调用程序</span>
                invoker = oldHook; <span class="hljs-comment">//直接老的钩子函数直接覆盖新的钩子函数</span>
                <span class="hljs-comment">//为钩子函数的fns 添加一个函数</span>
                invoker.fns.push(wrappedHook);
            &#125; <span class="hljs-keyword">else</span> &#123;
                <span class="hljs-comment">// existing plain hook</span>
                invoker = createFnInvoker([oldHook, wrappedHook]);
            &#125;
        &#125;

        invoker.merged = <span class="hljs-literal">true</span>;
        <span class="hljs-comment">//把钩子函数用对象存起来</span>
        def[hookKey] = invoker;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>_update->mergeVNodeHook->createFnInvoker</strong>，创建一个钩子函数</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-comment">// 如果事件只是个函数就为为事件添加多一个静态类， invoker.fns = fns; 把真正的事件放在fns。</span>
    <span class="hljs-comment">// 而 invoker 则是转义fns然后再运行fns</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createFnInvoker</span>(<span class="hljs-params">
        fns <span class="hljs-comment">// 传入参数可能是数组/函数，数组项是函数 例：invoker = createFnInvoker([wrappedHook]);</span>
        </span>) </span>&#123;
        <span class="hljs-comment">// 先看后面的赋值，再看这个函数定义</span>
        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">invoker</span>(<span class="hljs-params"></span>) </span>&#123;
            <span class="hljs-keyword">var</span> arguments$<span class="hljs-number">1</span> = <span class="hljs-built_in">arguments</span>;

            <span class="hljs-comment">//静态方法传进来的函数 赋值给fns</span>
            <span class="hljs-keyword">var</span> fns = invoker.fns;

            <span class="hljs-comment">//判断fns 是否是一个数组</span>
            <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(fns)) &#123;
                <span class="hljs-comment">//如果是数组 浅拷贝</span>
                <span class="hljs-keyword">var</span> cloned = fns.slice();
                <span class="hljs-comment">//执行fns 数组中的函数 并且把 invoker  arguments$1参数一个个传给fns 函数中</span>
                <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < cloned.length; i++) &#123;

                    cloned[i].apply(<span class="hljs-literal">null</span>, arguments$<span class="hljs-number">1</span>);
                &#125;
            &#125; <span class="hljs-keyword">else</span> &#123;
                <span class="hljs-comment">// return handler return value for single handlers</span>
                <span class="hljs-comment">//如果fns只是一个函数 则执行arguments$1参数一个个传给fns 函数中</span>
                <span class="hljs-keyword">return</span> fns.apply(<span class="hljs-literal">null</span>, <span class="hljs-built_in">arguments</span>)
            &#125;
        &#125;
        <span class="hljs-comment">// 挂载传入的函数数组到invoker的fns属性上</span>
        invoker.fns = fns;
        <span class="hljs-keyword">return</span> invoker  <span class="hljs-comment">//静态类</span>
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再回到<code>_update</code>函数，我们已经分析完了这个函数了,它实现了更新新旧节点指令和执行钩子函数。
回推回去，<code>directives</code>也分析完了,指令章节也分析完了。</p>
<h3 data-id="heading-38">15. 定义一些指令，属性的全局对象</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//定义一个空的指令修饰对象</span>
<span class="hljs-keyword">var</span> emptyModifiers = <span class="hljs-built_in">Object</span>.create(<span class="hljs-literal">null</span>);
<span class="hljs-keyword">var</span> baseModules = [
        ref,  <span class="hljs-comment">//创建，更新 ，销毁 函数 详细查看章节：【12. 定义ref】</span>
        directives <span class="hljs-comment">//自定义指令 创建 ，更新，销毁函数 详细查看章节：【14. 定义指令】</span>
]
<span class="hljs-comment">// 属性相关</span>
<span class="hljs-keyword">var</span> attrs = &#123;
    <span class="hljs-attr">create</span>: updateAttrs, <span class="hljs-comment">//创建属性</span>
    <span class="hljs-attr">update</span>: updateAttrs  <span class="hljs-comment">//更新属性</span>
&#125;
<span class="hljs-comment">// 类相关</span>
<span class="hljs-keyword">var</span> klass = &#123;
        <span class="hljs-attr">create</span>: updateClass,
        <span class="hljs-attr">update</span>: updateClass
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>15-1</strong>：现在分析下：<strong>attrs=》updateAttrs</strong>，更新属性，比较新的vnode和旧的oldVnode中的属性值</p>
<ul>
<li>如果不相等则设置属性；</li>
<li>如果新的vnode 属性中没有了则删除该属性</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateAttrs</span>(<span class="hljs-params">oldVnode, vnode</span>) </span>&#123;
        <span class="hljs-keyword">debugger</span>
        <span class="hljs-keyword">var</span> opts = vnode.componentOptions;  <span class="hljs-comment">//获取组件的拓展参数</span>
        <span class="hljs-comment">// 退出函数</span>
        <span class="hljs-keyword">if</span> (isDef(opts) && opts.Ctor.options.inheritAttrs === <span class="hljs-literal">false</span>) &#123; 
            <span class="hljs-keyword">return</span>
        &#125;
        <span class="hljs-comment">// 退出函数</span>
        <span class="hljs-keyword">if</span> (isUndef(oldVnode.data.attrs) && isUndef(vnode.data.attrs)) &#123;
            <span class="hljs-keyword">return</span>
        &#125;
        <span class="hljs-keyword">var</span> key, cur, old;
        <span class="hljs-keyword">var</span> elm = vnode.elm;
        <span class="hljs-keyword">var</span> oldAttrs = oldVnode.data.attrs || &#123;&#125;;  <span class="hljs-comment">// 旧属性</span>
        <span class="hljs-keyword">var</span> attrs = vnode.data.attrs || &#123;&#125;; <span class="hljs-comment">// 新属性</span>
        <span class="hljs-comment">// clone observed objects, as the user probably wants to mutate it</span>
        <span class="hljs-comment">// 克隆观察到的对象，因为用户可能希望对其进行变种</span>

        <span class="hljs-keyword">if</span> (isDef(attrs.__ob__)) &#123;  <span class="hljs-comment">//重新克隆一个</span>
            attrs = vnode.data.attrs = extend(&#123;&#125;, attrs);
        &#125;

        <span class="hljs-comment">// 如果不相等则设置属性</span>
        <span class="hljs-keyword">for</span> (key <span class="hljs-keyword">in</span> attrs) &#123; 
            cur = attrs[key];  <span class="hljs-comment">// 新属性值</span>
            old = oldAttrs[key]; <span class="hljs-comment">// 旧属性值</span>
            <span class="hljs-keyword">if</span> (old !== cur) &#123; 
                <span class="hljs-comment">//设置属性</span>
                setAttr(elm, key, cur);
            &#125;
        &#125;
        <span class="hljs-comment">// #4391: in IE9, setting type can reset value for input[type=radio] </span>
        <span class="hljs-comment">// #6666: IE/Edge forces progress value down to 1 before setting a max </span>
        <span class="hljs-comment">/* istanbul ignore if */</span>
        <span class="hljs-comment">// 在IE9中，设置类型可以重置输入值[type=radio]</span>
        <span class="hljs-comment">// 在设置最大值之前，IE/Edge会将进度值降低到1</span>

        <span class="hljs-comment">// 如果是ie浏览器，或者是edge浏览器 新的值和旧的值不相等的时候</span>
        <span class="hljs-keyword">if</span> ((isIE || isEdge) && attrs.value !== oldAttrs.value) &#123; 
            setAttr(elm, <span class="hljs-string">'value'</span>, attrs.value); <span class="hljs-comment">//设置新的value值</span>
        &#125;

        <span class="hljs-comment">// 如果旧的属性不在新的属性中，说明要删除</span>
        <span class="hljs-keyword">for</span> (key <span class="hljs-keyword">in</span> oldAttrs) &#123; 
            <span class="hljs-keyword">if</span> (isUndef(attrs[key])) &#123;
                <span class="hljs-keyword">if</span> (isXlink(key)) &#123; <span class="hljs-comment">//判断是否是xml</span>
                    elm.removeAttributeNS(xlinkNS, getXlinkProp(key)); <span class="hljs-comment">//设置属性</span>
                &#125;<span class="hljs-comment">//如果不是 'contenteditable,draggable,spellcheck' 属性</span>
                <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (!isEnumeratedAttr(key)) &#123; 
                    elm.removeAttribute(key); <span class="hljs-comment">//设置属性</span>
                &#125;
            &#125;
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在分析下：<strong>attrs=》updateAttrs=>setAttr</strong>, 设置属性</p>
<pre><code class="copyable">    function setAttr(
        el, // vnode.elm
        key, // 属性key 例： 'value'
        value // 新属性值
        ) &#123;
        //如果dom 标签名 含有'-' 则是自定义标签
        if (el.tagName.indexOf('-') > -1) &#123;
            //设置属性
            baseSetAttr(el, key, value);
        &#125; 
        // 检查是否是html中的布尔值属性  就是该属性只有 true 和 false
        // 详细查看：【10. 定义判断属性相关函数】
        else if (isBooleanAttr(key)) &#123; 
            // set attribute for blank value 为空值设置属性
            // e.g. <option disabled>Select one</option>
            if (isFalsyAttrValue(value)) &#123; 
                el.removeAttribute(key);
            &#125; else &#123;
                // technically allowfullscreen is a boolean attribute for <iframe>
                // but Flash expects a value of "true" when used on <embed> tag 
                // 从技术上讲，allowfullscreen是一个布尔属性
                // 但是Flash希望在<embed>标签上使用时，其值为"true"
                value = key === 'allowfullscreen' && el.tagName === 'EMBED'
                    ? 'true'
                    : key;
                el.setAttribute(key, value);
            &#125;
        &#125; else if 
        // 判断是否是contenteditable，draggable，spellcheck 这三个属性的其中一个
        // 详细查看：【10. 定义判断属性相关函数】
        (isEnumeratedAttr(key)) &#123; 
            el.setAttribute(key, isFalsyAttrValue(value) || value === 'false' ? 'false' : 'true');
        &#125; else if 
        // 判断是否是xmlns 属性 例： <bookstore xmlns:xlink="http://www.w3.org/1999/xlink">
        (isXlink(key)) &#123;   
            if (isFalsyAttrValue(value)) &#123; //value 没有值
                //xml 则用个方法删除属性
                el.removeAttributeNS(xlinkNS, getXlinkProp(key));
            &#125; else &#123;
                //设置xml 属性
                el.setAttributeNS(xlinkNS, key, value);
            &#125;
        &#125; else &#123;
            //设置基本属性
            baseSetAttr(el, key, value);
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在分析下：<strong>attrs=》updateAttrs=>setAttr=>baseSetAttr</strong>， 设置属性,做一些边界处理</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">baseSetAttr</span>(<span class="hljs-params">
        el,   <span class="hljs-comment">// dom节点</span>
        key,  <span class="hljs-comment">// 属性的 key</span>
        value <span class="hljs-comment">// 属性的值</span>
    </span>) </span>&#123;
        <span class="hljs-comment">// 判断val 是否是 【null,undefined,false】中的一个</span>
        <span class="hljs-keyword">if</span> (isFalsyAttrValue(value)) &#123;
            el.removeAttribute(key);  <span class="hljs-comment">//从dom中删除属性</span>
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-comment">// #7138: IE10 & 11 fires input event when setting placeholder on IE10和11在设置占位符时触发输入事件</span>
            <span class="hljs-comment">// <textarea>... block the first input event and remove the blocker 阻塞第一个输入事件并删除该阻塞程序</span>
            <span class="hljs-comment">// immediately.</span>
            <span class="hljs-comment">/* istanbul ignore if */</span>
            <span class="hljs-keyword">if</span> (
                isIE &&  <span class="hljs-comment">//如果是is</span>
                !isIE9 &&  <span class="hljs-comment">//如果不是ie9  不支持ie9</span>
                el.tagName === <span class="hljs-string">'TEXTAREA'</span> &&  <span class="hljs-comment">//如果标签是TEXTAREA(textarea)</span>
                key === <span class="hljs-string">'placeholder'</span> && 
                !el.__ieph
            ) &#123;
                <span class="hljs-keyword">var</span> blocker = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">e</span>) </span>&#123;
                    <span class="hljs-comment">/**
                     * 如果有多个相同类型事件的事件监听函数绑定到同一个元素，当该类型的事件触发时，
                     * 它们会按照被添加的顺序执行。如果其中某个监听函数执行了 event.stopImmediatePropagation() 方法，
                     * 则当前元素剩下的监听函数将不会被执行。
                     */</span>
                    <span class="hljs-comment">// stopImmediatePropagation 则是阻止事件冒泡</span>
                    e.stopImmediatePropagation();
                    <span class="hljs-comment">//删除input 事件</span>
                    el.removeEventListener(<span class="hljs-string">'input'</span>, blocker);
                &#125;;
                <span class="hljs-comment">//添加新的input 事件</span>
                el.addEventListener(<span class="hljs-string">'input'</span>, blocker);
                <span class="hljs-comment">// $flow-disable-line</span>
                <span class="hljs-comment">//标志已经添加过 或者更新过input事件</span>
                el.__ieph = <span class="hljs-literal">true</span>;
                <span class="hljs-comment">/* IE placeholder patched  占位符打补丁 */</span>
            &#125;
            <span class="hljs-comment">//设置属性</span>
            el.setAttribute(key, value);
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>设置属性更新<code>updateAttrs</code>分析完成，</p>
<p><strong>15-2</strong>：现在分析下：<strong>klass=》updateClass</strong>，更新属性，更新 真实dom的  calss</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateClass</span>(<span class="hljs-params">oldVnode, vnode</span>) </span>&#123;
        <span class="hljs-keyword">var</span> el = vnode.elm;  <span class="hljs-comment">//获取【新】的 dom节点</span>
        <span class="hljs-keyword">var</span> data = vnode.data; <span class="hljs-comment">//获取【新】的 vnode数据</span>
        <span class="hljs-keyword">var</span> oldData = oldVnode.data; <span class="hljs-comment">//获取【旧的】oldVnode 数据</span>
        <span class="hljs-comment">// 边界处理，【可不看】</span>
        <span class="hljs-keyword">if</span> (
            isUndef(data.staticClass) && <span class="hljs-comment">//如果没有定义静态的 staticClass</span>
            isUndef(data.class) && <span class="hljs-comment">//没有定义calss</span>
            (
                isUndef(oldData) ||
                (
                    isUndef(oldData.staticClass) && isUndef(oldData.class)
                )
            )
        ) &#123;
            <span class="hljs-comment">// 退出函数</span>
            <span class="hljs-keyword">return</span>
        &#125;
        <span class="hljs-comment">//class 转码获取vonde 中的staticClass 静态class  和class动态class转义成真实dom需要的class格式。然后返回class字符串</span>

        <span class="hljs-keyword">var</span> cls = genClassForVnode(vnode);

        <span class="hljs-comment">// handle transition classes</span>
        <span class="hljs-comment">// 处理转换类</span>
        <span class="hljs-keyword">var</span> transitionClass = el._transitionClasses;
        <span class="hljs-keyword">if</span> (isDef(transitionClass)) &#123;
            cls = concat(cls, stringifyClass(transitionClass));
        &#125;

        <span class="hljs-comment">// set the class _prevClass 上一个css表示是否已经更新过</span>
        <span class="hljs-keyword">if</span> (cls !== el._prevClass) &#123;
            el.setAttribute(<span class="hljs-string">'class'</span>, cls);
            el._prevClass = cls;
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>klass=》updateClass=》genClassForVnode</strong>，将class 转码，获取vonde 中的<code>staticClass</code>（静态class）  和<code>class</code>（动态class），转义成真实dom需要的class格式，然后返回class字符串：</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">genClassForVnode</span>(<span class="hljs-params">vnode</span>) </span>&#123;
        <span class="hljs-keyword">var</span> data = vnode.data;  <span class="hljs-comment">//获取vnode.data 数据 标签属性数据</span>
        <span class="hljs-keyword">var</span> parentNode = vnode; <span class="hljs-comment">//获取 父节点</span>
        <span class="hljs-keyword">var</span> childNode = vnode; <span class="hljs-comment">//获取子节点</span>

        <span class="hljs-keyword">while</span> (isDef(childNode.componentInstance)) &#123; 
            <span class="hljs-comment">// 如果定义了componentInstance（组件实例），递归合并子组件的class</span>
            childNode = childNode.componentInstance._vnode; <span class="hljs-comment">//上一个vnode</span>
            <span class="hljs-keyword">if</span> (childNode && childNode.data) &#123;
                data = mergeClassData(childNode.data, data);
            &#125;
        &#125;
        <span class="hljs-keyword">while</span> (isDef(parentNode = parentNode.parent)) &#123; <span class="hljs-comment">//递归父组件parent 合并父组件class</span>
            <span class="hljs-keyword">if</span> (parentNode && parentNode.data) &#123;
                <span class="hljs-comment">//合并calss数据</span>
                data = mergeClassData(data, parentNode.data);
            &#125;
        &#125;
        <span class="hljs-keyword">return</span> renderClass(data.staticClass, data.class) <span class="hljs-comment">//渲染calss</span>
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>klass=》updateClass=》genClassForVnode=》mergeClassData</strong>，合并calss数据</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mergeClassData</span>(<span class="hljs-params">child, parent</span>) </span>&#123;
        <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">staticClass</span>: concat(child.staticClass, parent.staticClass), <span class="hljs-comment">//静态calss</span>
            <span class="hljs-attr">class</span>: isDef(child.class)  <span class="hljs-comment">//data中动态calss</span>
                ? [child.class, parent.class]
                : parent.class
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>klass=》updateClass=》genClassForVnode=》renderClass</strong>，渲染calss 这里获取到已经转码的calss</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mergeClassData</span>(<span class="hljs-params">child, parent</span>) </span>&#123;
        <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">staticClass</span>: concat(child.staticClass, parent.staticClass), <span class="hljs-comment">//静态calss</span>
            <span class="hljs-attr">class</span>: isDef(child.class)  <span class="hljs-comment">//data中动态calss</span>
                ? [child.class, parent.class]
                : parent.class
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>klass=》updateClass=》genClassForVnode=》renderClass=》stringifyClass</strong>，转码 class，把数组格式，对象格式的calss 全部转化成 字符串格式</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">stringifyClass</span>(<span class="hljs-params">value</span>) </span>&#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(value)) &#123; <span class="hljs-comment">//如果是数组</span>
            <span class="hljs-comment">// 数组变成字符串，然后用空格 隔开 拼接 起来变成字符串</span>
            <span class="hljs-comment">// 本质是递归调用，数组的每一项调用stringifyClass</span>
            <span class="hljs-keyword">return</span> stringifyArray(value)
        &#125;
        <span class="hljs-keyword">if</span> (isObject(value)) &#123;
            <span class="hljs-keyword">return</span> stringifyObject(value)
        &#125;
        <span class="hljs-comment">//直到全部转成 字符串才结束递归</span>
        <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> value === <span class="hljs-string">'string'</span>) &#123;
            <span class="hljs-keyword">return</span> value
        &#125;
        <span class="hljs-comment">/* istanbul ignore next */</span>
        <span class="hljs-keyword">return</span> <span class="hljs-string">''</span>
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>klass=》updateClass=》genClassForVnode=》renderClass=》stringifyClass=>stringifyArray</strong>，  数组变成字符串，然后用空格 隔开 拼接 起来变成字符串</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">stringifyArray</span>(<span class="hljs-params">value</span>) </span>&#123;
        <span class="hljs-keyword">var</span> res = <span class="hljs-string">''</span>;
        <span class="hljs-keyword">var</span> stringified;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>, l = value.length; i < l; i++) &#123;
            <span class="hljs-comment">// 如果value[i]的类型都没有命中，则stringifyClass返回''，即stringified为''，则不进行拼接</span>
            <span class="hljs-keyword">if</span> (isDef(stringified = stringifyClass(value[i])) && stringified !== <span class="hljs-string">''</span>) &#123;
                <span class="hljs-keyword">if</span> (res) &#123;
                    res += <span class="hljs-string">' '</span>;
                &#125;
                res += stringified;
            &#125;
        &#125;
        <span class="hljs-keyword">return</span> res
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>klass=》updateClass=》genClassForVnode=》renderClass=》stringifyClass=>stringifyObject</strong>，对象字符串变成字符串，然后用空格 隔开 拼接 起来变成字符串</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">stringifyObject</span>(<span class="hljs-params">value</span>) </span>&#123;
        <span class="hljs-keyword">var</span> res = <span class="hljs-string">''</span>;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> key <span class="hljs-keyword">in</span> value) &#123;
            <span class="hljs-keyword">if</span> (value[key]) &#123;
                <span class="hljs-keyword">if</span> (res) &#123;
                    res += <span class="hljs-string">' '</span>;
                &#125;
                res += key;
            &#125;
        &#125;
        <span class="hljs-keyword">return</span> res
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>stringifyClass分析完成，renderClass执行完毕（拿到了转码后的class），genClassForVnode（拿到转义成真实dom需要的class格式）也执行完毕，updateClass（拿到了真实dom的  calss）</p>
<h3 data-id="heading-39">16. 定义更新dom事件</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> events = &#123;
    <span class="hljs-attr">create</span>: updateDOMListeners,
    <span class="hljs-attr">update</span>: updateDOMListeners
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>16-1. updateDOMListeners</strong>,更新dom事件</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateDOMListeners</span>(<span class="hljs-params">oldVnode, vnode</span>) </span>&#123;
        <span class="hljs-comment">// 边界处理</span>
        <span class="hljs-keyword">if</span> (isUndef(oldVnode.data.on) && isUndef(vnode.data.on)) &#123;
            <span class="hljs-keyword">return</span>
        &#125;
        <span class="hljs-keyword">var</span> on = vnode.data.on || &#123;&#125;;
        <span class="hljs-keyword">var</span> oldOn = oldVnode.data.on || &#123;&#125;;
        target$<span class="hljs-number">1</span> = vnode.elm; <span class="hljs-comment">//真实的dom</span>
        normalizeEvents(on);    <span class="hljs-comment">//为事件 多添加 change 或者input 事件加进去</span>
        <span class="hljs-comment">// 更新数据源 并且为新的值 添加函数 旧的值删除函数等功能</span>
        updateListeners(
            on, <span class="hljs-comment">//新的事件对象</span>
            oldOn, <span class="hljs-comment">//旧的事件对象</span>
            add$<span class="hljs-number">1</span>, <span class="hljs-comment">//添加真实dom的事件函数</span>
            remove$<span class="hljs-number">2</span>, <span class="hljs-comment">//删除真实dom的事件函数</span>
            vnode.context <span class="hljs-comment">//vue 实例化的对象 new Vue 或者组件 构造函数实例化的对象</span>
        );
        target$<span class="hljs-number">1</span> = <span class="hljs-literal">undefined</span>;
    &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>16-1. updateDOMListeners=>normalizeEvents</strong>,为事件 多添加 change 或者input 事件加进去，<code>可不关注</code></p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">normalizeEvents</span>(<span class="hljs-params">on</span>) </span>&#123;
        <span class="hljs-comment">/* istanbul ignore if */</span>
        <span class="hljs-keyword">if</span> (isDef(on[RANGE_TOKEN])) &#123;
            <span class="hljs-comment">// IE input[type=range] only supports `change` event</span>
            <span class="hljs-comment">// 判断是否是ie 浏览器，如果是则选择 change 事件，如果不是则选择input事件</span>
            <span class="hljs-keyword">var</span> event = isIE ? <span class="hljs-string">'change'</span> : <span class="hljs-string">'input'</span>;  
            <span class="hljs-comment">// 连接事件 把change或者input 事件添加进去</span>
            on[event] = [].concat(on[RANGE_TOKEN], on[event] || []); 
            <span class="hljs-keyword">delete</span> on[RANGE_TOKEN]; <span class="hljs-comment">//删除旧的事件</span>
        &#125;
        <span class="hljs-comment">// This was originally intended to fix #4521 but no longer necessary</span>
        <span class="hljs-comment">// after 2.5. Keeping it for backwards compat with generated code from < 2.4</span>
        <span class="hljs-comment">/* istanbul ignore if */</span>
        <span class="hljs-comment">//最初的目的是修复#4521，但现在已经没有必要了</span>
        <span class="hljs-comment">// 2.5之后。保留它以便与< 2.4生成的代码进行反向比较</span>
        <span class="hljs-comment">//添加change事件</span>
        <span class="hljs-keyword">if</span> (isDef(on[CHECKBOX_RADIO_TOKEN])) &#123;

            on.change = [].concat(on[CHECKBOX_RADIO_TOKEN], on.change || []);
            <span class="hljs-keyword">delete</span> on[CHECKBOX_RADIO_TOKEN];
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>16-1. updateDOMListeners=>updateListeners</strong>,更新数据源 并且为新的值 添加函数 旧的值删除函数等功能</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateListeners</span>(<span class="hljs-params">
        on,  <span class="hljs-comment">//新的事件</span>
        oldOn, <span class="hljs-comment">//旧的事件</span>
        add,  <span class="hljs-comment">//添加事件函数</span>
        remove$$<span class="hljs-number">1</span>, <span class="hljs-comment">//删除事件函数</span>
        vm<span class="hljs-comment">//vue 实例化对象</span>
    </span>) </span>&#123;
        <span class="hljs-keyword">var</span> name, def, cur, old, event;

        <span class="hljs-keyword">for</span> (name <span class="hljs-keyword">in</span> on) &#123;
            def = cur = on[name];  <span class="hljs-comment">//on 新的事件值</span>
            old = oldOn[name];  <span class="hljs-comment">// 旧的值</span>
            event = normalizeEvent(name);   <span class="hljs-comment">//normalizeEvent 如果是事件，则过滤 事件修饰符</span>

            <span class="hljs-comment">/* istanbul ignore if */</span>
            <span class="hljs-comment">// isUndef 值是空的 undefined || null</span>
            <span class="hljs-keyword">if</span> (isUndef(cur)) &#123;
                <span class="hljs-comment">//如果不是生产环境</span>
                <span class="hljs-string">"development"</span> !== <span class="hljs-string">'production'</span> && warn(
                    <span class="hljs-string">"Invalid handler for event \""</span> + (event.name) + <span class="hljs-string">"\": got "</span> + <span class="hljs-built_in">String</span>(cur),
                    vm
                );
            &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isUndef(old)) &#123;

                <span class="hljs-keyword">if</span> (isUndef(cur.fns)) &#123; <span class="hljs-comment">//如果函数不存在 则绑定函数</span>
                    <span class="hljs-comment">//函数 获取钩子函数</span>
                    <span class="hljs-comment">// 创建函数调用器并重新复制给cur和on[name]</span>
                    cur = on[name] = createFnInvoker(cur); <span class="hljs-comment">//这个时候cur.fns就存在了</span>
                &#125;



                name = <span class="hljs-string">'&'</span> + name; <span class="hljs-comment">// mark the event as passive 将事件标记为被动的</span>
                <span class="hljs-comment">//添加事件</span>
                add(
                    event.name, <span class="hljs-comment">//事件名称</span>
                    cur, <span class="hljs-comment">// 转义过的事件 执行静态类</span>
                    event.once, <span class="hljs-comment">//是否只触发一次的状态</span>
                    event.capture, <span class="hljs-comment">//  事件俘获或是冒泡行为</span>
                    event.passive, <span class="hljs-comment">// 检测事件修饰符 是否是   '&'</span>
                    event.params <span class="hljs-comment">//事件参数</span>
                );

            &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (cur !== old) &#123;
                <span class="hljs-comment">//如果新的值不等于旧的值</span>
                <span class="hljs-comment">//则更新新旧值</span>
                old.fns = cur;
                on[name] = old;
            &#125;
        &#125;
        <span class="hljs-keyword">for</span> (name <span class="hljs-keyword">in</span> oldOn) &#123;
            <span class="hljs-comment">//循环旧的值 为空的时候</span>
            <span class="hljs-keyword">if</span> (isUndef(on[name])) &#123;
                <span class="hljs-comment">//获取事件</span>
                event = normalizeEvent(name);
                <span class="hljs-comment">//删除旧的值的事件</span>
                remove$$1(event.name, oldOn[name], event.capture);
            &#125;
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>updateDOMListeners分析完成。</p>
<h3 data-id="heading-40">17. updateDOMProps更新真实dom的props属性</h3>
<pre><code class="copyable">var domProps = &#123;
        create: updateDOMProps, //更新真实dom的props 属性值
        update: updateDOMProps
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>17-1. updateDOMProps</strong>,更新真实dom的props属性</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateDOMProps</span>(<span class="hljs-params">oldVnode, vnode</span>) </span>&#123;

        <span class="hljs-keyword">if</span> (isUndef(oldVnode.data.domProps) && isUndef(vnode.data.domProps)) &#123;
            <span class="hljs-keyword">return</span>
        &#125;
        <span class="hljs-keyword">var</span> key, cur;
        <span class="hljs-keyword">var</span> elm = vnode.elm;
        <span class="hljs-keyword">var</span> oldProps = oldVnode.data.domProps || &#123;&#125;; <span class="hljs-comment">//获取旧的props属性</span>
        <span class="hljs-keyword">var</span> props = vnode.data.domProps || &#123;&#125;; <span class="hljs-comment">//获取新的props</span>
        <span class="hljs-comment">// clone observed objects, as the user probably wants to mutate it</span>
        <span class="hljs-comment">// 克隆观察到的对象，因为用户可能希望对其进行修改</span>
        <span class="hljs-comment">// 如果是props添加了观察者，重新克隆他，这样就可以修改了</span>
        <span class="hljs-keyword">if</span> (isDef(props.__ob__)) &#123; 
            props = vnode.data.domProps = extend(&#123;&#125;, props);
        &#125;

        <span class="hljs-keyword">for</span> (key <span class="hljs-keyword">in</span> oldProps) &#123;
            <span class="hljs-keyword">if</span> (isUndef(props[key])) &#123;
                elm[key] = <span class="hljs-string">''</span>;
            &#125;
        &#125;
        <span class="hljs-keyword">for</span> (key <span class="hljs-keyword">in</span> props) &#123;
            cur = props[key]; 
            <span class="hljs-comment">// ignore children if the node has textContent or innerHTML,</span>
            <span class="hljs-comment">// as these will throw away existing DOM nodes and cause removal errors</span>
            <span class="hljs-comment">// on subsequent patches (#3360)</span>
            <span class="hljs-comment">//忽略子节点，如果节点有textContent或innerHTML，</span>
            <span class="hljs-comment">//因为这将丢弃现有的DOM节点并导致删除错误</span>
            <span class="hljs-comment">//其后的修补程式(#3360)</span>
            <span class="hljs-keyword">if</span> (
                key === <span class="hljs-string">'textContent'</span> ||
                key === <span class="hljs-string">'innerHTML'</span>
            ) &#123;
                <span class="hljs-keyword">if</span> (vnode.children) &#123;
                    vnode.children.length = <span class="hljs-number">0</span>;
                &#125;
                <span class="hljs-keyword">if</span> (cur === oldProps[key]) &#123;
                    <span class="hljs-keyword">continue</span>
                &#125;
                <span class="hljs-comment">// #6601 work around Chrome version <= 55 bug where single textNode</span>
                <span class="hljs-comment">// replaced by innerHTML/textContent retains its parentNode property</span>
                <span class="hljs-comment">// #6601解决Chrome版本<= 55的bug，其中只有一个textNode</span>
                <span class="hljs-comment">//被innerHTML/textContent替换后，保留了它的parentNode属性</span>
                <span class="hljs-keyword">if</span> (elm.childNodes.length === <span class="hljs-number">1</span>) &#123; <span class="hljs-comment">//文本节点</span>
                    elm.removeChild(elm.childNodes[<span class="hljs-number">0</span>]);
                &#125;
            &#125;

            <span class="hljs-keyword">if</span> (key === <span class="hljs-string">'value'</span>) &#123;
                <span class="hljs-comment">// store value as _value as well since</span>
                <span class="hljs-comment">// non-string values will be stringified</span>
                <span class="hljs-comment">//将value存储为_value以及since</span>
                <span class="hljs-comment">//非字符串值将被字符串化</span>
                elm._value = cur;
                <span class="hljs-comment">// avoid resetting cursor position when value is the same</span>
                <span class="hljs-comment">// 当值相同时，避免重置光标位置</span>
                <span class="hljs-keyword">var</span> strCur = isUndef(cur) ? <span class="hljs-string">''</span> : <span class="hljs-built_in">String</span>(cur); <span class="hljs-comment">//转义成字符串</span>
                <span class="hljs-keyword">if</span> (shouldUpdateValue(
                    elm,   <span class="hljs-comment">//真实的dom</span>
                    strCur <span class="hljs-comment">//value</span>
                )) &#123;
                    elm.value = strCur; <span class="hljs-comment">//赋值</span>
                &#125;
            &#125; <span class="hljs-keyword">else</span> &#123;
                elm[key] = cur; <span class="hljs-comment">//直接赋值</span>
            &#125;
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-41">18. style 字符串 格式化为对象</h3>
<p>把<code>style 字符串</code> 转换成<code>对象</code> 比如<code>'width:100px;height:200px;'</code> 转化成 <code>&#123;width:100px,height:200px&#125;</code></p>
<pre><code class="copyable">    var parseStyleText = cached(function (cssText) &#123;
        var res = &#123;&#125;;
        //匹配字符串中的 ;符号。但是不属于 (;)的 符号 如果是括号中的;不能匹配出来
        var listDelimiter = /;(?![^(]*\))/g; 
        var propertyDelimiter = /:(.+)/;  //:+任何字符串
        cssText.split(listDelimiter).forEach(function (item) &#123;
            if (item) &#123;
                var tmp = item.split(propertyDelimiter);
                tmp.length > 1 && (res[tmp[0].trim()] = tmp[1].trim());
            &#125;
        &#125;);
        return res
    &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-42">19. 设置属性和样式</h3>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-keyword">var</span> cssVarRE = <span class="hljs-regexp">/^--/</span>; <span class="hljs-comment">//开始以 --开始</span>
    <span class="hljs-keyword">var</span> importantRE = <span class="hljs-regexp">/\s*!important$/</span>; <span class="hljs-comment">//以!important 结束</span>

    <span class="hljs-keyword">var</span> setProp = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">el, name, val</span>) </span>&#123;
        <span class="hljs-comment">//object.setProperty(propertyname, value, priority)</span>
        <span class="hljs-comment">// propertyname必需。一个字符串，表示创建或修改的属性。</span>
        <span class="hljs-comment">// value可选，新的属性值。</span>
        <span class="hljs-comment">// priority可选。字符串，规定是否需要设置属性的优先级 important。</span>
        <span class="hljs-comment">// 可以是下面三个值:"important"，undefined，""</span>
        <span class="hljs-comment">/* istanbul ignore if */</span>
        <span class="hljs-keyword">if</span> (cssVarRE.test(name)) &#123; <span class="hljs-comment">//开始以 --开始</span>
            el.style.setProperty(name, val); <span class="hljs-comment">//设置真实dom样式</span>
        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (importantRE.test(val)) &#123; <span class="hljs-comment">//以!important 结束</span>
            el.style.setProperty(
                name,
                val.replace(importantRE, <span class="hljs-string">''</span>),
                <span class="hljs-string">'important'</span>
            );
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-comment">//给css加前缀</span>
            <span class="hljs-keyword">var</span> normalizedName = normalize(name);
            <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(val)) &#123;
                <span class="hljs-comment">// Support values array created by autoprefixer, e.g.</span>
                <span class="hljs-comment">// &#123;display: ["-webkit-box", "-ms-flexbox", "flex"]&#125;</span>
                <span class="hljs-comment">// Set them one by one, and the browser will only set those it can recognize</span>
                <span class="hljs-comment">//支持自动修复程序创建的值数组。</span>
                <span class="hljs-comment">//&#123;显示:[“-webkit-box”、“-ms-flexbox”,“柔化”)&#125;</span>
                <span class="hljs-comment">//一个一个设置，浏览器只会设置它能识别的</span>
                <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>, len = val.length; i < len; i++) &#123;
                    el.style[normalizedName] = val[i]; <span class="hljs-comment">//循环一个个设置样式</span>
                &#125;
            &#125; <span class="hljs-keyword">else</span> &#123;
                el.style[normalizedName] = val;
            &#125;
        &#125;
    &#125;;

    <span class="hljs-keyword">var</span> vendorNames = [<span class="hljs-string">'Webkit'</span>, <span class="hljs-string">'Moz'</span>, <span class="hljs-string">'ms'</span>];
    <span class="hljs-keyword">var</span> emptyStyle;
    <span class="hljs-comment">//给css加前缀。解决浏览器兼用性问题，加前缀</span>
    <span class="hljs-keyword">var</span> normalize = cached(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">prop</span>) </span>&#123;
        emptyStyle = emptyStyle || <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'div'</span>).style; <span class="hljs-comment">//获取浏览器中的style样式</span>
        prop = camelize(prop);
        <span class="hljs-keyword">if</span> (prop !== <span class="hljs-string">'filter'</span> && (prop <span class="hljs-keyword">in</span> emptyStyle)) &#123; <span class="hljs-comment">//如果该属性已经在样式中</span>
            <span class="hljs-keyword">return</span> prop
        &#125;
        <span class="hljs-keyword">var</span> capName = prop.charAt(<span class="hljs-number">0</span>).toUpperCase() + prop.slice(<span class="hljs-number">1</span>); <span class="hljs-comment">//首字母变成大写</span>
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < vendorNames.length; i++) &#123;
            <span class="hljs-keyword">var</span> name = vendorNames[i] + capName; <span class="hljs-comment">//加前缀</span>
            <span class="hljs-keyword">if</span> (name <span class="hljs-keyword">in</span> emptyStyle) &#123;
                <span class="hljs-keyword">return</span> name
            &#125;
        &#125;
    &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-43">19. 更新样式</h3>
<pre><code class="copyable">    var style = &#123;
        create: updateStyle,
        update: updateStyle
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>19-1. updateStyle</strong>，将vonde虚拟dom的css 转义成并且渲染到真实dom的css</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateStyle</span>(<span class="hljs-params">oldVnode, vnode</span>) </span>&#123;
        <span class="hljs-keyword">var</span> data = vnode.data; <span class="hljs-comment">//获取新虚拟dom的标签属性</span>
        <span class="hljs-keyword">var</span> oldData = oldVnode.data; <span class="hljs-comment">//获取旧虚拟dom的标签属性</span>

        <span class="hljs-keyword">if</span> (isUndef(data.staticStyle) && isUndef(data.style) &&
            isUndef(oldData.staticStyle) && isUndef(oldData.style)
        ) &#123;
            <span class="hljs-keyword">return</span>
        &#125;

        <span class="hljs-keyword">var</span> cur, name;
        <span class="hljs-keyword">var</span> el = vnode.elm; <span class="hljs-comment">//获取真实的dom</span>
        <span class="hljs-keyword">var</span> oldStaticStyle = oldData.staticStyle; <span class="hljs-comment">//获取旧的静态 staticStyle</span>
        <span class="hljs-keyword">var</span> oldStyleBinding = oldData.normalizedStyle || oldData.style || &#123;&#125;; <span class="hljs-comment">//获取旧的动态style</span>

        <span class="hljs-comment">// if static style exists, stylebinding already merged into it when doing normalizeStyleData</span>
        <span class="hljs-comment">//  如果存在静态样式，则在执行normalizeStyleData时，stylebinding已经合并到其中</span>
        <span class="hljs-keyword">var</span> oldStyle = oldStaticStyle || oldStyleBinding; <span class="hljs-comment">//旧的style样式</span>


        <span class="hljs-comment">//将可能的数组/字符串值规范化为对象 //把style 字符串 转换成对象 比如'width:100px;height:200px;' 转化成 &#123;width:100px,height:200px&#125;</span>
        <span class="hljs-keyword">var</span> style = normalizeStyleBinding(vnode.data.style) || &#123;&#125;;

        <span class="hljs-comment">// store normalized style under a different key for next diff</span>
        <span class="hljs-comment">// make sure to clone it if it's reactive, since the user likely wants</span>
        <span class="hljs-comment">// to mutate it.</span>
        <span class="hljs-comment">//为下一个diff在不同的键下存储规范化样式</span>
        <span class="hljs-comment">//如果它是反应性的，请确保克隆它，因为用户可能希望这样做</span>
        <span class="hljs-comment">//使之变异</span>
        vnode.data.normalizedStyle = isDef(style.__ob__) ? <span class="hljs-comment">//如果style 加入了观察者之后</span>
            extend(&#123;&#125;, style) :  <span class="hljs-comment">//重新克隆,可以修改</span>
            style; <span class="hljs-comment">//直接赋值</span>
        <span class="hljs-comment">//getStyle循环子组件和组件的样式，把它全部合并到一个样式对象中返回 样式对象 如&#123;width:100px,height:200px&#125; 返回该字符串。</span>
        <span class="hljs-keyword">var</span> newStyle = getStyle(
            vnode,
            <span class="hljs-literal">true</span>
        );

        <span class="hljs-keyword">for</span> (name <span class="hljs-keyword">in</span> oldStyle) &#123; <span class="hljs-comment">//获取旧虚拟dom的样式</span>
            <span class="hljs-keyword">if</span> (isUndef(newStyle[name])) &#123; <span class="hljs-comment">// 如果新的虚拟dom vonde没有了</span>
                setProp(el, name, <span class="hljs-string">''</span>); <span class="hljs-comment">//则设置样式为空</span>
            &#125;
        &#125;
        <span class="hljs-keyword">for</span> (name <span class="hljs-keyword">in</span> newStyle) &#123; <span class="hljs-comment">//循环新的虚拟dom vonde 样式</span>
            cur = newStyle[name];
            <span class="hljs-keyword">if</span> (cur !== oldStyle[name]) &#123; <span class="hljs-comment">//如果旧的和新的不同了 就设置新的样式</span>
                <span class="hljs-comment">// ie9 setting to null has no effect, must use empty string</span>
                setProp(el, name, cur == <span class="hljs-literal">null</span> ? <span class="hljs-string">''</span> : cur);
            &#125;
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>updateStyle=》normalizeStyleBinding</strong>，将可能的数组/字符串值规范化为对象</p>
<pre><code class="copyable">    function normalizeStyleBinding(bindingStyle) &#123;
        if (Array.isArray(bindingStyle)) &#123;
            return toObject(bindingStyle)
        &#125;
        if (typeof bindingStyle === 'string') &#123;
            // 把style 字符串 转换成对象 比如'width:100px;height:200px;' 
            // 转化成 &#123;width:100px,height:200px&#125;
            // 详细查看章节：18. style 字符串 格式化为对象
            return parseStyleText(bindingStyle)
        &#125;
        return bindingStyle
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>updateStyle=》getStyle</strong>，  父组件样式应该在子组件样式之后，这样父组件的样式就可以覆盖它，循环子组件和组件的样式，把它全部合并到一个样式对象中，返回 样式对象 如&#123;width:100px,height:200px&#125; 返回该字符串。</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getStyle</span>(<span class="hljs-params">
        vnode, <span class="hljs-comment">//虚拟dom</span>
        checkChild <span class="hljs-comment">//标志点 布尔值</span>
    </span>) </span>&#123;
        <span class="hljs-keyword">var</span> res = &#123;&#125;;
        <span class="hljs-keyword">var</span> styleData; <span class="hljs-comment">//style data</span>
        <span class="hljs-keyword">if</span> (checkChild) &#123; <span class="hljs-comment">// 标志点 布尔值</span>
            <span class="hljs-keyword">var</span> childNode = vnode; <span class="hljs-comment">//获取子节点</span>
            <span class="hljs-keyword">while</span> (childNode.componentInstance) &#123; <span class="hljs-comment">//已经实例化过的 就是子节点有vonde</span>
                childNode = childNode.componentInstance._vnode;
                <span class="hljs-keyword">if</span> (
                    childNode &&
                    childNode.data &&
                    (styleData = normalizeStyleData(childNode.data))
                ) &#123;
                    extend(res, styleData);
                &#125;
            &#125;
        &#125;

        <span class="hljs-keyword">if</span> ((styleData = normalizeStyleData(vnode.data))) &#123;
            extend(res, styleData);
        &#125;

        <span class="hljs-keyword">var</span> parentNode = vnode;
        <span class="hljs-keyword">while</span> ((parentNode = parentNode.parent)) &#123;
            <span class="hljs-keyword">if</span> (parentNode.data && (styleData = normalizeStyleData(parentNode.data))) &#123;
                extend(res, styleData);
            &#125;
        &#125;
        <span class="hljs-keyword">return</span> res
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>updateStyle=》getStyle=> normalizeStyleData</strong>,在同一个vnode上合并静态和动态样式数据</p>
<pre><code class="copyable">function normalizeStyleData(data) &#123;
        // //将可能的数组/字符串值规范化为对象  把style 字符串 转换成对象 比如'width:100px;height:200px;' 转化成 &#123;width:100px,height:200px&#125; 返回该字符串。
        var style = normalizeStyleBinding(data.style); //获取到vonde中的style属性值
        // static style is pre-processed into an object during compilation
        // and is always a fresh object, so it's safe to merge into it
        //静态样式在编译期间被预处理为对象
        //始终是一个新鲜的对象，所以可以安全地融入其中
        return data.staticStyle ?
            extend(data.staticStyle, style) : //合并静态
            style
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>updateStyle分析完成。</p>
<h3 data-id="heading-44">20. 封装工具模板</h3>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-keyword">var</span> platformModules = [
        <span class="hljs-comment">// attrs包含两个方法create和update都是更新设置真实dom属性值 </span>
        <span class="hljs-comment">// &#123;create: updateAttrs, /*创建属性*/ update: updateAttrs  /*更新属性 */&#125;</span>
        attrs,  
        <span class="hljs-comment">// klass包含类包含两个方法create和update都是更新calss。</span>
        <span class="hljs-comment">// 其实就是updateClass方法。 设置真实dom的class</span>
        klass, 
        events, <span class="hljs-comment">//更新真实dom的事件</span>
        domProps, <span class="hljs-comment">//更新真实dom的props 属性值</span>
        <span class="hljs-comment">// 更新真实dom的style属性。有两个方法create 和update 不过函数都是updateStyle更新真实dom的style属性值.</span>
        <span class="hljs-comment">// 将vonde虚拟dom的css 转义成并且渲染到真实dom的css中</span>
        style, 
        transition <span class="hljs-comment">// 过度动画</span>
    ]
    <span class="hljs-keyword">var</span> modules = platformModules.concat(baseModules);
    <span class="hljs-comment">//path 把vonde 渲染成真实的dom</span>
    <span class="hljs-keyword">var</span> patch = createPatchFunction(
        &#123;
            <span class="hljs-attr">nodeOps</span>: nodeOps,
            <span class="hljs-attr">modules</span>: modules
        &#125;
    );
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-45">21 .定义插入更新指令函数</h3>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-keyword">var</span> directive = &#123;
        <span class="hljs-attr">inserted</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">inserted</span>(<span class="hljs-params">el, binding, vnode, oldVnode</span>) </span>&#123;

            <span class="hljs-keyword">if</span> (vnode.tag === <span class="hljs-string">'select'</span>) &#123;
                <span class="hljs-comment">// #6903</span>
                <span class="hljs-keyword">if</span> (oldVnode.elm && !oldVnode.elm._vOptions) &#123;
                    mergeVNodeHook(vnode, <span class="hljs-string">'postpatch'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
                        directive.componentUpdated(el, binding, vnode);
                    &#125;);
                &#125; <span class="hljs-keyword">else</span> &#123;
                    setSelected(el, binding, vnode.context);
                &#125;
                el._vOptions = [].map.call(el.options, getValue);
            &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (vnode.tag === <span class="hljs-string">'textarea'</span> || isTextInputType(el.type)) &#123;
                el._vModifiers = binding.modifiers;
                <span class="hljs-keyword">if</span> (!binding.modifiers.lazy) &#123;
                    el.addEventListener(<span class="hljs-string">'compositionstart'</span>, onCompositionStart);
                    el.addEventListener(<span class="hljs-string">'compositionend'</span>, onCompositionEnd);
                    <span class="hljs-comment">// Safari < 10.2 & UIWebView doesn't fire compositionend when</span>
                    <span class="hljs-comment">// switching focus before confirming composition choice</span>
                    <span class="hljs-comment">// this also fixes the issue where some browsers e.g. iOS Chrome</span>
                    <span class="hljs-comment">// fires "change" instead of "input" on autocomplete.</span>
                    el.addEventListener(<span class="hljs-string">'change'</span>, onCompositionEnd);
                    <span class="hljs-comment">/* istanbul ignore if */</span>
                    <span class="hljs-keyword">if</span> (isIE9) &#123;
                        el.vmodel = <span class="hljs-literal">true</span>;
                    &#125;
                &#125;
            &#125;
        &#125;,

        <span class="hljs-attr">componentUpdated</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">componentUpdated</span>(<span class="hljs-params">el, binding, vnode</span>) </span>&#123;
            <span class="hljs-keyword">if</span> (vnode.tag === <span class="hljs-string">'select'</span>) &#123;
                setSelected(el, binding, vnode.context);
                <span class="hljs-comment">// in case the options rendered by v-for have changed,</span>
                <span class="hljs-comment">// it's possible that the value is out-of-sync with the rendered options.</span>
                <span class="hljs-comment">// detect such cases and filter out values that no longer has a matching</span>
                <span class="hljs-comment">// option in the DOM.</span>
                <span class="hljs-keyword">var</span> prevOptions = el._vOptions;
                <span class="hljs-keyword">var</span> curOptions = el._vOptions = [].map.call(el.options, getValue);
                <span class="hljs-keyword">if</span> (curOptions.some(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">o, i</span>) </span>&#123;
                    <span class="hljs-keyword">return</span> !looseEqual(o, prevOptions[i]);
                &#125;)) &#123;
                    <span class="hljs-comment">// trigger change event if</span>
                    <span class="hljs-comment">// no matching option found for at least one value</span>
                    <span class="hljs-keyword">var</span> needReset = el.multiple
                        ? binding.value.some(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">v</span>) </span>&#123;
                            <span class="hljs-keyword">return</span> hasNoMatchingOption(v, curOptions);
                        &#125;)
                        : binding.value !== binding.oldValue && hasNoMatchingOption(binding.value, curOptions);
                    <span class="hljs-keyword">if</span> (needReset) &#123;
                        trigger(el, <span class="hljs-string">'change'</span>);
                    &#125;
                &#125;
            &#125;
        &#125;
    &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-46">22. 定义更新绑定指令函数</h3>
<pre><code class="hljs language-js copyable" lang="js">   <span class="hljs-keyword">var</span> show = &#123;
        <span class="hljs-attr">bind</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">bind</span>(<span class="hljs-params">el, ref, vnode</span>) </span>&#123;
            <span class="hljs-keyword">var</span> value = ref.value;

            vnode = locateNode(vnode);
            <span class="hljs-keyword">var</span> transition$$1 = vnode.data && vnode.data.transition;
            <span class="hljs-keyword">var</span> originalDisplay = el.__vOriginalDisplay =
                el.style.display === <span class="hljs-string">'none'</span> ? <span class="hljs-string">''</span> : el.style.display;
            <span class="hljs-keyword">if</span> (value && transition$$1) &#123;
                vnode.data.show = <span class="hljs-literal">true</span>;
                enter(vnode, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
                    el.style.display = originalDisplay;
                &#125;);
            &#125; <span class="hljs-keyword">else</span> &#123;
                el.style.display = value ? originalDisplay : <span class="hljs-string">'none'</span>;
            &#125;
        &#125;,

        <span class="hljs-attr">update</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">update</span>(<span class="hljs-params">el, ref, vnode</span>) </span>&#123;
            <span class="hljs-keyword">var</span> value = ref.value;
            <span class="hljs-keyword">var</span> oldValue = ref.oldValue;

            <span class="hljs-comment">/* istanbul ignore if */</span>
            <span class="hljs-keyword">if</span> (!value === !oldValue) &#123;
                <span class="hljs-keyword">return</span>
            &#125;
            vnode = locateNode(vnode);
            <span class="hljs-keyword">var</span> transition$$1 = vnode.data && vnode.data.transition;
            <span class="hljs-keyword">if</span> (transition$$1) &#123;
                vnode.data.show = <span class="hljs-literal">true</span>;
                <span class="hljs-keyword">if</span> (value) &#123;
                    enter(vnode, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
                        el.style.display = el.__vOriginalDisplay;
                    &#125;);
                &#125; <span class="hljs-keyword">else</span> &#123;
                    leave(vnode, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
                        el.style.display = <span class="hljs-string">'none'</span>;
                    &#125;);
                &#125;
            &#125; <span class="hljs-keyword">else</span> &#123;
                el.style.display = value ? el.__vOriginalDisplay : <span class="hljs-string">'none'</span>;
            &#125;
        &#125;,

        <span class="hljs-attr">unbind</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">unbind</span>(<span class="hljs-params">el,
            binding,
            vnode,
            oldVnode,
            isDestroy</span>) </span>&#123;
            <span class="hljs-keyword">if</span> (!isDestroy) &#123;
                el.style.display = el.__vOriginalDisplay;
            &#125;
        &#125;
    &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-47">23 . 封装指令</h3>
<pre><code class="copyable">    var platformDirectives = &#123;
        model: directive,
        show: show
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-48">24. 检验属性</h3>
<pre><code class="copyable">    Vue.config.mustUseProp = mustUseProp;    //校验属性


    Vue.config.isReservedTag = isReservedTag;
    Vue.config.isReservedAttr = isReservedAttr;
    Vue.config.getTagNamespace = getTagNamespace;
    Vue.config.isUnknownElement = isUnknownElement;

    // install platform runtime directives & components
    extend(Vue.options.directives, platformDirectives);
    extend(Vue.options.components, platformComponents);

    // install platform patch function 安装平台补丁功能
    Vue.prototype.__patch__ = inBrowser ? patch : noop;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-49">25. 挂载$mount</h3>
<pre><code class="copyable">    Vue.prototype.$mount = function (el, hydrating) &#123;
        debugger
        // query(el) 获取dom，已经是dom就返回,不是dom并且获取不到，警告提示，创建一个新的dev
        el = el && inBrowser ? query(el) : undefined;
        // 安装组件
        return mountComponent(
            this, // Vue实例
            el,  // 真实dom
            hydrating
        )
    &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-50">26 .vue 开发工具配置</h3>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-keyword">if</span> (inBrowser) &#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
            <span class="hljs-keyword">if</span> (config.devtools) &#123;
                <span class="hljs-keyword">if</span> (devtools) &#123;
                    devtools.emit(<span class="hljs-string">'init'</span>, Vue);
                &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (
                    <span class="hljs-string">"development"</span> !== <span class="hljs-string">'production'</span> &&
                    <span class="hljs-string">"development"</span> !== <span class="hljs-string">'test'</span> &&
                    isChrome
                ) &#123;
                    <span class="hljs-built_in">console</span>[<span class="hljs-built_in">console</span>.info ? <span class="hljs-string">'info'</span> : <span class="hljs-string">'log'</span>](
                        <span class="hljs-string">'Download the Vue Devtools extension for a better development experience:\n'</span> +
                        <span class="hljs-string">'https://github.com/vuejs/vue-devtools'</span>
                    );
                &#125;
            &#125;
            <span class="hljs-comment">//如果不是生产环境</span>
            <span class="hljs-keyword">if</span> (<span class="hljs-string">"development"</span> !== <span class="hljs-string">'production'</span> &&
                <span class="hljs-string">"development"</span> !== <span class="hljs-string">'test'</span> &&
                config.productionTip !== <span class="hljs-literal">false</span> &&
                <span class="hljs-keyword">typeof</span> <span class="hljs-built_in">console</span> !== <span class="hljs-string">'undefined'</span>
            ) &#123;
                <span class="hljs-built_in">console</span>[<span class="hljs-built_in">console</span>.info ? <span class="hljs-string">'info'</span> : <span class="hljs-string">'log'</span>](
                    <span class="hljs-string">"You are running Vue in development mode.\n"</span> +
                    <span class="hljs-string">"Make sure to turn on production mode when deploying for production.\n"</span> +
                    <span class="hljs-string">"See more tips at https://vuejs.org/guide/deployment.html"</span>
                );
            &#125;
        &#125;, <span class="hljs-number">0</span>);
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            
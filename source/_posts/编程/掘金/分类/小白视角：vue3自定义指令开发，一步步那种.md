
---
title: '小白视角：vue3自定义指令开发，一步步那种'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f54d83d6da7844388fe9f055954782a4~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 21 Jun 2021 00:44:49 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f54d83d6da7844388fe9f055954782a4~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">注意事项：写法从extend替换成了createApp</h2>
<p><strong>阅前须知：</strong>
vue2 和 vue3 的自定义指令方式有点不一样
vue2 是 <strong>extend</strong> 去挂载dom元素
vue3 不再支持 extend 了，要用<strong>createApp</strong>生成实例去挂载
（我也是看文章才知道，大家可以去搜下，然后这个demo我是用TS去写的，后面会是anyScript，因为刚接触TS不太懂语法，然后就直接在这个项目上写来玩了）</p>
<p><strong>不对的地方大家多多体谅哈~小编是小萌新</strong></p>
<h3 data-id="heading-1">第一步: 创建loading.vue组件</h3>
<p>创建一个.vue 文件，写出你loading的样式，这里我就不写了，大家可以网上找下（毕竟需求不一样）。</p>
<h3 data-id="heading-2">第二步: 创建ts文件</h3>
<p>创建一个.ts文件，作为一个导出文件。</p>
<h3 data-id="heading-3">第三步: 挂载与导出</h3>
<p>我们需要在.ts文件引入我们写好的
loading.vue 文件、
createApp方法：
下面展示一些 <code>示例</code>。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> Loading <span class="hljs-keyword">from</span> <span class="hljs-string">"./loading.vue"</span>
<span class="hljs-keyword">import</span> &#123; createApp &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>随后我们定义一个导出对象，用来暴露在main中的进行注册，然后方法就可以在里面书写了。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> loadingObj = &#123;
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> loadingObj;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">注意： 暴露出来的钩子函数不太一样了</h3>
<p><strong>vue2：</strong> bind，inserted，update，componentUpdated，unbind。
<strong>vue3：</strong>  created，mounted，updated，unmounted</p>
<blockquote>
<p>createApp的作用：</p>
</blockquote>
<p>创建app实例，这个时候是处于游荡阶段，等待挂载。
这个时候的app实例属于Vue的一个准备阶段，为后面的mount等操作准备好了所需要使用到的函数。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f54d83d6da7844388fe9f055954782a4~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>mount是比较核心，和vue2差不多，反正一句话就是进行渲染该组件</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f0a64edc45d24994825951ce20ea3503~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">接下来写下代码~（AnyScript了解一下）</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-comment">// 这段代码可以放在mounted里面挂载在el身上，方便操作。但是我试过放在顶部也是可以用的</span>
  <span class="hljs-keyword">const</span> app = createApp(Loading);
  <span class="hljs-keyword">const</span> instance:any = app.mount(<span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">"div"</span>)); <span class="hljs-comment">// 你也可以挂载在全局的app下，反正就给个dom它</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后和vue2的写法差不多，就是钩子有点变化而已：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params">el:any, bind:any</span>)</span> &#123;
    <span class="hljs-comment">// 这段代码我放在mounted里挂载在el身上，传参的时候可以方便调用</span>
    <span class="hljs-keyword">const</span> app = createApp(Loading);
    <span class="hljs-keyword">const</span> instance:any = app.mount(<span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">"div"</span>));
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"instance"</span>,instance);
    el.instance = instance;
    <span class="hljs-comment">// 这里是我组件里面的方法，调用这个去更新值，也可以直接改data的值，见仁见智哈~安全而已</span>
    el.instance.setLoading(<span class="hljs-string">"我是努力加载中"</span>);
    <span class="hljs-keyword">if</span>(bind.value) &#123;  <span class="hljs-comment">// v-loading="true"时候调用添加在组件</span>
      appndChild(el)
    &#125;
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来是更新的时候触发的事件：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-function"><span class="hljs-title">updated</span>(<span class="hljs-params">el:any, bind:any</span>)</span>&#123;
    <span class="hljs-keyword">if</span>(bind.value !== bind.oldValue)&#123;
      bind.value? appndChild(el): remove(el);
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>公共方法：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">appndChild</span>(<span class="hljs-params">el:any</span>)</span>&#123;
  el.appendChild(el.instance.$el);
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">remove</span>(<span class="hljs-params">el:any</span>)</span>&#123;
  el.removeChild(el.instance.$el);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在<strong>main.ts</strong>中去注册就行。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; createApp &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App.vue'</span>
<span class="hljs-keyword">import</span> direactive <span class="hljs-keyword">from</span> <span class="hljs-string">"../src/hooks/direactive"</span>

<span class="hljs-keyword">const</span> app = createApp(App);

app.directive(<span class="hljs-string">"loading"</span>,direactive).mount(<span class="hljs-string">'#app'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">接下来谈谈题外话，自定义指令的注册方式：</h3>
<blockquote>
<p>第一种：和以前vue2一样，通过暴露出一个对象，里面有install方法，然后通过vue.use去全局注册，代码如下：</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; App &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-function"><span class="hljs-title">install</span>(<span class="hljs-params">vue</span>)</span>&#123;
      app.directive(<span class="hljs-string">"loading"</span>,&#123;
        <span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span>&#123;
        &#125;,
        <span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params"></span>)</span>&#123;
        &#125;
      &#125;)
    &#125;
&#125;
**然后在main.ts注册就行**
<span class="hljs-keyword">import</span> loading  <span class="hljs-keyword">from</span> <span class="hljs-string">'./loading'</span>
<span class="hljs-keyword">let</span> app = createApp(App)
app.use(loading)

<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>第二种就是我上面写的方式，在app实例下，通过调用app.directive("loading",direactive)去使用，这种写法我感觉就相当于局部创建的一样，不过这个局部是全局的实例而已。（个人理解，不对别打我哈~）</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; createApp &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App.vue'</span>
<span class="hljs-keyword">import</span> direactive <span class="hljs-keyword">from</span> <span class="hljs-string">"../src/hooks/direactive"</span>

<span class="hljs-keyword">const</span> app = createApp(App);

app.directive(<span class="hljs-string">"loading"</span>,direactive).mount(<span class="hljs-string">'#app'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">下面打印下挂载后的instance实例，方便和我一样懒的小伙伴</h3>
<blockquote>
<p>const instance:any = app.mount(document.createElement("div"));</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9162d996800e4f6f8e335cf3e771ed82~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
</blockquote>
<blockquote>
<p>挂载后的dom对象结构，你可以直接去改data的值控制显示的样式~
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5cf10bb25cc94ceb9139391ab8376d0e~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<h2 data-id="heading-8">我贴下全部的代码：</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> Loading <span class="hljs-keyword">from</span> <span class="hljs-string">"./loading.vue"</span>;
<span class="hljs-keyword">import</span> &#123; createApp &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;

<span class="hljs-keyword">const</span> LoadingObj = &#123;
  <span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params">el:any, bind:any</span>)</span> &#123;
    <span class="hljs-keyword">const</span> app = createApp(Loading);
    <span class="hljs-keyword">const</span> instance:any = app.mount(<span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">"div"</span>));
    el.instance = instance;
    el.instance.setLoading(<span class="hljs-string">"我是努力加载中"</span>);
    <span class="hljs-keyword">if</span>(bind.value) &#123;
      appndChild(el)
    &#125;
  &#125;,
  <span class="hljs-function"><span class="hljs-title">updated</span>(<span class="hljs-params">el:any, bind:any</span>)</span>&#123;
    <span class="hljs-keyword">if</span>(bind.value !== bind.oldValue)&#123;
      bind.value? appndChild(el): remove(el);
    &#125;
  &#125;
 
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">appndChild</span>(<span class="hljs-params">el:any</span>)</span>&#123;
  el.appendChild(el.instance.$el);
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">remove</span>(<span class="hljs-params">el:any</span>)</span>&#123;
  el.removeChild(el.instance.$el);
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> LoadingObj;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-9">最后如果有不对的地方，各位大佬请见谅并指出，这是弟弟的个人理解而已~小萌新一个，一起加油。</h1></div>  
</div>
            
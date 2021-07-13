
---
title: '组件库实战 _ 用vue3+ts实现全局Header和列表数据渲染ColumnList'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/641e626902b142659b82a25f62b02098~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 12 Jul 2021 20:49:53 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/641e626902b142659b82a25f62b02098~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p>「本文已参与好文召集令活动，点击查看：<a href="https://juejin.cn/post/6978685539985653767" target="_blank" title="https://juejin.cn/post/6978685539985653767">后端、大前端双赛道投稿，2万元奖池等你挑战！</a>」</p>
<h1 data-id="heading-0">🖼️序言</h1>
<p>最近在用 <code>vue3</code> 和 <code>ts</code> 捣鼓一些小工具，发现平常开发中一个很常见的需求就是，<strong>数据列表的渲染</strong>。现在重新学习，发现我在学 <code>vue2</code> 时的很多设计规范和逻辑都考虑的不是特别妥当。</p>
<p>因此，写下这篇文章，记录组件设计中数据列表渲染和全局头部的设计。</p>
<p>一起来学习吧~🙆</p>
<h1 data-id="heading-1">📻一、ColumnList数据渲染</h1>
<h2 data-id="heading-2">1、设计稿抢先知</h2>
<p>在了解功能实现之前，我们先来看看<strong>原型图</strong>，看我们想要实现的数据列表是怎么样的。<strong>如下图所示：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/641e626902b142659b82a25f62b02098~tplv-k3u1fbpfcp-zoom-1.image" alt="columnList设计稿" loading="lazy" referrerpolicy="no-referrer"></p>
<p>大家可以先了解一下，我们待会所要实现内容的效果图。</p>
<h2 data-id="heading-3">2、数据构思</h2>
<p>了解完具体的效果图之后呢，现在我们要开始来干活啦！</p>
<p>首先我们需要先构思这个组件所需要的数据有哪一些呢？</p>
<p>这个组件所需要的数据，首先是每一行数据它自己唯一的 <code>id</code> ，其次就是标题 <code>title</code> ，还有一个是头像 <code>avatar</code> ，最后一个是每个标题对应的文字描述 <code>description</code> 。</p>
<p>分析完成之后，我们现在在 <code>vue3</code> 项目下的 <code>src|components</code> 文件夹下新建一个文件，命名为 <code>ColumnList.vue</code> 。之后再编写这段业务代码。<strong>具体代码如下：</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; computed, defineComponent, PropType &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-comment">//用ts写一个接口，存放列表数据的属性</span>
<span class="hljs-keyword">export</span> interface ColumnProps &#123;
  <span class="hljs-attr">id</span>: number;
  title: string;
  avatar?: string;
  description: string;
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineComponent(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'ColumnList'</span>,
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-comment">//将接口的内容赋值给list数组，方便接收父组件传来的数据</span>
    <span class="hljs-attr">list</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Array</span> <span class="hljs-keyword">as</span> PropType<ColumnProps[]>,
      required: <span class="hljs-literal">true</span>
    &#125;
  &#125;
&#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"scss"</span> <span class="hljs-attr">scoped</span>></span>
  
<span class="hljs-tag"></<span class="hljs-name">style</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">3、视图数据绑定</h2>
<p>现在，对数据构思完毕之后，我们是还没有取到任何数据可以渲染的，相当于是一个空的 <code>ColumnList</code> 。但是我们已经有了接口的属性内容，所以我们先来把数据绑定到视图当中。<strong>具体代码如下：</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"row"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"column in columnList"</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">"column.id"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"col-4 mb-3"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"card h-100 shadow-sm"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"card-body text-center"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">:src</span>=<span class="hljs-string">"column.avatar"</span> <span class="hljs-attr">:alt</span>=<span class="hljs-string">"column.title"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"rounded-circle border border-light w-25 my-3"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">h5</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"title"</span>></span>&#123;&#123;column.title&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h5</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"card-text text-left"</span>></span>&#123;&#123;column.description&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"btn btn-outline-primary"</span>></span>进入专栏<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; computed, defineComponent, PropType &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">export</span> interface ColumnProps &#123;
  <span class="hljs-attr">id</span>: number;
  title: string;
  avatar?: string;
  description: string;
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineComponent(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'ColumnList'</span>,
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">list</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Array</span> <span class="hljs-keyword">as</span> PropType<ColumnProps[]>,
      required: <span class="hljs-literal">true</span>
    &#125;
  &#125;
&#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"scss"</span> <span class="hljs-attr">scoped</span>></span>
  
<span class="hljs-tag"></<span class="hljs-name">style</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注：</strong> 这里我用到的是 <code>bootstrap</code> 的样式库，所以 <code>css</code> 方面不做过多的编写，大家有需要可以到<a href="https://link.juejin.cn/?target=https%3A%2F%2Fv5.bootcss.com%2Fdocs%2Fgetting-started%2Fintroduction%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://v5.bootcss.com/docs/getting-started/introduction/" ref="nofollow noopener noreferrer">官方中文文档</a>进行查看，也可以自己进行样式设计。</p>
<p>到此，我们就完成了第一轮的数据绑定。接下来我们在父组件中，进行数据传递。</p>
<h2 data-id="heading-5">4、数据传递</h2>
<p>我们在vue3项目中的 <code>src</code> 文件夹下的 <code>App.vue</code> 中来进行数据传递。<strong>具体代码如下：</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"container"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">column-list</span> <span class="hljs-attr">:list</span>=<span class="hljs-string">"list"</span>></span><span class="hljs-tag"></<span class="hljs-name">column-list</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; defineComponent &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-comment">//在根文件下引入bootstrap</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">'bootstrap/dist/css/bootstrap.min.css'</span>
<span class="hljs-comment">//引入子组件</span>
<span class="hljs-keyword">import</span> ColumnList, &#123; ColumnProps &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./components/ColumnList.vue'</span>

<span class="hljs-comment">//制造子组件的接口数据</span>
<span class="hljs-keyword">const</span> testData: ColumnProps[] = [
  &#123;
    <span class="hljs-attr">id</span>: <span class="hljs-number">1</span>,
    <span class="hljs-attr">title</span>: <span class="hljs-string">'test1专栏'</span>,
    <span class="hljs-attr">description</span>: <span class="hljs-string">'众所周知， js 是一门弱类型语言，并且规范较少。这就很容易导致在项目上线之前我们很难发现到它的错误，等到项目一上线，浑然不觉地，bug就UpUp了。于是，在过去的这两年，ts悄悄的崛起了。 本专栏将介绍关于ts的一些学习记录。'</span>
    <span class="hljs-attr">avatar</span>: <span class="hljs-string">'https://img0.baidu.com/it/u=3101694723,748884042&fm=26&fmt=auto&gp=0.jpg'</span>
  &#125;,
  &#123;
    <span class="hljs-attr">id</span>: <span class="hljs-number">2</span>,
    <span class="hljs-attr">title</span>: <span class="hljs-string">'test2专栏'</span>,
    <span class="hljs-attr">description</span>: <span class="hljs-string">'众所周知， js 是一门弱类型语言，并且规范较少。这就很容易导致在项目上线之前我们很难发现到它的错误，等到项目一上线，浑然不觉地，bug就UpUp了。于是，在过去的这两年，ts悄悄的崛起了。 本专栏将介绍关于ts的一些学习记录。'</span>,
    <span class="hljs-attr">avatar</span>: <span class="hljs-string">'https://img0.baidu.com/it/u=3101694723,748884042&fm=26&fmt=auto&gp=0.jpg'</span>
  &#125;
]

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineComponent(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'App'</span>,
  <span class="hljs-attr">components</span>: &#123;
    ColumnList
  &#125;,
  setup () &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">list</span>: testData
    &#125;
  &#125;
&#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
<span class="hljs-selector-id">#app</span> &#123;
  <span class="hljs-attribute">font-family</span>: Avenir, Helvetica, Arial, sans-serif;
  -webkit-<span class="hljs-attribute">font-smoothing</span>: antialiased;
  -moz-osx-<span class="hljs-attribute">font-smoothing</span>: grayscale;
  <span class="hljs-attribute">text-align</span>: center;
  <span class="hljs-attribute">color</span>: <span class="hljs-number">#2c3e50</span>;
  <span class="hljs-attribute">margin-top</span>: <span class="hljs-number">60px</span>;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在，我们来看下<strong>此时浏览器的运行效果：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/26ded614ee324a148391d6647094db62~tplv-k3u1fbpfcp-zoom-1.image" alt="columnList静态组件" loading="lazy" referrerpolicy="no-referrer"></p>
<p>大家可以看到，通过以上的代码编写，数据正常的传递并运行成功了。</p>
<h2 data-id="heading-6">5、挠头情况</h2>
<p>看到这里，感觉整个组件的设计还挺尽善尽美的。但是呢，大家有没有想过有一种特殊情况，假设后端传来的数据中，<strong>有一行数据里面，没有头像avatar的值</strong>。那这个时候，如果我们前期没有考虑清楚有可能遇到的各种情况，程序估计很容易地就报错了。</p>
<p>所以我们还要做的一件事情就是，当收不到头像的数据时，我们要给它加一张初始化的图片，以至于保持列表内容一致。</p>
<p>现在我们来对 <code>ColumnList.vue</code> 文件进行改造，<strong>具体代码如下：</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"row"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"column in columnList"</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">"column.id"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"col-4 mb-3"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"card h-100 shadow-sm"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"card-body text-center"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">:src</span>=<span class="hljs-string">"column.avatar"</span> <span class="hljs-attr">:alt</span>=<span class="hljs-string">"column.title"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"rounded-circle border border-light w-25 my-3"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">h5</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"title"</span>></span>&#123;&#123;column.title&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h5</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"card-text text-left"</span>></span>&#123;&#123;column.description&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"btn btn-outline-primary"</span>></span>进入专栏<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; computed, defineComponent, PropType &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-comment">//用ts写一个接口，存放列表数据的属性</span>
<span class="hljs-keyword">export</span> interface ColumnProps &#123;
  <span class="hljs-attr">id</span>: number;
  title: string;
  avatar?: string;
  description: string;
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineComponent(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'ColumnList'</span>,
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-comment">//将接口的内容赋值给list数组，方便接收父组件传来的数据</span>
    <span class="hljs-attr">list</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Array</span> <span class="hljs-keyword">as</span> PropType<ColumnProps[]>,
      required: <span class="hljs-literal">true</span>
    &#125;
  &#125;,
  <span class="hljs-comment">//将props传递给setup</span>
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params">props</span>)</span> &#123;
    <span class="hljs-keyword">const</span> columnList = computed(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-comment">//遍历list数组数据的每一行</span>
      <span class="hljs-keyword">return</span> props.list.map(<span class="hljs-function"><span class="hljs-params">column</span> =></span> &#123;
        <span class="hljs-comment">//当遇到当前行数据没有头像时</span>
        <span class="hljs-keyword">if</span> (!column.avatar) &#123;
          <span class="hljs-comment">//赋予初始化图片</span>
          column.avatar = <span class="hljs-built_in">require</span>(<span class="hljs-string">'@/assets/logo.png'</span>)
        &#125;
        <span class="hljs-keyword">return</span> column
      &#125;)
    &#125;)
    <span class="hljs-keyword">return</span> &#123;
      columnList
    &#125;
  &#125;
&#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"scss"</span> <span class="hljs-attr">scoped</span>></span>
  
<span class="hljs-tag"></<span class="hljs-name">style</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>继续，我们把 <code>App.vue</code> 中 <code>testData</code> 的数据进行删减。<strong>具体代码如下：</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"container"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">column-list</span> <span class="hljs-attr">:list</span>=<span class="hljs-string">"list"</span>></span><span class="hljs-tag"></<span class="hljs-name">column-list</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span>></span><span class="javascript">

<span class="hljs-comment">//制造子组件的接口数据</span>
<span class="hljs-keyword">const</span> testData: ColumnProps[] = [
  &#123;
    <span class="hljs-attr">id</span>: <span class="hljs-number">1</span>,
    <span class="hljs-attr">title</span>: <span class="hljs-string">'test1专栏'</span>,
    <span class="hljs-attr">description</span>: <span class="hljs-string">'众所周知， js 是一门弱类型语言，并且规范较少。这就很容易导致在项目上线之前我们很难发现到它的错误，等到项目一上线，浑然不觉地，bug就UpUp了。于是，在过去的这两年，ts悄悄的崛起了。 本专栏将介绍关于ts的一些学习记录。'</span>
    <span class="hljs-comment">//avatar: 'https://img0.baidu.com/it/u=3101694723,748884042&fm=26&fmt=auto&gp=0.jpg'</span>
  &#125;,
  &#123;
    <span class="hljs-attr">id</span>: <span class="hljs-number">2</span>,
    <span class="hljs-attr">title</span>: <span class="hljs-string">'test2专栏'</span>,
    <span class="hljs-attr">description</span>: <span class="hljs-string">'众所周知， js 是一门弱类型语言，并且规范较少。这就很容易导致在项目上线之前我们很难发现到它的错误，等到项目一上线，浑然不觉地，bug就UpUp了。于是，在过去的这两年，ts悄悄的崛起了。 本专栏将介绍关于ts的一些学习记录。'</span>,
    <span class="hljs-attr">avatar</span>: <span class="hljs-string">'https://img0.baidu.com/it/u=3101694723,748884042&fm=26&fmt=auto&gp=0.jpg'</span>
  &#125;
]
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>大家定位到 <code>testData</code> 中的 <code>avatar</code> 那一行，我们把第一个数据的  <code>avatar</code> 属性进行注释。现在，<strong>我们来看下浏览器的效果：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ddb050be306434e870d1cc0b48d6772~tplv-k3u1fbpfcp-zoom-1.image" alt="缺avatar时的效果" loading="lazy" referrerpolicy="no-referrer"></p>
<p>大家可以看到，缺 <code>avatar</code> 属性时，按照我们预期的，浏览器自动显示了我们<strong>预先初始化的图片</strong>。这样，不论从组件结构设计还是从代码逻辑结构设计来说，是不是感觉可扩展性又增强了许多。</p>
<h1 data-id="heading-7">☎️二、GlobalHeader全局Header</h1>
<h2 data-id="heading-8">1、设计稿抢先看</h2>
<p>写完 <code>columnList</code> 组件，我们用一个新的组件来强化这种设计方法。接下来我们来写一个新的组件，<code>GlobalHeader</code> ，即全局头部。先来看下我们要实现的效果图。<strong>详情见下图：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ba2d612136294a1db4657ac5007b7dcd~tplv-k3u1fbpfcp-zoom-1.image" alt="globalHeader原型图" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-9">2、数据构思</h2>
<p>了解完具体的效果图之后呢，同样地，我们先来构思这个组件所需要的数据有哪一些。</p>
<p>这个组件所需要的数据，首先是针对每一个用户的，所以它每个用户拥有自己唯一的 <code>id</code> ，其次就是<strong>用户名</strong> <code>name</code> ，最后一个是 <strong>是否登录</strong> <code>isLogin</code> 。</p>
<p>分析完成之后，我们现在在 <code>vue3</code> 项目下的 <code>src|components</code> 文件夹下新建一个文件，命名为 <code>GlobalHeader.vue</code> 。之后编写这段业务代码。<strong>具体代码如下：</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; defineComponent, PropType &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>

<span class="hljs-comment">//用ts写一个接口，存放列表数据的属性</span>
<span class="hljs-comment">//name和id加？表示是可选项</span>
<span class="hljs-keyword">export</span> interface UserProps&#123;
    <span class="hljs-attr">isLogin</span>: boolean;
    name?: string;
    id?: number;
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineComponent(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'GlobalHeader'</span>,
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-comment">//将接口的内容赋值给user对象，方便接收父组件传来的数据</span>
    <span class="hljs-attr">user</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Object</span> <span class="hljs-keyword">as</span> PropType<UserProps>,
      required: <span class="hljs-literal">true</span>
    &#125;
  &#125;
&#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"scss"</span> <span class="hljs-attr">scoped</span>></span>
  
<span class="hljs-tag"></<span class="hljs-name">style</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">3、视图数据绑定</h2>
<p>现在，对数据构思完毕之后，我们来把数据绑定到视图当中。<strong>具体代码如下：</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">nav</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"navbar navbar-dark bg-primary justify-content-between mb-4 px-4"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"navbar-brand"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span>></span>周一专栏<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"!user.isLogin"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"list-inline mb-0"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"list-inline-item"</span>></span><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"btn btn-outline-light my-2"</span>></span>登录<span class="hljs-tag"></<span class="hljs-name">a</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"list-inline-item"</span>></span><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"btn btn-outline-light my-2"</span>></span>注册<span class="hljs-tag"></<span class="hljs-name">a</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">v-else</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"list-inline mb-0"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"list-inline-item"</span>></span><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"btn btn-outline-light my-2"</span>></span>欢迎你 &#123;&#123;user.name&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">a</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">nav</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; computed, defineComponent, PropType &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">export</span> interface ColumnProps &#123;
  <span class="hljs-attr">id</span>: number;
  title: string;
  avatar?: string;
  description: string;
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineComponent(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'ColumnList'</span>,
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">list</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Array</span> <span class="hljs-keyword">as</span> PropType<ColumnProps[]>,
      required: <span class="hljs-literal">true</span>
    &#125;
  &#125;
&#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"scss"</span> <span class="hljs-attr">scoped</span>></span>
  
<span class="hljs-tag"></<span class="hljs-name">style</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">4、数据传递</h2>
<p>现在，我们在 <code>vue3</code> 项目中的 <code>src</code> 文件夹下的 <code>App.vue</code> 中来进行数据传递。<strong>具体代码如下：</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"container"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">global-header</span> <span class="hljs-attr">:user</span>=<span class="hljs-string">"user"</span>></span><span class="hljs-tag"></<span class="hljs-name">global-header</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; defineComponent &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-comment">//在根文件下引入bootstrap</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">'bootstrap/dist/css/bootstrap.min.css'</span>
<span class="hljs-comment">//引入子组件</span>
<span class="hljs-keyword">import</span> GlobalHeader, &#123; UserProps &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./components/GlobalHeader.vue'</span>

<span class="hljs-comment">//制造子组件的接口数据</span>
<span class="hljs-keyword">const</span> currentUser: UserProps = &#123;
  <span class="hljs-attr">isLogin</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">name</span>: <span class="hljs-string">'Monday'</span>
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineComponent(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'App'</span>,
  <span class="hljs-attr">components</span>: &#123;
    GlobalHeader
  &#125;,
  setup () &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">user</span>: currentUser
    &#125;
  &#125;
&#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"scss"</span> <span class="hljs-attr">scoped</span>></span>

<span class="hljs-tag"></<span class="hljs-name">style</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>当前 <code>isLogin</code> 的状态我们是设置成 <code>false</code> 。现在，我们来看下<strong>此时浏览器的运行效果：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/65447f9b200047e8ba3d928c608ce876~tplv-k3u1fbpfcp-zoom-1.image" alt="isLogin为false时" loading="lazy" referrerpolicy="no-referrer"></p>
<p>大家可以看到，当前状态为 <code>false</code> ，所以 <code>header</code> 的右边显示的是<strong>登录</strong>和<strong>注册</strong>两个按钮，如预期所料。</p>
<p>现在，我们来把 <code>isLogin</code> 的状态改为 <code>true</code> ，<strong>具体代码如下：</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> currentUser: UserProps = &#123;
  <span class="hljs-attr">isLogin</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">name</span>: <span class="hljs-string">'Monday'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时我们来看下浏览器的显示效果，<strong>如下图所示：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1cce3e6bc7fa473880769d8c99041b73~tplv-k3u1fbpfcp-zoom-1.image" alt="isLogin为true时" loading="lazy" referrerpolicy="no-referrer"></p>
<p>现在，可以看到，当 <code>isLogin</code> 为 <code>true</code> 时，表示用户成功登录了。所以 <code>header</code> 的右方显示的是 <strong>欢迎你 Monday</strong> 的字样，也如我们预期所料。</p>
<h1 data-id="heading-12">📸三、Dropdown下拉菜单</h1>
<p>看完上面的内容，大家心里是否有一个疑惑，我们 <code>header</code> 最右方的<strong>下拉菜单</strong>还没有实现。不着急，接下来我们就来设计这个组件。</p>
<h2 data-id="heading-13">1、组件基本功能</h2>
<p>我们现在先来设计下这个组件的基本功能。首先在 <code>vue3</code> 项目的 <code>src|components</code> 文件夹下，新增一个 <code>.vue</code> 文件，命名为 <code>Dropdown.vue</code> 。之后编写该文件的代码，<strong>具体代码如下：</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"dropdown"</span>></span>
        <span class="hljs-comment"><!-- 下拉菜单标题 --></span>
        <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"btn btn-outline-light my-2dropdown-toggle"</span> @<span class="hljs-attr">click.prevent</span>=<span class="hljs-string">"toggleOpen()"</span>></span>
            &#123;&#123;title&#125;&#125;
        <span class="hljs-tag"></<span class="hljs-name">a</span>></span>
        <span class="hljs-comment"><!-- 下拉菜单内容 --></span>
        <span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"dropdown-menu"</span> <span class="hljs-attr">:style</span>=<span class="hljs-string">"&#123; display: 'block' &#125;"</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"isOpen"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"dropdown-item"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span>></span>新建文章<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">li</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"dropdown-item"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span>></span>编辑资料<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; defineComponent, ref, onMounted, onUnmounted, watch &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineComponent(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'Dropdown'</span>,
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">title</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
      <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>
    &#125;
  &#125;,
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> isOpen = ref(<span class="hljs-literal">false</span>)
    <span class="hljs-comment">//点击后打开菜单</span>
    <span class="hljs-keyword">const</span> toggleOpen = <span class="hljs-function">() =></span> &#123;
      isOpen.value = !isOpen.value
    &#125;
    <span class="hljs-keyword">return</span> &#123;
      isOpen,
      toggleOpen
    &#125;
  &#125;
&#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"scss"</span> <span class="hljs-attr">scoped</span>></span>

<span class="hljs-tag"></<span class="hljs-name">style</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<p>继续，我们来改造下刚刚的 <code>GlobalHeader.vue</code> 文件。<strong>具体代码如下：</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">nav</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"navbar navbar-dark bg-primary justify-content-between mb-4 px-4"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"navbar-brand"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span>></span>周一专栏<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"!user.isLogin"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"list-inline mb-0"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"list-inline-item"</span>></span><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"btn btn-outline-light my-2"</span>></span>登录<span class="hljs-tag"></<span class="hljs-name">a</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"list-inline-item"</span>></span><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"btn btn-outline-light my-2"</span>></span>注册<span class="hljs-tag"></<span class="hljs-name">a</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">v-else</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"list-inline mb-0"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"list-inline-item"</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">dropdown</span> <span class="hljs-attr">:title</span>=<span class="hljs-string">"`欢迎你 $&#123;user.name&#125;`"</span>></span><span class="hljs-tag"></<span class="hljs-name">dropdown</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">nav</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; defineComponent, PropType &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> Dropdown <span class="hljs-keyword">from</span> <span class="hljs-string">'./Dropdown.vue'</span>

<span class="hljs-keyword">export</span> interface UserProps&#123;
    <span class="hljs-attr">isLogin</span>: boolean;
    name?: string;
    id?: number;
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineComponent(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'GlobalHeader'</span>,
  <span class="hljs-attr">components</span>: &#123;
    Dropdown
  &#125;,
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">user</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Object</span> <span class="hljs-keyword">as</span> PropType<UserProps>,
      required: <span class="hljs-literal">true</span>
    &#125;
  &#125;
&#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"scss"</span> <span class="hljs-attr">scoped</span>></span>

<span class="hljs-tag"></<span class="hljs-name">style</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在，我们来看下<strong>浏览器的显示效果：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ba77612376eb4f49a080944c5c548fda~tplv-k3u1fbpfcp-zoom-1.image" alt="dropdown组件基本功能" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-14">2、自定义菜单内容DropdownItem</h2>
<p>现在，我们已经完成了组件的基本功能。但是细心的小伙伴已经发现，下拉菜单没有办法自定义，因为它被写成固定的了。还有一个问题就是，点击其他区域我们不能收起菜单，这间接地，用户体验好像就没有那么好了。所以呢，有需求了，我们就来完成需求。现在，我们就来解决上述所说的两个问题。</p>
<p>同样地，在vue3项目中的 <code>src|components</code> 文件夹下添加一个 <code>.vue</code> 文件，命名为 <code>DropdownItem.vue</code> 。具体代码如下：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span>
    <span class="hljs-attr">class</span>=<span class="hljs-string">"dropdown-option"</span>
    <span class="hljs-attr">:class</span>=<span class="hljs-string">"&#123;'is-disabled': disabled&#125;"</span>
    ></span>
        <span class="hljs-comment"><!-- 定义一个插槽，供给父组件使用 --></span>
        <span class="hljs-tag"><<span class="hljs-name">slot</span>></span><span class="hljs-tag"></<span class="hljs-name">slot</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; defineComponent &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineComponent(&#123;
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-comment">//禁用状态属性</span>
    <span class="hljs-attr">disabled</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Boolean</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-literal">false</span>
    &#125;
  &#125;
&#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
<span class="hljs-comment">/* 注意：*表示两个类下面的所有元素 */</span>
<span class="hljs-selector-class">.dropdown-option</span><span class="hljs-selector-class">.is-disabled</span> * &#123;
    <span class="hljs-attribute">color</span>: <span class="hljs-number">#6c757d</span>;
    <span class="hljs-comment">/* 不让其点击，将pointer-events设置为none */</span>
    <span class="hljs-attribute">pointer-events</span>: none;
    <span class="hljs-attribute">background</span>: transparent;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来我们来将之前写死的内容进行该打造，大家定位到 <code>Dropdown.vue</code> 文件，<strong>具体代码如下：</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"dropdown"</span>></span>
        <span class="hljs-comment"><!-- 下拉菜单标题 --></span>
        <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"btn btn-outline-light my-2dropdown-toggle"</span> @<span class="hljs-attr">click.prevent</span>=<span class="hljs-string">"toggleOpen()"</span>></span>
            &#123;&#123;title&#125;&#125;
        <span class="hljs-tag"></<span class="hljs-name">a</span>></span>
        <span class="hljs-comment"><!-- 下拉菜单内容 --></span>
        <span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"isOpen"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"dropdown-menu"</span> <span class="hljs-attr">:style</span>=<span class="hljs-string">"&#123; display: 'block' &#125;"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">slot</span>></span><span class="hljs-tag"></<span class="hljs-name">slot</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; defineComponent, ref  &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineComponent(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'Dropdown'</span>,
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">title</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
      <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>
    &#125;
  &#125;,
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> isOpen = ref(<span class="hljs-literal">false</span>)
    <span class="hljs-comment">//点击后打开菜单</span>
    <span class="hljs-keyword">const</span> toggleOpen = <span class="hljs-function">() =></span> &#123;
      isOpen.value = !isOpen.value
    &#125;
    <span class="hljs-keyword">return</span> &#123;
      isOpen,
      toggleOpen
    &#125;
  &#125;
&#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"scss"</span> <span class="hljs-attr">scoped</span>></span>

<span class="hljs-tag"></<span class="hljs-name">style</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过以上代码我们可以了解到，将插槽放到 <code>dropdown-menu</code> 中去。</p>
<hr>
<p>现在，到了最后一步，我们来看把它引入 <code>GlobalHeader.vue</code> 文件中。<strong>具体代码如下：</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">nav</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"navbar navbar-dark bg-primary justify-content-between mb-4 px-4"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"navbar-brand"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span>></span>周一专栏<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"!user.isLogin"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"list-inline mb-0"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"list-inline-item"</span>></span><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"btn btn-outline-light my-2"</span>></span>登录<span class="hljs-tag"></<span class="hljs-name">a</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"list-inline-item"</span>></span><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"btn btn-outline-light my-2"</span>></span>注册<span class="hljs-tag"></<span class="hljs-name">a</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">v-else</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"list-inline mb-0"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"list-inline-item"</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">dropdown</span> <span class="hljs-attr">:title</span>=<span class="hljs-string">"`欢迎你 $&#123;user.name&#125;`"</span>></span>
                    <span class="hljs-tag"><<span class="hljs-name">drop-down-item</span>></span><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"dropdown-item"</span>></span>新建文章<span class="hljs-tag"></<span class="hljs-name">a</span>></span><span class="hljs-tag"></<span class="hljs-name">drop-down-item</span>></span>
                    <span class="hljs-tag"><<span class="hljs-name">drop-down-item</span> <span class="hljs-attr">disabled</span>></span><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"dropdown-item"</span>></span>编辑资料<span class="hljs-tag"></<span class="hljs-name">a</span>></span><span class="hljs-tag"></<span class="hljs-name">drop-down-item</span>></span>
                    <span class="hljs-tag"><<span class="hljs-name">drop-down-item</span>></span><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"dropdown-item"</span>></span>退出登陆<span class="hljs-tag"></<span class="hljs-name">a</span>></span><span class="hljs-tag"></<span class="hljs-name">drop-down-item</span>></span>
                <span class="hljs-tag"></<span class="hljs-name">dropdown</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">nav</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; defineComponent, PropType &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> Dropdown <span class="hljs-keyword">from</span> <span class="hljs-string">'./Dropdown.vue'</span>
<span class="hljs-keyword">import</span> DropDownItem <span class="hljs-keyword">from</span> <span class="hljs-string">'./DropDownItem.vue'</span>

<span class="hljs-keyword">export</span> interface UserProps&#123;
    <span class="hljs-attr">isLogin</span>: boolean;
    name?: string;
    id?: number;
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineComponent(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'GlobalHeader'</span>,
  <span class="hljs-attr">components</span>: &#123;
    Dropdown,
    DropDownItem
  &#125;,
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">user</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Object</span> <span class="hljs-keyword">as</span> PropType<UserProps>,
      required: <span class="hljs-literal">true</span>
    &#125;
  &#125;
&#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"scss"</span> <span class="hljs-attr">scoped</span>></span>

<span class="hljs-tag"></<span class="hljs-name">style</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时，我们来看下<strong>浏览器的显示效果：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/336d85e9d9e742d98acc681efd47bf0d~tplv-k3u1fbpfcp-zoom-1.image" alt="dropdown自定义菜单内容" loading="lazy" referrerpolicy="no-referrer"></p>
<p>大家可以看到，此时的编辑资料已经变成了<strong>灰色</strong>并且无法进行点击和跳转。同时，自定义菜单的内容也一一显示了出来。</p>
<p>到这里，这一步的内容我们就完成啦！接下来我们继续升华这个组件，让它的用户体验更为极致。</p>
<h2 data-id="heading-15">3、组件点击外部区域自动隐藏</h2>
<p>大家可以联想到平常自己点击各大网站时的场景，当点击菜单外部区域时，组件是不是就会自动隐藏。所以，接下来我们就来实现这个功能。</p>
<p>首先我们要明确，<strong>需要完成的两个任务：</strong></p>
<ul>
<li>在 <code>onMounted</code> 时候添加 <code>click</code> 事件，在 <code>onUnmounted</code> 的时候将事件删除；</li>
<li>拿到 <code>Dropdown</code> 的 <code>DOM</code> 元素，从而判断点击的内容是否被这个元素包含。</li>
</ul>
<p>接下来我们定位到 <code>Dropdown.vue</code> 文件，继续升级改造。<strong>具体代码如下：</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"dropdown"</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"dropdownRef"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"btn btn-outline-light my-2 dropdown-toggle"</span> @<span class="hljs-attr">click.prevent</span>=<span class="hljs-string">"toggleOpen()"</span>></span>
            &#123;&#123;title&#125;&#125;
        <span class="hljs-tag"></<span class="hljs-name">a</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"isOpen"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"dropdown-menu"</span> <span class="hljs-attr">:style</span>=<span class="hljs-string">"&#123; display: 'block' &#125;"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">slot</span>></span><span class="hljs-tag"></<span class="hljs-name">slot</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; defineComponent, ref, onMounted, onUnmounted, watch &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineComponent(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'DropDown'</span>,
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">title</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
      <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>
    &#125;
  &#125;,
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> isOpen = ref(<span class="hljs-literal">false</span>)
    <span class="hljs-comment">// 获取ref的dow节点</span>
    <span class="hljs-keyword">const</span> dropdownRef = ref<<span class="hljs-literal">null</span> | HTMLElement>(<span class="hljs-literal">null</span>)
    <span class="hljs-keyword">const</span> toggleOpen = <span class="hljs-function">() =></span> &#123;
      isOpen.value = !isOpen.value
    &#125;
    <span class="hljs-keyword">const</span> handler = <span class="hljs-function">(<span class="hljs-params">e: MouseEvent</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (dropdownRef.value) &#123;
        <span class="hljs-comment">// 用contains来判断是否包含另外一个dow节点</span>
        <span class="hljs-comment">// 当点击的不是当前区域的节点，并且菜单是打开的</span>
        <span class="hljs-keyword">if</span> (!dropdownRef.value.contains(e.target <span class="hljs-keyword">as</span> HTMLElement) && isOpen.value) &#123;
          isOpen.value = <span class="hljs-literal">false</span>
        &#125;
      &#125;
    &#125;
    onMounted(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">document</span>.addEventListener(<span class="hljs-string">'click'</span>, handler)
    &#125;)
    onUnmounted(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">document</span>.removeEventListener(<span class="hljs-string">'click'</span>, handler)
    &#125;)
    <span class="hljs-keyword">return</span> &#123;
      isOpen,
      toggleOpen,
      dropdownRef,
      handler
    &#125;
  &#125;
&#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"scss"</span> <span class="hljs-attr">scoped</span>></span>

<span class="hljs-tag"></<span class="hljs-name">style</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时我们来看下<strong>浏览器的显示效果：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9079036104c6476db6ac66238d1e50ed~tplv-k3u1fbpfcp-zoom-1.image" alt="dowpdown组件点击外部区域自动隐藏" loading="lazy" referrerpolicy="no-referrer"></p>
<p>大家可以看到，改造完 <code>dropdown</code> 的逻辑后，如我们预期所料的，当我们点击组件外部区域时，组件也自动隐藏了。</p>
<h2 data-id="heading-16">4、自定义函数</h2>
<p>到这里，整个 <code>GlobalHeader</code> 组件可以说是相对比较完美了。但是大家有没有发现，在设计 <code>dropdown</code> 组件时，<code>dropdown.vue</code> 的代码好像看起来还稍微有一点点冗余。</p>
<p>这个时候我们可以考虑把它的逻辑抽离出来，单独放到一个自定义函数里面。接下来一起来实现一下吧~</p>
<p>首先我们在 <code>vue3</code> 项目中的 <code>src</code> 文件夹下，新建一个文件夹，命名为 <code>hooks</code> 。之后在 <code>hooks</code> 下新建一个文件，命名为 <code>useClickOutside.ts</code> 。 <code>useClickOutside</code> 的<strong>具体代码如下：</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; ref, onMounted, onUnmounted, Ref &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;

<span class="hljs-keyword">const</span> useClickOutside = <span class="hljs-function">(<span class="hljs-params">elementRef: Ref<<span class="hljs-literal">null</span> | HTMLElement></span>) =></span> &#123;
    <span class="hljs-keyword">const</span> isClickOutside = ref(<span class="hljs-literal">false</span>)
    <span class="hljs-keyword">const</span> handler = <span class="hljs-function">(<span class="hljs-params">e: MouseEvent</span>) =></span> &#123;
        <span class="hljs-keyword">if</span> (elementRef.value)&#123;
            <span class="hljs-keyword">if</span>(elementRef.value.contains(e.target <span class="hljs-keyword">as</span> HTMLElement))&#123;
                isClickOutside.value = <span class="hljs-literal">true</span>   
            &#125;<span class="hljs-keyword">else</span>&#123;
                isClickOutside.value = <span class="hljs-literal">false</span>
            &#125;
        &#125;
    &#125;
    onMounted( <span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">document</span>.addEventListener(<span class="hljs-string">'click'</span>, handler)
    &#125;)
    onUnmounted(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">document</span>.removeEventListener(<span class="hljs-string">'click'</span>, handler)
    &#125;)
    <span class="hljs-keyword">return</span> isClickOutside
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> useClickOutside
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<p>抽离完代码后，我们继续把 <code>Dropdown.vue</code> 化繁为简。具体代码如下：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"dropdown"</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"dropdownRef"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"btn btn-outline-light my-2 dropdown-toggle"</span> @<span class="hljs-attr">click.prevent</span>=<span class="hljs-string">"toggleOpen()"</span>></span>
            &#123;&#123;title&#125;&#125;
        <span class="hljs-tag"></<span class="hljs-name">a</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"isOpen"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"dropdown-menu"</span> <span class="hljs-attr">:style</span>=<span class="hljs-string">"&#123; display: 'block' &#125;"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">slot</span>></span><span class="hljs-tag"></<span class="hljs-name">slot</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; defineComponent, ref, onMounted, onUnmounted, watch &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> useClickOutside <span class="hljs-keyword">from</span> <span class="hljs-string">'../hooks/useClickOutside'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineComponent(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'DropDown'</span>,
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">title</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
      <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>
    &#125;
  &#125;,
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> isOpen = ref(<span class="hljs-literal">false</span>)
    <span class="hljs-comment">// 获取ref的dow节点</span>
    <span class="hljs-keyword">const</span> dropdownRef = ref<<span class="hljs-literal">null</span> | HTMLElement>(<span class="hljs-literal">null</span>)
    <span class="hljs-keyword">const</span> toggleOpen = <span class="hljs-function">() =></span> &#123;
      isOpen.value = !isOpen.value
    &#125;
    <span class="hljs-keyword">const</span> isClickOutside = useClickOutside(dropdownRef)
    <span class="hljs-keyword">if</span> (isOpen.value && isClickOutside) &#123;
      isOpen.value = <span class="hljs-literal">false</span>
    &#125;
    watch(isClickOutside, <span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">if</span> (isOpen.value && isClickOutside.value) &#123;
        isOpen.value = <span class="hljs-literal">false</span>
      &#125;
    &#125;)
    <span class="hljs-keyword">return</span> &#123;
      isOpen,
      toggleOpen,
      dropdownRef
    &#125;
  &#125;
&#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span> <span class="hljs-attr">scoped</span>></span>

<span class="hljs-tag"></<span class="hljs-name">style</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>此时浏览器的显示效果如下：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/73a9a99f6c3d40549dfcca3b1b2556b0~tplv-k3u1fbpfcp-zoom-1.image" alt="dowpdown组件点击外部区域自动隐藏" loading="lazy" referrerpolicy="no-referrer"></p>
<p>大家可以看到，最终的显示效果也是一样的。但是呢，通过代码逻辑抽离，我们整个组件的设计看起来也更加完美，可扩展性也变得更高。</p>
<h2 data-id="heading-17">5、联合效果</h2>
<p>最后，我们把上面所学的GlobalHeader和Columnist结合起来，来看一下一体化的效果。<strong>详情见下图：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/861ebdaa50df48e8bd0080d2ad104f60~tplv-k3u1fbpfcp-zoom-1.image" alt="联合效果" loading="lazy" referrerpolicy="no-referrer"></p>
<p>以上就是关于 <code>ColumnList</code> 和 <code>GlobalHeader</code> 两个组件的实现方式。不知道大家是否还意犹未尽呢~</p>
<p>后面还会持续出关于组件设计的文章，欢迎关注~</p>
<h1 data-id="heading-18">🛒四、结束语</h1>
<p>讲到这里，关于组件 <code>GlobalHeader</code> 和 <code>ColumnList</code> 的设计就结束啦！在设计组件的时候呢，要特别考虑组件的可扩展性。如果一个组件在写的时候，感觉没什么复用度，那么这个时候可能就得思考下，是不是哪个环节出现问题了。多问自己为什么，多问自己这个组件是否能抽离的更好。</p>
<p>以上就是本文的全部内容！如有疑问或文章有误欢迎评论区留言或公众号后台加我微信交流~</p>
<blockquote>
<ul>
<li>
<p>关注公众号<strong>星期一研究室</strong>，第一时间关注学习干货，<strong>更多精选专栏待你解锁</strong>~</p>
</li>
<li>
<p>如果这篇文章对你有用，记得留下脚印再走哦~</p>
</li>
<li>
<p>我们下期见！🥂🥂🥂</p>
</li>
</ul>
</blockquote>
<h1 data-id="heading-19">🐣彩蛋 One More Thing</h1>
<h2 data-id="heading-20">基础知识回顾</h2>
<ul>
<li><a href="https://juejin.cn/column/6976040277068759077" target="_blank" title="https://juejin.cn/column/6976040277068759077">vuejs基础知识</a></li>
<li><a href="https://juejin.cn/column/6979926803238354952" target="_blank" title="https://juejin.cn/column/6979926803238354952">ts基础知识</a></li>
</ul>
<h2 data-id="heading-21">软件推荐</h2>
<p>这里给大家推荐文章用到的一个画图软件：<strong>Axure RP 9</strong></p>
<p>Axure RP 旨在用于画低保真原型图，对于开发者来说也是极其友好的。丰富的控件库和动画交互，可以满足日常画图的大部分需求。</p>
<p>安利一波~</p>
<p>👋👋👋</p></div>  
</div>
            
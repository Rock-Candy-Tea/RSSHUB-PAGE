
---
title: '尤雨溪的5KB petite-vue源码解析'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/31690ba72aff47cc9fefc53d892c3de1~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 13 Jul 2021 17:55:26 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/31690ba72aff47cc9fefc53d892c3de1~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">写在开头</h4>
<ul>
<li>近期尤雨溪发布了5kb的petite-vue,好奇的我,clone了他的源码，给大家解析一波。</li>
<li>最近由于工作事情多，所以放缓了原创的脚步！大家谅解</li>
<li>想看我往期手写源码+各种源码解析的可以关注我公众号看我的<code>GitHub</code>,基本上前端的框架源码都有解析过</li>
</ul>
<h4 data-id="heading-1">正式开始</h4>
<ul>
<li><code>petite-vue</code>是只有5kb的vue,我们先找到仓库，克隆下来</li>
</ul>
<pre><code class="copyable">https://github.com/vuejs/petite-vue
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>克隆下来后发现，用的是vite + petite-vue + 多页面形式启动的</p>
</li>
<li>
<p>启动命令：</p>
</li>
</ul>
<pre><code class="copyable">git clone https://github.com/vuejs/petite-vue
cd /petite-vue
npm i 
npm run dev

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>然后打开<code>http://localhost:3000/</code>即可看到页面:</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/31690ba72aff47cc9fefc53d892c3de1~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<h4 data-id="heading-2">保姆式教学</h4>
<ul>
<li>项目已经启动了，接下来我们先解析下项目入口,由于使用的构建工具是<code>vite</code>,从根目录下的<code>index.html</code>人口找起：</li>
</ul>
<pre><code class="copyable"><h2>Examples</h2>
<ul>
  <li><a href="/examples/todomvc.html">TodoMVC</a></li>
  <li><a href="/examples/commits.html">Commits</a></li>
  <li><a href="/examples/grid.html">Grid</a></li>
  <li><a href="/examples/markdown.html">Markdown</a></li>
  <li><a href="/examples/svg.html">SVG</a></li>
  <li><a href="/examples/tree.html">Tree</a></li>
</ul>

<h2>Tests</h2>
<ul>
  <li><a href="/tests/scope.html">v-scope</a></li>
  <li><a href="/tests/effect.html">v-effect</a></li>
  <li><a href="/tests/bind.html">v-bind</a></li>
  <li><a href="/tests/on.html">v-on</a></li>
  <li><a href="/tests/if.html">v-if</a></li>
  <li><a href="/tests/for.html">v-for</a></li>
  <li><a href="/tests/model.html">v-model</a></li>
  <li><a href="/tests/once.html">v-once</a></li>
  <li><a href="/tests/multi-mount.html">Multi mount</a></li>
</ul>

<style>
  a &#123;
    font-size: 18px;
  &#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>这就是多页面模式+vue+vite的一个演示项目，我们找到一个简单的演示页<code>commits</code>:</li>
</ul>
<pre><code class="copyable"><script type="module">
  import &#123; createApp, reactive &#125; from '../src'

  const API_URL = `https://api.github.com/repos/vuejs/vue-next/commits?per_page=3&sha=`

  createApp(&#123;
    branches: ['master', 'v2-compat'],
    currentBranch: 'master',
    commits: null,

    truncate(v) &#123;
      const newline = v.indexOf('\n')
      return newline > 0 ? v.slice(0, newline) : v
    &#125;,

    formatDate(v) &#123;
      return v.replace(/T|Z/g, ' ')
    &#125;,

    fetchData() &#123;
      fetch(`$&#123;API_URL&#125;$&#123;this.currentBranch&#125;`)
        .then((res) => res.json())
        .then((data) => &#123;
          this.commits = data
        &#125;)
    &#125;
  &#125;).mount()
</script>

<div v-scope v-effect="fetchData()">
  <h1>Latest Vue.js Commits</h1>
  <template v-for="branch in branches">
    <input
      type="radio"
      :id="branch"
      :value="branch"
      name="branch"
      v-model="currentBranch"
    />
    <label :for="branch">&#123;&#123; branch &#125;&#125;</label>
  </template>
  <p>vuejs/vue@&#123;&#123; currentBranch &#125;&#125;</p>
  <ul>
    <li v-for="&#123; html_url, sha, author, commit &#125; in commits">
      <a :href="html_url" target="_blank" class="commit"
        >&#123;&#123; sha.slice(0, 7) &#125;&#125;</a
      >
      - <span class="message">&#123;&#123; truncate(commit.message) &#125;&#125;</span><br />
      by
      <span class="author"
        ><a :href="author.html_url" target="_blank"
          >&#123;&#123; commit.author.name &#125;&#125;</a
        ></span
      >
      at <span class="date">&#123;&#123; formatDate(commit.author.date) &#125;&#125;</span>
    </li>
  </ul>
</div>

<style>
  body &#123;
    font-family: 'Helvetica', Arial, sans-serif;
  &#125;
  a &#123;
    text-decoration: none;
    color: #f66;
  &#125;
  li &#123;
    line-height: 1.5em;
    margin-bottom: 20px;
  &#125;
  .author, .date &#123;
    font-weight: bold;
  &#125;
</style>

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>可以看到页面顶部引入了</li>
</ul>
<pre><code class="copyable">import &#123; createApp, reactive &#125; from '../src'
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">开始从源码启动函数入手</h4>
<ul>
<li>启动函数为<code>createApp</code>,找到源码:</li>
</ul>
<pre><code class="copyable">//index.ts
export &#123; createApp &#125; from './app'
...
import &#123; createApp &#125; from './app'

let s
if ((s = document.currentScript) && s.hasAttribute('init')) &#123;
  createApp().mount()
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>Document.currentScript 属性返回当前正在运行的脚本所属的 <code><script> </code>元素。调用此属性的脚本不能是 JavaScript 模块，模块应当使用 import.meta 对象。</p>
</blockquote>
<ul>
<li>
<p>上面这段代码意思是，创建<code>s</code>变量记录当前运行的脚本元素，如果存在制定属性<code>init</code>，那么就调用createApp和mount方法.</p>
</li>
<li>
<p>但是这里项目里面是主动调用了暴露的<code>createApp</code>方法，我们去看看<code>createApp</code>这个方法的源码，有大概80行代码</p>
</li>
</ul>
<pre><code class="copyable">import &#123; reactive &#125; from '@vue/reactivity'
import &#123; Block &#125; from './block'
import &#123; Directive &#125; from './directives'
import &#123; createContext &#125; from './context'
import &#123; toDisplayString &#125; from './directives/text'
import &#123; nextTick &#125; from './scheduler'

export default function createApp(initialData?: any)&#123;
...
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>createApp方法接收一个初始数据，可以是任意类型，也可以不传。这个方法是入口函数，依赖的函数也比较多，我们要静下心来。这个函数进来就搞了一堆东西</li>
</ul>
<pre><code class="copyable">createApp(initialData?: any)&#123;
   // root context
  const ctx = createContext()
  if (initialData) &#123;
    ctx.scope = reactive(initialData)
  &#125;

  // global internal helpers
  ctx.scope.$s = toDisplayString
  ctx.scope.$nextTick = nextTick
  ctx.scope.$refs = Object.create(null)

  let rootBlocks: Block[]

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>上面这段代码，是创建了一个ctx上下文对象，并且给它上面赋予了很多属性和方法。然后提供给createApp返回的对象使用</li>
<li><code>createContext</code>创建上下文:</li>
</ul>
<pre><code class="copyable">export const createContext = (parent?: Context): Context => &#123;
  const ctx: Context = &#123;
    ...parent,
    scope: parent ? parent.scope : reactive(&#123;&#125;),
    dirs: parent ? parent.dirs : &#123;&#125;,
    effects: [],
    blocks: [],
    cleanups: [],
    effect: (fn) => &#123;
      if (inOnce) &#123;
        queueJob(fn)
        return fn as any
      &#125;
      const e: ReactiveEffect = rawEffect(fn, &#123;
        scheduler: () => queueJob(e)
      &#125;)
      ctx.effects.push(e)
      return e
    &#125;
  &#125;
  return ctx
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>根据传入的父对象，做一个简单的继承，然后返回一个新的<code>ctx</code>对象。</li>
</ul>
<blockquote>
<p>我一开始差点掉进误区，我写这篇文章，是想让大家明白简单的<code>vue</code>原理，像上次我写的掘金编辑器源码解析，写得太细，太累了。这次简化下，让大家都能懂，上面这些东西不重要。这个<code>createApp</code>函数返回了一个对象：</p>
</blockquote>
<pre><code class="copyable">return &#123;
  directive(name: string, def?: Directive) &#123;
      if (def) &#123;
        ctx.dirs[name] = def
        return this
      &#125; else &#123;
        return ctx.dirs[name]
      &#125;
    &#125;,
mount(el?: string | Element | null)&#123;&#125;...,
unmount()&#123;&#125;...
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>对象上有三个方法，例如<code>directive</code>指令就会用到<code>ctx</code>的属性和方法。所以上面一开始搞一大堆东西挂载到<code>ctx</code>上，是为了给下面的方法使用</p>
</li>
<li>
<p>重点看<code>mount</code>方法:</p>
</li>
</ul>
<pre><code class="copyable">     mount(el?: string | Element | null) &#123;
     if (typeof el === 'string') &#123;
        el = document.querySelector(el)
        if (!el) &#123;
          import.meta.env.DEV &&
            console.error(`selector $&#123;el&#125; has no matching element.`)
          return
        &#125;
      &#125;
     ...
    
     &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>首先会判断如果传入的是string,那么就回去找这个节点，否则就会找<code>document</code></li>
</ul>
<pre><code class="copyable">el = el || document.documentElement
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>定义<code>roots</code>,一个节点数组</li>
</ul>
<pre><code class="copyable">let roots: Element[]
     if (el.hasAttribute('v-scope')) &#123;
       roots = [el]
     &#125; else &#123;
       roots = [...el.querySelectorAll(`[v-scope]`)].filter(
         (root) => !root.matches(`[v-scope] [v-scope]`)
       )
     &#125;
     if (!roots.length) &#123;
       roots = [el]
     &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>如果有<code>v-scope</code>这个属性，就把el存入数组中，赋值给<code>roots</code>,否则就要去这个<code>el</code>下面找到所以的带<code>v-scope</code>属性的节点，然后筛选出这些带<code>v-scope</code>属性下面的不带<code>v-scope</code>属性的节点,塞入<code>roots</code>数组</li>
</ul>
<blockquote>
<p>此时如果<code>roots</code>还是为空，那么就把<code>el</code>放进去。
这里在开发模式下有个警告：<code>Mounting on documentElement - this is non-optimal as petite-vue </code>,意思是用<code>document</code>不是最佳选择。</p>
</blockquote>
<ul>
<li>在把<code>roots</code>处理完毕后，开始行动。</li>
</ul>
<pre><code class="copyable">  rootBlocks = roots.map((el) => new Block(el, ctx, true))
      // remove all v-cloak after mount
      ;[el, ...el.querySelectorAll(`[v-cloak]`)].forEach((el) =>
        el.removeAttribute('v-cloak')
      )
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>这个<code>Block</code>构造函数是重点，将节点和上下文传入以后，外面就只是去除掉'v-cloak'属性，这个mount函数就调用结束了，那么怎么原理就隐藏在<code>Block</code>里面。</li>
</ul>
<blockquote>
<p>这里带着一个问题，我们目前仅仅拿到了<code>el</code>这个<code>dom</code>节点，但是vue里面都是模板语法，那些模板语法是怎么转化成真的dom呢？</p>
</blockquote>
<ul>
<li>Block原来不是一个函数，而是一个class.</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e86503ad139474c9ccbf4ed3e4b6ede~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>在constructor构造函数中可以看到</li>
</ul>
<pre><code class="copyable">  constructor(template: Element, parentCtx: Context, isRoot = false) &#123;
    this.isFragment = template instanceof HTMLTemplateElement

    if (isRoot) &#123;
      this.template = template
    &#125; else if (this.isFragment) &#123;
      this.template = (template as HTMLTemplateElement).content.cloneNode(
        true
      ) as DocumentFragment
    &#125; else &#123;
      this.template = template.cloneNode(true) as Element
    &#125;

    if (isRoot) &#123;
      this.ctx = parentCtx
    &#125; else &#123;
      // create child context
      this.parentCtx = parentCtx
      parentCtx.blocks.push(this)
      this.ctx = createContext(parentCtx)
    &#125;

    walk(this.template, this.ctx)
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>以上代码可以分为三个逻辑
<ul>
<li>创建模板<code>template</code>（使用clone节点的方式，由于<code>dom</code>节点获取到以后是一个对象，所以做了一层clone）</li>
<li>如果不是根节点就递归式的继承<code>ctx</code>上下文</li>
<li>在处理完ctx和Template后，调用<code>walk</code>函数</li>
</ul>
</li>
<li><code>walk</code>函数解析：</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/823439b44a1b42eeb71e507bc549741f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p>会先根据nodetype进行判断，然后做不同的处理</p>
</li>
<li>
<p>如果是一个<code>element</code>节点,就要处理不同的指令，例如<code>v-if</code></p>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/169a0b53924a4f009520f2be32e39e39~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>这里有一个工具函数要先看看</li>
</ul>
<pre><code class="copyable">export const checkAttr = (el: Element, name: string): string | null => &#123;
  const val = el.getAttribute(name)
  if (val != null) el.removeAttribute(name)
  return val
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>这个函数意思是检测下这个节点是否包含<code>v-xx</code>的属性，然后返回这个结果并且删除这个属性</p>
</li>
<li>
<p>拿<code>v-if</code>举例，当判断这个节点有<code>v-if</code>属性后，那么就去调用方法处理它，并且删除掉这个属性（作为标识已经处理过了）</p>
</li>
</ul>
<blockquote>
<p>这里本了我想12点前睡觉的，别人告诉我只有5kb,我想着找个最简单的指令解析下，结果每个指令代码都有一百多行，今晚加班到九点多，刚把微前端改造的上了生产，还是想着坚持下给大家写完吧。现在已经凌晨了</p>
</blockquote>
<ul>
<li><code>v-if</code>处理函数大概60行</li>
</ul>
<pre><code class="copyable">export const _if = (el: Element, exp: string, ctx: Context) => &#123;
...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>首先_if函数先拿到el节点和exp这个v-if的值，以及ctx上下文对象</li>
</ul>
<pre><code class="copyable">  if (import.meta.env.DEV && !exp.trim()) &#123;
    console.warn(`v-if expression cannot be empty.`)
  &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>如果为空的话报出警告</li>
<li>然后拿到el节点的父节点，并且根据这个exp的值创建一个comment注释节点（暂存）并且插入到el之前，同时创建一个branches数组，储存exp和el</li>
</ul>
<pre><code class="copyable"> const parent = el.parentElement!
  const anchor = new Comment('v-if')
  parent.insertBefore(anchor, el)

  const branches: Branch[] = [
    &#123;
      exp,
      el
    &#125;
  ]

  // locate else branch
  let elseEl: Element | null
  let elseExp: string | null
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>Comment 接口代表标签（markup）之间的文本符号（textual notations）。尽管它通常不会显示出来，但是在查看源码时可以看到它们。在 HTML 和 XML 里，注释（Comments）为 <code>'<!--' 和 '-->'</code> 之间的内容。在 XML 里，注释中不能出现字符序列 '--'。</p>
</blockquote>
<ul>
<li>接着创建<code>elseEl</code>和<code>elseExp</code>的变量，并且循环遍历搜集了所有的else分支，并且存储在了branches里面</li>
</ul>
<pre><code class="copyable">  while ((elseEl = el.nextElementSibling)) &#123;
    elseExp = null
    if (
      checkAttr(elseEl, 'v-else') === '' ||
      (elseExp = checkAttr(elseEl, 'v-else-if'))
    ) &#123;
      parent.removeChild(elseEl)
      branches.push(&#123; exp: elseExp, el: elseEl &#125;)
    &#125; else &#123;
      break
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>这样Branches里面就有了v-if所有的分支啦,这里可以看成是一个树的遍历（广度优先搜索）</p>
</blockquote>
<ul>
<li>接下来根据副作用函数的触发，每次都去branches里面遍历寻找到需要激活的那个分支，将节点插入到parentNode中，并且返回nextNode即可实现<code>v-if</code>的效果</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/689fa7cb7f8147af9b65f564332813b8~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>这里由于都是html,给我们省去了虚拟dom这些东西,可是上面仅仅是处理单个节点，如果是深层级的<code>dom</code>节点，就要用到后面的深度优先搜索了</p>
</blockquote>
<pre><code class="copyable"> // process children first before self attrs
    walkChildren(el, ctx)


const walkChildren = (node: Element | DocumentFragment, ctx: Context) => &#123;
  let child = node.firstChild
  while (child) &#123;
    child = walk(child, ctx) || child.nextSibling
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>当节点上没有<code>v-if</code>之类的属性时，这个时候就去取他们的第一个子节点去做上述的动作，匹配每个<code>v-if v-for</code>之类的指令</li>
</ul>
<h5 data-id="heading-4">如果是文本节点</h5>
<pre><code class="copyable">else if (type === 3) &#123;
    // Text
    const data = (node as Text).data
    if (data.includes('&#123;&#123;')) &#123;
      let segments: string[] = []
      let lastIndex = 0
      let match
      while ((match = interpolationRE.exec(data))) &#123;
        const leading = data.slice(lastIndex, match.index)
        if (leading) segments.push(JSON.stringify(leading))
        segments.push(`$s($&#123;match[1]&#125;)`)
        lastIndex = match.index + match[0].length
      &#125;
      if (lastIndex < data.length) &#123;
        segments.push(JSON.stringify(data.slice(lastIndex)))
      &#125;
      applyDirective(node, text, segments.join('+'), ctx)
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>这个地方很经典，是通过正则匹配，然后一系列操作匹配，最终返回了一个文本字符串。这个代码是挺精髓的，但是由于时间关系这里不细讲了</p>
</blockquote>
<ul>
<li><code>applyDirective</code>函数</li>
</ul>
<pre><code class="copyable">const applyDirective = (
  el: Node,
  dir: Directive<any>,
  exp: string,
  ctx: Context,
  arg?: string,
  modifiers?: Record<string, true>
) => &#123;
  const get = (e = exp) => evaluate(ctx.scope, e, el)
  const cleanup = dir(&#123;
    el,
    get,
    effect: ctx.effect,
    ctx,
    exp,
    arg,
    modifiers
  &#125;)
  if (cleanup) &#123;
    ctx.cleanups.push(cleanup)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>接下来<code>nodeType是11</code>意味着是一个Fragment节点，那么直接从它的第一个子节点开始即可</li>
</ul>
<pre><code class="copyable">&#125; else if (type === 11) &#123;
    walkChildren(node as DocumentFragment, ctx)
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-5">nodeType 说 明</h5>
<pre><code class="copyable">此属性只读且传回一个数值。
有效的数值符合以下的型别：
1-ELEMENT
2-ATTRIBUTE
3-TEXT
4-CDATA
5-ENTITY REFERENCE
6-ENTITY
7-PI (processing instruction)
8-COMMENT
9-DOCUMENT
10-DOCUMENT TYPE
11-DOCUMENT FRAGMENT
12-NOTATION
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">梳理总结</h4>
<ul>
<li>拉取代码</li>
<li>启动项目</li>
<li>找到入口createApp函数</li>
<li>定义ctx以及层层继承</li>
<li>发现block方法</li>
<li>根据节点是element还是text分开做处理</li>
<li>如果是text就去通过正则匹配，拿到数据返回字符串</li>
<li>如果是element就去做一个递归处理，解析所有的<code>v-if</code>等模板语法，返回真实的节点</li>
</ul>
<blockquote>
<p>这里所有的dom节点改变，都是直接通过js操作dom</p>
</blockquote>
<h4 data-id="heading-7">有趣的源码补充</h4>
<ul>
<li>这里的nextTick实现，是直接通过<code>promise.then</code></li>
</ul>
<pre><code class="copyable">const p = Promise.resolve()

export const nextTick = (fn: () => void) => p.then(fn)

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">写在最后</h4>
<ul>
<li>有点晚了，写到1点多不知不觉，如果感觉写得不错，帮我点波再看/关注/赞吧</li>
<li>如果你想看往期的源码分析文章可以关注我的<code>gitHub</code> - 公众号：<code>前端巅峰 </code></li>
</ul></div>  
</div>
            
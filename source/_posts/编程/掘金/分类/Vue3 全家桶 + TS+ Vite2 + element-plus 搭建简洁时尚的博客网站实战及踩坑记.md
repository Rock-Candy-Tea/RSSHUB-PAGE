
---
title: 'Vue3 全家桶 + TS+ Vite2 + element-plus 搭建简洁时尚的博客网站实战及踩坑记'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d374db50212c4e5481ac97bf78cd99f8~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 06 May 2021 05:50:42 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d374db50212c4e5481ac97bf78cd99f8~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d374db50212c4e5481ac97bf78cd99f8~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>五一期间，花了 3 天时间，边学 Vue3 和 Vite2，边重构自己的项目，终于都用 Vue3 + TypeScript + Vite2 + Vuex4 + Vue-Router4 + element-plus 重构完啦！</p>
<p>终于完成一项心心念念的 2021 年度目标了 ✌️</p>
<p>项目地址:</p>
<blockquote>
<p><a href="https://github.com/biaochenxuying/blog-vue-typescript" target="_blank" rel="nofollow noopener noreferrer">github.com/biaochenxuy…</a></p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/15929f581416455e96a9bac789c55862~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">效果</h2>
<p>效果图：</p>
<ul>
<li>pc 端</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/823ec327136b41f2b6752402587d3bb3~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>移动端</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1665409b8cd246cb90c7ec21312cb2d5~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>完整效果请看：</p>
<blockquote>
<p><a href="https://biaochenxuying.cn/" target="_blank" rel="nofollow noopener noreferrer">biaochenxuying.cn</a></p>
</blockquote>
<h2 data-id="heading-1">功能</h2>
<h3 data-id="heading-2">已经完成功能</h3>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" checked disabled> 登录</li>
<li class="task-list-item"><input type="checkbox" checked disabled> 注册</li>
<li class="task-list-item"><input type="checkbox" checked disabled> 文章列表</li>
<li class="task-list-item"><input type="checkbox" checked disabled> 文章归档</li>
<li class="task-list-item"><input type="checkbox" checked disabled> 标签</li>
<li class="task-list-item"><input type="checkbox" checked disabled> 关于</li>
<li class="task-list-item"><input type="checkbox" checked disabled> 点赞与评论</li>
<li class="task-list-item"><input type="checkbox" checked disabled> 留言</li>
<li class="task-list-item"><input type="checkbox" checked disabled> 历程</li>
<li class="task-list-item"><input type="checkbox" checked disabled> 文章详情（支持代码语法高亮）</li>
<li class="task-list-item"><input type="checkbox" checked disabled> 文章详情目录</li>
<li class="task-list-item"><input type="checkbox" checked disabled> 移动端适配</li>
<li class="task-list-item"><input type="checkbox" checked disabled> github 授权登录</li>
</ul>
<h2 data-id="heading-3">前端主要技术</h2>
<p>所有技术都是当前最新的。</p>
<ul>
<li>vue：^3.0.5</li>
<li>typescript : ^4.1.3</li>
<li>element-plus: ^1.0.2-beta.41</li>
<li>vue-router : ^4.0.6</li>
<li>vite: ^2.2.3</li>
<li>vuex: ^4.0.0</li>
<li>axios: ^0.21.1</li>
<li>highlight.js: ^10.7.2</li>
<li>marked：^2.0.3</li>
</ul>
<h2 data-id="heading-4">1. 初化化项目</h2>
<p>用 vite-app 创建项目</p>
<pre><code class="hljs language-js copyable" lang="js">yarn create vite-app <project-name>

# 或者
npm init vite-app <project-name>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后按照提示操作即可！</p>
<p>进入项目，安装依赖</p>
<pre><code class="hljs language-js copyable" lang="js">cd <project-name>

yarn # 或 npm i
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行项目</p>
<pre><code class="hljs language-js copyable" lang="js">yarn dev 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打开浏览器 <a href="http://localhost:3000/" target="_blank" rel="nofollow noopener noreferrer">http://localhost:3000</a> 查看</p>
<h2 data-id="heading-5">2. 引入 TypeScript</h2>
<p>在创建项目的时候可以 TypeScript 的，如果你选择了 TypeScript ，可以忽略第 2 个步骤。</p>
<p>加入 ts 依赖</p>
<pre><code class="hljs language-js copyable" lang="js">yarn add --dev typescript
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 项目根目录下创建 TypeScript 的配置文件 tsconfig.json</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-string">"compilerOptions"</span>: &#123;
    <span class="hljs-comment">// 允许从没有设置默认导出的模块中默认导入。这并不影响代码的输出，仅为了类型检查。</span>
    <span class="hljs-string">"allowSyntheticDefaultImports"</span>: <span class="hljs-literal">true</span>,
    
    <span class="hljs-comment">// 解析非相对模块名的基准目录</span>
    <span class="hljs-string">"baseUrl"</span>: <span class="hljs-string">"."</span>,

    <span class="hljs-string">"esModuleInterop"</span>: <span class="hljs-literal">true</span>,

    <span class="hljs-comment">// 从 tslib 导入辅助工具函数（比如 __extends， __rest等）</span>
    <span class="hljs-string">"importHelpers"</span>: <span class="hljs-literal">true</span>,

    <span class="hljs-comment">// 指定生成哪个模块系统代码</span>
    <span class="hljs-string">"module"</span>: <span class="hljs-string">"esnext"</span>,

    <span class="hljs-comment">// 决定如何处理模块。</span>
    <span class="hljs-string">"moduleResolution"</span>: <span class="hljs-string">"node"</span>,

    <span class="hljs-comment">// 启用所有严格类型检查选项。</span>
    <span class="hljs-comment">// 启用 --strict相当于启用 --noImplicitAny, --noImplicitThis, --alwaysStrict， </span>
    <span class="hljs-comment">// --strictNullChecks和 --strictFunctionTypes和--strictPropertyInitialization。</span>
    <span class="hljs-string">"strict"</span>: <span class="hljs-literal">true</span>,

    <span class="hljs-comment">// 生成相应的 .map文件。</span>
    <span class="hljs-string">"sourceMap"</span>: <span class="hljs-literal">true</span>,

    <span class="hljs-comment">// 忽略所有的声明文件（ *.d.ts）的类型检查。</span>
    <span class="hljs-string">"skipLibCheck"</span>: <span class="hljs-literal">true</span>,

    <span class="hljs-comment">// 指定ECMAScript目标版本 </span>
    <span class="hljs-string">"target"</span>: <span class="hljs-string">"esnext"</span>,
    
    <span class="hljs-comment">// 要包含的类型声明文件名列表</span>
    <span class="hljs-string">"types"</span>: [

    ],

    <span class="hljs-string">"isolatedModules"</span>: <span class="hljs-literal">true</span>,

    <span class="hljs-comment">// 模块名到基于 baseUrl的路径映射的列表。</span>
    <span class="hljs-string">"paths"</span>: &#123;
      <span class="hljs-string">"@/*"</span>: [
        <span class="hljs-string">"src/*"</span>
      ]
    &#125;,
    <span class="hljs-comment">// 编译过程中需要引入的库文件的列表。</span>
    <span class="hljs-string">"lib"</span>: [
      <span class="hljs-string">"ESNext"</span>,
      <span class="hljs-string">"DOM"</span>,
      <span class="hljs-string">"DOM.Iterable"</span>,
      <span class="hljs-string">"ScriptHost"</span>
    ]
  &#125;,
  <span class="hljs-string">"include"</span>: [
    <span class="hljs-string">"src/**/*.ts"</span>,
    <span class="hljs-string">"src/**/*.tsx"</span>,
    <span class="hljs-string">"src/**/*.vue"</span>,
    <span class="hljs-string">"tests/**/*.ts"</span>,
    <span class="hljs-string">"tests/**/*.tsx"</span>
  ],
  <span class="hljs-string">"exclude"</span>: [
    <span class="hljs-string">"node_modules"</span>
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 src 目录下新加 shim.d.ts 文件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/* eslint-disable */</span>
<span class="hljs-keyword">import</span> type &#123; DefineComponent &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>

declare <span class="hljs-built_in">module</span> <span class="hljs-string">'*.vue'</span> &#123;
  <span class="hljs-keyword">const</span> component: DefineComponent<&#123;&#125;, &#123;&#125;, any>
  <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> component
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>把 main.js 修改成 main.ts</p>
<p>在根目录，打开 Index.html</p>
<pre><code class="hljs language-js copyable" lang="js"><script type=<span class="hljs-string">"module"</span> src=<span class="hljs-string">"/src/main.js"</span>></script>
修改为：
<script type=<span class="hljs-string">"module"</span> src=<span class="hljs-string">"/src/main.ts"</span>></script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">3. 引入 eslint</h2>
<p>安装 eslint prettier 依赖</p>
<p><code>@typescript-eslint/parser @typescr ipt-eslint/eslint-plugin</code> 为 eslint 对 typescript 支持。</p>
<pre><code class="hljs language-js copyable" lang="js">yarn add --dev eslint prettier eslint-config-prettier eslint-plugin-prettier eslint-plugin-vue @typescript-eslint/parser @typescr ipt-eslint/eslint-plugin
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在根目录下建立 eslint 配置文件： .eslintrc.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">parser</span>: <span class="hljs-string">'vue-eslint-parser'</span>,
  <span class="hljs-attr">parserOptions</span>: &#123;
    <span class="hljs-attr">parser</span>: <span class="hljs-string">'@typescript-eslint/parser'</span>,
    <span class="hljs-attr">ecmaVersion</span>: <span class="hljs-number">2020</span>,
    <span class="hljs-attr">sourceType</span>: <span class="hljs-string">'module'</span>,
    <span class="hljs-attr">ecmaFeatures</span>: &#123;
      <span class="hljs-attr">jsx</span>: <span class="hljs-literal">true</span>
    &#125;
  &#125;,
  <span class="hljs-attr">extends</span>: [
    <span class="hljs-string">'plugin:vue/vue3-recommended'</span>,
    <span class="hljs-string">'plugin:@typescript-eslint/recommended'</span>,
    <span class="hljs-string">'prettier/@typescript-eslint'</span>,
    <span class="hljs-string">'plugin:prettier/recommended'</span>
  ],
  <span class="hljs-attr">rules</span>: &#123;
    <span class="hljs-string">'@typescript-eslint/ban-ts-ignore'</span>: <span class="hljs-string">'off'</span>,
    <span class="hljs-string">'@typescript-eslint/explicit-function-return-type'</span>: <span class="hljs-string">'off'</span>,
    <span class="hljs-string">'@typescript-eslint/no-explicit-any'</span>: <span class="hljs-string">'off'</span>,
    <span class="hljs-string">'@typescript-eslint/no-var-requires'</span>: <span class="hljs-string">'off'</span>,
    <span class="hljs-string">'@typescript-eslint/no-empty-function'</span>: <span class="hljs-string">'off'</span>,
    <span class="hljs-string">'vue/custom-event-name-casing'</span>: <span class="hljs-string">'off'</span>,
    <span class="hljs-string">'no-use-before-define'</span>: <span class="hljs-string">'off'</span>,
    <span class="hljs-comment">// 'no-use-before-define': [</span>
    <span class="hljs-comment">//   'error',</span>
    <span class="hljs-comment">//   &#123;</span>
    <span class="hljs-comment">//     functions: false,</span>
    <span class="hljs-comment">//     classes: true,</span>
    <span class="hljs-comment">//   &#125;,</span>
    <span class="hljs-comment">// ],</span>
    <span class="hljs-string">'@typescript-eslint/no-use-before-define'</span>: <span class="hljs-string">'off'</span>,
    <span class="hljs-comment">// '@typescript-eslint/no-use-before-define': [</span>
    <span class="hljs-comment">//   'error',</span>
    <span class="hljs-comment">//   &#123;</span>
    <span class="hljs-comment">//     functions: false,</span>
    <span class="hljs-comment">//     classes: true,</span>
    <span class="hljs-comment">//   &#125;,</span>
    <span class="hljs-comment">// ],</span>
    <span class="hljs-string">'@typescript-eslint/ban-ts-comment'</span>: <span class="hljs-string">'off'</span>,
    <span class="hljs-string">'@typescript-eslint/ban-types'</span>: <span class="hljs-string">'off'</span>,
    <span class="hljs-string">'@typescript-eslint/no-non-null-assertion'</span>: <span class="hljs-string">'off'</span>,
    <span class="hljs-string">'@typescript-eslint/explicit-module-boundary-types'</span>: <span class="hljs-string">'off'</span>,
    <span class="hljs-string">'@typescript-eslint/no-unused-vars'</span>: [
      <span class="hljs-string">'error'</span>,
      &#123;
        <span class="hljs-attr">argsIgnorePattern</span>: <span class="hljs-string">'^h$'</span>,
        <span class="hljs-attr">varsIgnorePattern</span>: <span class="hljs-string">'^h$'</span>
      &#125;
    ],
    <span class="hljs-string">'no-unused-vars'</span>: [
      <span class="hljs-string">'error'</span>,
      &#123;
        <span class="hljs-attr">argsIgnorePattern</span>: <span class="hljs-string">'^h$'</span>,
        <span class="hljs-attr">varsIgnorePattern</span>: <span class="hljs-string">'^h$'</span>
      &#125;
    ],
    <span class="hljs-string">'space-before-function-paren'</span>: <span class="hljs-string">'off'</span>,
    <span class="hljs-attr">quotes</span>: [<span class="hljs-string">'error'</span>, <span class="hljs-string">'single'</span>],
    <span class="hljs-string">'comma-dangle'</span>: [<span class="hljs-string">'error'</span>, <span class="hljs-string">'never'</span>]
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>建立 prettier.config.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">printWidth</span>: <span class="hljs-number">100</span>,
  <span class="hljs-attr">tabWidth</span>: <span class="hljs-number">2</span>,
  <span class="hljs-attr">useTabs</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">semi</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 未尾逗号</span>
  <span class="hljs-attr">vueIndentScriptAndStyle</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">singleQuote</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 单引号</span>
  <span class="hljs-attr">quoteProps</span>: <span class="hljs-string">'as-needed'</span>,
  <span class="hljs-attr">bracketSpacing</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">trailingComma</span>: <span class="hljs-string">'none'</span>, <span class="hljs-comment">// 未尾分号</span>
  <span class="hljs-attr">jsxBracketSameLine</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">jsxSingleQuote</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">arrowParens</span>: <span class="hljs-string">'always'</span>,
  <span class="hljs-attr">insertPragma</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">requirePragma</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">proseWrap</span>: <span class="hljs-string">'never'</span>,
  <span class="hljs-attr">htmlWhitespaceSensitivity</span>: <span class="hljs-string">'strict'</span>,
  <span class="hljs-attr">endOfLine</span>: <span class="hljs-string">'lf'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">4. vue-router、vuex</h2>
<pre><code class="copyable">npm install vue-router@4 vuex
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">4.1 vuex</h3>
<p>在根目录下创建 store/index.ts</p>
<pre><code class="copyable">import &#123; InjectionKey &#125; from 'vue'
import &#123; createStore, Store &#125; from 'vuex'

export interface State &#123;
  count: number
&#125;

export const key: InjectionKey<Store<State>> = Symbol()

export const store = createStore<State>(&#123;
  state() &#123;
    return &#123;
      count: 0
    &#125;
  &#125;,
  mutations: &#123;
    increment(state) &#123;
      state.count++
    &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>main.ts 修改</p>
<pre><code class="copyable">import &#123; createApp &#125; from 'vue'
import &#123; store, key &#125; from './store'
import App from './App'
import './index.css'

const app = createApp(App)

app.use(store, key)

app.mount('#app')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>components/HelloWord.vue 修改</p>
<pre><code class="copyable"><template>
  <h1>&#123;&#123; msg &#125;&#125;</h1>
  <button @click="inCrement"> count is: </button>
  <p>&#123;&#123; count &#125;&#125;</p>
</template>

<script>
  import &#123; defineComponent, computed &#125; from 'vue'
  import &#123; useStore &#125; from 'vuex'
  import &#123; key &#125; from '../store'

  export default defineComponent(&#123;
    name: 'HelloWorld',
    props: &#123;
      msg: &#123;
        type: String,
        default: ''
      &#125;
    &#125;,
    setup() &#123;
      const store = useStore(key)

      const count = computed(() => store.state.count)

      return &#123;
        count,
        inCrement: () => store.commit('increment')
      &#125;
    &#125;
  &#125;)
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">4.2 vue-router</h3>
<p>在 src 目录下建立 router/index.ts，内容如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; createRouter, createWebHistory, RouteRecordRaw &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue-router"</span>;
<span class="hljs-keyword">import</span> HelloWorld <span class="hljs-keyword">from</span> <span class="hljs-string">"../components/HelloWorld.vue"</span>;

<span class="hljs-keyword">const</span> routes: <span class="hljs-built_in">Array</span><RouteRecordRaw> = [
    &#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">"/"</span>,
        <span class="hljs-attr">name</span>: <span class="hljs-string">"HelloWorld"</span>,
        <span class="hljs-attr">component</span>: HelloWorld,
    &#125;,
    &#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">"/about"</span>,
        <span class="hljs-attr">name</span>: <span class="hljs-string">"About"</span>,
        <span class="hljs-comment">// route level code-splitting</span>
        <span class="hljs-comment">// this generates a separate chunk (about.[hash].js) for this route</span>
        <span class="hljs-comment">// which is lazy-loaded when the route is visited.</span>
        <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span>
            <span class="hljs-keyword">import</span>(<span class="hljs-comment">/* webpackChunkName: "About" */</span> <span class="hljs-string">"../components/About.vue"</span>)
    &#125;
];

<span class="hljs-keyword">const</span> router = createRouter(&#123;
    <span class="hljs-attr">history</span>: createWebHistory(process.env.BASE_URL),
    routes,
&#125;);

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> router;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再新建一个 components/About.vue 文件，内容如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">img</span>
    <span class="hljs-attr">alt</span>=<span class="hljs-string">"Vue logo"</span>
    <span class="hljs-attr">src</span>=<span class="hljs-string">"../assets/logo.png"</span>
  /></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h1</span>></span>&#123;&#123; msg &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; defineComponent &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineComponent(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'About'</span>,
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">msg</span>: <span class="hljs-string">'Hello Vue 3.0 + Vite!'</span>
    &#125;
  &#125;,
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;&#125;
&#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再修改 main.ts</p>
<pre><code class="copyable">import &#123; createApp &#125; from 'vue'
import &#123; store, key &#125; from './store'
import router from "./router";
import App from './App'
import './index.css'

const app = createApp(App)

app.use(store, key)
app.use(router)
app.mount('#app')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再访问 <a href="http://localhost:3000/" target="_blank" rel="nofollow noopener noreferrer">http://localhost:3000/</a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/37a0219fc2294983a99a91f226f40184~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>和 <a href="http://localhost:3000/about" target="_blank" rel="nofollow noopener noreferrer">http://localhost:3000/about</a> 即可</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a904b44bd5b425098c802755f7bc8d1~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-10">5. 加入 Element Plus</h2>
<h3 data-id="heading-11">5.1 安装 element-plus</h3>
<p><strong>全局安装</strong></p>
<pre><code class="hljs language-js copyable" lang="js">npm install element-plus --save
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">5.2 引入 Element Plus</h3>
<p>你可以引入整个 Element Plus，或是根据需要仅引入部分组件。我们先介绍如何引入完整的 Element。</p>
<p><strong>完整引入</strong></p>
<p>在 main.js 中写入以下内容：</p>
<pre><code class="copyable">import &#123; createApp &#125; from 'vue'
import ElementPlus from 'element-plus';
import router from "./router";
import 'element-plus/lib/theme-chalk/index.css';
import App from './App.vue';
import './index.css'

const app = createApp(App)
app.use(ElementPlus)
app.use(router)
app.mount('#app')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上代码便完成了 Element Plus 的引入。需要注意的是，样式文件需要单独引入。</p>
<hr>
<p><strong>按需引入</strong></p>
<p>借助 <a href="https://github.com/QingWei-Li/babel-plugin-component" target="_blank" rel="nofollow noopener noreferrer">babel-plugin-component</a>，我们可以只引入需要的组件，以达到减小项目体积的目的。</p>
<p>首先，安装 babel-plugin-component：</p>
<pre><code class="copyable">npm install babel-plugin-component -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后，将 .babelrc 修改为：</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-string">"plugins"</span>: [
    [
      <span class="hljs-string">"component"</span>,
      &#123;
        <span class="hljs-string">"libraryName"</span>: <span class="hljs-string">"element-plus"</span>,
        <span class="hljs-string">"styleLibraryName"</span>: <span class="hljs-string">"theme-chalk"</span>
      &#125;
    ]
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来，如果你只希望引入部分组件，比如 Button 和 Select，那么需要在 main.js 中写入以下内容：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; createApp &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> &#123; store, key &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./store'</span>;
<span class="hljs-keyword">import</span> router <span class="hljs-keyword">from</span> <span class="hljs-string">"./router"</span>;
<span class="hljs-keyword">import</span> &#123; ElButton, ElSelect &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'element-plus'</span>;
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App.vue'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'./index.css'</span>

<span class="hljs-keyword">const</span> app = createApp(App)
app.component(ElButton.name, ElButton);
app.component(ElSelect.name, ElSelect);

<span class="hljs-comment">/* or
 * app.use(ElButton)
 * app.use(ElSelect)
 */</span>

app.use(store, key)
app.use(router)
app.mount(<span class="hljs-string">'#app'</span>)
app.mount(<span class="hljs-string">'#app'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更详细的安装方法请看 <a href="https://element-plus.org/#/zh-CN/component/quickstart" target="_blank" rel="nofollow noopener noreferrer">快速上手</a>。</p>
<h3 data-id="heading-13">5.3 全局配置</h3>
<p>在引入 Element Plus 时，可以传入一个全局配置对象。</p>
<p>该对象目前支持 <code>size</code> 与 <code>zIndex</code> 字段。<code>size</code> 用于改变组件的默认尺寸，<code>zIndex</code> 设置弹框的初始 z-index（默认值：2000）。按照引入 Element Plus 的方式，具体操作如下：</p>
<p>完整引入 Element：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; createApp &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> ElementPlus <span class="hljs-keyword">from</span> <span class="hljs-string">'element-plus'</span>;
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App.vue'</span>;

<span class="hljs-keyword">const</span> app = createApp(App)
app.use(ElementPlus, &#123; <span class="hljs-attr">size</span>: <span class="hljs-string">'small'</span>, <span class="hljs-attr">zIndex</span>: <span class="hljs-number">3000</span> &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>按需引入 Element：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; createApp &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> &#123; ElButton &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'element-plus'</span>;
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App.vue'</span>;

<span class="hljs-keyword">const</span> app = createApp(App)
app.config.globalProperties.$ELEMENT = option
app.use(ElButton);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>按照以上设置，项目中所有拥有 <code>size</code> 属性的组件的默认尺寸均为 'small'，弹框的初始 z-index 为 3000。</p>
<h3 data-id="heading-14">5.4 配置 vite.config.ts</h3>
<p>其中 proxy 和 alias 是和 vue-cli 区别比较大的地方。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; defineConfig &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vite'</span>
<span class="hljs-keyword">import</span> vue <span class="hljs-keyword">from</span> <span class="hljs-string">'@vitejs/plugin-vue'</span>
<span class="hljs-keyword">import</span> styleImport <span class="hljs-keyword">from</span> <span class="hljs-string">'vite-plugin-style-import'</span>
<span class="hljs-keyword">import</span> path <span class="hljs-keyword">from</span> <span class="hljs-string">'path'</span>

<span class="hljs-comment">// https://vitejs.dev/config/</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineConfig(&#123;
  <span class="hljs-attr">plugins</span>: [
    vue(),
    styleImport(&#123;
      <span class="hljs-attr">libs</span>: [
        &#123;
          <span class="hljs-attr">libraryName</span>: <span class="hljs-string">'element-plus'</span>,
          <span class="hljs-attr">esModule</span>: <span class="hljs-literal">true</span>,
          <span class="hljs-attr">ensureStyleFile</span>: <span class="hljs-literal">true</span>,
          <span class="hljs-attr">resolveStyle</span>: <span class="hljs-function">(<span class="hljs-params">name</span>) =></span> &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-string">`element-plus/lib/theme-chalk/<span class="hljs-subst">$&#123;name&#125;</span>.css`</span>;
          &#125;,
          <span class="hljs-attr">resolveComponent</span>: <span class="hljs-function">(<span class="hljs-params">name</span>) =></span> &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-string">`element-plus/lib/<span class="hljs-subst">$&#123;name&#125;</span>`</span>;
          &#125;,
        &#125;
      ]
    &#125;)
  ],

  <span class="hljs-comment">/**
   * 在生产中服务时的基本公共路径。
   * <span class="hljs-doctag">@default </span>'/'
   */</span>
  <span class="hljs-attr">base</span>: <span class="hljs-string">'./'</span>,
  <span class="hljs-comment">/**
  * 与“根”相关的目录，构建输出将放在其中。如果目录存在，它将在构建之前被删除。
  * <span class="hljs-doctag">@default </span>'dist'
  */</span>
  <span class="hljs-comment">// outDir: 'dist',</span>
  <span class="hljs-attr">server</span>: &#123;
    <span class="hljs-comment">// hostname: '0.0.0.0',</span>
    <span class="hljs-attr">host</span>: <span class="hljs-string">"localhost"</span>,
    <span class="hljs-attr">port</span>: <span class="hljs-number">3001</span>,
    <span class="hljs-comment">// // 是否自动在浏览器打开</span>
    <span class="hljs-comment">// open: true,</span>
    <span class="hljs-comment">// // 是否开启 https</span>
    <span class="hljs-comment">// https: false,</span>
    <span class="hljs-comment">// // 服务端渲染</span>
    <span class="hljs-comment">// ssr: false,</span>
    <span class="hljs-attr">proxy</span>: &#123;
      <span class="hljs-string">'/api'</span>: &#123;
        <span class="hljs-attr">target</span>: <span class="hljs-string">'http://localhost:3333/'</span>,
        <span class="hljs-attr">changeOrigin</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">ws</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">rewrite</span>: <span class="hljs-function">(<span class="hljs-params">pathStr</span>) =></span> pathStr.replace(<span class="hljs-string">'/api'</span>, <span class="hljs-string">''</span>)
      &#125;,
    &#125;,
  &#125;,
  <span class="hljs-attr">resolve</span>: &#123;
    <span class="hljs-comment">// 导入文件夹别名</span>
    <span class="hljs-attr">alias</span>: &#123;
      <span class="hljs-string">'@'</span>: path.resolve(__dirname, <span class="hljs-string">'./src'</span>),
      <span class="hljs-attr">views</span>: path.resolve(__dirname, <span class="hljs-string">'./src/views'</span>),
      <span class="hljs-attr">components</span>: path.resolve(__dirname, <span class="hljs-string">'./src/components'</span>),
      <span class="hljs-attr">utils</span>: path.resolve(__dirname, <span class="hljs-string">'./src/utils'</span>),
      <span class="hljs-attr">less</span>: path.resolve(__dirname, <span class="hljs-string">"./src/less"</span>),
      <span class="hljs-attr">assets</span>: path.resolve(__dirname, <span class="hljs-string">"./src/assets"</span>),
      <span class="hljs-attr">com</span>: path.resolve(__dirname, <span class="hljs-string">"./src/components"</span>),
      <span class="hljs-attr">store</span>: path.resolve(__dirname, <span class="hljs-string">"./src/store"</span>),
      <span class="hljs-attr">mixins</span>: path.resolve(__dirname, <span class="hljs-string">"./src/mixins"</span>)
    &#125;,
  &#125;
&#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">踩到坑</h2>
<p>在 <code>npm run dev</code> 打包时不报错，但是在 <code>npm run build</code> 时却报错了，build 的时候会把 <code>node_modules</code> 里面的文件也编译，所以挺多 element-plus 的类型文件报错了。</p>
<p>把 <code>tsconfig.json</code> 里面的 <code>include</code> 和 <code>exclude</code> 修改一下就不会了，配置如下</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-string">"compilerOptions"</span>: &#123;
    <span class="hljs-string">"target"</span>: <span class="hljs-string">"esnext"</span>,
    <span class="hljs-string">"module"</span>: <span class="hljs-string">"esnext"</span>,
    <span class="hljs-string">"moduleResolution"</span>: <span class="hljs-string">"node"</span>,
    <span class="hljs-string">"strict"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-string">"jsx"</span>: <span class="hljs-string">"preserve"</span>,
    <span class="hljs-string">"sourceMap"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-comment">// 忽略 this 的类型检查, Raise error on this expressions with an implied any type.</span>
    <span class="hljs-string">"noImplicitThis"</span>: <span class="hljs-literal">false</span>,
    <span class="hljs-string">"resolveJsonModule"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-string">"esModuleInterop"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-string">"lib"</span>: [<span class="hljs-string">"esnext"</span>, <span class="hljs-string">"dom"</span>],
    <span class="hljs-string">"types"</span>: [<span class="hljs-string">"vite/client"</span>]
  &#125;,
  <span class="hljs-string">"include"</span>: [<span class="hljs-string">"/src/**/*.ts"</span>, <span class="hljs-string">"/src/**/*.d.ts"</span>, <span class="hljs-string">"/src/**/*.tsx"</span>, <span class="hljs-string">"/src/**/*.vue"</span>],
  <span class="hljs-comment">// ts 排除的文件</span>
  <span class="hljs-string">"exclude"</span>: [<span class="hljs-string">"node_modules"</span>]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Vue3 + vite2 打包出来的文件和原来 vue2 版的差别也挺大的，由原来 2.5M 直接变成了 1.8M ，amazing！</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/456f3245e52f4051a437b4e04945c42e~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-16">最后</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dadde4e919d44b6ebc50a916f3d1ad49~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>项目代码大多都是 2 年前的，还有很多可以优化的地方，这次重构的过程没对原来的样式和代码做什么改动，没那么多时间，加上我懒 😂</p>
<p>这次就升级了主要框架与相应的 ui 库，过了一遍 Vue3 中的 API，发现很多 Vue3 中新的 API 都用不上，主要是要熟练一下 Vue3 和 Vite2 项目搭建，这假期也算有所收获。</p>
<p>具体项目源码请看：</p>
<blockquote>
<p><a href="https://github.com/biaochenxuying/blog-vue-typescript" target="_blank" rel="nofollow noopener noreferrer">github.com/biaochenxuy…</a></p>
</blockquote>
<p>至此，一个基于 Vue3 全家桶 + Vite2 + TypeScript + Element Plus 的开发环境已经搭建完毕，现在就可以编写代码了，各个组件的使用方法请参阅它们各自的文档。</p>
<p>不得不说 Vue3 + Element Plus + Vite + TypeScript 是真的香！</p>
<p>推荐一个 Vue3 相关的资料汇总： <a href="https://github.com/FrontEndGitHub/FrontEndGitHub/issues/18" target="_blank" rel="nofollow noopener noreferrer">Vue3 的学习教程汇总、源码解释项目、支持的 UI 组件库、优质实战项目</a>，相信你会挖到矿哦！</p>
<p>参考文章：<a href="https://segmentfault.com/a/1190000038533257" target="_blank" rel="nofollow noopener noreferrer">vue3 + vite + typescript + eslint + jest 项目配置实践</a></p>
<p><strong>推荐阅读</strong></p>
<ul>
<li><a href="https://mp.weixin.qq.com/s/qyIFAI0AuKDE1cjThbZqSw" target="_blank" rel="nofollow noopener noreferrer">TypeScript 中提升幸福感的 10 个高级技巧</a></li>
</ul>
<p>欢迎关注公众号： “<strong>全栈修炼</strong>”，回复 “<strong>电子书</strong>” 即可以获得 <strong>300</strong> 本技术精华书籍哦，猫哥 wx：CB834301747</p></div>  
</div>
            
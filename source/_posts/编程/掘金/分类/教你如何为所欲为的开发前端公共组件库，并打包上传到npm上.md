
---
title: '教你如何为所欲为的开发前端公共组件库，并打包上传到npm上'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79c17b8ab0654f49bd18b2a78b1595ff~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 10 Jul 2021 06:13:09 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79c17b8ab0654f49bd18b2a78b1595ff~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>「本文已参与好文召集令活动，点击查看：<a href="https://juejin.cn/post/6978685539985653767" target="_blank" title="https://juejin.cn/post/6978685539985653767">后端、大前端双赛道投稿，2万元奖池等你挑战！</a>」</p>
<blockquote>
<p>还在为不知如何开发前端公共组件库而烦恼吗？还在为不知道如何把开发好的公共组件库打包上传到npm上吗？这里我都可以一一教会你</p>
</blockquote>
<p>我们将会从两个方向出发，第一种是框架组件，如<code>Vue</code>、<code>react</code>、<code>Angular</code>...等。第二种则是工具组件，如 <code>JavaScript</code>、<code>JQ</code>...等。废话不多说，直接进入我们的主题。</p>
<h2 data-id="heading-0">框架组件</h2>
<pre><code class="copyable">这里以Vue2.x为例
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-1">第一步：使用 vue init webpack-simple yyl-npm-practice   初始化项目</h4>
<p>提示: 不要用 vue init webpack npm-practice 初始化项目，因为我们就开发个组件，不需要那么多配置，配置多了修改起来也麻烦，webpack-simple足够了。</p>
<p>初始完项目，按照提示输入项目信息即可，然后 npm install , npm run dev 让项目跑起来，如下图：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79c17b8ab0654f49bd18b2a78b1595ff~tplv-k3u1fbpfcp-watermark.image" alt="872412-20190413134048730-192549904.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-2">第二步：修改文件目录</h4>
<p>1.在src目录下新建components文件夹，然后在此文件夹下建立Main.vue文件</p>
<p>　　Main.vue 名字也可以是其他，我们写的这个组件就是放在该文件里面，之前的App.vue是用于本地开发，测试用的入口文件，也就是用于 npm run dev  的入口文件。</p>
<p>2.在webpack.config.js同级目录（也是该组件的根目录）下新建 index.js文件， index.js是把Main.vue文件暴露出去的出口。</p>
<p>修改完之后的文件目录如下，标红的就是新增的内容：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff74429812e7425899716f20883975ff~tplv-k3u1fbpfcp-watermark.image" alt="872412-20190413135247686-1665090067.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-3">第三步：修改文件内容，配置</h4>
<p>1.Main.vue内容如下（注意name）：</p>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"container"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;&#123;msg&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;&#123;propData&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'yyl-npm-practice'</span>,
  data () &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">msg</span>: <span class="hljs-string">'Welcome to Your Vue.js App'</span>
    &#125;
  &#125;,
  <span class="hljs-attr">props</span>: &#123;
      <span class="hljs-attr">propData</span>: &#123;
          <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
          <span class="hljs-attr">default</span>: <span class="hljs-string">'我是默认值'</span>
      &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"scss"</span>></span><span class="css">
<span class="hljs-selector-class">.container</span>&#123;
    <span class="hljs-attribute">text-align</span>: center;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.App.vue内容如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">Main</span> <span class="hljs-attr">:propData</span>=<span class="hljs-string">'initData'</span>/></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> Main <span class="hljs-keyword">from</span> <span class="hljs-string">'./components/Main'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">initData</span>: <span class="hljs-string">'hello 这里是陈杨下的年华'</span>
      &#125;
    &#125;,
    <span class="hljs-attr">components</span>:&#123;
      Main
    &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span>></span>

<span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3.index.js内容如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Main <span class="hljs-keyword">from</span> <span class="hljs-string">'./src/components/Main'</span>
 
<span class="hljs-comment">// 这一步判断window.Vue是否存在，因为直接引用vue.min.js， 它会把Vue绑到Window上，我们直接引用打包好的js才能正常跑起来。</span>
<span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">window</span> !== <span class="hljs-string">'undefined'</span> && <span class="hljs-built_in">window</span>.Vue) &#123;
<span class="hljs-built_in">window</span>.Vue.component(<span class="hljs-string">'yyl-npm-practice'</span>, Main)
&#125;
<span class="hljs-comment">//这样就可以使用Vue.use进行全局安装了。</span>
Main.install = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">Vue</span>)</span>&#123;
Vue.component(Main.name, Main)
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> Main
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em><strong>------ start 2019-05-06新增</strong></em></p>
<p>index.js内容改完如下， 因为使用 window.Vue.component('yyl-npm-practice', Main) 的时候 外部引用的时候 有可能会覆盖该组件，导致组件无法正常使用；</p>
<p>使用下面的的定义方式后， 在.vue 环境下 使用方式不变， 在只引用 ys-expression.js 环境下</p>
<p>需在 new Vue（） 之前加 window['ys-expression'].default.install();</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Main <span class="hljs-keyword">from</span> <span class="hljs-string">'./src/component/Main'</span>
<span class="hljs-keyword">import</span> _Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>

Main.install = <span class="hljs-function"><span class="hljs-params">Vue</span> =></span> &#123;
<span class="hljs-keyword">if</span> (!Vue) &#123;
<span class="hljs-built_in">window</span>.Vue = Vue = _Vue
&#125;
Vue.component(Main.name, Main)
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> Main;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em><strong>------ end 2019-05-06新增</strong></em></p>
<p>4.修改package.json</p>
<p>package.json需要修改private字段(private是true的时候不能发布到npm,需设置成false)； 并增加main字段， main字段是require方法可以通过这个配置找到入口文件，这输入模块加载规范，具体可以参考  这里， 主要内内容截图如下：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c5e327dff1974f029b23d5a42221939f~tplv-k3u1fbpfcp-watermark.image" alt="872412-20190413141046072-2009356377.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>修改完package.json如下，标红的就是新增和改变的属性。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4740b1fed55244388c77a1bb321f7aab~tplv-k3u1fbpfcp-watermark.image" alt="872412-20190413140615983-442956056.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>5.修改 webpack.config.js
其实就是修改entry 和output,截图如下：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9309ffbb247449d6863d0bce6f6446da~tplv-k3u1fbpfcp-watermark.image" alt="872412-20190413141834023-1036786115.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>说明：入口会根据开发环境 ，生产环境切换， main.js 是npm run dev 的入口，就是App.vue， 用于调试/测试我们开发的组件;   index.js是Main.vue， 就是我们开发的组件，我们打包到生产环境打包就只是单纯的 yyl-npm-practice 组件</p>
<p>6.修改index.html的js引用路径，因为我们修改了output 的 filename，所以引用文件的名字也得变。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff135c5645664f3189a23096831026ed~tplv-k3u1fbpfcp-watermark.image" alt="872412-20190413144119806-1318062074.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>到此组件就开发完了，打包下看看， npm run build dist下生成了俩文件，如下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f75c4c4bb7a94ff5abb65fa315987f6a~tplv-k3u1fbpfcp-watermark.image" alt="872412-20190413142640156-973748135.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这个.map文件怎么回事，其实就是这段代码：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b64fbcb3a84c4e78a017be234470ed99~tplv-k3u1fbpfcp-watermark.image" alt="872412-20190413142814520-358347593.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>生产环境的时候， 我们就不调试了，也不想要这个.map文件，那就先把这个 devtool删了，然后放在这里，看下图，只要在开发环境的时候才启用这个调试，</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e137194a61de48608cfba2892bdbed3c~tplv-k3u1fbpfcp-watermark.image" alt="872412-20190413143325761-1330974957.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>把dist目录下的俩文件删除，再npm run build 就不会产生.map文件了。</p>
<p>npm run dev 让项目跑起来，我们在App.vue里面调用该组件，并做测试，调试。</p>
<h4 data-id="heading-4">第四步： 发布到npm</h4>
<ol>
<li>去 npm 官网注册个账号 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/" ref="nofollow noopener noreferrer">www.npmjs.com/</a></li>
</ol>
<p>2.在该组件根目录下的终端（就是 平常输入 npm run dev的地方），运行npm login，会提示输入个人信息，Email是发布成功后，自动给这个邮箱发送一个邮件，通知发布成功，输入完，登录成功。</p>
<p>去自己的npm上点击Packages ，就能看到发布的包</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dae0b885646049f29301d2c50470ba83~tplv-k3u1fbpfcp-watermark.image" alt="872412-20190413145905774-579833772.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>包的具体信息如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/34f37e8229f94c43be19d143d276ce5c~tplv-k3u1fbpfcp-watermark.image" alt="872412-20190413154554888-529949089.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>大家最好在readme 里面写上组件的使用方法， 说明等等，方便你我他。</p>
<h4 data-id="heading-5">使用方法 ：</h4>
<p>1.组件内部使用</p>
<pre><code class="hljs language-js copyable" lang="js">html: 

　　<span class="xml"><span class="hljs-tag"><<span class="hljs-name">Main</span>/></span></span>

js：

    <span class="hljs-keyword">import</span> Main <span class="hljs-keyword">from</span> <span class="hljs-string">'yyl-npm-practice'</span>

    <span class="hljs-attr">components</span>: &#123;
      Main
    &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>main.js 全局安装：</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Main <span class="hljs-keyword">from</span> <span class="hljs-string">'yyl-npm-practice'</span>
Vue.use(Main)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在其他.vue文件里面，直接使用组件  即可</p>
<p>3.直接引用打包后的 yyl-npm-practice.js</p>
<p>这种方式就不需要webpack这类的构建工具，跟jquery的方式差不多，可以直接页面引用，使用方法示例如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><!DOCTYPE html>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">yyl-npm-practice</span> <span class="hljs-attr">:propData</span>=<span class="hljs-string">"propData"</span>></span><span class="hljs-tag"></<span class="hljs-name">yyl-npm-practice</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://unpkg.com/vue/dist/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./dist/yyl-npm-practice.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
    <span class="hljs-attr">data</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">propData</span>: <span class="hljs-string">'11111111111111111111'</span>
      &#125;
    &#125;,
    <span class="hljs-attr">methods</span>: &#123;
    &#125;
  &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
</span><span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">采坑记录：

1. 在webpack.config.js里设置 resolve（比如 设置@做为根目录 ）， 开发环境没问题，生产环境就用不了了，所以大家就用平常的相对路径类吧，虽然麻烦了点。

2. 图片生产环境不能用，解决方法可以把图片转成base64, 可以用这个 在线图片转base64,或者把图片放在网上，引用图片的网上资源路径。

3. 字体图标在生产环境也用不了，如果用到了字体图标，就别把字体图标的资源打包进去了，引用该组件的时候，需要再引用字体图标的资源。
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em><strong>start ====> 2019-04-17更新</strong></em></p>
<p>后来发现其实图片和字体图标也可一起打包到js里面，需要用到 url-loader 把limit参数设置大点就行，这样就可以把图片，字体图标也都打包到js里面了，这样使用的时候，就不用单独引用这些静态资源了， 代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
    <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(png|jpg|gif|svg)$/</span>,
    loader: <span class="hljs-string">'url-loader'</span>,
    <span class="hljs-attr">options</span>: &#123;
      <span class="hljs-attr">name</span>: <span class="hljs-string">'[name].[ext]?[hash]'</span>,
      <span class="hljs-attr">limit</span>: <span class="hljs-number">99999</span>
    &#125;
    &#125;,
    &#123; 
    <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(svg|ttf|eot|woff|woff2)$/</span>, 
    loader: <span class="hljs-string">'url-loader'</span>, 
    <span class="hljs-attr">options</span>:&#123; 
     <span class="hljs-attr">name</span>:<span class="hljs-string">'[name].[ext]'</span>,
        <span class="hljs-attr">limit</span>: <span class="hljs-number">9999999</span>
    &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">第二种工具库</h2>
<blockquote>
<p>这里以JavaScript为例子。 开发Js的工具库不需要像框架一样那么复杂，不需要webpack打包机制，我们使用rollup.js打包工具即可</p>
</blockquote>
<h4 data-id="heading-7">第一步，安装rollup.js打包工具</h4>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.rollupjs.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.rollupjs.com/" ref="nofollow noopener noreferrer">rollup.js</a>按照官网的原话说：</p>
<blockquote>
<p>Rollup 是一个 JavaScript 模块打包器，可以将小块代码编译成大块复杂的代码，例如 library 或应用程序。</p>
<p>Rollup 对代码模块使用新的标准化格式，这些标准都包含在 JavaScript 的 ES6 版本中，而不是以前的特殊解决方案，如 CommonJS 和 AMD。ES6 模块可以使你自由、无缝地使用你最喜爱的 library 中那些最有用独立函数，而你的项目不必携带其他未使用的代码。ES6 模块最终还是要由浏览器原生实现，但当前 Rollup 可以使你提前体验。</p>
</blockquote>
<p>1.全局安装 rollup</p>
<pre><code class="hljs language-js copyable" lang="js">npm i rollup -g
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.新建项目，初始项目</p>
<pre><code class="hljs language-js copyable" lang="js">mkdir rollup-demo ## 新建项目文件夹
cd rollup-demo    ## 进入项目根目录
npm init          ## 初始化项目
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">第二步，编写插件源码bundle.js</h4>
<p>1.创建 src/main.js 编写源码</p>
<pre><code class="hljs language-js copyable" lang="js">cd rollup-demo ## 进入项目根目录
mkdir src      ## 创建 src 目录
cd src
touch main.js  ## 在 src 目录下创建 main.js
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.main.js 文件内容</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> answer = <span class="hljs-string">'100'</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`the answer is <span class="hljs-subst">$&#123;answer&#125;</span>。`</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">第三步，工具库的相关配置</h4>
<p>1.rollup 配置文件</p>
<p>项目根目录下新建 rollup.config.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">input</span>: <span class="hljs-string">'src/main.js'</span>,  <span class="hljs-comment">// 入口文件</span>
  <span class="hljs-attr">output</span>: &#123;  <span class="hljs-comment">// 输出 options</span>
    <span class="hljs-attr">file</span>: <span class="hljs-string">'bundle.js'</span>,  <span class="hljs-comment">// 输出文件名</span>
    <span class="hljs-attr">format</span>: <span class="hljs-string">'cjs'</span>       <span class="hljs-comment">// 输出格式</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.修改 package.json 的 scripts</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-string">"scripts"</span>: &#123;
   <span class="hljs-string">"dev"</span>: <span class="hljs-string">"rollup -c"</span>  <span class="hljs-comment">// 打包命令</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行 npm run dev 打包编译</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/219ef2c07de642d5a0670307606005d9~tplv-k3u1fbpfcp-watermark.image" alt="1567373-42264fb97c88b0e1.webp" loading="lazy" referrerpolicy="no-referrer"></p>
<p>生成的bundle.js 文件内容：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-meta">'use strict'</span>;

<span class="hljs-keyword">var</span> answer = <span class="hljs-string">'100'</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">main</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"the answer is "</span>.concat(answer, <span class="hljs-string">"\u3002"</span>));
&#125;

<span class="hljs-built_in">module</span>.exports = main;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3.使用插件编译 babel</p>
<p>3.1 安装 rollup-plugin-babel</p>
<pre><code class="hljs language-js copyable" lang="js">npm i -D rollup-plugin-babel
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编辑 <code>rollup.config.js</code>，添加插件配置</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> babel <span class="hljs-keyword">from</span> <span class="hljs-string">'rollup-plugin-babel'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">input</span>: <span class="hljs-string">'src/main.js'</span>,
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">file</span>: <span class="hljs-string">'bundle.js'</span>,
    <span class="hljs-attr">format</span>: <span class="hljs-string">'cjs'</span>
  &#125;,
  <span class="hljs-attr">plugins</span>: [ <span class="hljs-comment">// 增加 plugins</span>
    babel(&#123;
      <span class="hljs-attr">exclude</span>: <span class="hljs-string">'node_modules/**'</span> <span class="hljs-comment">// 不对node_modules进行编译</span>
    &#125;)
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3.2 安装 babel 的相关依赖</p>
<pre><code class="hljs language-js copyable" lang="js">npm i -D @babel/core @babel/preset-env
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 src 目录下添加 .babelrc 配置文件 （项目根目录下也是可以的，区别在于 src 目录下的 .babelrc 只会影响 src 目录下的文件）</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-string">"presets"</span>: [
    [<span class="hljs-string">"@babel/env"</span>, &#123;<span class="hljs-string">"modules"</span>: <span class="hljs-literal">false</span>&#125;]
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3.3 将 main.js 更改为es6语法</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> answer = <span class="hljs-string">'100'</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> () => &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`the answer is <span class="hljs-subst">$&#123;answer&#125;</span>。`</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>重新打包</p>
<p>npm run dev</p>
<p>当前 bundle.js 的内容</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-meta">'use strict'</span>;

<span class="hljs-keyword">var</span> answer = <span class="hljs-string">'100'</span>;
<span class="hljs-keyword">var</span> main = (<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"the answer is "</span>.concat(answer, <span class="hljs-string">"\u3002"</span>));
&#125;);

<span class="hljs-built_in">module</span>.exports = main;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>使用 npm packages 依赖</li>
</ol>
<p>rollup 不知道如何处理 node_modules 中的依赖，需要通过插件 rollup-plugin-node-resolve 告诉 rollup 如何查找外部模块。</p>
<pre><code class="hljs language-js copyable" lang="js">npm i -D rollup-plugin-node-resolve
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编辑 rollup.config.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> resolve <span class="hljs-keyword">from</span> <span class="hljs-string">'rollup-plugin-node-resolve'</span>;
<span class="hljs-keyword">import</span> babel <span class="hljs-keyword">from</span> <span class="hljs-string">'rollup-plugin-babel'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">input</span>: <span class="hljs-string">'src/main.js'</span>,
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">file</span>: <span class="hljs-string">'bundle.js'</span>,
    <span class="hljs-attr">format</span>: <span class="hljs-string">'cjs'</span>
  &#125;,
  <span class="hljs-attr">plugins</span>: [
    resolve(),
    babel(&#123;
      <span class="hljs-attr">exclude</span>: <span class="hljs-string">'node_modules/**'</span>
    &#125;)
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在就可以去代码中引用 node_modules 中的依赖了，以 the-answer 为例：</p>
<pre><code class="hljs language-js copyable" lang="js">npm i the-answer
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 main.js 中引用 the-answer</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> answer <span class="hljs-keyword">from</span> <span class="hljs-string">'the-answer'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> () => &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`the answer is <span class="hljs-subst">$&#123;answer&#125;</span>。`</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打包编译后的结果：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-meta">'use strict'</span>;

<span class="hljs-keyword">var</span> index = <span class="hljs-number">42</span>;

<span class="hljs-keyword">var</span> main = (<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"the answer is "</span>.concat(index, <span class="hljs-string">"\u3002"</span>));
&#125;);

<span class="hljs-built_in">module</span>.exports = main;

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">打包发布npm</h4>
<blockquote>
<p>这里的流程我就不重复说，跟上面的Vue组件库打包上传的流程是一样的（其实就是偷懒...，大家懂了就好，见谅见谅）</p>
</blockquote>
<h4 data-id="heading-11">补充</h4>
<p>今天的技术就介绍到这里了，大家有什么建议的可以下面评论，我会第一时间回，或者有什么问题我们都可以讨论，谢谢大家，创作不易，请多多支持点赞、分享</p></div>  
</div>
            
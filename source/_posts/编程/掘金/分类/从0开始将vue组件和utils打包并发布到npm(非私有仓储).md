
---
title: '从0开始将vue组件和utils打包并发布到npm(非私有仓储)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/45a29546dc044839aaa1fe0a39eb4607~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 27 Jul 2021 01:55:07 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/45a29546dc044839aaa1fe0a39eb4607~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">1.注意</h3>
<p>本文主要是模拟将组件和常见的utils打包到npm,结果就是在npm平台上任何人都能搜到这个包,是一种共享的行为,是公开的!方法是比较适用于个人或者公司愿意将一些稳定的包公开,给大家共同使用,并且长期维护</p>
<p>不适用于:<br>假设我司好几个项目,有很多重复的组件,utils,想减少代码复用,较少维护成本,所以建立npm私有仓储,只有项目内部使用,不公开,这种就千万不要发到公开平台去了,可参考<a href="https://link.juejin.cn/?target=https%3A%2F%2Fswmlee.com%2F2019%2F12%2F18%2Ftechnicalessays%2Fverdaccio-private-registry%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://swmlee.com/2019/12/18/technicalessays/verdaccio-private-registry/" ref="nofollow noopener noreferrer">使用 Verdaccio 搭建 npm 私有仓储</a></p>
<h3 data-id="heading-1">2.打包成npm 包的流程(vue页面代码)</h3>
<h5 data-id="heading-2">2.1 vue页面代码</h5>
<p>父页面</p>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">welcome</span>
      <span class="hljs-attr">title</span>=<span class="hljs-string">"首页"</span>
    /></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> welcome <span class="hljs-keyword">from</span> <span class="hljs-string">'./components/welcome.vue'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">components</span>: &#123;
     welcome,
  &#125;,
  <span class="hljs-attr">name</span>: <span class="hljs-string">'App'</span>,
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>子页面-公共组件welcome</p>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"each-page-title"</span>></span>欢迎进入&#123;&#123; title &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">title</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
      <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>,
    &#125;
  &#125;,
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">scoped</span>></span><span class="css">
  <span class="hljs-selector-class">.each-page-title</span> &#123;
    <span class="hljs-attribute">text-align</span>: center;
    <span class="hljs-attribute">color</span>: red;
    <span class="hljs-attribute">background-color</span>: yellowgreen;
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/45a29546dc044839aaa1fe0a39eb4607~tplv-k3u1fbpfcp-watermark.image" alt="93a97e49a762eb2a1a62bb18b1f56fe.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-3">2.2 将vue组件打包到npm</h5>
<h6 data-id="heading-4">1 新建包bingxixi-common-title->新建src-> 初始化</h6>
<pre><code class="hljs language-js copyable" lang="js">mkdir bingxixi-common-title
 这里的包名,我是由 项目名+功能
cd bingxixi-common-title
mkdir src
 待会把我们的welcome.vue放到src地下(一般是src地下,如果是单纯index.js页面,我觉得可以不用放)
npm init
这里如果文件名没问题的话,直接enter就好
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-5">2.在src同级建立一个index.js的文件</h6>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> welcome <span class="hljs-keyword">from</span> <span class="hljs-string">'./src/welcome'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> welcome
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-6">3.创建npm 帐号以及邮箱验证</h6>
<p>进入<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/" ref="nofollow noopener noreferrer">官网</a>,输入帐号,密码,邮箱,并且要把这里记录下来,待会要用<br>
如果有收到邮件就去<code>邮箱验证</code>一下,或者在登录不上去的时候去看看邮箱需要验证(邮箱一定要验证一下)</p>
<h6 data-id="heading-7">4.正式发布</h6>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c7e73da472e948d4a066c90f51795f98~tplv-k3u1fbpfcp-watermark.image" alt="1627375503(1).png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在bingxixi-common-title文件下进行git操作</p>
<pre><code class="hljs language-js copyable" lang="js">npm login
#如果你们公司有自己的默认npm仓库或者使用的淘宝镜像，注意需要指定一下仓库地址；
<span class="hljs-string">`npm login --registry=https://registry.npmjs.org`</span>

依次让你输入用户名、密码、和邮箱
<span class="hljs-attr">Username</span>: 
Password: 
Email: (<span class="hljs-built_in">this</span> IS public)

npm publish --registry=https:<span class="hljs-comment">//registry.npmjs.org</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/366712688b304d35ae32804bd27df5c0~tplv-k3u1fbpfcp-watermark.image" alt="2ee7e57456b47d5ffa26eba29142b4e.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>以上就是发布成功了~</p>
<h6 data-id="heading-8">5.查询</h6>
<blockquote>
<p>1.登录npm帐号,可以看到</p>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/69db3c4255b644ba8fab2c78546e4ef9~tplv-k3u1fbpfcp-watermark.image" alt="dc84f125e17098e242f392c328aaf8a.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>2.直接在npm上搜这个包</p>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5b757c4becb47bbaf4acddfd3182040~tplv-k3u1fbpfcp-watermark.image" alt="1627376795(1).png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>3.直接在项目里面下载,去package.json</p>
</blockquote>
<blockquote>
<p>npm i bingxixi-common-title</p>
</blockquote>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/120327e756324003ab62fce32c23cf6e~tplv-k3u1fbpfcp-watermark.image" alt="7659e627f365336768fd96f22a63a11.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h6 data-id="heading-9">6.vue里面如何使用这个包</h6>
<p>1.安装</p>
<pre><code class="hljs language-js copyable" lang="js">npm i bingxixi-common-title --save
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.main.js里面引入,并且全局注册</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> welcome <span class="hljs-keyword">from</span> <span class="hljs-string">'bingxixi-common-title'</span>
Vue.component(<span class="hljs-string">'welcome'</span>, welcome);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3.刚刚的公共组件不需要了，只保留父页面
父页面代码</p>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">welcome</span>
      <span class="hljs-attr">title</span>=<span class="hljs-string">"首页"</span>
    /></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-10">7.如何更新包以及添加md文件</h6>
<p>1 新建<code>README.md</code>文件并写入规范,用markdown写就行</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4ee8b1ab929040e4b5dc6d739d88af28~tplv-k3u1fbpfcp-watermark.image" alt="1627377554(1).png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这些使用说明,随便在npm找个,看别人怎么写的,随便改改就行</p>
<p>2.更新包</p>
<pre><code class="hljs language-js copyable" lang="js">npm version patch
npm publish --registry=https:<span class="hljs-comment">//registry.npmjs.org</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意:npm version patch是在你原有的版本号,假设v1.0.0,他会在这个基础上加1,如果你的版本不是加1,你可以不用npm version patch,直接手动改package.json,然后再<code>npm publish --registry=https://registry.npmjs.org</code></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a2bb95b950674b67ba33f5ec08422cfa~tplv-k3u1fbpfcp-watermark.image" alt="98703da3e7153b7b84ce9cef59696b6.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h6 data-id="heading-11">8.如何避免每次都要我输入--registry=<a href="https://link.juejin.cn/?target=https%3A%2F%2Fregistry.npmjs.org" target="_blank" rel="nofollow noopener noreferrer" title="https://registry.npmjs.org" ref="nofollow noopener noreferrer">registry.npmjs.org</a></h6>
<pre><code class="hljs language-js copyable" lang="js">在src同级加上.npmrc文件
通过指令npm config edit
将下面位置改成registry=https:<span class="hljs-comment">//registry.npmjs.org</span>
以后就不用运行指令每次都要加这句话拉
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e0d3a32a3c9645d5ac58ed8d331d6b1e~tplv-k3u1fbpfcp-watermark.image" alt="1627378648(1).png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-12">3.2.打包成npm 包的流程(utils代码)</h3>
<h5 data-id="heading-13">3.1 vue页面代码以及utils</h5>
<p>vue页面</p>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    call me : &#123;&#123; userPrivate(phone) &#125;&#125;
    <span class="hljs-tag"><<span class="hljs-name">br</span>></span>你的捐款是&#123;&#123; money &#125;&#125;, 总共有 &#123;&#123; userPrivate(money)&#125;&#125; 位数 
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; userPrivate, getNumBit &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./utils/index'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'App'</span>,
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">phone</span>: <span class="hljs-number">18819168888</span>,
      <span class="hljs-attr">money</span>: <span class="hljs-number">12345.88</span>,
      userPrivate,
      getNumBit,
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>utils</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-comment">/**
   * 用户手机信息加密显示
   * <span class="hljs-doctag">@param <span class="hljs-type">&#123; Number, String &#125;</span> </span>phone 用户手机/帐号
   */</span>
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// 给电话号码加密</span>
  <span class="hljs-function"><span class="hljs-title">userPrivate</span>(<span class="hljs-params">phone</span>)</span> &#123;
    <span class="hljs-keyword">const</span> phoneStr = <span class="hljs-built_in">String</span>(phone)
    <span class="hljs-keyword">if</span> (!phone || phoneStr.length < <span class="hljs-number">11</span>) <span class="hljs-keyword">return</span> phone
    <span class="hljs-keyword">const</span> privateIndex = phoneStr.indexOf(<span class="hljs-string">'86'</span>) > -<span class="hljs-number">1</span> ? <span class="hljs-number">5</span> : <span class="hljs-number">3</span>
    <span class="hljs-keyword">return</span> <span class="hljs-string">`<span class="hljs-subst">$&#123;phoneStr.substring(<span class="hljs-number">0</span>, privateIndex)&#125;</span>****<span class="hljs-subst">$&#123;
    phoneStr.substring(privateIndex + <span class="hljs-number">4</span>, phoneStr.length)&#125;</span>`</span>
  &#125;,
  <span class="hljs-comment">// 获取数字的整数位长度</span>
  <span class="hljs-function"><span class="hljs-title">getNumBit</span>(<span class="hljs-params">num</span>)</span> &#123;
    <span class="hljs-keyword">let</span> intNum = num.toFixed(<span class="hljs-number">0</span>);
    <span class="hljs-keyword">return</span> intNum.length;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/03911c6c317a4644a275a5e6beafa430~tplv-k3u1fbpfcp-watermark.image" alt="1627379614(1).png" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-14">2.2 将utils打包到npm</h5>
<h6 data-id="heading-15">1 新建包bingxixi-common-utils->将utils的index.js放到bingxixi-common-title文件底下(直接做入口文件)->初始化</h6>
<pre><code class="hljs language-js copyable" lang="js">mkdir bingxixi-common-utils
 这里的包名,我是由 项目名+功能
cd bingxixi-common-utils
npm init
这里如果文件名没问题的话,直接enter就好
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-16">3.4.5.7步骤同上</h5>
<h5 data-id="heading-17">6.vue里面如何使用这个包</h5>
<p>1.安装</p>
<pre><code class="hljs language-js copyable" lang="js">npm i bingxixi-common-utils --save
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.main.js里面引入,并且全局注册</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; userPrivate, getNumBit &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'bingxixi-common-utils'</span>
Vue.prototype.$userPrivate = userPrivate
Vue.prototype.$getNumBit = getNumBit
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3.页面代码</p>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    call me : &#123;&#123; $userPrivate(phone) &#125;&#125;
    <span class="hljs-tag"><<span class="hljs-name">br</span>></span>你的捐款是&#123;&#123; money &#125;&#125;, 总共有 &#123;&#123; $userPrivate(money)&#125;&#125; 位数
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'App'</span>,
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">phone</span>: <span class="hljs-number">18819168888</span>,
      <span class="hljs-attr">money</span>: <span class="hljs-number">12345.88</span>,
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-18">7.添加md文件</h5>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d2626044bc64fd69715198b85277900~tplv-k3u1fbpfcp-watermark.image" alt="1627379335(1).png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-19">3.结尾哦~</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f07edc1e826a4dc4a17728dba354896b~tplv-k3u1fbpfcp-watermark.image" alt="1627379466(1).png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f47c09feafd42cf9c77578988dbb6a8~tplv-k3u1fbpfcp-watermark.image" alt="1627379494(1).png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>推荐<a href="https://juejin.cn/post/6844903919106129933" target="_blank" title="https://juejin.cn/post/6844903919106129933">从0到1发布一个npm包</a></p></div>  
</div>
            
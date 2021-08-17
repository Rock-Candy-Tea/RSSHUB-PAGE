
---
title: '【今天你更博学了么】从0到1发布属于自己的库到npm'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b3dc84454b39420ca70a0ae88889e7dc~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 16 Aug 2021 16:04:44 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b3dc84454b39420ca70a0ae88889e7dc~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p>这是我参与8月更文挑战的第5天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<h1 data-id="heading-0">什么是NPM</h1>
<p><code>NPM（Node Package Manager）</code>，一个 <code>Node.js</code> 的包管理工具。本文不是 <code>npm</code> 的教程，简单说一下，最显著的作用就是用来管理和共享代码的。</p>
<h1 data-id="heading-1">我的代码为什么要发布到NPM</h1>
<p>相信每个开发现代化工程的前端，都或多或少接触过 <code>NPM</code> ，也或许敲了无数次的 <code>npm i xxx</code> ，同时我也相信，每一个前端在自己的开发生涯中，或多或少的总结了各种奇淫巧技，封装了各种函数工具。</p>
<p>但是我们都知道每次 <code>npm i</code> 下来的东西有什么作用，如何使用，但从来没有 <code>npm i</code> 过自己的代码。</p>
<p>我们每次切换新的项目都会复制一份到新项目里，甚至在别人问的时候，直接发了段代码过去。</p>
<p>所以我为什么要发布自己的代码到 <code>NPM</code> 呢？</p>
<p>一是为了自己方便，更换工程的时候直接一个 <code>npm i my-xxx</code> 就能在新项目里使用自己封装的骚操作。</p>
<p>二是为了他人方便，当别人需要的时候，只需告诉他安装什么什么包，然后看 <code>README</code>，完活。</p>
<h1 data-id="heading-2">如何发布代码到NPM</h1>
<h2 data-id="heading-3">首先你要有个 NPM 账号</h2>
<p>你要到👉👉<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/" ref="nofollow noopener noreferrer">NPM官网</a> 注册一个账号。注册账号就不详细讲了，就跟你注册大多数网站的账号是一样的，很傻瓜🤣，然后记下自己的 <strong>用户名</strong>，<strong>密码</strong>，和 <strong>邮箱</strong>。</p>
<h2 data-id="heading-4">然后你要新建一个文件夹</h2>
<p>新建一个文件夹，命名没有要求，正常开发项目怎么命名，这里就怎么命名就行。</p>
<h2 data-id="heading-5">配置包的参数</h2>
<p>进入到目标文件夹，我们终端输入</p>
<pre><code class="hljs language-js copyable" lang="js">npm init
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后会让我们输入一些配置项，来看看都有哪些内容</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b3dc84454b39420ca70a0ae88889e7dc~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><strong>package name：</strong> 括号里面这个就是替你默认把文件夹名放在这里了，直接使用就行，也可以改成其他的。这是我们后面用于下载时候的包名。</li>
<li><strong>version：</strong> 版本号。括号里默认是 <code>1.0.0</code> ，并且需要遵循 <code>x.x.x</code> 的格式。</li>
<li><strong>description：</strong> 编写描述信息，有助于人们在 <code>npm</code> 库中搜索的时候发现你的模块。</li>
<li><strong>entry point：</strong> 指定了加载的入口文件，默认是 <code>index.js</code>。</li>
<li><strong>test command：</strong> 测试指令，本文用不到，可以不填。</li>
<li><strong>git repository：</strong> 指定一个代码存放地址，，本文用不到，可以不填。</li>
<li><strong>keywords：</strong> 关键字，有助于人们在 <code>npm</code> 库中搜索的时候发现你的模块。</li>
<li><strong>author：</strong> 作者的名字。</li>
<li><strong>license：</strong> 当前项目的协议，让用户知道他们有何权限来使用你的模块，默认是 <code>ISC</code>。</li>
</ul>
<p>全部输入完以后，会给我们一个预览，问我们这样可以吗，然后我们回车即可。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/30fbacdfa1a54550b5c85cdccc593a13~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>之后会在根目录下生成一个 <code>package.json</code> 的文件。内容就是我们刚刚配置的哪些。</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-comment">//package.json</span>
&#123;
  <span class="hljs-attr">"name"</span>: <span class="hljs-string">"testnpm"</span>,
  <span class="hljs-attr">"version"</span>: <span class="hljs-string">"1.0.0"</span>,
  <span class="hljs-attr">"description"</span>: <span class="hljs-string">"this is a test package"</span>,
  <span class="hljs-attr">"main"</span>: <span class="hljs-string">"index.js"</span>,
  <span class="hljs-attr">"scripts"</span>: &#123;
    <span class="hljs-attr">"test"</span>: <span class="hljs-string">"echo \"Error: no test specified\" && exit 1"</span>
  &#125;,
  <span class="hljs-attr">"keywords"</span>: [
    <span class="hljs-string">"test"</span>
  ],
  <span class="hljs-attr">"author"</span>: <span class="hljs-string">"yiweiliuying"</span>,
  <span class="hljs-attr">"license"</span>: <span class="hljs-string">"ISC"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">生成package-lock.json</h2>
<p>执行下方命令，生成 <code>package-lock.json</code> 文件，方便我们查看和调试。</p>
<pre><code class="hljs language-js copyable" lang="js">npm link
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">登录账号</h2>
<pre><code class="hljs language-js copyable" lang="js">npm login 
<span class="hljs-comment">//然后输入Username Password Email 即可</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b9be7aef92444afa27e06ac0c3cb0ce~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我这里用淘宝源的时候报了 <code>500</code> 错误，改成 <code>npm</code> 的源就好了，当看到<code> Logged in as hanzhiwei0174 on https://registry.npmjs.org/.。</code> 就说明我们登录成功了。</p>
<h2 data-id="heading-8">然后就可以发布我们的代码了</h2>
<pre><code class="hljs language-js copyable" lang="js">npm publish
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/494f832db91c44ab9ea5ee792a033b5f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>发现图中报了 <code>403</code> 的错误，这是因为我们的包名已经被别人使用了，所以我们需要修改一下。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6ec6021d7bec4ba1b643186e2165ab9a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>修改完以后再次运行 <code>npm publish</code> ，当我们看到 <code>+xxx</code> 就证明我们已经发布成功了。现在去 <code>npm</code> 的官网看一下。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/840a67e0eda94e33903aa6dfa4041c95~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到我们的代码就成功的被发布到 <code>npm</code> 上了。</p>
<h1 data-id="heading-9">如何使用已经发布的NPM包</h1>
<p>这个步骤其实有点多余，谁还没通过 <code>npm</code> 使用过别人的库了。</p>
<p>毕竟是自己的库，搞一手。</p>
<p>我随便找了个 <code>vue3</code> 的项目</p>
<pre><code class="hljs language-js copyable" lang="js">npm i vuf3 -s
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在 <code>node_modules</code> 找一下，打开 <code>index.js</code> 发现和我们之前写的一模一样。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/38b5c36e667d48c68126b7ff2a751b41~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; test &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vuf3'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>测试一下</p>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">'handleTest'</span>></span>测试NPM<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; test &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vuf3'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  setup () &#123;
    <span class="hljs-keyword">const</span> handleTest = <span class="hljs-function">() =></span> &#123;
      test(<span class="hljs-number">123</span>);
    &#125;;

    <span class="hljs-keyword">return</span> &#123;
      handleTest,
    &#125;;
  &#125;,
&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d7e27828352408e803fa2bee3198bcd~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>成功!以后就可以封装自己的各种工具函数到这里，开始打造自己的库。</p>
<h1 data-id="heading-10">如何更新版本</h1>
<p>代码修改完成后，修改 <code>package.json</code> 中的 <code>version</code> 字段，然后再次执行 <code>npm publish</code> 即可。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d298c77288dd481eba844992e7636e71~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到，<code>npm</code> 官网上的版本已经到了<code>3.0.1</code>。
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/636c0aad08e7484daa6efa7e7937e063~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-11">如何删除版本</h1>
<pre><code class="hljs language-js copyable" lang="js">npm unpublish package.name@version
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/97b3f4484eac4394ac48ff2f17273ca8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当我们看到 <code>-vuf3@3.0.1</code> 的时候，说明版本已经成功的删除掉了。</p>
<p>可以看到，版本再次回退到 <code>1.0.21</code> 了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8a5d37fef58648e9afdad81c8f1d40dd~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>注意</strong></p>
<ul>
<li>只有在发包的<strong>24小时内才允许</strong>撤销发布的包</li>
<li><strong>即使</strong>你撤销了发布的包，<strong>发包的时候也不能再和被撤销的包的名称和版本重复了</strong></li>
</ul>
<p>本文旨在记录如何发布一个包到 <code>npm</code> ，至于每个字段的细节，每个命令的限制等知识点，需要自行了解。</p></div>  
</div>
            
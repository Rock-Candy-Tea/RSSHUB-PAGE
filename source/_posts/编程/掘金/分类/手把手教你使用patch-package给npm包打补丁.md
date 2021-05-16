
---
title: '手把手教你使用patch-package给npm包打补丁'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ef998ad8fee4a28904fd326cdb430f5~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 15 May 2021 08:31:54 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ef998ad8fee4a28904fd326cdb430f5~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">一、背景</h1>
<p>故事从日常团队协作开发展开，整个team使用<code>react + antd4</code>搭建前端页面，在开发中我发现<code>antd4.9.*</code>版本的<code>Input.TextArea</code>组件存在一个bug，该bug表现为<code>maxLength</code>属性限制不符合预期，当输入中文字符时，该属性会将与中文对应的预输入拼音字数一同限制，导致汉字输入长度受阻。查阅了github仓库issue及相关changelog发现官方在v4.15.*版本修复了该bug。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ef998ad8fee4a28904fd326cdb430f5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>遇到这种问题和大多数人一样，我首先想到的就是升级antd到最新版本，于是二话不说一顿操作，升级完后果然问题迎刃而解~</p>
<p>然而问题真的解决了么？事情往往不是预期的那么顺利，本以为一波愉快升级已经完美的解决了问题，不料好景不长一周后小A同学发来问候：“我发现antd <code>v4.15.3</code>版本存在一个bug，<code>upload</code>组件在<code>windows</code>上无法触发<code>beforeUpload</code>钩子，新功能着急走查于是我将antd定了4.9.4版本”。如此噩耗袭来内心自然是千般不适，进退两难之间脑海中浮现出了之前早有耳闻但一直疏于尝试的<strong>打补丁</strong>大法，二话不说开始操作。</p>
<h1 data-id="heading-1">二、给npm包打补丁</h1>
<h2 data-id="heading-2">1.安装 patch-package</h2>
<pre><code class="hljs language-js copyable" lang="js">npm i patch-package --save-dev
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">2.修改npm包</h2>
<p>为了避免 v4.15.3 版本之前的其他组件存在未知bug，本次补丁我们基于 4.15.3 版本给 upload 组件打补丁。</p>
<p>打开目标项目代码 <code>node_modules</code> 文件夹，确认是4.15.3版本</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6b31001de25e4ebf98d3b4465dc2cdbd~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>打开一个不用的工程，安装 v4.9.4 版本并同样打开antd目录</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4611557cd5a446b2a22996db7c1e6a2e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>使用复制大法将我们要修改的upload组件代码从 4.9.4 copy到 4.15.3 ，然后 <code>npm run dev</code>启动项目，测试upload组件的bug是否被修复。</p>
<h2 data-id="heading-4">3.生成补丁</h2>
<p>经验证效果符合预期，此时<code>cd</code>到根木录下，执行如下命令生成补丁文件：</p>
<pre><code class="hljs language-shell copyable" lang="shell">npx patch-package antd
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时在根目录下会得到如下文件</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d4f4b67bab2c4ff280869479886fea61~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>很好奇<code>.patch</code>文件是个什么东东，打开文件一目了然，其实就是一些<code>git diff</code>记录描述，补丁原理呼之欲出 ——
<code>patch-package</code>会将当前<code>node_modules</code>下的源码与原始源码进行<code>git diff</code>，并在项目根目录下生成一个<code>patch</code>补丁文件。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c3ca74bc47884af29d82b51201823ad1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">4.加入版本管理</h2>
<p>至此补丁文件已经生成完毕，我们需要将它提交到<code>git</code>中，直接执行常规git操作即可：</p>
<pre><code class="hljs language-Shell copyable" lang="Shell">git add patches/antd+4.15.3.patch

git commit -m "feat:添加antd补丁"

git push
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">5.完善npm脚本</h2>
<p>当其他同事拉到代码如何应用补丁呢？基于上述操作我们在<code>npm install</code>后执行<code>patch-package</code>命令即可，这个流程可借助<code>npm script</code>实现，在<code>package.json</code>的<code>script</code>中添加如下字段及内容：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
    <span class="hljs-attr">"postinstall"</span>:<span class="hljs-string">"patch-package"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行一次完成的「依赖安装 -> 构建发布」，一切符合预期，大功告成~</p>
<h1 data-id="heading-7">三、其他方式</h1>
<p>那其实想要单纯修改 <code>npm</code> 包方法不止本文介绍的patch-package，对比下其他方法，才能感受到为何patch-package是最优解。</p>
<h2 data-id="heading-8">1、单文件修改法</h2>
<p>原理是先找到要修改的<code>npm</code>包的文件，先把这个文件拷贝一份到项目目录下，接着修改文件内容并使用</p>
<ul>
<li>拷贝覆盖法</li>
</ul>
<p>还是用<code>postinstall</code>这个勾子，在这个勾子执行<code>cp </code>修改过的文件 <code>./node_modules/包名/原始文件</code>拷贝过去，最终<code>node_modules</code>下的文件就变成了修改后的文件了，应用在本篇antd例子中如下：</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-attr">"postinstall"</span>: <span class="hljs-string">"cp ./patches/upload/* ./node_modules/antd/lib/"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>即在每次install包后执行用修改后文件覆盖原始文件逻辑。</p>
<ul>
<li>修改引用法</li>
</ul>
<p>配置一个<code>webpack alias</code>别名，如<code>'原始文件的引用路径': '修改后文件的引用路径'</code>，使得最终修改后的文件被引用，如：</p>
<pre><code class="hljs language-js copyable" lang="js">resolve: &#123;
      <span class="hljs-attr">alias</span>: &#123;
          <span class="hljs-string">'antd/upload'</span>: path.resolve(__dirname, <span class="hljs-string">'./patched/upload/*'</span>),
      &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">2、整体copy项目法</h2>
<p>将需要修改的包的项目源码整个拷贝下来，进行修改，然后使用</p>
<ul>
<li>
<p>直接引用法</p>
<p>直接使用完成的源码，不再通过npm包方式引用。</p>
</li>
<li>
<p>发布私库法</p>
<p>适合一个npm包几个项目在用的场景，可以把修改后的源码发布到私有的npm仓库上，供项目使用，这样多个项目就只需要修改一次源码</p>
</li>
</ul>
<h2 data-id="heading-10">3、外部代码修改法</h2>
<p>这个方法就是不直接修改 <code>node_modules</code> 的源码，而是利用js特性，在执行时，修改这个包的内部属性，从而达到目的。</p>
<p>简单来说就是利用<code>defineProperty</code>、<code>prototype</code>等特性修改包内的类，举个不恰当的例子，如<code>Vue2.0</code>中使用<code>defineProperty</code>给组件实例做<code>数据劫持和代理</code>。在vue项目中我们也经常在<code>main.js</code>中给<code>Vue根实例</code>通过<code>Vue.prototype.xxx=xxxx</code>挂一些全局属性和方法。</p>
<h2 data-id="heading-11">4、patch-package优势</h2>
<p>使用上述三种方式虽然能通过一些骚操作解决某些特定场景下的问题，但都无法避免<code>版本升级</code>带来的困扰，如果该npm包升级，可能会导致原先的修改产生错误，所以如果想使用上述三种办法，最好还是要将版本号写死。然而patch-package有如下特性：</p>
<ul>
<li>
<p>版本试错</p>
<p>如果你装的包版本和你之前生成的补丁中记录的版本不一样，<code>npx patch-package</code>会直接报错<code>**ERROR** Failed to apply patch for package xxxx at path</code>，通过提示你可以更方便的定位问题</p>
</li>
<li>
<p>节省空间</p>
<p>使用<code>git diff</code>来记录补丁比起重写一份源码的方法更节省空间，<code>即安全</code>，<code>又便捷</code></p>
</li>
</ul>
<h1 data-id="heading-12">总结</h1>
<p>通过本文介绍，相信你已经对<code>patch-package</code>有了很好的理解，可以在日常开发中优雅的解决<code>鱼和熊掌不可兼得</code>的难题，但补丁虽能避风日也不及新衣保暖，问题出现时最好还是从正规渠道寻求最根本的解决，如给官方提<code>issue</code>并关注版本更新和bug修复情况，以便及时更新或者移除补丁。愿天下补丁都能早日换新衣~</p></div>  
</div>
            
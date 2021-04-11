
---
title: '新型前端构建工具 Vitejs 开发使用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/02e76704411c4110b0cf528e742de82c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 10 Apr 2021 07:03:54 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/02e76704411c4110b0cf528e742de82c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><blockquote>
<ul>
<li>原文地址：<a href="https://blog.bitsrc.io/the-new-king-of-bundlers-is-here-all-bow-before-vitejs-fe6f42c97ce9" target="_blank" rel="nofollow noopener noreferrer">The New King of Bundlers Is Here: All Bow Before Vitejs</a></li>
<li>原文作者：<a href="https://medium.com/@deleteman123" target="_blank" rel="nofollow noopener noreferrer">Fernando Doglio</a></li>
<li>译文出自：<a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a></li>
<li>本文永久链接：<a href="https://github.com/xitu/gold-miner/blob/master/article/2021/the-new-king-of-bundlers-is-here-all-bow-before-vitejs.md" target="_blank" rel="nofollow noopener noreferrer">github.com/xitu/gold-m…</a></li>
<li>译者：<a href="https://github.com/zenblo" target="_blank" rel="nofollow noopener noreferrer">zenblo</a></li>
<li>校对者：<a href="https://juejin.cn/user/1134351730353207" target="_blank">Badd</a>、<a href="https://github.com/5Reasons" target="_blank" rel="nofollow noopener noreferrer">5Reasons</a></li>
</ul>
</blockquote>
<h1 data-id="heading-0">新型前端构建工具 Vitejs 开发使用</h1>
<p><img alt="11.jpg" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/02e76704411c4110b0cf528e742de82c~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>在我刚接触编程的时候，JavaScript 只是被用来给网站添加一些交互效果。你还记得如何添加鼠标拖拽效果吗？或者如何在鼠标悬停时改变链接颜色？</p>
<p>当然，多年来，Web 开发已经有了很大的发展，如今 JavaScript 在 Web 应用中的使用量正在呈指数级增长。正因为如此，JavaScript 愈加笨重的依赖包正在成为它的瓶颈。</p>
<p>一些应用程序的依赖包体积已经影响到用户使用应用程序前的等待时长了（在依赖包下载完成之前，他们无法使用应用程序），构建过程本身也导致开发时间的增加（有时改变一行代码就会触发一个需要几分钟的编译过程）。虽然有一些技术可以帮助解决这个问题，但并不是所有的技术都能斩草除根，而能斩草除根者往往需要花费大量精力才能实现。作为这些构建工具的使用者，你或许不在意它的实现技术，但如果你是构建工具的开发者，那么维护起来就会变得非常痛苦。</p>
<p>这就是为什么今天我想向你介绍一款能解决所有这些问题的工具：<a href="https://vitejs.dev/" target="_blank" rel="nofollow noopener noreferrer">ViteJS</a>。</p>
<h2 data-id="heading-1">ViteJS 为何如此优秀</h2>
<p>显然，这是你应该问自己的第一个问题。</p>
<p>已经有很多的构建工具了，你还需要一个吗？是的，你需要。</p>
<p>ViteJS 不仅仅是一个构建工具。事实上，ViteJS 的目标是成为构建任何基于 JavaScript 项目的首选工具。它改变了通常的构建工具对依赖包的处理方式，直接利用 ES 模块来打包构建，让浏览器来完成一些工作。</p>
<p>它还大量使用 HTTP 缓存不更改的代码。所以，与其使用一个巨大的依赖文件，把所有的代码发送给客户端，不如由客户端决定保留哪些代码和经常刷新哪些代码（下文会详细阐述）。</p>
<p>你可能要注意的 ViteJS 功能特性：</p>
<ul>
<li><strong>构建时考虑到了处理时效</strong>。ViteJS 所做的少量依赖和转码工作，都是使用 <a href="https://esbuild.github.io/" target="_blank" rel="nofollow noopener noreferrer">esbuild</a> 来完成的，而 esbuild 是建立在 Go 中的。这反过来又提供了更快的体验（根据他们的说法，比任何基于 JavaScript 的构建工具快 10~20 倍）。</li>
<li><strong>与 TypesScript 兼容</strong>。虽然它不执行类型检查，但通常你的 IDE 会处理这个问题，你甚至可以在构建脚本中添加一个快速的单行代码来为你做这件事（快速的 <code>tsc --noEmit</code>）。</li>
<li><strong>它支持热模块替换（HMR）</strong>。ViteJS 提供了一个 <a href="https://vitejs.dev/guide/api-hmr.html#hot-data" target="_blank" rel="nofollow noopener noreferrer">API</a>，供任何 ESM 兼容的框架使用。</li>
<li><strong>改进了代码拆分技术</strong>。ViteJS 实现了对浏览器正常分块加载过程的一些改进。这确保了如果有机会并行加载几个分块，它们将以这种方式加载。</li>
</ul>
<p>事实上，ViteJS 的功能特性还在继续增加，所以一定要去 ViteJS 网站查看更多详情。</p>
<h2 data-id="heading-2">ViteJS 内置插件系统</h2>
<p>ViteJS 的主要优势之一是它内置了一个插件系统，这意味着社区可以（并且已经）给其他框架（如 React 和 Vue）添加额外的功能和插件。</p>
<h3 data-id="heading-3">Vue 项目使用 ViteJS</h3>
<p><a href="https://github.com/vitejs/awesome-vite#vue" target="_blank" rel="nofollow noopener noreferrer">Vue 的插件列表</a>是相当丰富的，唯一需要注意的是，这些插件并不都是兼容同一个版本的框架（有的插件适用于 Vue 2，而有的插件只适用于 Vue 3，有的则是两者都适用）。</p>
<p>为了让你的 Vue App 方便使用，你可以使用一个插件，例如 <a href="https://github.com/antfu/vitesse" target="_blank" rel="nofollow noopener noreferrer">Vitesse</a>，你可以简单地克隆和重命名。它预装了多种内置功能和插件，例如：</p>
<ul>
<li><a href="https://github.com/windicss/windicss" target="_blank" rel="nofollow noopener noreferrer"><strong>WindiCSS</strong></a> 作为 UI 框架和 <a href="https://windicss.netlify.app/guide/plugins.html#typography" target="_blank" rel="nofollow noopener noreferrer"><strong>WindiCSS 排版</strong></a>。</li>
<li><a href="https://iconify.design/" target="_blank" rel="nofollow noopener noreferrer"><strong>Iconify</strong></a> 允许你使用网络上多个图标库的图标。</li>
<li><strong>ViteJS 的 <a href="https://github.com/intlify/vite-plugin-vue-i18n" target="_blank" rel="nofollow noopener noreferrer">Vue i18n 插件</a></strong>，增加国际化支持。</li>
<li><strong>VS Code 扩展系列</strong> (例如 Vite 的 <code>dev server</code>、<code>i18n ally</code>、<code>WindiCSS</code>、<code>Iconify Intellisense</code> 等)，如果你是 VS Code 用户，这是很好的选择。</li>
</ul>
<p>还有更多的内置功能，一定要去看 <a href="https://github.com/antfu/vitesse" target="_blank" rel="nofollow noopener noreferrer">Repo</a>。</p>
<p>如果你只是想从头开始，构建自己的应用，你也可以简单地使用 ViteJS 的 CLI 工具。</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 如果你正在使用 npm 7</span>
$ npm init @vitejs/app my-vue-app -- --template vue 

<span class="hljs-comment"># 如果你正在使用 npm 6</span>
$ npm init @vitejs/app my-vue-app --template vue

<span class="hljs-comment"># 如果你是一个偏向于使用 yarn 的开发者</span>
$ yarn create @vitejs/app my-vue-app --template vue
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上任意一个命令都会产生相同的输出：</p>
<p><img alt="22.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca10b3e19313471eac9cf8857f0026c1~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>它的速度真的很快（不到一秒），在遵循这额外的三个步骤后，你的 Vue 应用就会启动并运行。</p>
<p><img alt="33.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb4d5939df1f4cee9eb2d33f3911a359~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">React 项目使用 ViteJS</h3>
<p>你不是 Vue 开发者？没问题，Vite 可以帮你解决。</p>
<p>只需使用与之前相同的命令行，并且使用 <code>react</code> 或 <code>react-ts</code> 代替 <code>vue</code> 就可以了。</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ npm init @vitejs/app my-react-app --template react-ts
$ <span class="hljs-built_in">cd</span> my-react-app
$ npm install
$ npm run dev
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上命令行将使用 TypeScript 输出相同的 React 应用程序。</p>
<p><img alt="44.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d755a321c84e4661a916a75022b39f53~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>你想要更多的预设吗？根据你的需求可以找到两个插件：</p>
<ol>
<li>如果你正在寻找一个带有 TypeScript、<a href="https://chakra-ui.com/" target="_blank" rel="nofollow noopener noreferrer">Chakra</a> 和 <a href="https://www.cypress.io/" target="_blank" rel="nofollow noopener noreferrer">Cypress</a> 的项目，你可以使用这个<a href="https://github.com/Dieman89/vite-reactts-chakra-starter" target="_blank" rel="nofollow noopener noreferrer">插件</a>。</li>
<li>如果你不想使用 Chakra，而是想创建一个 Electron 应用，你可以使用这个<a href="https://github.com/maxstue/vite-reactts-electron-starter" target="_blank" rel="nofollow noopener noreferrer">插件</a>，它还包含了 <a href="https://tailwindcss.com/" target="_blank" rel="nofollow noopener noreferrer">TailwindCSS</a>。</li>
</ol>
<p>这两个选项都可以和 TypeScript 一起使用，如果你熟悉这些组合，我建议你选择使用这些插件而不是从头开始。你要知道，默认的启动项目是完全没有问题的，但是你可以通过这些插件得到一部分已经完成的模板设置。</p>
<h2 data-id="heading-5">关于其它构建工具</h2>
<p>ViteJS 并不是第一个尝试这样做的工具，也绝对不是最知名的。但它之所以被创造出来，是因为目前的主流工具并没有用行业的最新趋势来解决性能问题。他们还在试图解决一些鉴于当今最先进的技术而不应该存在的问题。</p>
<p>ViteJS 和其他构建工具（如 Webpack）的主要区别在于，后者会尝试通过你的依赖树，编译和优化打包后的代码，以更好地让任何浏览器获取你的代码。注意这里的<strong>任何</strong>一词，因为这将是 ViteJS 的主要问题。然而，这个过程需要时间，如果你一直在使用这些成熟的构建工具，你可能知道我的意思。它需要一段时间，但最终的结果对任何浏览器来说都是好的。</p>
<p>另一方面，我们有 ViteJS，就像我已经提到的，它利用了浏览器的 ES 模块支持。这意味着浏览器将负责处理 <code>import</code> 和 <code>export</code>，并单独请求它们。这意味着你可以在短时间内让你的应用运行起来，但这也意味着只有新的浏览器才能兼容你的应用。</p>
<p>从下面的 <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules" target="_blank" rel="nofollow noopener noreferrer">MDN</a> 表格中可以看出，现代浏览器对 <code>import</code> 的支持是很好的，但是，旧版本永远无法支持。</p>
<p><img alt="55.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f0850014273b46a2807708d3132a03bb~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>兼容性方面还有工作要做，所以如果你考虑在下一个项目中使用 ViteJS，请确保你的目标受众倾向于定期更新他们的浏览器。</p>
<p>当涉及到依赖工具时，ViteJS 有可能颠覆当前的行业标准。它有技术，它有插件生态系统，它有所需的功能。唯一阻止它获得事实上的构建工具桂冠的，是它对旧浏览器的兼容性。</p>
<p>显然，浏览器兼容性在今天仍旧是一个问题，但这是我们行业中越来越少的一部分人的问题，所以请关注 ViteJS，因为它会随着浏览器的更新而愈加流行。</p>
<blockquote>
<p>如果发现译文存在错误或其他需要改进的地方，欢迎到 <a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a> 对译文进行修改并 PR，也可获得相应奖励积分。文章开头的 <strong>本文永久链接</strong> 即为本文在 GitHub 上的 MarkDown 链接。</p>
</blockquote>
<hr>
<blockquote>
<p><a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a> 是一个翻译优质互联网技术文章的社区，文章来源为 <a href="https://juejin.im/" target="_blank" rel="nofollow noopener noreferrer">掘金</a> 上的英文分享文章。内容覆盖 <a href="https://github.com/xitu/gold-miner#android" target="_blank" rel="nofollow noopener noreferrer">Android</a>、<a href="https://github.com/xitu/gold-miner#ios" target="_blank" rel="nofollow noopener noreferrer">iOS</a>、<a href="https://github.com/xitu/gold-miner#%E5%89%8D%E7%AB%AF" target="_blank" rel="nofollow noopener noreferrer">前端</a>、<a href="https://github.com/xitu/gold-miner#%E5%90%8E%E7%AB%AF" target="_blank" rel="nofollow noopener noreferrer">后端</a>、<a href="https://github.com/xitu/gold-miner#%E5%8C%BA%E5%9D%97%E9%93%BE" target="_blank" rel="nofollow noopener noreferrer">区块链</a>、<a href="https://github.com/xitu/gold-miner#%E4%BA%A7%E5%93%81" target="_blank" rel="nofollow noopener noreferrer">产品</a>、<a href="https://github.com/xitu/gold-miner#%E8%AE%BE%E8%AE%A1" target="_blank" rel="nofollow noopener noreferrer">设计</a>、<a href="https://github.com/xitu/gold-miner#%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD" target="_blank" rel="nofollow noopener noreferrer">人工智能</a>等领域，想要查看更多优质译文请持续关注 <a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a>、<a href="http://weibo.com/juejinfanyi" target="_blank" rel="nofollow noopener noreferrer">官方微博</a>、<a href="https://zhuanlan.zhihu.com/juejinfanyi" target="_blank" rel="nofollow noopener noreferrer">知乎专栏</a>。</p>
</blockquote></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            
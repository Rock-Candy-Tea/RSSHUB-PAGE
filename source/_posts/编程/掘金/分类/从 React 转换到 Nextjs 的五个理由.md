
---
title: '从 React 转换到 Next.js 的五个理由'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/de82647f7039418784c69034dc4337f1~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 30 Apr 2021 02:21:01 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/de82647f7039418784c69034dc4337f1~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><blockquote>
<ul>
<li>原文地址：<a href="https://javascript.plainenglish.io/5-reasons-to-switch-from-react-to-next-js-f776413693d0" target="_blank" rel="nofollow noopener noreferrer">5 Reasons to Switch from React to Next.js</a></li>
<li>原文作者：<a href="https://medium.com/@anuragkanoria" target="_blank" rel="nofollow noopener noreferrer">anuragkanoria</a></li>
<li>译文出自：<a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a></li>
<li>本文永久链接：<a href="https://github.com/xitu/gold-miner/blob/master/article/2021/5-Reasons-to-Switch-from-React-to-Next-js.md" target="_blank" rel="nofollow noopener noreferrer">github.com/xitu/gold-m…</a></li>
<li>译者：<a href="https://github.com/zenblo" target="_blank" rel="nofollow noopener noreferrer">Zz招锦</a></li>
<li>校对者：<a href="https://github.com/KimYangOfCat" target="_blank" rel="nofollow noopener noreferrer">Kim Yang</a>、<a href="https://github.com/Cyberhan123" target="_blank" rel="nofollow noopener noreferrer">Cyberhan123</a></li>
</ul>
</blockquote>
<h1 data-id="heading-0">从 React 转换到 Next.js 的五个理由</h1>
<blockquote>
<p>选择错误的框架可能会成为一个可怕的噩梦。</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/de82647f7039418784c69034dc4337f1~tplv-k3u1fbpfcp-watermark.image" alt="11.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>那是在 2020 年，第一次疫情封城刚开始的时候。像全球各地的人们一样，我发现自己有计划外的闲暇时间。</p>
<p>我决定利用这段闲暇时间学习新技术，最终学习了 React 并提升了我的 Node.js 技能。</p>
<p>我构建了一个博客平台，前端部分使用 React，后端部分使用 Node.js 服务器。该平台具有你所期望的一个标准应用程序所具有的所有功能。</p>
<ol>
<li>
<p>多种账号登录选项（用谷歌、Twitter 账号等登录）。</p>
</li>
<li>
<p>功能丰富的编辑器，可以写出漂亮的博客。</p>
</li>
<li>
<p>能够创建草稿和编辑已发表的文章。</p>
</li>
<li>
<p>分析以及管理面板。</p>
</li>
</ol>
<p>在这个过程中，我学到了一些关于 Web 开发的很有价值的经验知识。</p>
<p>从用户的角度来看，一切似乎都很好，但对于开发者来说，维护项目代码是一场噩梦。</p>
<p>这时我才明白 Next.js 的标语 —— “用于生产的 React 框架”的真正含义。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9e22223a33044f6fb0de0cbf84f9702e~tplv-k3u1fbpfcp-watermark.image" alt="22.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我从 React 转到 Next.js 主要有以下五个原因。</p>
<h2 data-id="heading-1">1. React 对 SEO 不友好</h2>
<p>每一个博客或一个可生产的网站都需要为搜索引擎进行优化（SEO），除了一些像控制面板或用户设置的网站。</p>
<p>已经快一年了，但我的 React 网站的大部分博客仍然没有出现在谷歌搜索上，即使我专门使用 URL 和其他工具进行搜索。</p>
<p>此后，我尝试过使用 <a href="https://www.npmjs.com/package/react-helmet" target="_blank" rel="nofollow noopener noreferrer">React Helmet</a> 等库来对 React 网站进行搜索引擎优化。</p>
<p>React 对 SEO 不友好，是因为它不在服务器端渲染。与之相对，Next.js 的主要优势是它支持服务器端渲染。</p>
<p>一个好的搜索引擎优化方案可以提升有效流量，Next.js 似乎是能够保证这一点的解决方案。</p>
<p>然而，我想指出的是，客户端 ReactJS 应用程序并不是不能被谷歌机器人爬取。它们是能被爬取的，只是其 SEO 效果不如 Next.js 所提供的好。</p>
<p>如果你想详细了解 JavaScript 应用程序中的渲染和 SEO，请查看我的博客，在那里我用通俗的语言讲解过这些话题。
在建立了多个网站之后编写的初级 JavaScript 网络应用程序 SEO 指南：
<a href="https://javascript.plainenglish.io/a-beginners-guide-to-seo-for-javascript-web-applications-c67d55728291" target="_blank" rel="nofollow noopener noreferrer">以下是我学到的关于有效流量和 SEO 的内容——javascript.plainenglish.io</a></p>
<h2 data-id="heading-2">2. AdSense 审核问题</h2>
<p>React 创建单页应用程序（SPA），该应用程序本质上是一个单页，只需要加载一次。</p>
<p>当你浏览页面并跳转到其它页面时，数据将动态加载。</p>
<p>尽管单页应用程序以快速响应和提供原生应用程序而闻名，但它们确实存在缺点。</p>
<p>当尝试使用 <a href="https://www.google.com/adsense/start/#/?modal_active=none" target="_blank" rel="nofollow noopener noreferrer">Google 的 AdSense</a> 来获取网站收益时，我发现了一个缺点。</p>
<p>AdSense 不是简单地检测他们要求我放入 index.html 文件中的代码，更出人意料的是，它根本找不到该网站上的任何内容。</p>
<p>这是因为博客是动态加载的，并且 AdSense 需要在批准网站展示广告之前先查看真实内容。</p>
<p>通过简单的 Google 搜索，我发现这是许多单页应用程序网站的常见问题。</p>
<p>这个问题根源是缺乏适当的服务器端渲染支持，而 Next.js 可以轻松解决它。</p>
<h2 data-id="heading-3">3. 更简单的导航</h2>
<p>理解 React 的导航和路由需要花费很大的学习成本，特别是当这个人之前使用 Vue 这样的框架（比如我）。</p>
<p>React 的路由使用了一个叫 <code>React-Router-Dom</code> 依赖包，代码看上去似乎很复杂。<a href="https://reactrouter.com/web/example/basic" target="_blank" rel="nofollow noopener noreferrer">这里有一个 React 路由的示例</a>。</p>
<p>由于我的网站功能丰富，拥有大量的页面，从预设的博客和注册页到常见问题和服务条款页。</p>
<p>Next.js 简化了所有这些页面的路由。它提供了一个基于文件系统的路由导航，建立在页面的概念上，而页面基本上就是一个 React 组件。</p>
<p>将这些页面文件添加到 pages 目录中，会自动使它成为一个路由。</p>
<p>这极大简化了路由配置，作为一个从 Vue 和 Nuxt 转换过来的开发者，这似乎很容易接受。</p>
<p>你可以在<a href="https://nextjs.org/docs/routing/introduction" target="_blank" rel="nofollow noopener noreferrer">这里</a>找到更多相关信息。</p>
<h2 data-id="heading-4">4. 支持 API 路由</h2>
<p>Next.js 内置了对 API 路由的支持，这使你能够使用已知的基于文件系统快速创建 API 端点。</p>
<p>你放在 <code>pages/api</code> 目录下的任何文件都将被视为 API 端点（作为一个 Node.js 的 serverless 功能）。</p>
<p>如果你需要运行一些服务器端的功能，这将是非常有用的特性，因为这些端点并不是客户端依赖包的一部分。</p>
<p>例如，如果你的网站上有一个输入表单，你可以向 API 端点发送 POST 请求，它将验证输入并将数据存储到数据库中。</p>
<p>这基本上可以让你创建 serverless 功能，它使我能够将 Node.js 和 React 代码合并为单一的 Next.js 应用程序。</p>
<p>Next.js 创建的前端 API 路由是 Next 利用本身的数据完成的。</p>
<p>如果你打算创建一个移动应用程序并从服务器获取数据，它可以提供帮助。</p>
<h2 data-id="heading-5">5. 内置图像组件</h2>
<p>正如我前面提到的，我建立了一个博客网站，任何博客都需要有媒体内容以及文本。</p>
<p>单独看这个博客本身，除了书面内容，它还有一些图片。</p>
<p><a href="https://nextjs.org/blog/next-10#images-on-the-web:~:text=Images%20take%20up%2050%25%20of%20the%20total%20bytes%20on%20web%20pages." target="_blank" rel="nofollow noopener noreferrer">根据 Next.js 文档说明，图像占网页内容的 50%</a>。</p>
<p>通常，媒体文件的大小有一个限制，例如 25 MB。</p>
<p>此外，一些加载的图片不在用户的视口中，也就是说，用户必须向下滚动才能看到图片。</p>
<p>因此，必须考虑许多因素，如懒加载、压缩、大小和格式。</p>
<p>Next.js 使用图像组件和自动图像优化功能解决了所有这些问题，它取代了HTML 的 <code><img></code> 标签。</p>
<p>通过使用它，图像在默认情况下被懒加载，浏览器适配图像的尺寸，在图像加载前留出空白。这就避免了图像的随机跳入，提高了用户体验。</p>
<p>此外，Next.js 的 <code>next/image</code> 组件使用最新的格式，如 WebP，按需缩小图片大小，WebP 比 JPEG 对应的图片要轻 30%。</p>
<p>此外，这些优化是按需进行的，所以不会影响构建时间，来自外部的图像也会被优化。</p>
<h2 data-id="heading-6">本文总结</h2>
<p>React 是<a href="https://www.codeinwp.com/blog/angular-vs-vue-vs-react/" target="_blank" rel="nofollow noopener noreferrer">最流行的框架</a>，毫无疑问，它是每个 Web 开发者必学的内容。</p>
<p>然而，这并不意味着 React 适用于每一种类型的网站。像其他框架一样，React 也有自己的不足。</p>
<p>构建于 React 之上的 Next.js 旨在为 React 的一些问题提供解决方案，同时也通过引入一些现代的内置解决方案来促进应用程序开发。</p>
<p>从 React 切换到 Next 是可行的，但如果你刚开始，请明智地选择 Next 而不是 React。</p>
<p>必须说明的是，在每个项目中使用 Next.js 而完全抛弃 React 也是不可取的。</p>
<p>每个网站和应用程序的建立都有其特定的意图和目标，这在选择正确的框架和库时可以起到至关重要的作用。</p>
<p>不幸的是，在我的案例中，我在完全用 React 构建网站之后，才发现我应该用 Next.js 而不是 React，原因就在上面。</p>
<p>希望你能从我的错误中学到一些东西，并能选择一个合适的框架。</p>
<p>感谢你的阅读！</p>
<p>更多内容请访问 <a href="https://plainenglish.io/" target="_blank" rel="nofollow noopener noreferrer">plainenglish.io</a>。</p>
<blockquote>
<p>如果发现译文存在错误或其他需要改进的地方，欢迎到 <a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a> 对译文进行修改并 PR，也可获得相应奖励积分。文章开头的 <strong>本文永久链接</strong> 即为本文在 GitHub 上的 MarkDown 链接。</p>
</blockquote>
<hr>
<blockquote>
<p><a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a> 是一个翻译优质互联网技术文章的社区，文章来源为 <a href="https://juejin.im/" target="_blank" rel="nofollow noopener noreferrer">掘金</a> 上的英文分享文章。内容覆盖 <a href="https://github.com/xitu/gold-miner#android" target="_blank" rel="nofollow noopener noreferrer">Android</a>、<a href="https://github.com/xitu/gold-miner#ios" target="_blank" rel="nofollow noopener noreferrer">iOS</a>、<a href="https://github.com/xitu/gold-miner#%E5%89%8D%E7%AB%AF" target="_blank" rel="nofollow noopener noreferrer">前端</a>、<a href="https://github.com/xitu/gold-miner#%E5%90%8E%E7%AB%AF" target="_blank" rel="nofollow noopener noreferrer">后端</a>、<a href="https://github.com/xitu/gold-miner#%E5%8C%BA%E5%9D%97%E9%93%BE" target="_blank" rel="nofollow noopener noreferrer">区块链</a>、<a href="https://github.com/xitu/gold-miner#%E4%BA%A7%E5%93%81" target="_blank" rel="nofollow noopener noreferrer">产品</a>、<a href="https://github.com/xitu/gold-miner#%E8%AE%BE%E8%AE%A1" target="_blank" rel="nofollow noopener noreferrer">设计</a>、<a href="https://github.com/xitu/gold-miner#%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD" target="_blank" rel="nofollow noopener noreferrer">人工智能</a>等领域，想要查看更多优质译文请持续关注 <a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a>、<a href="http://weibo.com/juejinfanyi" target="_blank" rel="nofollow noopener noreferrer">官方微博</a>、<a href="https://zhuanlan.zhihu.com/juejinfanyi" target="_blank" rel="nofollow noopener noreferrer">知乎专栏</a>。</p>
</blockquote></div>  
</div>
            
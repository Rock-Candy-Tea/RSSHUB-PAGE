
---
title: 'antd mobile v5 它悄悄的来了'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a828af5c473c42bda14aba55b0380da6~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 28 Aug 2021 06:29:33 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a828af5c473c42bda14aba55b0380da6~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p>在 React 领域里，一直缺少一套靠谱、好用的移动端组件，蚂蚁的 antd mobile v2 年久失修，几乎无人维护，跟 antd 相差甚远，在设计上，也有很多也已经跟不再符合 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdesign.alipay.com%2F" title="https://design.alipay.com/" target="_blank" rel="nofollow noopener noreferrer" ref="nofollow noopener noreferrer">Alipay Design</a>。</p>
<p><strong>激动人心的是</strong>，就在前两天，在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile" title="https://github.com/ant-design/ant-design-mobile" target="_blank" rel="nofollow noopener noreferrer" ref="nofollow noopener noreferrer">ant-design-mobile</a> 的 discussions 里面已经发布了 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fdiscussions%2F3924" title="https://github.com/ant-design/ant-design-mobile/discussions/3924" target="_blank" rel="nofollow noopener noreferrer" ref="nofollow noopener noreferrer">5.0（白杨）的 Roadmap</a>。</p>
<p>在 8 月 26 号晚上也已经宣布 v5 已经进入 beta。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a828af5c473c42bda14aba55b0380da6~tplv-k3u1fbpfcp-watermark.image" alt="image-20210827081425771" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">5.0（白杨） Roadmap</h2>
<p>5.0（白杨） 是我们最新在开发的下一代 antd-mobile 组件库，经过近 5 个月的开发，已经覆盖了 48 个组件，并已在许多项目中落地使用。</p>
<p>我们最近发布了 alpha 版本的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fantd-mobile" title="https://www.npmjs.com/package/antd-mobile" target="_blank" rel="nofollow noopener noreferrer" ref="nofollow noopener noreferrer">npm 包</a>，也部署了新的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fnext.mobile.ant.design%2F" title="https://next.mobile.ant.design/" target="_blank" rel="nofollow noopener noreferrer" ref="nofollow noopener noreferrer">文档站点</a>。坦白地讲，antd mobile 5.0 还并不够成熟，但我们希望能够尽早地推送给社区上的各位同学，也希望整个研发进程和规划尽可能地符合开源精神：透明、开放、合作。</p>
<p>所以，为了帮助大家更好地了解 5.0 版本，这里简单分享一下我们的思路和方向。</p>
<h2 data-id="heading-1">5.0 会带来什么</h2>
<h3 data-id="heading-2">视觉规范</h3>
<p>和 v3 v4 版本一致，v5 也将沿用最新版本的支付宝基础设计规范 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdesign.alipay.com%2F" title="https://design.alipay.com/" target="_blank" rel="nofollow noopener noreferrer" ref="nofollow noopener noreferrer">Alipay Design</a>。</p>
<h3 data-id="heading-3">手势和动画</h3>
<p>v5 使用了 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fpmndrs%2Fuse-gesture" title="https://github.com/pmndrs/use-gesture" target="_blank" rel="nofollow noopener noreferrer" ref="nofollow noopener noreferrer">use-gesture</a> 作为手势库、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fpmndrs%2Freact-spring" title="https://github.com/pmndrs/react-spring" target="_blank" rel="nofollow noopener noreferrer" ref="nofollow noopener noreferrer">react-spring</a> 作为动画库，具有更流畅细腻的手势交互和动画效果。</p>
<h3 data-id="heading-4">重新设计的 API</h3>
<p>v5 所有的组件都是完全重写的，API 也是重新设计的，更现代化也更优雅。</p>
<h3 data-id="heading-5">拥抱 css 变量</h3>
<p>css 变量提供了更加动态化的样式调整能力，也让组件的样式调整变得更加简洁优雅。在业务中对组件样式魔改是一件非常痛苦也非常难以维护的事情，我们希望通过 css 变量改变这一现状。</p>
<h2 data-id="heading-6">了解更多</h2>
<p>如果你想了解如何使用，可以<a href="https://link.juejin.cn/?target=https%3A%2F%2Fnext.mobile.ant.design%2Fguide%2Fquick-start" title="https://next.mobile.ant.design/guide/quick-start" target="_blank" rel="nofollow noopener noreferrer" ref="nofollow noopener noreferrer">去这里</a></p>
<p>如果你想点点试试各种组件，可以<a href="https://link.juejin.cn/?target=https%3A%2F%2Fnext.mobile.ant.design%2Fcomponents%2Fbutton" title="https://next.mobile.ant.design/components/button" target="_blank" rel="nofollow noopener noreferrer" ref="nofollow noopener noreferrer">去这里</a></p>
<p>此外，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fnext.mobile.ant.design%2Fguide%2Ffaq" title="https://next.mobile.ant.design/guide/faq" target="_blank" rel="nofollow noopener noreferrer" ref="nofollow noopener noreferrer">在这里</a>我们汇总了一些常见问题，希望能帮到你</p>
<h2 data-id="heading-7">发布计划</h2>
<blockquote>
<p>这些里程碑只是我们大致的计划，随着项目的不断推进，可能会有所调整</p>
</blockquote>
<h3 data-id="heading-8">Alpha</h3>
<p>我们在 7 月 12 日发布了第一个 alpha 版本，经过了一个多月的不断迭代，API 渐渐趋于稳定。</p>
<h3 data-id="heading-9">Beta</h3>
<p>我们预计将在近期开始推送 beta 版本，相较于 alpha 版本，beta 版本 API 更加稳定也更加完善。</p>
<p>在这个阶段我们还会增加更多的新组件：</p>
<ul>
<li>Swiper</li>
<li>ImageUpload</li>
<li>Sidebar</li>
<li>Calendar</li>
<li>Stepper</li>
<li>SegmentedControl</li>
<li>Skeleton</li>
<li>NumberKeyboard</li>
<li>SwipeAction</li>
<li>Navbar</li>
</ul>
<p>补充组件库的整体能力：</p>
<ul>
<li>支持国际化</li>
<li>暴露出更多的 css 变量</li>
<li>逐步完善自动化测试</li>
<li>增加英文文档</li>
<li>支持无障碍</li>
</ul>
<h3 data-id="heading-10">RC</h3>
<p>我们预计将在 10 月开始推送 rc 版本，在这期间我们将几乎不会再引入新的 break change。</p>
<h3 data-id="heading-11">Release</h3>
<p>我们预计在 11 月正式发布 5.0 版本。</p>
<h2 data-id="heading-12">最后</h2>
<p>最后让我们期待 11 月，antd mobile v5 的正式发吧，另外如果你对 antd mobile v5 如果很有兴趣，欢迎去试用，然后参与 v5 的开发，欢迎提 PR。</p>
<blockquote>
<p>悄悄的说一下我也是 v5 的贡献者，也是内部人员，后面会给大家带来更多的 antd mobile 的消息，欢迎关注、点赞。  欢迎关注我的公众号「前端桃园」</p>
</blockquote></div>  
</div>
            
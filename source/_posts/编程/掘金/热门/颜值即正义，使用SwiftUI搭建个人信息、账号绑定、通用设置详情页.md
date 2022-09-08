
---
title: '颜值即正义，使用SwiftUI搭建个人信息、账号绑定、通用设置详情页'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fcc9ef3883004503af0c799761a6f973~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
author: 掘金
comments: false
date: Thu, 11 Aug 2022 19:26:15 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fcc9ef3883004503af0c799761a6f973~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p>携手创作，共同成长！这是我参与「掘金日新计划 · 8 月更文挑战」的第17天，<a href="https://juejin.cn/post/7123120819437322247" title="https://juejin.cn/post/7123120819437322247" target="_blank">点击查看活动详情</a>。</p>
<p>承接上一章的内容，我们完成了一个<a href="https://juejin.cn/post/7130609032447918110" target="_blank" title="https://juejin.cn/post/7130609032447918110">基本设置</a>页面。</p>
<p>那本章中，我们继续来完成功能设置的详情页。</p>
<h2 data-id="heading-0">个人信息页</h2>
<p>个人信息页承载的功能是帮助用户修改和查看个人的基本信息，包含但不限于<strong>用户头像</strong>、<strong>用户昵称</strong>、<strong>用户ID</strong>、<strong>个人简介</strong>，针对于不同的业务场景，可以补充<strong>职位</strong>、<strong>公司</strong>等信息。</p>
<p>以下图个人信息详情页为例：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fcc9ef3883004503af0c799761a6f973~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们从设置的首页，<strong>点击</strong>个人信息栏，就可以<strong>跳转</strong>进入<strong>个人详细详情页</strong>。最基础的页面跳转方法，我们可以使用基于<code>NavigationView</code>的页面跳转方法。</p>
<p>但首先，我们需要先完成详情页的内容。示例：</p>
<pre><code class="hljs language-less copyable" lang="less"><span class="hljs-comment">// MARK: 个人资料详情页</span>

<span class="hljs-selector-tag">struct</span> <span class="hljs-selector-tag">PersonalDataView</span>: <span class="hljs-selector-tag">View</span> &#123;
    <span class="hljs-selector-tag">var</span> <span class="hljs-selector-tag">body</span>: <span class="hljs-selector-tag">some</span> <span class="hljs-selector-tag">View</span> &#123;
        <span class="hljs-selector-tag">ZStack</span> &#123;
            <span class="hljs-selector-tag">Color</span>(<span class="hljs-attribute">red</span>: <span class="hljs-number">246</span> / <span class="hljs-number">255</span>, <span class="hljs-attribute">green</span>: <span class="hljs-number">246</span> / <span class="hljs-number">255</span>, <span class="hljs-attribute">blue</span>: <span class="hljs-number">246</span> / <span class="hljs-number">255</span>)<span class="hljs-selector-class">.edgesIgnoringSafeArea</span>(.all)
            <span class="hljs-selector-tag">VStack</span>(<span class="hljs-attribute">spacing</span>: <span class="hljs-number">20</span>) &#123;
                <span class="hljs-selector-tag">Image</span>(<span class="hljs-string">"me"</span>)
                    <span class="hljs-selector-class">.resizable</span>()
                    <span class="hljs-selector-class">.aspectRatio</span>(<span class="hljs-attribute">contentMode</span>: .fit)
                    <span class="hljs-selector-class">.frame</span>(<span class="hljs-attribute">width</span>: <span class="hljs-number">100</span>)
                    <span class="hljs-selector-class">.clipShape</span>(Circle())
                    <span class="hljs-selector-class">.overlay</span>(Circle().stroke(<span class="hljs-attribute">Color</span>(.systemGray5), <span class="hljs-attribute">lineWidth</span>: <span class="hljs-number">1</span>))
                <span class="hljs-selector-tag">Text</span>(<span class="hljs-string">"修改头像"</span>)
                    <span class="hljs-selector-class">.font</span>(.system(<span class="hljs-attribute">size</span>: <span class="hljs-number">14</span>))
                    <span class="hljs-selector-class">.foregroundColor</span>(.gray)

                <span class="hljs-selector-tag">Form</span> &#123;
                    <span class="hljs-selector-tag">Section</span> &#123;
                        <span class="hljs-selector-tag">listItemView</span>(<span class="hljs-attribute">itemImage</span>: <span class="hljs-string">""</span>, <span class="hljs-attribute">itemName</span>: <span class="hljs-string">"用户名"</span>, <span class="hljs-attribute">itemContent</span>: <span class="hljs-string">"文如秋雨"</span>)
                        <span class="hljs-selector-tag">listItemView</span>(<span class="hljs-attribute">itemImage</span>: <span class="hljs-string">""</span>, <span class="hljs-attribute">itemName</span>: <span class="hljs-string">"掘金ID"</span>, <span class="hljs-attribute">itemContent</span>: <span class="hljs-string">"3897092103223517"</span>)
                        <span class="hljs-selector-tag">listItemView</span>(<span class="hljs-attribute">itemImage</span>: <span class="hljs-string">""</span>, <span class="hljs-attribute">itemName</span>: <span class="hljs-string">"职位"</span>, <span class="hljs-attribute">itemContent</span>: <span class="hljs-string">"高级产品经理"</span>)
                        <span class="hljs-selector-tag">listItemView</span>(<span class="hljs-attribute">itemImage</span>: <span class="hljs-string">""</span>, <span class="hljs-attribute">itemName</span>: <span class="hljs-string">"公司"</span>, <span class="hljs-attribute">itemContent</span>: <span class="hljs-string">"未知"</span>)
                        <span class="hljs-selector-tag">listItemView</span>(<span class="hljs-attribute">itemImage</span>: <span class="hljs-string">""</span>, <span class="hljs-attribute">itemName</span>: <span class="hljs-string">"简介"</span>, <span class="hljs-attribute">itemContent</span>: <span class="hljs-string">"什么也没留下"</span>)
                    &#125;
                &#125;
            &#125;<span class="hljs-selector-class">.padding</span>(.top, <span class="hljs-number">40</span>)
        &#125;<span class="hljs-selector-class">.navigationBarTitle</span>(<span class="hljs-string">"个人信息"</span>, <span class="hljs-attribute">displayMode</span>: .inline)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一般来说，如果我们需要设计一个新的页面，通常使用结构体创建一个新的视图。这里，我们创建了一个新的视图<code>PersonalDataView</code>来承载内容。</p>
<p>页面样式内容包括使用<code>ZStack</code>将页面包裹填充背景颜色，然后使用<code>Image</code>图片和<code>Text</code>构建修改头像样式，使用<code>Form</code>表单和<code>listItemView</code>栏目结构构建详情页的可修改栏目。这里由于后续我们也可以使用<code>NavigationView</code>跳转方法，因此先不加指示器。</p>
<p>最后我们回到<code>ContentView</code>视图中，完善跳转方法。示例：</p>
<pre><code class="hljs language-css copyable" lang="css">NavigationLink(destination: <span class="hljs-built_in">PersonalDataView</span>()) &#123;
    mineMessageView
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们预览下效果：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7b820d80c39f495fa251d56033e0c3eb~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="2.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">账号绑定页</h2>
<p>账号绑定页面承载着该<code>App</code>关联绑定的用户账号信息，包含注册的<strong>账号</strong>（一般为手机号、邮箱）、<strong>登录密码</strong>，以及<strong>第三方</strong>授权的社交账号、社区帐号等。</p>
<p>以下图账号绑定详情页为例：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/496ca2c90531462894c2febe7434fa49~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>以上图为例，我们发现账号绑定详情页的结构和<code>Form</code>表单的结构，这里我们可以采用和设置页面相同的页面布局结构，示例：</p>
<pre><code class="hljs language-less copyable" lang="less"><span class="hljs-comment">// MARK: 绑定账号详情页</span>
<span class="hljs-selector-tag">struct</span> <span class="hljs-selector-tag">AccountBindingView</span>: <span class="hljs-selector-tag">View</span> &#123;
    <span class="hljs-variable">@State</span> var isWechatBingding = true
    <span class="hljs-variable">@State</span> var isGitHubBingding = false
    <span class="hljs-variable">@State</span> var isWeiboBingding = false

    var <span class="hljs-attribute">body</span>: some View &#123;
        <span class="hljs-selector-tag">ZStack</span> &#123;
            <span class="hljs-selector-tag">Color</span>(<span class="hljs-attribute">red</span>: <span class="hljs-number">246</span> / <span class="hljs-number">255</span>, <span class="hljs-attribute">green</span>: <span class="hljs-number">246</span> / <span class="hljs-number">255</span>, <span class="hljs-attribute">blue</span>: <span class="hljs-number">246</span> / <span class="hljs-number">255</span>)<span class="hljs-selector-class">.edgesIgnoringSafeArea</span>(.all)
            <span class="hljs-selector-tag">Form</span> &#123;
                <span class="hljs-selector-tag">Section</span> &#123;
                    <span class="hljs-selector-tag">listItemView</span>(<span class="hljs-attribute">itemImage</span>: <span class="hljs-string">""</span>, <span class="hljs-attribute">itemName</span>: <span class="hljs-string">"手机号"</span>, <span class="hljs-attribute">itemContent</span>: <span class="hljs-string">"1666666666"</span>)
                    <span class="hljs-selector-tag">listItemView</span>(<span class="hljs-attribute">itemImage</span>: <span class="hljs-string">""</span>, <span class="hljs-attribute">itemName</span>: <span class="hljs-string">"修改密码"</span>, <span class="hljs-attribute">itemContent</span>: <span class="hljs-string">""</span>)
                &#125;
                <span class="hljs-selector-tag">Section</span>(<span class="hljs-attribute">header</span>: Text(<span class="hljs-string">"第三方账号"</span>)) &#123;
                    <span class="hljs-selector-tag">Toggle</span>(<span class="hljs-attribute">isOn</span>: $isWechatBingding) &#123;
                        <span class="hljs-selector-tag">Text</span>(<span class="hljs-string">"微信"</span>)
                    &#125;
                    <span class="hljs-selector-tag">Toggle</span>(<span class="hljs-attribute">isOn</span>: $isGitHubBingding) &#123;
                        <span class="hljs-selector-tag">Text</span>(<span class="hljs-string">"GitHub"</span>)
                    &#125;
                    <span class="hljs-selector-tag">Toggle</span>(<span class="hljs-attribute">isOn</span>: $isWeiboBingding) &#123;
                        <span class="hljs-selector-tag">Text</span>(<span class="hljs-string">"新浪微博"</span>)
                    &#125;
                &#125;<span class="hljs-selector-class">.padding</span>(.vertical, <span class="hljs-number">5</span>)
                <span class="hljs-selector-tag">Section</span> &#123;
                    <span class="hljs-selector-tag">cancelAccount</span>
                &#125;
            &#125;<span class="hljs-selector-class">.navigationBarTitle</span>(<span class="hljs-string">"账号绑定"</span>, <span class="hljs-attribute">displayMode</span>: .inline)
        &#125;
    &#125;

    <span class="hljs-comment">// 注销账号</span>
    <span class="hljs-selector-tag">private</span> <span class="hljs-selector-tag">var</span> <span class="hljs-selector-tag">cancelAccount</span>: <span class="hljs-selector-tag">some</span> <span class="hljs-selector-tag">View</span> &#123;
        <span class="hljs-selector-tag">Button</span>(<span class="hljs-attribute">action</span>: &#123;
        &#125;) &#123;
            <span class="hljs-selector-tag">Text</span>(<span class="hljs-string">"注销账号"</span>)
                <span class="hljs-selector-class">.font</span>(.system(<span class="hljs-attribute">size</span>: <span class="hljs-number">17</span>))
                <span class="hljs-selector-class">.frame</span>(<span class="hljs-attribute">minWidth</span>: <span class="hljs-number">0</span>, <span class="hljs-attribute">maxWidth</span>: .infinity, <span class="hljs-attribute">minHeight</span>: <span class="hljs-number">30</span>, <span class="hljs-attribute">maxHeight</span>: <span class="hljs-number">30</span>)
                <span class="hljs-selector-class">.foregroundColor</span>(.red)
                <span class="hljs-selector-class">.cornerRadius</span>(<span class="hljs-number">8</span>)
                <span class="hljs-selector-class">.padding</span>(.vertical, <span class="hljs-number">5</span>)
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述代码中，我们依旧使用<code>ZStack</code>层叠覆盖一个背景颜色，然后使用<code>Form</code>表单和<code>Section</code>段落构建样式。</p>
<p>第三方账号绑定由于我们使用<code>Toggle</code>开关的方式，我们需要提前声明3个变量<code>isWechatBingding</code>绑定微信、<code>isGitHubBingding</code>绑定<code>GitHub</code>、<code>isWeiboBingding</code>绑定微博。</p>
<p>最后我们和退出登录按钮一样构建了<code>cancelAccount</code>注销账号按钮。</p>
<p>我们回到<code>ContentView</code>视图中，完善跳转方法。示例：</p>
<pre><code class="hljs language-less copyable" lang="less"><span class="hljs-selector-tag">NavigationLink</span>(<span class="hljs-attribute">destination</span>: PersonalDataView()) &#123;
    <span class="hljs-selector-tag">listItemView</span>(<span class="hljs-attribute">itemImage</span>: <span class="hljs-string">"lock"</span>, <span class="hljs-attribute">itemName</span>: <span class="hljs-string">"账号绑定"</span>, <span class="hljs-attribute">itemContent</span>: <span class="hljs-string">"已绑定"</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们预览下效果：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0fb35a7bf54d40dcb88b84b412162de2~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="4.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">通用设置面</h2>
<p>原有的掘金App存在一些难以理解的操作功能，示例：<strong>基础版掘金</strong>、<strong>个性化推荐设置</strong>、<strong>推送通知设置</strong>。用户对于这些设置功能<strong>学习成本较高</strong>，以及存在由于<strong>功能分散</strong>而导致找不到设置操作等问题。</p>
<blockquote>
<p>这，不够优雅。</p>
</blockquote>
<p>这里提供的产品方案是将功能设置操作统归为一个通用设置页面。示例：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a493c5474334c7bb58f1f5e2946f43b~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="5.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>页面内容也比较简单，我们可以使用<code>Form</code>表单、<code>Section</code>段落、<code>Toggle</code>开关来构建样式。示例：</p>
<pre><code class="hljs language-less copyable" lang="less"><span class="hljs-comment">// MARK: 通用设置详情页</span>
<span class="hljs-selector-tag">struct</span> <span class="hljs-selector-tag">GeneralSettingView</span>: <span class="hljs-selector-tag">View</span> &#123;
    <span class="hljs-variable">@State</span> var isFullSelected = true
    <span class="hljs-variable">@State</span> var isIndividuationSelected = true
    <span class="hljs-variable">@State</span> var isChoicenessSelected = true
    <span class="hljs-variable">@State</span> var isInformationSelected = true

    var <span class="hljs-attribute">body</span>: some View &#123;
        <span class="hljs-selector-tag">ZStack</span> &#123;
            <span class="hljs-selector-tag">Color</span>(<span class="hljs-attribute">red</span>: <span class="hljs-number">246</span> / <span class="hljs-number">255</span>, <span class="hljs-attribute">green</span>: <span class="hljs-number">246</span> / <span class="hljs-number">255</span>, <span class="hljs-attribute">blue</span>: <span class="hljs-number">246</span> / <span class="hljs-number">255</span>)<span class="hljs-selector-class">.edgesIgnoringSafeArea</span>(.all)
            <span class="hljs-selector-tag">Form</span> &#123;
                <span class="hljs-selector-tag">Section</span> &#123;
                    <span class="hljs-selector-tag">Toggle</span>(<span class="hljs-attribute">isOn</span>: $isFullSelected) &#123;
                        <span class="hljs-selector-tag">VStack</span>(<span class="hljs-attribute">alignment</span>: .leading, <span class="hljs-attribute">spacing</span>: <span class="hljs-number">5</span>) &#123;
                            <span class="hljs-selector-tag">Text</span>(<span class="hljs-string">"完整版功能"</span>)
                                <span class="hljs-selector-class">.font</span>(.system(<span class="hljs-attribute">size</span>: <span class="hljs-number">17</span>))
                                <span class="hljs-selector-class">.foregroundColor</span>(.black)
                            <span class="hljs-selector-tag">Text</span>(<span class="hljs-string">"开启后可享有完整功能，建议开启"</span>)
                                <span class="hljs-selector-class">.font</span>(.system(<span class="hljs-attribute">size</span>: <span class="hljs-number">14</span>))
                                <span class="hljs-selector-class">.foregroundColor</span>(.gray)
                        &#125;
                    &#125;
                    <span class="hljs-selector-tag">Toggle</span>(<span class="hljs-attribute">isOn</span>: $isIndividuationSelected) &#123;
                        <span class="hljs-selector-tag">VStack</span>(<span class="hljs-attribute">alignment</span>: .leading, <span class="hljs-attribute">spacing</span>: <span class="hljs-number">5</span>) &#123;
                            <span class="hljs-selector-tag">Text</span>(<span class="hljs-string">"个性化推荐"</span>)
                                <span class="hljs-selector-class">.font</span>(.system(<span class="hljs-attribute">size</span>: <span class="hljs-number">17</span>))
                                <span class="hljs-selector-class">.foregroundColor</span>(.black)
                            <span class="hljs-selector-tag">Text</span>(<span class="hljs-string">"开启后将根据您的喜好进行内容推荐"</span>)
                                <span class="hljs-selector-class">.font</span>(.system(<span class="hljs-attribute">size</span>: <span class="hljs-number">14</span>))
                                <span class="hljs-selector-class">.foregroundColor</span>(.gray)
                        &#125;
                    &#125;
                    <span class="hljs-selector-tag">Toggle</span>(<span class="hljs-attribute">isOn</span>: $isChoicenessSelected) &#123;
                        <span class="hljs-selector-tag">VStack</span>(<span class="hljs-attribute">alignment</span>: .leading, <span class="hljs-attribute">spacing</span>: <span class="hljs-number">5</span>) &#123;
                            <span class="hljs-selector-tag">Text</span>(<span class="hljs-string">"精选内容推送"</span>)
                                <span class="hljs-selector-class">.font</span>(.system(<span class="hljs-attribute">size</span>: <span class="hljs-number">17</span>))
                                <span class="hljs-selector-class">.foregroundColor</span>(.black)
                            <span class="hljs-selector-tag">Text</span>(<span class="hljs-string">"开启后将享有精选内容推荐"</span>)
                                <span class="hljs-selector-class">.font</span>(.system(<span class="hljs-attribute">size</span>: <span class="hljs-number">14</span>))
                                <span class="hljs-selector-class">.foregroundColor</span>(.gray)
                        &#125;
                    &#125;
                    <span class="hljs-selector-tag">Toggle</span>(<span class="hljs-attribute">isOn</span>: $isInformationSelected) &#123;
                        <span class="hljs-selector-tag">VStack</span>(<span class="hljs-attribute">alignment</span>: .leading, <span class="hljs-attribute">spacing</span>: <span class="hljs-number">5</span>) &#123;
                            <span class="hljs-selector-tag">Text</span>(<span class="hljs-string">"消息推送"</span>)
                                <span class="hljs-selector-class">.font</span>(.system(<span class="hljs-attribute">size</span>: <span class="hljs-number">17</span>))
                                <span class="hljs-selector-class">.foregroundColor</span>(.black)
                            <span class="hljs-selector-tag">Text</span>(<span class="hljs-string">"关闭后将无法收到及时通知，建议开启"</span>)
                                <span class="hljs-selector-class">.font</span>(.system(<span class="hljs-attribute">size</span>: <span class="hljs-number">14</span>))
                                <span class="hljs-selector-class">.foregroundColor</span>(.gray)
                        &#125;
                    &#125;
                &#125;<span class="hljs-selector-class">.padding</span>(.vertical, <span class="hljs-number">5</span>)
            &#125;<span class="hljs-selector-class">.navigationBarTitle</span>(<span class="hljs-string">"通用设置"</span>, <span class="hljs-attribute">displayMode</span>: .inline)
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后我们回到<code>ContentView</code>视图中，完善跳转方法。示例：</p>
<pre><code class="hljs language-less copyable" lang="less"><span class="hljs-selector-tag">NavigationLink</span>(<span class="hljs-attribute">destination</span>: PersonalDataView()) &#123;
    <span class="hljs-selector-tag">listItemView</span>(<span class="hljs-attribute">itemImage</span>: <span class="hljs-string">"gear.circle"</span>, <span class="hljs-attribute">itemName</span>: <span class="hljs-string">"通用设置"</span>, <span class="hljs-attribute">itemContent</span>: <span class="hljs-string">""</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们预览下效果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8a07714fadff48a2b5fbbca6c0e28bd0~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="6.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>恭喜你，完成了本章的全部内容！</p>
<p>快来动手试试吧。</p>
<p><strong>如果本专栏对你有帮助，不妨点赞、评论、关注～</strong></p></div>  
</div>
            
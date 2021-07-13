
---
title: 'html2canvas在vue2中的应用-移动端'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d052968a09b4fb9a3c605e70d353de0~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 11 Jul 2021 19:06:17 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d052968a09b4fb9a3c605e70d353de0~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>将DOM页面中的一部分（动态生成的二维码、动态生成海报）转化为图片，甚至点击下载按钮，将这部分保存为图片下载到手机里或者电脑上，是一个非常常见的需求，而使用canvas转也是非常麻烦，于是找到html2canvas。</p>
</blockquote>
<p>前提：npm下载html2canvas0.5.0-beta02版本的依赖包</p>
<p>html2canvas 中npm 包官方文档：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fhtml2canvas" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/html2canvas" ref="nofollow noopener noreferrer">www.npmjs.com/package/htm…</a></p>
<h1 data-id="heading-0">在项目中的使用</h1>
<h2 data-id="heading-1">一、安装html2canvas</h2>
<pre><code class="hljs language-js copyable" lang="js">npm install --save html2canvas
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">二、在项目中使用</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> html2canvas <span class="hljs-keyword">from</span> <span class="hljs-string">'html2canvas'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">页面(saveImg组件)具体如下：</h3>
<p><strong>vue文件</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"canvasBox"</span> <span class="hljs-attr">v-show</span>=<span class="hljs-string">"isShareCards"</span> @<span class="hljs-attr">touchmove.prevent</span>></span>
    <span class="hljs-comment"><!-- 需裁剪的位置 --></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"canvasMain"</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"canvasMain"</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"!img"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"canvasContent"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"top"</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"avatar"</span>></span>
                    <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">:src</span>=<span class="hljs-string">"data.avatar_img ? data.avatar_img : default_img"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">"avatar"</span> /></span>
                <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"name"</span>></span>&#123;&#123;data.contact_name&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"content"</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">h3</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"title"</span>></span>&#123;&#123;lang.title&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h3</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"base_info"</span>></span>
                    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"tel"</span>></span>
                        <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../../assets/img/sharePromotion/popup/samll_phone.png"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">"phone_icon"</span> /></span>
                        <span class="hljs-tag"><<span class="hljs-name">span</span>></span>&#123;&#123;data.contact_number&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
                    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
                    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"company"</span>></span>
                        <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../../assets/img/sharePromotion/popup/samll_company.png"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">"company_icon"</span> /></span>
                        <span class="hljs-tag"><<span class="hljs-name">span</span>></span>&#123;&#123;data.license_name&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
                    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"address"</span>></span>
                    <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../../assets/img/sharePromotion/popup/samll_address.png"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">"address_icon"</span> /></span>
                    <span class="hljs-tag"><<span class="hljs-name">span</span>></span>&#123;&#123;data.contact_address&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
                <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"business_scope"</span>></span>
                    <span class="hljs-tag"><<span class="hljs-name">h3</span>></span>&#123;&#123;lang.businessScopeTitle&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h3</span>></span>
                    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"business_content"</span>></span>
                        <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"item,index in data.business_scope"</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">"index"</span>></span>&#123;&#123;item&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
                    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"more_tips"</span>></span>&#123;&#123;lang.moreTips&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"kong"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-comment"><!-- 存放裁剪base64图片的位置 --></span>
    <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"img"</span> <span class="hljs-attr">:class</span>=<span class="hljs-string">"['canvasimg', (isApp || isWeixin) ? '' : 'canvasimg-web' ]"</span> <span class="hljs-attr">:src</span>=<span class="hljs-string">"img"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">""</span>></span>
    <span class="hljs-comment"><!-- 保存图片的按钮 --></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"footer"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"top"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../../assets/img/sharePromotion/popup/press_icon.png"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">"press_img"</span> /></span>
            <span class="hljs-tag"><<span class="hljs-name">span</span>></span>&#123;&#123;lang.pressTips&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"f-kong"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"bottom"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"cancel_btn"</span> <span class="hljs-attr">:isShareShow</span>=<span class="hljs-string">"isShareCards"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"cancelHandle"</span>></span>&#123;&#123;lang.cancel&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>less文件</strong></p>
<pre><code class="hljs language-less copyable" lang="less"><span class="hljs-keyword">@import</span> <span class="hljs-string">'../../assets/less/mixin.less'</span>;

<span class="hljs-selector-class">.canvasBox</span> &#123;
    <span class="hljs-attribute">position</span>: fixed;
    <span class="hljs-attribute">top</span>: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">background</span>: rgba(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>, .<span class="hljs-number">8</span>);
    <span class="hljs-comment">/* 需裁剪的位置 */</span>
    <span class="hljs-selector-class">.canvasMain</span> &#123;
        <span class="hljs-attribute">position</span>: absolute;
        <span class="hljs-attribute">top</span>: <span class="hljs-number">0</span>;
        <span class="hljs-attribute">right</span>: <span class="hljs-number">0</span>;
        <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
        <span class="hljs-attribute">bottom</span>: <span class="hljs-number">2.56rem</span>;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">5.5rem</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">7.7rem</span>;
        <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">0.12rem</span>;
        <span class="hljs-attribute">margin</span>: auto;
        <span class="hljs-attribute">overflow</span>: hidden;
        <span class="hljs-selector-class">.canvasContent</span> &#123;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
            <span class="hljs-attribute">margin</span>: auto;
            <span class="hljs-attribute">overflow</span>: hidden;
            <span class="hljs-comment">// background-color: #fff;</span>
            <span class="hljs-comment">// background-repeat: no-repeat;</span>
            <span class="hljs-comment">// background-size: 100% 100%;</span>
            <span class="hljs-comment">// background-position: center center;</span>
            <span class="hljs-attribute">background</span>: <span class="hljs-number">#fff</span> no-repeat center center / <span class="hljs-number">100%</span> <span class="hljs-number">100%</span>;
            <span class="hljs-attribute">position</span>: absolute;
            <span class="hljs-attribute">z-index</span>: <span class="hljs-number">90</span>;
            <span class="hljs-attribute">font-size</span>: <span class="hljs-number">24px</span>;
            <span class="hljs-attribute">color</span>: <span class="hljs-number">#333</span>;
            <span class="hljs-selector-class">.top</span> &#123;
                <span class="hljs-attribute">display</span>: flex;
                <span class="hljs-attribute">justify-content</span>: center;
                <span class="hljs-attribute">align-items</span>: center;
                <span class="hljs-attribute">flex-direction</span>: column;
                <span class="hljs-attribute">padding-top</span>: <span class="hljs-number">28px</span>;
                <span class="hljs-selector-class">.avatar</span> &#123;
                    <span class="hljs-attribute">width</span>: <span class="hljs-number">98px</span>;
                    <span class="hljs-attribute">height</span>: <span class="hljs-number">98px</span>;
                    <span class="hljs-selector-tag">img</span> &#123;
                        <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
                        <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
                        <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">50%</span>;
                    &#125;
                &#125;
                <span class="hljs-selector-class">.name</span> &#123;
                    <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
                    <span class="hljs-attribute">font-size</span>: <span class="hljs-number">26px</span>;
                    <span class="hljs-attribute">font-weight</span>: bold;
                    <span class="hljs-attribute">padding-top</span>: <span class="hljs-number">20px</span>;
                    <span class="hljs-selector-class">.textOverflow</span>();
                &#125;
            &#125;
            <span class="hljs-selector-class">.content</span> &#123;
                <span class="hljs-selector-class">.title</span> &#123;
                    <span class="hljs-attribute">color</span>: <span class="hljs-number">#666</span>;
                    <span class="hljs-attribute">padding-top</span>: <span class="hljs-number">20px</span>;
                    <span class="hljs-attribute">font-size</span>: <span class="hljs-number">26px</span>;
                    <span class="hljs-attribute">font-weight</span>: normal;
                &#125;
                <span class="hljs-selector-class">.base_info</span> &#123;
                    <span class="hljs-attribute">display</span>: flex;
                    <span class="hljs-attribute">justify-content</span>: space-between;
                    <span class="hljs-attribute">padding</span>: <span class="hljs-number">38px</span> <span class="hljs-number">30px</span> <span class="hljs-number">40px</span> <span class="hljs-number">30px</span>;
                    <span class="hljs-attribute">border-bottom</span>: <span class="hljs-number">1px</span> solid <span class="hljs-number">#efefef</span>;
                    <span class="hljs-selector-tag">div</span> &#123;
                        <span class="hljs-attribute">text-align</span>: left;
                        <span class="hljs-attribute">width</span>: <span class="hljs-number">50%</span>;
                        <span class="hljs-attribute">display</span>: flex;
                        <span class="hljs-attribute">justify-content</span>: flex-start;
                        <span class="hljs-selector-tag">img</span> &#123;
                            <span class="hljs-attribute">width</span>: <span class="hljs-number">26px</span>;
                            <span class="hljs-attribute">height</span>: <span class="hljs-number">26px</span>;
                        &#125;
                        <span class="hljs-selector-tag">span</span> &#123;
                            <span class="hljs-attribute">padding-left</span>: <span class="hljs-number">12px</span>;
                            <span class="hljs-attribute">flex</span>: <span class="hljs-number">1</span>;
                            <span class="hljs-attribute">line-height</span>: <span class="hljs-number">28px</span>;
                            <span class="hljs-attribute">overflow</span>: hidden;
                            <span class="hljs-attribute">text-overflow</span>: ellipsis;
                            <span class="hljs-attribute">white-space</span>: nowrap;
                        &#125;
                    &#125;
                &#125;
                <span class="hljs-selector-class">.address</span> &#123;
                    <span class="hljs-attribute">display</span>: flex;
                    <span class="hljs-attribute">height</span>: <span class="hljs-number">98px</span>;
                    <span class="hljs-attribute">justify-content</span>: flex-start;
                    <span class="hljs-attribute">padding</span>: <span class="hljs-number">20px</span> <span class="hljs-number">30px</span> <span class="hljs-number">25px</span> <span class="hljs-number">30px</span>;
                    <span class="hljs-attribute">border-bottom</span>: <span class="hljs-number">1px</span> solid <span class="hljs-number">#efefef</span>;
                    <span class="hljs-attribute">box-sizing</span>: border-box;
                    <span class="hljs-selector-tag">img</span> &#123;
                        <span class="hljs-attribute">width</span>: <span class="hljs-number">26px</span>;
                        <span class="hljs-attribute">height</span>: <span class="hljs-number">26px</span>;
                    &#125;
                    <span class="hljs-selector-tag">span</span> &#123;
                        <span class="hljs-attribute">text-align</span>: left;
                        <span class="hljs-attribute">line-height</span>: <span class="hljs-number">28px</span>;
                        <span class="hljs-attribute">padding-left</span>: <span class="hljs-number">12px</span>;
                        <span class="hljs-attribute">overflow</span>: hidden;
                        <span class="hljs-attribute">text-overflow</span>: ellipsis;
                    &#125;
                &#125;
                <span class="hljs-selector-class">.business_scope</span> &#123;
                    <span class="hljs-attribute">height</span>: <span class="hljs-number">276px</span>;
                    <span class="hljs-attribute">padding</span>: <span class="hljs-number">20px</span> <span class="hljs-number">30px</span> <span class="hljs-number">18px</span> <span class="hljs-number">30px</span>;
                    <span class="hljs-attribute">border-bottom</span>: <span class="hljs-number">1px</span> solid <span class="hljs-number">#efefef</span>;
                    <span class="hljs-attribute">box-sizing</span>: border-box;
                    <span class="hljs-attribute">overflow</span>: hidden;
                    <span class="hljs-attribute">display</span>: flex;
                    <span class="hljs-attribute">justify-content</span>: flex-start;
                    <span class="hljs-attribute">flex-direction</span>: column;
                    <span class="hljs-selector-tag">h3</span> &#123;
                        <span class="hljs-attribute">color</span>: <span class="hljs-number">#666</span>;
                        <span class="hljs-attribute">font-size</span>: <span class="hljs-number">24px</span>;
                        <span class="hljs-attribute">font-weight</span>: normal;
                        <span class="hljs-attribute">height</span>: <span class="hljs-number">26px</span>;
                        <span class="hljs-attribute">padding-bottom</span>: <span class="hljs-number">16px</span>;
                    &#125;
                    <span class="hljs-selector-class">.business_content</span> &#123;
                        <span class="hljs-attribute">flex</span>: <span class="hljs-number">1</span>;
                        <span class="hljs-selector-tag">p</span> &#123;
                            <span class="hljs-attribute">line-height</span>: <span class="hljs-number">28px</span>;
                            <span class="hljs-attribute">text-align</span>: left;
                            <span class="hljs-attribute">overflow</span>: hidden;
                            <span class="hljs-attribute">padding-top</span>: <span class="hljs-number">2px</span>;
                        &#125;
                        <span class="hljs-attribute">overflow</span>: hidden;
                    &#125;
                &#125;
                <span class="hljs-selector-class">.more_tips</span> &#123;
                    <span class="hljs-attribute">text-align</span>: left;
                    <span class="hljs-attribute">padding</span>: <span class="hljs-number">20px</span> <span class="hljs-number">30px</span> <span class="hljs-number">0px</span> <span class="hljs-number">30px</span>;
                &#125;
            &#125;
        &#125;
        <span class="hljs-selector-class">.kong</span> &#123;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
            <span class="hljs-attribute">z-index</span>: <span class="hljs-number">9999</span>;
            <span class="hljs-attribute">position</span>: absolute;
            <span class="hljs-attribute">top</span>: <span class="hljs-number">0</span>;
            <span class="hljs-attribute">right</span>: <span class="hljs-number">0</span>;
            <span class="hljs-attribute">bottom</span>: <span class="hljs-number">0</span>;
            <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
        &#125;
    &#125;
    <span class="hljs-comment">/* 存放裁剪base64图片的位置 */</span>
    <span class="hljs-selector-class">.canvasimg</span>  &#123;
        <span class="hljs-attribute">z-index</span>: <span class="hljs-number">9999999</span>;
        <span class="hljs-attribute">position</span>: absolute;
        <span class="hljs-attribute">top</span>: <span class="hljs-number">0</span>;
        <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
        <span class="hljs-attribute">right</span>: <span class="hljs-number">0</span>;
        <span class="hljs-attribute">bottom</span>: <span class="hljs-number">276px</span>;
        <span class="hljs-comment">// position: fixed;</span>
        <span class="hljs-comment">// left: 100px;</span>
        <span class="hljs-comment">// bottom: 356px;</span>
        <span class="hljs-attribute">width</span>: <span class="hljs-number">550px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">776px</span>;
        <span class="hljs-attribute">margin</span>: auto;
        <span class="hljs-attribute">pointer-events</span>:auto;
        -webkit-touch-callout: default;
    &#125;
    <span class="hljs-selector-class">.canvasimg-web</span> &#123;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">500px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">726px</span>;
    &#125;
    <span class="hljs-comment">/* 保存图片的按钮 */</span>
    <span class="hljs-selector-class">.footer</span> &#123;
        <span class="hljs-attribute">position</span>: fixed;
        <span class="hljs-attribute">bottom</span>: <span class="hljs-number">0</span>;
        <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">256px</span>;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#efefef</span>;
        <span class="hljs-attribute">color</span>: <span class="hljs-number">#666</span>;
        <span class="hljs-attribute">font-size</span>: <span class="hljs-number">24px</span>;
        <span class="hljs-selector-class">.top</span> &#123;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">158px</span>;
            <span class="hljs-attribute">position</span>: relative;
            <span class="hljs-attribute">display</span>: flex;
            <span class="hljs-attribute">justify-content</span>: center;
            <span class="hljs-attribute">align-items</span>: center;
            <span class="hljs-selector-tag">img</span> &#123;
                <span class="hljs-attribute">width</span>: <span class="hljs-number">34px</span>;
                <span class="hljs-attribute">padding-right</span>: <span class="hljs-number">10px</span>;
            &#125;
            <span class="hljs-selector-class">.f-kong</span> &#123;
                <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
                <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
                <span class="hljs-attribute">position</span>: absolute;
                <span class="hljs-attribute">top</span>: <span class="hljs-number">0</span>;
                <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
                <span class="hljs-attribute">z-index</span>: <span class="hljs-number">999</span>;
            &#125;
        &#125;
        <span class="hljs-selector-class">.bottom</span> &#123;
            <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#fff</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">98px</span>;
            <span class="hljs-attribute">line-height</span>: <span class="hljs-number">98px</span>;
            <span class="hljs-selector-class">.cancel_btn</span> &#123;
                <span class="hljs-attribute">color</span>: <span class="hljs-number">#333</span>;
                <span class="hljs-attribute">font-size</span>: <span class="hljs-number">30px</span>;
            &#125;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>js文件</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/* eslint-disable */</span>
<span class="hljs-keyword">import</span> lang <span class="hljs-keyword">from</span> <span class="hljs-string">'../../i18n/sharePromotion'</span>;
<span class="hljs-keyword">import</span> toast <span class="hljs-keyword">from</span> <span class="hljs-string">'../toast'</span>;
<span class="hljs-keyword">import</span> loading <span class="hljs-keyword">from</span> <span class="hljs-string">'../../components/loading/index'</span>;
<span class="hljs-keyword">import</span> html2canvas <span class="hljs-keyword">from</span> <span class="hljs-string">'html2canvas'</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'saveImg'</span>,
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">lang</span>: lang,
            <span class="hljs-attr">img</span>: <span class="hljs-string">''</span>,
            <span class="hljs-attr">imgurl</span>: <span class="hljs-string">''</span>,
            <span class="hljs-attr">firstFlag</span>: <span class="hljs-literal">true</span>,
            <span class="hljs-attr">default_img</span>: <span class="hljs-built_in">require</span>(<span class="hljs-string">'../../assets/img/sharePromotion/default_avatar.png'</span>),
            <span class="hljs-attr">canvas</span>: <span class="hljs-literal">null</span>,
            <span class="hljs-attr">imgName</span>: <span class="hljs-string">'poster'</span>
        &#125;;
    &#125;,
    <span class="hljs-attr">props</span>: [<span class="hljs-string">'isShareCards'</span>, <span class="hljs-string">'data'</span>, <span class="hljs-string">'isApp'</span>, <span class="hljs-string">'isWeixin'</span>],
    <span class="hljs-attr">watch</span>: &#123;
        <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params">newData</span>)</span> &#123;
            <span class="hljs-built_in">this</span>.data = newData;
        &#125;,
        <span class="hljs-function"><span class="hljs-title">dataURL</span>(<span class="hljs-params">newImg</span>)</span> &#123;
            <span class="hljs-built_in">this</span>.img = newImg;
        &#125;
    &#125;,
    created () &#123;
        <span class="hljs-built_in">this</span>.firstFlag = <span class="hljs-literal">true</span>
    &#125;,
    <span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params"></span>)</span> &#123;
    &#125;,
    <span class="hljs-attr">methods</span>: &#123;
        <span class="hljs-comment">// 取消</span>
        <span class="hljs-function"><span class="hljs-title">cancelHandle</span>(<span class="hljs-params"></span>)</span> &#123;
            <span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">'update:isShareCards'</span>, <span class="hljs-literal">false</span>);
            <span class="hljs-built_in">this</span>.img = <span class="hljs-string">''</span>;
        &#125;,
        <span class="hljs-comment">/* canvas裁剪 */</span>
        <span class="hljs-function"><span class="hljs-title">getCanvas</span>(<span class="hljs-params">imgUrl</span>)</span> &#123;
            loading.show();
            <span class="hljs-keyword">const</span> that = <span class="hljs-built_in">this</span>;
            <span class="hljs-keyword">const</span> canEle = <span class="hljs-built_in">this</span>.$refs.canvasMain;   <span class="hljs-comment">// 获取存放截图的包裹的上一级dom对象（原生）</span>
            <span class="hljs-keyword">const</span> width = canEle.offsetWidth; <span class="hljs-comment">// 获取dom宽</span>
            <span class="hljs-keyword">const</span> height = canEle.offsetHeight;   <span class="hljs-comment">// 获取dom高</span>
            <span class="hljs-keyword">const</span> canvas = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'canvas'</span>);  <span class="hljs-comment">// 创建一个canvas节点</span>
            <span class="hljs-keyword">const</span> scale = <span class="hljs-number">2</span>; <span class="hljs-comment">// 定义任意放大倍数 支持小数</span>
            <span class="hljs-keyword">const</span> context = canvas.getContext(<span class="hljs-string">'2d'</span>);
            canvas.width = width * scale; <span class="hljs-comment">// 定义canvas 宽度 * 缩放</span>
            canvas.height = height * scale; <span class="hljs-comment">// 定义canvas高度 *缩放</span>
            context.scale(scale, scale);
            <span class="hljs-keyword">const</span> rect = canEle.getBoundingClientRect(); <span class="hljs-comment">//获取元素相对于视察的偏移量</span>
            context.translate(-rect.left, -rect.top); <span class="hljs-comment">//设置context位置，值为相对于视窗的偏移量负值，让图片复位</span>
            <span class="hljs-keyword">const</span> options = &#123;
                <span class="hljs-attr">useCORS</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 【重要】开启跨域配置</span>
                <span class="hljs-attr">tainttest</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 检测每张图片都已经加载完成</span>
                <span class="hljs-attr">scale</span>: scale, <span class="hljs-comment">// 添加的scale 参数</span>
                <span class="hljs-attr">backgroundColor</span>: <span class="hljs-literal">null</span>, <span class="hljs-comment">// 避免下载不全</span>
                canvas, <span class="hljs-comment">// 自定义 canvas</span>
                <span class="hljs-attr">width</span>: width, <span class="hljs-comment">// dom 原始宽度</span>
                <span class="hljs-attr">height</span>: height,
            &#125;;
            <span class="hljs-keyword">const</span> imgs = <span class="hljs-keyword">new</span> Image();
            imgs.onload = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
                html2canvas(canEle, options).then(<span class="hljs-function"><span class="hljs-params">canvas</span> =></span> &#123;
                    that.canvas = canvas;
                    canvas.style.width = width+<span class="hljs-string">"px"</span>;
                    canvas.style.height = height+<span class="hljs-string">"px"</span>;
                    <span class="hljs-keyword">let</span> dataURL = canvas.toDataURL(<span class="hljs-string">"image/png"</span>);
                    that.img = dataURL;
                    that.firstFlag = <span class="hljs-literal">false</span>
                    <span class="hljs-keyword">const</span> context = canvas.getContext(<span class="hljs-string">'2d'</span>);
                    <span class="hljs-comment">// 关闭抗锯齿 保证生成的分享图是清晰的</span>
                    context.mozImageSmoothingEnabled = <span class="hljs-literal">false</span>;
                    context.webkitImageSmoothingEnabled = <span class="hljs-literal">false</span>;
                    context.msImageSmoothingEnabled = <span class="hljs-literal">false</span>;
                    context.imageSmoothingEnabled = <span class="hljs-literal">false</span>;
                    loading.hide();
                &#125;);
            &#125;;
            imgs.onerror = <span class="hljs-function">() =></span> &#123;
                <span class="hljs-comment">// 安卓机canvas.toDataUrl的时候导出的base64图片没有base64前缀 走了 imgs.onerror</span>
                html2canvas(canEle, options).then(<span class="hljs-function"><span class="hljs-params">canvas</span> =></span> &#123;
                    canvas.style.width = width+<span class="hljs-string">"px"</span>;
                    canvas.style.height = height+<span class="hljs-string">"px"</span>;
                    <span class="hljs-keyword">let</span> dataURL = canvas.toDataURL(<span class="hljs-string">"image/png"</span>);
                    that.img = dataURL;
                    that.firstFlag = <span class="hljs-literal">false</span>
                    <span class="hljs-keyword">const</span> context = canvas.getContext(<span class="hljs-string">'2d'</span>);
                    <span class="hljs-comment">// 关闭抗锯齿 保证生成的分享图是清晰的</span>
                    context.mozImageSmoothingEnabled = <span class="hljs-literal">false</span>;
                    context.webkitImageSmoothingEnabled = <span class="hljs-literal">false</span>;
                    context.msImageSmoothingEnabled = <span class="hljs-literal">false</span>;
                    context.imageSmoothingEnabled = <span class="hljs-literal">false</span>;
                    loading.hide();
                &#125;);
            &#125;
            imgs.src = imgUrl;
        &#125;,
        <span class="hljs-comment">// 获取设备像素密度的方法</span>
        <span class="hljs-function"><span class="hljs-title">getPixelRatio</span>(<span class="hljs-params">context</span>)</span>&#123;
            <span class="hljs-keyword">var</span> backingStore = context.backingStorePixelRatio ||
                context.webkitBackingStorePixelRatio ||
                context.mozBackingStorePixelRatio ||
                context.msBackingStorePixelRatio ||
                context.oBackingStorePixelRatio ||
                context.backingStorePixelRatio || <span class="hljs-number">1</span>;
            <span class="hljs-keyword">return</span> (<span class="hljs-built_in">window</span>.devicePixelRatio || <span class="hljs-number">1</span>) / backingStore;
        &#125;,
    &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">组件在具体页面上的使用：</h3>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-comment">// vue</span>
 <saveImg ref=<span class="hljs-string">"child"</span> :isApp.sync=<span class="hljs-string">"isApp"</span> :isWeixin.sync=<span class="hljs-string">'isWeixin'</span> :isShareCards.sync=<span class="hljs-string">"isShareCards"</span> :data.sync=<span class="hljs-string">"data"</span>></saveImg>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// js</span>
<span class="hljs-keyword">import</span> saveImg <span class="hljs-keyword">from</span> <span class="hljs-string">'../../components/saveImg/saveImg.vue'</span>;

@Component(&#123;
    <span class="hljs-attr">components</span>: &#123;
        saveImg,
    &#125;
&#125;);



<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Sharepromotion</span>  <span class="hljs-keyword">extends</span> <span class="hljs-title">Vue</span> </span>&#123;
    <span class="hljs-comment">// 是否为本地app-web</span>
    @getter(<span class="hljs-string">'isApp'</span>)
    <span class="hljs-attr">isApp</span>: number;
    <span class="hljs-comment">// 是否是微信环境</span>
    @state(<span class="hljs-string">'appInfo'</span>, <span class="hljs-string">'isWeixin'</span>)
    <span class="hljs-attr">isWeixin</span>: boolean;
    @state(<span class="hljs-string">'shareOperatorInfo'</span>, <span class="hljs-string">'data'</span>)

    <span class="hljs-attr">data</span>: any;
    lang = lang;
    isShareCards = <span class="hljs-literal">false</span>; <span class="hljs-comment">// 是否保存图片弹窗</span>
    default_img = <span class="hljs-built_in">require</span>(<span class="hljs-string">'../../assets/img/sharePromotion/default_avatar.png'</span>);
    <span class="hljs-function"><span class="hljs-title">shareCards</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.isShareCards = <span class="hljs-literal">true</span>; <span class="hljs-comment">// 显示保存图片</span>
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.isShareCards ) &#123;
            <span class="hljs-built_in">this</span>.$nextTick(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
                <span class="hljs-keyword">const</span> handle: any = <span class="hljs-built_in">this</span>.$refs.child;
                handle.getCanvas((!<span class="hljs-built_in">this</span>.data.avatar_img ? <span class="hljs-built_in">this</span>.data.avatar_img : <span class="hljs-built_in">this</span>.default_img));
            &#125;);
        &#125;
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d052968a09b4fb9a3c605e70d353de0~tplv-k3u1fbpfcp-watermark.image" alt="03.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-5">遇到的Bug及对策</h1>
<h2 data-id="heading-6">一、图片跨域无法加载问题</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e672c764bb134b029f351103f403dc0c~tplv-k3u1fbpfcp-watermark.image" alt="04.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">1、前端js设置：useCORS: true</h3>
<blockquote>
<p><strong><code>这里有几个关键的地方：</code></strong></p>
<p>（1）allowTaint: true 和 useCORS: true 都是解决跨域问题的方式，不同的是使用allowTaint 会对canvas造成污染，就无法读取其数据，不能使用画布的toBolb()，toDataURL()或getImageData()方法，否则会出错，所以这里不能使用allowTaint: true</p>
<p>（2）在跨域的图片里设置 crossOrigin="anonymous" 并且需要给imageUrl加上随机数</p>
<p>（3）canvas.toDataURL('image/jpg') 是将canvas转成base64图片格式。</p>
</blockquote>
<h3 data-id="heading-8">2、服务端设置CORS</h3>
<p>解决跨域最常用的方法是跨域资源共享，我们将图片服务器的<code>response header</code>设置。</p>
<p>图片若存放在阿里云之类的，则也需要处理【接口的返回的图片地址是允许跨域的+项目的域名（不同环境）允许跨域，那么各个环境看都是可以运行的。】</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/969072e2c38047698931586eab0a5928~tplv-k3u1fbpfcp-watermark.image" alt="08.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>开发过程中，前后端设置配置都OK，但是就是还是报错，那么一个关键点就是运行环境如何看的问题了。</p>
<p>使用的图片不能在本地，因为图片可能还在本地服务器上，你的代码也还在本地；</p>
<p>若放在服务器上了，是没有问题的。想要查看有无问题，则把浏览器的跨域给设置一下，然后跑本地代码，若没有问题则该问题也是OK的。</p>
<p><strong><code>切记：图片url代码运行环境一定要保持一致！</code></strong></p>
<h2 data-id="heading-9">二、下载最新依赖包报错</h2>
<p>当解决了图片跨域问题（1、接口返回的图片是允许跨域的---由服务器那边控制；2、域名的控制：允许域名跨域），还是报错:</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff1cdaa8304b4eb48bb4534f08625714~tplv-k3u1fbpfcp-watermark.image" alt="07.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>一开始使用<code>html2canvas包的版本为1.0.0-rc.5</code>，减低至<code>html2canvas@0.5.0-beta3</code>的包，但是用npm 指定版本下载：<code>npm install html2canvas@0.5.0-beta3 </code>实际下载下来的却是<code>beta4</code>的版本；因此指定版本下载后还是有上述截图的问题；而后<strong>使用vue引入js插件来进行使用</strong>，竟然解决了。</p>
<h3 data-id="heading-10">1、在vue+ts项目中如何引入原生js插件来进行使用</h3>
<p>在<code>config/index.js</code>进行配置</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/306e31eb2b4c4737ab847ac24eb29857~tplv-k3u1fbpfcp-watermark.image" alt="config.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong><code>此方式导致的问题：整个文件都打包到项目中，导致项目体积变大，须优化！</code></strong></p>
<h3 data-id="heading-11">2、引入稳定的版本html2canvas 0.5.0-beta3，且解决了跨越问题；但如果截图区域有base64图片依然不成功。</h3>
<p>原因是node包里面对解析的base64后面加了时间戳导致src不能识别，所以修改了<code>config/templateInlineResources/html2canvas.js</code>包里面<code>1263行</code>代码为：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (src.match(<span class="hljs-regexp">/data:image\/.*;base64,/i</span>)) &#123;
   self.image.src = src;
 &#125; <span class="hljs-keyword">else</span> &#123;
    self.image.src = src +<span class="hljs-string">'?'</span>+ <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().getTime();
 &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f3a01fcda2b42019439f799c5df47f7~tplv-k3u1fbpfcp-watermark.image" alt="05.png" loading="lazy" referrerpolicy="no-referrer">
<strong><code>此刻完美解决报错~</code></strong></p>
<h3 data-id="heading-12">3、优化</h3>
<p>npm进行下载包时，无法正确对应的下载0.5.0-beta3的版本，下载下来的是0.5.0-beta4的版本；</p>
<p>直接引入html2canvas.js插件的方式，每个页面都会有这个插件在，导致项目体积过大；</p>
<p>npm 形式下载的话，在需要的时候才会用，所以最后决定<code>降低到0.5.0-beta02</code>的版本尝试看看改包是否有用？最后<code>beta2可以用</code>，就出现了位偏移的问题；加上需要改动包里边的内容，因此采取把该包直接拉取，然后进行改动后，放入自己git里边进行引用。</p>
<h4 data-id="heading-13">配置如下：</h4>
<ul>
<li>package.json的文件</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96e8123c92cf42aba3162f5c4af6d3f0~tplv-k3u1fbpfcp-watermark.image" alt="config_package01.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>package-log.json的文件</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2b886e3868574b6e84a7460db31c4df5~tplv-k3u1fbpfcp-watermark.image" alt="cofing_package02.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-14">三、在安卓手机上截屏清晰度问题</h2>
<p><strong><code>主要是scale的参数作用。</code></strong></p>
<h3 data-id="heading-15">1、使用设备像素密度</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 获取设备像素密度的方法</span>
getPixelRatio（context）&#123;
       <span class="hljs-keyword">var</span> backingStoreRatio = context.webkitBackingStorePixelRatio ||
            context.mozBackingStorePixelRatio ||
            context.msBackingStorePixelRatio ||
            context.oBackingStorePixelRatio ||
            context.backingStorePixelRatio || <span class="hljs-number">1</span>;
       <span class="hljs-keyword">return</span>  (<span class="hljs-built_in">window</span>.devicePixelRatio || <span class="hljs-number">1</span>) / backingStoreRatio; 
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cd7c0fd873bc4df2b41184cd197bfc7f~tplv-k3u1fbpfcp-watermark.image" alt="config_canvas01.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-16">2、放大比例倍数设置为固定值</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> scale = <span class="hljs-number">2</span>; <span class="hljs-comment">// 定义任意放大倍数 支持小数</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d71b5ddffa694cca8ba7cd5b2bf578bd~tplv-k3u1fbpfcp-watermark.image" alt="config_canvas02.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-17">3、关闭抗锯齿 保证生成的分享图是清晰的</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 关闭抗锯齿 保证生成的分享图是清晰的</span>
 context.mozImageSmoothingEnabled = <span class="hljs-literal">false</span>;
 context.webkitImageSmoothingEnabled = <span class="hljs-literal">false</span>;
 context.msImageSmoothingEnabled = <span class="hljs-literal">false</span>;
 context.imageSmoothingEnabled = <span class="hljs-literal">false</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a7d9361a52dd490cb1c80cbbe16669f4~tplv-k3u1fbpfcp-watermark.image" alt="config_canvas04.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-18">四、出现位偏移的问题问题</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> context = canvas.getContext(<span class="hljs-string">'2d'</span>);
<span class="hljs-keyword">var</span> rect = canEle.getBoundingClientRect(); <span class="hljs-comment">//获取元素相对于视察的偏移量</span>
context.translate(-rect.left, -rect.top); <span class="hljs-comment">//设置context位置，值为相对于视窗的偏移量负值，让图片复位</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8be00e47f4bb40f9b00b7a76a96296ae~tplv-k3u1fbpfcp-watermark.image" alt="config_canvas03.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            
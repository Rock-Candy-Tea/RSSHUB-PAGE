
---
title: 'css - 字体'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/123375a70edd4d04904f46945b27daec~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 15 Jun 2021 07:35:06 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/123375a70edd4d04904f46945b27daec~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与更文挑战的第15天，活动详情查看</strong>： <a href="https://juejin.cn/post/6967194882926444557" target="_blank"><strong>更文挑战</strong></a></p>
<p>工作比较忙，为了不断更，只能发以前的了。</p>
<p><a name="user-content-Dg67w" href="https://juejin.cn/post/undefined"></a></p>
<h1 data-id="heading-0">通用字体系列</h1>
<p><a name="user-content-tidf5" href="https://juejin.cn/post/undefined"></a></p>
<h2 data-id="heading-1">Serif字体</h2>
<p>字体成比例，而且有上下短线。如果字体中的所有字符根据其不同大小有不同的宽度，则称为字体是成比例的。例如：小写的i和m的宽度就不同。上下短线指的是每个字符笔画末端的装饰，如大写两条腿底部的短线。包括Times\Georgia\New century Schoolbook。<br>
<a name="user-content-VnDYr" href="https://juejin.cn/post/undefined"></a></p>
<h2 data-id="heading-2">sans-serif字体</h2>
<p>字体成比例，且没有上下短线(无衬线字体)，包括Helvetica\Geneva\Verdana\Arial\Univers<br>
<a name="user-content-TUVLC" href="https://juejin.cn/post/undefined"></a></p>
<h2 data-id="heading-3">Monospace字体</h2>
<p>字体不成比例，等宽字体，包括Courier\Courier New\Andale Mono<br>
<a name="user-content-KKxoS" href="https://juejin.cn/post/undefined"></a></p>
<h2 data-id="heading-4">Cursive字体</h2>
<p>手写体，包括Zapf Chancery\Author\Comic Sans<br>
<a name="user-content-wV2jX" href="https://juejin.cn/post/undefined"></a></p>
<h2 data-id="heading-5">Fantasy字体</h2>
<p>无法归类的字体，包括Western\Woodblock\Klingon<br></p>
<p>请看示例：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>  
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>  
    <span class="hljs-tag"><<span class="hljs-name">head</span>></span>  
        <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>  
        <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>  
        <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
            <span class="hljs-selector-tag">html</span> &#123;
                <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
                <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
                <span class="hljs-attribute">font-size</span>: <span class="hljs-number">20px</span>;
            &#125;
 
            <span class="hljs-selector-tag">div</span> &#123;
                <span class="hljs-attribute">margin</span>: <span class="hljs-number">20px</span>;
                <span class="hljs-attribute">background-color</span>: gray;
            &#125;
 
            <span class="hljs-selector-class">.serif</span> &#123;
                <span class="hljs-attribute">font-family</span>: <span class="hljs-string">"Times"</span>;
                
            &#125;
 
            <span class="hljs-selector-class">.sans-serif</span> &#123;
                <span class="hljs-attribute">font-family</span>: <span class="hljs-string">"Arial"</span>;
            &#125;
 
            <span class="hljs-selector-class">.Monospace</span> &#123;
                <span class="hljs-attribute">font-family</span>: <span class="hljs-string">"Courier"</span>;
            &#125;
 
            <span class="hljs-selector-class">.Cursive</span> &#123;
                <span class="hljs-attribute">font-family</span>: <span class="hljs-string">"Comic Sans"</span>;
            &#125;
 
            <span class="hljs-selector-class">.Fantasy</span> &#123;
                <span class="hljs-attribute">font-family</span>: <span class="hljs-string">"Western"</span>;
            &#125;
        </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">head</span>></span>  
    <span class="hljs-tag"><<span class="hljs-name">body</span>></span>  
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">'serif'</span>></span>serif字体: y l A<span class="hljs-tag"><<span class="hljs-name">font</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"background-color: red"</span>></span>i<span class="hljs-tag"></<span class="hljs-name">font</span>></span><span class="hljs-tag"><<span class="hljs-name">font</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"background-color: yellow"</span>></span>m<span class="hljs-tag"></<span class="hljs-name">font</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">'sans-serif'</span>></span>sans-serif字体: y l A<span class="hljs-tag"><<span class="hljs-name">font</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"background-color: red"</span>></span>i<span class="hljs-tag"></<span class="hljs-name">font</span>></span><span class="hljs-tag"><<span class="hljs-name">font</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"background-color: yellow"</span>></span>m<span class="hljs-tag"></<span class="hljs-name">font</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">'Monospace'</span>></span>Monospace字体: y l A<span class="hljs-tag"><<span class="hljs-name">font</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"background-color: red"</span>></span>i<span class="hljs-tag"></<span class="hljs-name">font</span>></span><span class="hljs-tag"><<span class="hljs-name">font</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"background-color: yellow"</span>></span>m<span class="hljs-tag"></<span class="hljs-name">font</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">'Cursive'</span>></span>Cursive字体: y l A<span class="hljs-tag"><<span class="hljs-name">font</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"background-color: red"</span>></span>i<span class="hljs-tag"></<span class="hljs-name">font</span>></span><span class="hljs-tag"><<span class="hljs-name">font</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"background-color: yellow"</span>></span>m<span class="hljs-tag"></<span class="hljs-name">font</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">'Fantasy'</span>></span>Fantasy字体: y l A<span class="hljs-tag"><<span class="hljs-name">font</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"background-color: red"</span>></span>i<span class="hljs-tag"></<span class="hljs-name">font</span>></span><span class="hljs-tag"><<span class="hljs-name">font</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"background-color: yellow"</span>></span>m<span class="hljs-tag"></<span class="hljs-name">font</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">body</span>></span>  
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>   
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/123375a70edd4d04904f46945b27daec~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>这里只介绍CSS 字体<br>serif字体，可以看到字母A是具有上下短线的，而且字母i和m的宽度不等，所以字体成比例。<br></p>
<p>​<br>
<a name="user-content-pLNGA" href="https://juejin.cn/post/undefined"></a></p>
<h1 data-id="heading-6">使用字体</h1>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">font-family</span>：<span class="hljs-selector-attr">[ <family-name> | <generic-family> ]</span> #
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong> = arial | georgia | verdana | helvetica | simsun and etc.</strong></li>
<li><strong> = cursive | fantasy | monospace | serif | sans-serif</strong></li>
</ul>
<ul>
<li>如果多个字体，则会首先匹配第一个字体。识别不到，才会识别第二个<br></li>
<li>字体为多个单词，则需要用引号将单词包含起来<br></li>
<li>如果只想使用某一个通用字体，但是不关心具体的字体名称，可以直接使用通用字体名称，如serif<br>​<br></li>
</ul>
<p><a name="user-content-bZLed" href="https://juejin.cn/post/undefined"></a></p>
<h1 data-id="heading-7">中文字体</h1>
<p><strong>字体中文名  字体英文名</strong><br>宋体           SimSun<br>黑体           SimHei<br>微软雅黑     Microsoft Yahei<br>微软正黑体  Microsoft JhengHei<br>楷体           KaiTi<br>新宋体  NSimSun <br>仿宋          FangSong<br>更多详情访问<a href="http://www.zhangxinxu.com/study/201703/font-family-chinese-english.html" target="_blank" rel="nofollow noopener noreferrer">文章</a><br>​</p>
<p><a name="user-content-ptNIl" href="https://juejin.cn/post/undefined"></a></p>
<h1 data-id="heading-8">字体加粗</h1>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">font-weight</span>：<span class="hljs-attribute">normal</span> | bold | bolder | lighter | <integer>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>取值：</p>
<ul>
<li>normal：正常的字体。相当于数字值400</li>
<li>bold：粗体。相当于数字值700。</li>
<li>bolder：定义比继承值更重的值</li>
<li>lighter：定义比继承值更轻的值</li>
<li><code><integer></code>：用数字表示文本字体粗细。取值范围：100 | 200 | 300 | 400 | 500 | 600 | 700 | 800 | 900</li>
</ul>
<p>​<br>
<a name="user-content-DibnL" href="https://juejin.cn/post/undefined"></a></p>
<h2 data-id="heading-9">解释bolder</h2>
<p>首先我们会得到从父元素继承而来的font-weight。当子元素设置成bolder的时候。会有一种规则(测试而来)：如下，</p>
<ul>
<li><strong>100 | 200 | 300 -> normal (400)</strong></li>
<li><strong>normal (400) | 500 | 600 -> bold (700)</strong></li>
<li><strong>bold (700) | 800 | x > 900 -> 900</strong></li>
</ul>
<p>​</p>
<ul>
<li>当父元素的font-weight为100 | 200 | 300，子元素的bolder都会跳到400。</li>
<li>当父元素的font-weight为normal (400) | 500 | 600，子元素的bolder都会跳到bold (700)。</li>
<li>当父元素的font-weight为bold (700) | 800 | x > 900，子元素的bolder都会跳到900。</li>
</ul>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.parent1</span> &#123;
    <span class="hljs-attribute">font-weight</span>: normal; <span class="hljs-comment">/*400*/</span>
&#125;
 
<span class="hljs-selector-class">.child1</span> &#123;
    <span class="hljs-attribute">font-weight</span>: bolder; <span class="hljs-comment">/*700*/</span>
&#125;
 
 
<span class="hljs-selector-class">.parent2</span> &#123;
    <span class="hljs-attribute">font-weight</span>: normal; <span class="hljs-comment">/*100*/</span>
&#125;
 
<span class="hljs-selector-class">.child2</span> &#123;
    <span class="hljs-attribute">font-weight</span>: bolder; <span class="hljs-comment">/*400*/</span>
&#125;
 
 
<span class="hljs-selector-class">.parent3</span> &#123;
    <span class="hljs-attribute">font-weight</span>: normal; <span class="hljs-comment">/*700*/</span>
&#125;
 
<span class="hljs-selector-class">.child3</span> &#123;
    <span class="hljs-attribute">font-weight</span>: bolder; <span class="hljs-comment">/*900*/</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/94bf32a7a443460ca4c40b537c7ecd39~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<a name="user-content-mh1Fn" href="https://juejin.cn/post/undefined"></a></p>
<h2 data-id="heading-10">解释lighter</h2>
<p>首先我们会得到从父元素继承而来的font-weight。当子元素设置成lighter的时候。会有一种规则(测试而来)：如下</p>
<ul>
<li><strong>500 | 400 | 300 | 200 | 100 -> 100</strong></li>
<li><strong>700 | 600 -> normal (400)</strong></li>
<li><strong>900 | 800 -> bold (700)</strong></li>
<li><strong>x > 900 -> (chorme: 400), (IE, firefox : 100)</strong></li>
</ul>
<p>​
<a name="user-content-PZC9h" href="https://juejin.cn/post/undefined"></a></p>
<h1 data-id="heading-11">字体大小</h1>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">font-size</span>：<absolute-size> | <relative-size> | <length> | <percentage>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong><code><absolute-size></code>= xx-small | x-small | small | medium | large | x-large | xx-large</strong></li>
<li><strong><code><relative-size></code>= smaller | larger</strong></li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>  
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>  
    <span class="hljs-tag"><<span class="hljs-name">head</span>></span>  
        <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>  
        <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>  
        <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
            <span class="hljs-selector-tag">html</span> &#123;
                <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
                <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
            &#125;
 
            <span class="hljs-selector-class">.xx-small</span> &#123;
                <span class="hljs-attribute">font-size</span>: xx-small;
            &#125;
 
            <span class="hljs-selector-class">.x-small</span> &#123;
                <span class="hljs-attribute">font-size</span>: x-small;
            &#125;
 
            <span class="hljs-selector-class">.small</span> &#123;
                <span class="hljs-attribute">font-size</span>: small;
            &#125;
 
            <span class="hljs-selector-class">.medium</span>  &#123;
                <span class="hljs-attribute">font-size</span>: medium ;
            &#125;
 
            <span class="hljs-selector-class">.large</span>  &#123;
                <span class="hljs-attribute">font-size</span>: large ;
            &#125;
 
            <span class="hljs-selector-class">.x-large</span> &#123;
                <span class="hljs-attribute">font-size</span>: x-large;
            &#125;
 
            <span class="hljs-selector-class">.xx-large</span> &#123;
                <span class="hljs-attribute">font-size</span>: xx-large;
            &#125;
        </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">head</span>></span>  
    <span class="hljs-tag"><<span class="hljs-name">body</span>></span>  
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            normal text
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"xx-small"</span>></span>
            xx-small text
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"x-small"</span>></span>
            x-small text
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"small"</span>></span>
            small text
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"medium"</span>></span>
            medium text
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"large"</span>></span>
            large text
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"x-large"</span>></span>
            xlarge text
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"xx-large"</span>></span>
            xx-large text
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">body</span>></span>  
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>   
<span class="copy-code-btn">复制代码</span></code></pre>
<p><br>测试结果：<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3e1f92d624a541cea52e4dd16cfe220f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><br>​<br>
<a name="user-content-b0Oqe" href="https://juejin.cn/post/undefined"></a></p>
<h2 data-id="heading-12">测试larger</h2>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>  
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>  
    <span class="hljs-tag"><<span class="hljs-name">head</span>></span>  
        <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>  
        <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>  
        <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
            <span class="hljs-selector-tag">html</span> &#123;
                <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
                <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
            &#125;
 
            <span class="hljs-selector-class">.child</span> &#123;
                <span class="hljs-attribute">font-size</span>: larger;
            &#125;
 
            <span class="hljs-selector-class">.xx-small</span> &#123;
                <span class="hljs-attribute">font-size</span>: xx-small;
            &#125;
 
            <span class="hljs-selector-class">.x-small</span> &#123;
                <span class="hljs-attribute">font-size</span>: x-small;
            &#125;
 
            <span class="hljs-selector-class">.small</span> &#123;
                <span class="hljs-attribute">font-size</span>: small;
            &#125;
 
            <span class="hljs-selector-class">.medium</span>  &#123;
                <span class="hljs-attribute">font-size</span>: medium ;
            &#125;
 
            <span class="hljs-selector-class">.large</span>  &#123;
                <span class="hljs-attribute">font-size</span>: large ;
            &#125;
 
            <span class="hljs-selector-class">.x-large</span> &#123;
                <span class="hljs-attribute">font-size</span>: x-large;
            &#125;
 
            <span class="hljs-selector-class">.xx-large</span> &#123;
                <span class="hljs-attribute">font-size</span>: xx-large;
            &#125;
 
        </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">head</span>></span>  
    <span class="hljs-tag"><<span class="hljs-name">body</span>></span>  
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"xx-small"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"child"</span>></span>
                xx-small parent
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"x-small"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"child"</span>></span>
                x-small parent
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"small"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"child"</span>></span>
                small parent
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"medium"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"child"</span>></span>
                medium parent
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"large"</span>></span>
           <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"child"</span>></span>
                large parent
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"x-large"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"child"</span>></span>
                x-large parent
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"xx-large"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"child"</span>></span>
                xx-large parent
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">body</span>></span>  
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>   
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f412410f8b52497f9a2b1ef360b3e8ae~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6c3e7031a17846148ac71b53140cda98~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><br>​<br>
<a name="user-content-IvGSx" href="https://juejin.cn/post/undefined"></a></p>
<h2 data-id="heading-13">测试smaller</h2>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>  
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>  
    <span class="hljs-tag"><<span class="hljs-name">head</span>></span>  
        <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>  
        <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>  
        <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
            <span class="hljs-selector-tag">html</span> &#123;
                <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
                <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
            &#125;
 
            <span class="hljs-selector-class">.child</span> &#123;
                <span class="hljs-attribute">font-size</span>: smaller;
            &#125;
 
            <span class="hljs-selector-class">.xx-small</span> &#123;
                <span class="hljs-attribute">font-size</span>: xx-small;
            &#125;
 
            <span class="hljs-selector-class">.x-small</span> &#123;
                <span class="hljs-attribute">font-size</span>: x-small;
            &#125;
 
            <span class="hljs-selector-class">.small</span> &#123;
                <span class="hljs-attribute">font-size</span>: small;
            &#125;
 
            <span class="hljs-selector-class">.medium</span>  &#123;
                <span class="hljs-attribute">font-size</span>: medium ;
            &#125;
 
            <span class="hljs-selector-class">.large</span>  &#123;
                <span class="hljs-attribute">font-size</span>: large ;
            &#125;
 
            <span class="hljs-selector-class">.x-large</span> &#123;
                <span class="hljs-attribute">font-size</span>: x-large;
            &#125;
 
            <span class="hljs-selector-class">.xx-large</span> &#123;
                <span class="hljs-attribute">font-size</span>: xx-large;
            &#125;
 
        </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">head</span>></span>  
    <span class="hljs-tag"><<span class="hljs-name">body</span>></span>  
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"xx-small"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"child"</span>></span>
                xx-small parent
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"x-small"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"child"</span>></span>
                x-small parent
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"small"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"child"</span>></span>
                small parent
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"medium"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"child"</span>></span>
                medium parent
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"large"</span>></span>
           <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"child"</span>></span>
                large parent
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"x-large"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"child"</span>></span>
                x-large parent
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"xx-large"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"child"</span>></span>
                xx-large parent
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">body</span>></span>  
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>   
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ce255f8ae844066840a1b217139cd90~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><br>​</p>
<p><a name="user-content-H8YOd" href="https://juejin.cn/post/undefined"></a></p>
<h1 data-id="heading-14">字体风格</h1>
<ul>
<li><strong>normal：指定文本字体样式为正常的字体</strong></li>
<li><strong>italic：指定文本字体样式为斜体。对于没有设计斜体的特殊字体，如果要使用斜体外观将应用oblique</strong></li>
<li><strong>oblique：指定文本字体样式为倾斜的字体。人为的使文字倾斜，而不是去选取字体中的斜体字</strong></li>
</ul>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.italic</span> &#123;
    <span class="hljs-attribute">font-style</span>: italic;
&#125;
 
<span class="hljs-selector-class">.oblique</span> &#123;
    <span class="hljs-attribute">font-style</span>: oblique;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>​<br>
<a name="user-content-rPHar" href="https://juejin.cn/post/undefined"></a></p>
<h1 data-id="heading-15">字体变形</h1>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">font-variant</span>：<span class="hljs-attribute">normal</span> | small-caps
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>normal：正常的字体</strong></li>
<li><strong>small-caps：小型的大写字母字体，如果文本源中出现大写字母，则会显示正常的大写字母</strong></li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>  
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>  
    <span class="hljs-tag"><<span class="hljs-name">head</span>></span>  
        <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>  
        <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>  
        <span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">
            <span class="hljs-selector-class">.normal</span> &#123;
                <span class="hljs-attribute">font-variant</span>: normal;
            &#125;
 
            <span class="hljs-selector-class">.small-caps</span> &#123;
                <span class="hljs-attribute">font-variant</span>: small-caps;
            &#125;
        </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">head</span>></span>  
    <span class="hljs-tag"><<span class="hljs-name">body</span>></span>  
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"normal"</span>></span>
            NORMAL 文字
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
 
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"small-caps"</span>></span>
            LARGE WORDS small-caps 文字
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">body</span>></span>  
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f57e51edfaa48b9b612e323040793ec~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7054d841cea94e0e9d67f2ed085bdfde~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>​<br>​<br>
<a name="user-content-nljEx" href="https://juejin.cn/post/undefined"></a></p>
<h1 data-id="heading-16">字体拉伸和调整（了解，几乎所有的浏览器不支持）</h1>
<p><a name="user-content-jAhLY" href="https://juejin.cn/post/undefined"></a></p>
<h2 data-id="heading-17">字体拉伸</h2>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">font-stretch</span>：<span class="hljs-attribute">normal</span> | ultra-condensed | extra-condensed | condensed | semi-condensed | semi-expanded | expanded | extra-expanded | ultra-expanded
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>normal：正常文字宽度</strong></li>
<li><strong>ultra-condensed：比正常文字宽度窄4个基数。</strong></li>
<li><strong>extra-condensed：比正常文字宽度窄3个基数。</strong></li>
<li><strong>condensed：比正常文字宽度窄2个基数。</strong></li>
<li><strong>semi-condensed：比正常文字宽度窄1个基数。</strong></li>
<li><strong>semi-expanded：比正常文字宽度宽1个基数。</strong></li>
<li><strong>expanded：比正常文字宽度宽2个基数。</strong></li>
<li><strong>extra-expanded：比正常文字宽度宽3个基数。</strong></li>
<li><strong>ultra-expanded：比正常文字宽度宽4个基数。</strong></li>
</ul>
<p>​<br>
<a name="user-content-dXDrl" href="https://juejin.cn/post/undefined"></a></p>
<h2 data-id="heading-18">字体调整</h2>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">font-size-adjust</span>：<span class="hljs-attribute">none</span> | <number>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>none：不保留首选字体的 x-height</strong></li>
<li><code><number></code>定义字体的 aspect 值**</li>
</ul>
<p>​<br>
<a name="user-content-TPjfa" href="https://juejin.cn/post/undefined"></a></p>
<h1 data-id="heading-19">复合属性font</h1>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">font</span>：<span class="hljs-selector-attr">[ [ <<span class="hljs-string">' font-style '</span>> || <<span class="hljs-string">' font-variant '</span>> || <<span class="hljs-string">' font-weight '</span>> ]</span>? <' <span class="hljs-attribute">font-size</span> '> <span class="hljs-selector-attr">[ / <<span class="hljs-string">' line-height '</span>> ]</span>? <' <span class="hljs-attribute">font-family</span> '> ] | <span class="hljs-selector-tag">caption</span> | <span class="hljs-attribute">icon</span> | <span class="hljs-selector-tag">menu</span> | message-box | small-<span class="hljs-selector-tag">caption</span> | status-bar 
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong><' font-style '>：指定文本字体样式</strong></li>
<li><strong><' font-variant '>：指定文本是否为小型的大写字母</strong></li>
<li><strong><' font-weight '>：指定文本字体的粗细</strong></li>
<li><strong><' font-size '>：指定文本字体尺寸</strong></li>
<li><strong><' line-height '>：指定文本字体的行高</strong></li>
<li><strong><' font-family '>：指定文本使用某个字体或字体序列</strong></li>
<li><strong>caption：使用有标题的系统控件的文本字体（如按钮，菜单等）（CSS2）</strong></li>
<li><strong>icon：使用图标标签的字体（CSS2）</strong></li>
<li><strong>menu：使用菜单的字体（CSS2）</strong></li>
<li><strong>message-box：使用信息对话框的文本字体（CSS2）</strong></li>
<li><strong>small-caption：使用小控件的字体（CSS2）</strong></li>
<li><strong>status-bar：使用窗口状态栏的字体（CSS2）</strong></li>
</ul>
<p>​<br>
<a name="user-content-GWfCA" href="https://juejin.cn/post/undefined"></a></p>
<h1 data-id="heading-20">@font-face</h1>
<p>在 CSS3 之前，web 设计师必须使用已在用户计算机上安装好的字体。通过 CSS3，web 设计师可以使用他们喜欢的任意字体。<br>
<br>当找到或购买到希望使用的字体时，可将该字体文件存放到 web 服务器上，它会在需要时被自动下载到用户的计算机上。字体是在 CSS3 @font-face 规则中定义的。但是如果我们下载的字体太大，会存在性能问题，不过好在现在的字体服务商给的文件都不大。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-keyword">@font-face</span> &#123;
    <span class="hljs-attribute">font-family</span>: <YourWebFontName>;
    <span class="hljs-attribute">src</span>: <source> [<format>][,<source> [<format>]]*;
    <span class="hljs-selector-attr">[font-weight: <weight>]</span>;
    <span class="hljs-selector-attr">[font-style: <style>]</span>;
    <span class="hljs-selector-attr">[unicode-range： <unicode-range>]</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>YourWebFontName：指的就是自定义的字体名称，最好是使用你下载的默认字体，它将被引用到你的Web元素中的font-family。如“font-family:”字体名”;”</strong></li>
<li><strong>Source：指的是自定义的字体的存放路径，可以是相对路径也可以是绝路径；</strong></li>
<li><strong>Format：指的是自定义的字体的格式，主要用来帮助浏览器识别，其值主要有以下几种类型：truetype,opentype,truetype-aat,embedded-opentype,avg等；</strong></li>
<li><strong>weight和style: weight定义字体是否为粗体，style主要定义字体样式，如斜体。</strong></li>
<li><strong>unicode-range: 可选。定义字体支持的 UNICODE 字符范围。默认是 "U+0-10FFFF"。</strong></li>
</ul>
<p>​<br>
<a name="user-content-UxyrJ" href="https://juejin.cn/post/undefined"></a></p>
<h2 data-id="heading-21">(1) 使用font-face自定义字体</h2>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-keyword">@font-face</span> &#123;
    <span class="hljs-attribute">font-family</span>: YourWebFontName;
    <span class="hljs-attribute">src</span>: <span class="hljs-built_in">url</span>(<span class="hljs-string">../font/test.eot</span>);
    <span class="hljs-attribute">src</span>: <span class="hljs-built_in">url</span>(<span class="hljs-string">../font/test.eot?#iefix</span>) <span class="hljs-built_in">format</span>(<span class="hljs-string">"embedded-opentype"</span>),
         <span class="hljs-built_in">url</span>(<span class="hljs-string">../font/test.woff</span>) <span class="hljs-built_in">format</span>(<span class="hljs-string">"woff"</span>), 
         <span class="hljs-built_in">url</span>(<span class="hljs-string">../font/test.ttf</span>) <span class="hljs-built_in">format</span>(<span class="hljs-string">"truetype"</span>),
         <span class="hljs-built_in">url</span>(<span class="hljs-string">../font/test.svg#jq</span>) <span class="hljs-built_in">format</span>(<span class="hljs-string">"svg"</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>​<br>
<a name="user-content-uuXNu" href="https://juejin.cn/post/undefined"></a></p>
<h2 data-id="heading-22">(2) 声明字体来源</h2>
<p>@font-face规则中有一个非常重要的参数，就是src。其值主要是用于连接到实际的字体文件。此外，可以声明多个来源，如果浏览器未能找到第一个来源，他回一次寸照下面的字体来源。<br>上面声明了四中字体：EOT, WOFF, TTF和SVG。</p>
<ul>
<li><strong>TureTpe(.ttf)格式</strong><br>.ttf字体是Windows和Mac的最常见的字体，是一种RAW格式，因此他不为网站优化,支持这种字体的浏览器有【IE9+,Firefox3.5+,Chrome4+,Safari3+,Opera10+,iOS Mobile Safari4.2+】；</li>
<li><strong>OpenType(.otf)格式</strong><br>.otf字体被认为是一种原始的字体格式，其内置在TureType的基础上，所以也提供了更多的功能,支持这种字体的浏览器有【Firefox3.5+,Chrome4.0+,Safari3.1+,Opera10.0+,iOS Mobile Safari4.2+】；</li>
<li><strong>Web Open Font Format(.woff)格式</strong><br>.woff字体是Web字体中最佳格式，他是一个开放的TrueType/OpenType的压缩版本，同时也支持元数据包的分离,支持这种字体的浏览器有【IE9+,Firefox3.5+,Chrome6+,Safari3.6+,Opera11.1+】；</li>
<li>**Embedded Open Type(.eot)格式 **<br>.eot字体是IE专用字体，可以从TrueType创建此格式字体,支持这种字体的浏览器有【IE4+】；</li>
<li>**SVG(.svg)格式 **<br>.svg字体是基于SVG字体渲染的一种格式,支持这种字体的浏览器有【Chrome4+,Safari3.1+,Opera10.0+,iOS Mobile Safari3.2+】。</li>
</ul>
<p>​<br>
<a name="user-content-R1mZF" href="https://juejin.cn/post/undefined"></a></p>
<h2 data-id="heading-23">(3) 创建各种字体</h2>
<p>这里以国内的网站<a href="https://www.youziku.com/onlinefont/index" target="_blank" rel="nofollow noopener noreferrer">有字库</a>为例。<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1efff8bd854c42559eaa3aa0b1d81d05~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><br>然后得到对应的font-face代码：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>  
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>  
    <span class="hljs-tag"><<span class="hljs-name">head</span>></span>  
        <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>  
        <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>  
        <span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">
            <span class="hljs-keyword">@font-face</span> &#123;
                <span class="hljs-attribute">font-family</span>: <span class="hljs-string">'ChannelSlanted2'</span>;
                <span class="hljs-attribute">src</span>: <span class="hljs-built_in">url</span>(<span class="hljs-string">'http://cdn.webfont.youziku.com/webfonts/nomal/118923/45817/5b0d6df4f629d91b10cd3bc2.gif?r=76000373532'</span>);
                <span class="hljs-attribute">src</span>: <span class="hljs-built_in">url</span>(<span class="hljs-string">'http://cdn.webfont.youziku.com/webfonts/nomal/118923/45817/5b0d6df4f629d91b10cd3bc2.gif?r=76000373532?#iefix'</span>) <span class="hljs-built_in">format</span>(<span class="hljs-string">'embedded-opentype'</span>),
                     <span class="hljs-built_in">url</span>(<span class="hljs-string">'http://cdn.webfont.youziku.com/webfonts/nomal/118923/45817/5b0d6df4f629d91b10cd3bc2.png?r=76000373532'</span>) <span class="hljs-built_in">format</span>(<span class="hljs-string">'woff2'</span>),
                     <span class="hljs-built_in">url</span>(<span class="hljs-string">'http://cdn.webfont.youziku.com/webfonts/nomal/118923/45817/5b0d6df4f629d91b10cd3bc2.bmp?r=76000373532'</span>) <span class="hljs-built_in">format</span>(<span class="hljs-string">'woff'</span>);
                <span class="hljs-attribute">font-weight</span>: normal;
                <span class="hljs-attribute">font-style</span>: normal;
            &#125;
 
            <span class="hljs-selector-class">.ChannelSlanted2</span> &#123;
                <span class="hljs-attribute">font-family</span>: <span class="hljs-string">"ChannelSlanted2"</span>
            &#125;
        </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">head</span>></span>  
    <span class="hljs-tag"><<span class="hljs-name">body</span>></span>  
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"ChannelSlanted2"</span>></span>
            LARGE WORDS small-caps 文字
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">body</span>></span>  
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>   
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后得到我们的图字效果。<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/53a6f0835a7f4ead9c777f8bc5f45752~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>还可以到网站（<a href="https://www.fontsquirrel.com/" target="_blank" rel="nofollow noopener noreferrer">www.fontsquirrel.com/</a>）去下载一些字体的格式。然后如果我们的到只是其中一种格式的话，因为前面给出的网站下载的都是.otf格式，所以我们还需要转换成其他格式。可以使用下面的网站进行格式转换。</p>
<ul>
<li>font2web：<a href="http://www.font2web.com/" target="_blank" rel="nofollow noopener noreferrer">www.font2web.com/</a></li>
<li>freefontconverter：<a href="http://www.freefontconverter.com/" target="_blank" rel="nofollow noopener noreferrer">www.freefontconverter.com/</a></li>
</ul>
<p>​<br>
<a name="user-content-RwIUG" href="https://juejin.cn/post/undefined"></a></p>
<h2 data-id="heading-24">(4) 延伸：@font-face使用本地字符</h2>
<p>@font-face 规则中的src 描述符还可以接受local()函数，用于指定本地字体的名称。当不需要用到任何外部的Web 字体，就可以直接在字体队列中指定一款本地字体：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-keyword">@font-face</span> &#123;
<span class="hljs-attribute">font-family</span>: Ampersand;
<span class="hljs-attribute">src</span>: <span class="hljs-built_in">local</span>(<span class="hljs-string">'Baskerville'</span>),
<span class="hljs-built_in">local</span>(<span class="hljs-string">'Goudy Old Style'</span>),
<span class="hljs-built_in">local</span>(<span class="hljs-string">'Garamond'</span>),
<span class="hljs-built_in">local</span>(<span class="hljs-string">'Palatino'</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>举例：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>  
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>  
    <span class="hljs-tag"><<span class="hljs-name">head</span>></span>  
        <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>  
        <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>  
        <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
            <span class="hljs-keyword">@font-face</span> &#123;
                <span class="hljs-attribute">font-family</span>: Ampersand;
                <span class="hljs-attribute">src</span>: <span class="hljs-built_in">local</span>(<span class="hljs-string">'Comic Sans MS'</span>);
            &#125;
 
            <span class="hljs-selector-class">.icon</span> &#123;
                <span class="hljs-attribute">font-family</span>: Ampersand
            &#125;
        </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">head</span>></span>  
    <span class="hljs-tag"><<span class="hljs-name">body</span>></span>  
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"icon"</span>></span>
            HTML & CSS
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">body</span>></span>  
<span class="hljs-tag"></<span class="hljs-name">html</span>></span> 
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/76741485d82a4af49546053534f808d9~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>​<br>
<a name="user-content-Mwych" href="https://juejin.cn/post/undefined"></a></p>
<h2 data-id="heading-25">(5) 延伸：unicode-range控制字体应用范围</h2>
<p>当我们想要控制字符应用的范围，需要一个描述符来声明我们想用这几款本地字体来显示哪些字符。<br></p>
<p>unicode-range 描述符只在@font-face 规则内部生效（因此这里用了描述符这个术语；它并不是一个CSS 属性），它可以把字体作用的字符范围限制在一个子集内。它对本地字体和远程字体都是有效<br></p>
<p>这个unicode-range 在实践中非常实用，但在语法上却非常晦涩。它的语法是基于“Unicode 码位”的，而不是基于字符的字面形态。<br></p>
<p>例如：我们想是上面的示例中HTML & CSS中的&应用字体，其他的不变化。
<a name="user-content-vGHx7" href="https://juejin.cn/post/undefined"></a></p>
<h3 data-id="heading-26">1) 在控制台执行下面代码得到十六进制码位</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-string">"&"</span>.charCodeAt(<span class="hljs-number">0</span>).toString(<span class="hljs-number">16</span>); <span class="hljs-comment">// 返回26</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a name="user-content-CuUQ7" href="https://juejin.cn/post/undefined"></a></p>
<h3 data-id="heading-27">2) 形成unicode-range代码</h3>
<p>需要在码位前面加上U+ 作为前缀</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">unicode-range: U+<span class="hljs-number">26</span>; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>*如果你想指定一个字符区间，还是要加上U+ 前缀，比如U+400-4FF。实际上对于这个区间来说，你还可以使用通配符，以这样的方式来写：U+4??。同时指定多个字符或多个区间也是允许的，把它们用逗号隔开即可，比如U+26, U+4??, U+2665-2670。<br></p>
<p><a name="user-content-QuDHJ" href="https://juejin.cn/post/undefined"></a></p>
<h3 data-id="heading-28">3) 修改代码如下</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><!DOCTYPE html>  
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>  
    <span class="hljs-tag"><<span class="hljs-name">head</span>></span>  
        <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>  
        <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>  
        <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
            <span class="hljs-keyword">@font-face</span> &#123;
                <span class="hljs-attribute">font-family</span>: Ampersand;
                <span class="hljs-attribute">src</span>: <span class="hljs-built_in">local</span>(<span class="hljs-string">'Comic Sans MS'</span>);
                unicode-range: U+<span class="hljs-number">26</span>; 
            &#125;
 
            <span class="hljs-selector-class">.icon</span> &#123;
                <span class="hljs-attribute">font-family</span>: Ampersand
            &#125;
        </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">head</span>></span>  
    <span class="hljs-tag"><<span class="hljs-name">body</span>></span>  
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"icon"</span>></span>
            HTML & CSS
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">body</span>></span>  
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>然后我们看一下现在的样式以及和之前的样式对比（红色的是带有unicode-range的html，可以看到当前只有&还是和之前相同，其他的不在应用Ampersand字体）：<br><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3db4307f1aaf42a08bf1494326b95354~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            
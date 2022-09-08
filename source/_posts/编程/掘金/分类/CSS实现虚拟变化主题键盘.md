
---
title: 'CSS实现虚拟变化主题键盘'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7410f3ba643141aeb3ec43b146b3e911~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
author: 掘金
comments: false
date: Wed, 07 Sep 2022 03:03:25 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7410f3ba643141aeb3ec43b146b3e911~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
---

<div>   
<div class="markdown-body cache"><style>@charset "UTF-8";.markdown-body&#123;font-family:-apple-system,system-ui,Segoe UI,Roboto,Ubuntu,Cantarell,Noto Sans,sans-serif,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial;color:#00325e&#125;.markdown-body ::selection&#123;background-color:#00325e;color:#fff&#125;.markdown-body blockquote&#123;padding:10px 20px;background-color:#fffaf0;box-shadow:0 3px 10px 0 rgba(255,172,194,.24);border:1px solid #f3ca8e;transition:all .2s;margin:1em 0;border-radius:5px&#125;.markdown-body blockquote p&#123;font-size:14px;line-height:25px;color:#795548&#125;.markdown-body blockquote p:last-child&#123;margin:0&#125;.markdown-body blockquote:hover&#123;border-color:#ff9800;background-color:#fff8e0;box-shadow:0 6px 10px -5px rgba(225,173,98,.3803921569)&#125;.markdown-body blockquote code&#123;color:#ff502c&#125;.markdown-body pre&#123;border:1px solid #8cc0f3;box-shadow:0 3px 10px 0 rgba(255,198,198,.28);border-radius:5px;transition:all .2s;overflow-x:auto;white-space:pre-wrap&#125;.markdown-body pre:hover&#123;border-color:#6d9dce&#125;.markdown-body pre>code&#123;padding:10px 20px;color:#00325e;background:#f0f8ff;font-size:12px;line-height:1.6;display:block&#125;.markdown-body code&#123;background:#f6fbff;color:#0b5393;padding:2px 4px;border-radius:4px;font-size:12px&#125;.markdown-body p&#123;font-size:14px;line-height:28px;text-align:justify;margin-bottom:17px;color:#595959&#125;.markdown-body a&#123;color:#00325e;text-decoration:none&#125;.markdown-body a:after&#123;content:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAAXNSR0IArs4c6QAAAQdJREFUKFNt0DtLA0EUBeBzZle0Eks7rcUfEfBRCha7NorYa6NmVJzgyi4smUgKtdZGCJktLMVH4Y8QeztLWyE7VyLEuNFbXj4Oh0P8c8mZm+uJrEN4BJFTeP/MUVe3bnocfALwkOlo1zS7iZAzf6Cx7oXgbaqjxiDEWCcVaGyxQ8pSWo9XhqhoQ/xUFbaKjhe5V+CmR7mnSplEEF6GSmJ+F/d0KHvbCIIJCLc85U6BC5mONgbJNM3uFag++sX7z8O8MzsWBucifMx0dDGE1kmm458KDVukAlnNdDz/exEeW3dNkbfsYC0xtmgDWP6ELLZ0/F6BJu/UoFQN5AkoeUjeJPvx6+i+X5Sjah4tA6gYAAAAAElFTkSuQmCC);margin-left:2px&#125;.markdown-body a:hover&#123;box-shadow:0 1px&#125;.markdown-body table&#123;max-width:100%;border-collapse:collapse;border-spacing:0;box-shadow:0 3px 10px 0 rgba(255,238,172,.24);transition:all .2s&#125;.markdown-body table:hover&#123;box-shadow:0 3px 10px 0 rgba(185,169,103,.24)&#125;.markdown-body table tr th&#123;border:1px solid #8cc0f3;background-color:#f0f8ff;padding:12px 15px&#125;.markdown-body table tr td&#123;border:1px solid rgba(243,202,142,.4);padding:12px 15px&#125;.markdown-body table tbody tr&#123;transition:all .2s&#125;.markdown-body table tbody tr:hover td&#123;border-color:#f3ca8e;background-color:#fff8e0;z-index:1&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body h1&#123;font-size:20px;margin-top:30px;margin-bottom:10px;padding-left:30px;position:relative&#125;.markdown-body h1>code&#123;font-size:20px&#125;.markdown-body h1:before&#123;content:"🍺";display:block;font-size:18px;width:18px;height:18px;left:0;position:absolute&#125;.markdown-body h2&#123;font-size:18px;margin-top:30px;margin-bottom:10px;padding-left:28px;position:relative&#125;.markdown-body h2>code&#123;font-size:18px&#125;.markdown-body h2:before&#123;content:"🍻";display:block;font-size:16px;width:16px;height:16px;left:0;position:absolute&#125;.markdown-body h3&#123;font-size:16px;margin-top:30px;margin-bottom:10px;padding-left:26px;position:relative&#125;.markdown-body h3>code&#123;font-size:16px&#125;.markdown-body h3:before&#123;content:"🥂";display:block;font-size:14px;width:14px;height:14px;left:0;position:absolute&#125;.markdown-body h4&#123;font-size:14px;margin-top:30px;margin-bottom:10px;padding-left:24px;position:relative&#125;.markdown-body h4>code&#123;font-size:14px&#125;.markdown-body h4:before&#123;content:"🥃";display:block;font-size:12px;width:12px;height:12px;left:0;position:absolute&#125;.markdown-body h5&#123;font-size:12px;margin-top:30px;margin-bottom:10px&#125;.markdown-body h5>code&#123;font-size:12px&#125;.markdown-body h6&#123;font-size:10px;margin-top:30px;margin-bottom:10px&#125;.markdown-body h6>code&#123;font-size:10px&#125;.markdown-body h1,.markdown-body h2&#123;color:#ff502c&#125;.markdown-body hr&#123;height:4px;border:none;margin-top:32px;margin-bottom:32px;background-size:4px 1px;background-image:linear-gradient(270deg,#6d9dce,#8cc0f3 25%,transparent 50%)&#125;.markdown-body hr:nth-child(2n)&#123;background-image:linear-gradient(270deg,#ff9800,#fff8e0 25%,transparent 50%)&#125;.markdown-body ul&#123;padding-inline-start:20px&#125;.markdown-body ul li&#123;list-style-type:"🔸"&#125;.markdown-body ul li li&#123;list-style-type:"◻️"&#125;.markdown-body ul li li li&#123;list-style-type:"▫️"&#125;.markdown-body ol&#123;padding-inline-start:20px&#125;.markdown-body ol ::marker&#123;color:#ff9800&#125;.markdown-body ol,.markdown-body ul&#123;line-height:2em&#125;.markdown-body li&#123;padding-inline-start:1ch&#125;.markdown-body li.task-list-item&#123;list-style:none;padding-inline-start:0&#125;.markdown-body li input&#123;padding-right:2px&#125;.markdown-body li input[type=checkbox i]&#123;appearance:none&#125;.markdown-body li input:before&#123;content:"🟩";display:block;width:13px;height:13px&#125;.markdown-body li input:checked:before&#123;content:"✅"&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>我正在参加「码上掘金挑战赛」详情请看：<a href="https://juejin.cn/post/7139728821862793223" title="https://juejin.cn/post/7139728821862793223" target="_blank">码上掘金挑战赛来了！</a></p>
</blockquote>
<blockquote>
<p>作为程序员天天敲打着键盘，我就想能否通过css实现呢，今天我们就用css来实现一下虚拟键盘，为了不让他看起来那么单调，我们在给它添加一个变化主题色的功能</p>
</blockquote>
<h1 data-id="heading-0">效果图</h1>
<blockquote>
<p>未变色前</p>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7410f3ba643141aeb3ec43b146b3e911~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="企业微信截图_16625465761176.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>变色后</p>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c61feb4215242b68382bde3724fece4~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="企业微信截图_16625465624906.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-1">实现思路</h1>
<blockquote>
<p>我们来分析下布局，这一个键盘是大盒子，然后大盒子里面有三个盒子，这三个盒子分别代表三行，每一行Y轴不对齐</p>
</blockquote>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8398016d1ece4f20a77f9da29c5a8caf~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="企业微信截图_16625466331825.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-2">页面结构</h1>
<blockquote>
<p>三行盒子我们通过无序列表进行实现，键盘上有一个Fn键，他是用于控制键盘主题色变化的，我们把他单独拿出来</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">  <!-- 大盒子 -->
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"btn"</span>></span>Fn<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
            <span class="hljs-comment"><!-- 键盘列 --></span>
            <span class="hljs-tag"><<span class="hljs-name">li</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span>></span>q<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span>></span>w<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span>></span>e<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span>></span>r<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span>></span>t<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span>></span>y<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span>></span>u<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span>></span>i<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span>></span>o<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span>></span>p<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">li</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">li</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span>></span>a<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span>></span>s<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span>></span>d<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span>></span>f<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span>></span>g<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span>></span>h<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span>></span>j<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span>></span>k<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span>></span>l<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">li</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">li</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span>></span>z<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span>></span>x<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span>></span>c<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span>></span>v<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span>></span>b<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span>></span>n<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span>></span>m<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3">样式实现</h1>
<blockquote>
<p>我们先清除所有元素的基本样式，给在外面的大盒子设置好样式，高度我们让里面的内容把他撑起来</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">  * &#123;
           box-<span class="hljs-attr">sizing</span>: border-box;
            list-<span class="hljs-attr">style</span>: none;
        &#125;

        <span class="hljs-comment">/* 大盒子 */</span>
        #app &#123;
            <span class="hljs-attr">position</span>: relative;

            <span class="hljs-attr">width</span>: 680px;
            <span class="hljs-attr">margin</span>: 13vh auto;
            <span class="hljs-attr">display</span>: flex;
            justify-<span class="hljs-attr">content</span>: center;
            <span class="hljs-attr">border</span>: 1px solid #ccc;
            border-<span class="hljs-attr">radius</span>: 10px;
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>在设置键盘的每一行的位置，我们这里使用外边距属性让无序列表的子元素距离左边都有距离，这样第一列初始就不对齐，后面每一列自然不对齐</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">   ul &#123;
            <span class="hljs-attr">padding</span>: <span class="hljs-number">0</span>;
        &#125;

        <span class="hljs-comment">/* 键盘每一列 */</span>
        ul li &#123;
            <span class="hljs-attr">display</span>: flex;
            <span class="hljs-attr">overflow</span>: hidden;
        &#125;

        ul <span class="hljs-attr">li</span>:nth-<span class="hljs-title function_">child</span>(<span class="hljs-params"><span class="hljs-number">2</span></span>) &#123;
            margin-<span class="hljs-attr">left</span>: 24px;
        &#125;

        ul <span class="hljs-attr">li</span>:nth-<span class="hljs-title function_">child</span>(<span class="hljs-params"><span class="hljs-number">3</span></span>) &#123;
            margin-<span class="hljs-attr">left</span>: 52px;
        &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>实现键帽的样式，我们这里给键帽里面的文字设置一个发光样式，由于初始是白光，所以看不到，只有当变换主题色的时候才可以看到</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">        <span class="hljs-comment">/* 键帽 */</span>
        ul li div &#123;
            <span class="hljs-attr">display</span>: flex;
            justify-<span class="hljs-attr">content</span>: center;
            align-<span class="hljs-attr">items</span>: center;
            <span class="hljs-attr">width</span>: 50px;
            <span class="hljs-attr">height</span>: 50px;
            text-<span class="hljs-attr">transform</span>: capitalize;
            <span class="hljs-attr">margin</span>: 8px;
            box-<span class="hljs-attr">shadow</span>: 0px 0px 3px 0px #ccc;
            border-<span class="hljs-attr">radius</span>: 10px;
            <span class="hljs-attr">cursor</span>: pointer;
            user-<span class="hljs-attr">select</span>: none;
            <span class="hljs-attr">transition</span>: background <span class="hljs-number">0.</span>05s;
            text-<span class="hljs-attr">shadow</span>: <span class="hljs-number">0</span> <span class="hljs-number">0</span> 10px #fff,
                <span class="hljs-number">0</span> <span class="hljs-number">0</span> 20px #fff,
                <span class="hljs-number">0</span> <span class="hljs-number">0</span> 30px #fff,
                <span class="hljs-number">0</span> <span class="hljs-number">0</span> 40px #00a67c,
                <span class="hljs-number">0</span> <span class="hljs-number">0</span> 70px #00a67c,
                <span class="hljs-number">0</span> <span class="hljs-number">0</span> 80px #00a67c,
                <span class="hljs-number">0</span> <span class="hljs-number">0</span> 100px #00a67c,
                <span class="hljs-number">0</span> <span class="hljs-number">0</span> 150px #00a67c;
        &#125;

        <span class="hljs-comment">/* 键帽滑过 */</span>
        ul li <span class="hljs-attr">div</span>:hover &#123;
            <span class="hljs-attr">background</span>: #eee;

        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a1b57244248475380a7df347ebd2298~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="企业微信截图_16625465856897.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>最后将Fn键样式写一下，在通过定位的方式定位到合适的位置即可</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">   <span class="hljs-comment">/* 按钮 */</span>
        #btn &#123;
            <span class="hljs-attr">position</span>: absolute;
            <span class="hljs-attr">bottom</span>: 4px;
            <span class="hljs-attr">right</span>: 20px;
            <span class="hljs-attr">margin</span>: 20px auto;
            <span class="hljs-attr">display</span>: flex;
            justify-<span class="hljs-attr">content</span>: center;
            align-<span class="hljs-attr">items</span>: center;
            <span class="hljs-attr">width</span>: 130px;
            <span class="hljs-attr">height</span>: 50px;
            user-<span class="hljs-attr">select</span>: none;
            <span class="hljs-attr">cursor</span>: pointer;
            border-<span class="hljs-attr">radius</span>: 10px;
            <span class="hljs-attr">background</span>: #eee;
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-4">主题色变换逻辑实现</h1>
<pre><code class="hljs language-js copyable" lang="js">           <span class="hljs-comment">// 获取Fn键</span>
        <span class="hljs-keyword">const</span> btn = <span class="hljs-variable language_">document</span>.<span class="hljs-title function_">getElementById</span>(<span class="hljs-string">'btn'</span>);
        <span class="hljs-comment">// 获取所有的键帽</span>
        <span class="hljs-keyword">const</span> keyupAll = <span class="hljs-variable language_">document</span>.<span class="hljs-title function_">querySelectorAll</span>(<span class="hljs-string">'ul li div'</span>);
        <span class="hljs-comment">// 给Fn键绑定点击事件</span>
        btn.<span class="hljs-property">onclick</span> = <span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) &#123;
            <span class="hljs-comment">// 随机获取3个0~255之间的数用于更换背景色</span>
            <span class="hljs-keyword">const</span> R = <span class="hljs-title class_">Math</span>.<span class="hljs-title function_">round</span>(<span class="hljs-title class_">Math</span>.<span class="hljs-title function_">random</span>() * <span class="hljs-number">255</span>);
            <span class="hljs-keyword">const</span> G = <span class="hljs-title class_">Math</span>.<span class="hljs-title function_">round</span>(<span class="hljs-title class_">Math</span>.<span class="hljs-title function_">random</span>() * <span class="hljs-number">255</span>);
            <span class="hljs-keyword">const</span> B = <span class="hljs-title class_">Math</span>.<span class="hljs-title function_">round</span>(<span class="hljs-title class_">Math</span>.<span class="hljs-title function_">random</span>() * <span class="hljs-number">255</span>);
          
            <span class="hljs-comment">// 把随机数添加到css的rgba属性中</span>
            <span class="hljs-keyword">let</span> rgba = <span class="hljs-string">`rgb(<span class="hljs-subst">$&#123;R&#125;</span>,<span class="hljs-subst">$&#123;G&#125;</span>,<span class="hljs-subst">$&#123;B&#125;</span>,<span class="hljs-subst">$&#123;<span class="hljs-number">0.5</span>&#125;</span>)`</span>
            <span class="hljs-comment">// 按键也需要用到背景色，更换主题按钮的背景色和普通的键帽需要有区别所以给出区别</span>
            <span class="hljs-variable language_">this</span>.<span class="hljs-property">style</span>.<span class="hljs-property">backgroundColor</span> = <span class="hljs-string">`rgb(<span class="hljs-subst">$&#123;R&#125;</span>,<span class="hljs-subst">$&#123;G&#125;</span>,<span class="hljs-subst">$&#123;R&#125;</span>,<span class="hljs-subst">$&#123;<span class="hljs-number">0.5</span>&#125;</span>)`</span>
            <span class="hljs-comment">// 循环每个键帽并赋值背景色</span>
            <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < keyupAll.<span class="hljs-property">length</span>; i++) &#123;
                keyupAll[i].<span class="hljs-property">style</span>.<span class="hljs-property">backgroundColor</span> = rgba
            &#125;
        &#125;
        <span class="hljs-comment">// 给键帽添加点击事件,当键帽点击弹出我们点击的按键内容</span>
        keyupAll.<span class="hljs-title function_">forEach</span>(<span class="hljs-keyword">function</span> (<span class="hljs-params">R</span>) &#123;
            R.<span class="hljs-property">onclick</span> = <span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) &#123;
                <span class="hljs-title function_">alert</span>(<span class="hljs-string">`您按下了<span class="hljs-subst">$&#123;<span class="hljs-variable language_">this</span>.innerText&#125;</span>键`</span>)
            &#125;
        &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>代码我放到码上掘金上了，感兴趣的可以看一看!</p>
</blockquote>
<p><span href="https://code.juejin.cn/pen/7140586021262983181" target="_blank" class="code-editor-container"><iframe class="code-editor-frame" data-code="code-editor-element" data-code-id="7140586021262983181" data-src="https://code.juejin.cn/pen/7140586021262983181" style="display: none" loading="lazy"></iframe></span></p>
<blockquote>
<p>坚持努力，无惧未来！</p>
</blockquote></div>  
</div>
            
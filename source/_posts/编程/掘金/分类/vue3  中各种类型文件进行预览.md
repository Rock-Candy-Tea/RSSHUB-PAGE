
---
title: 'vue3  中各种类型文件进行预览'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8174'
author: 掘金
comments: false
date: Wed, 01 Sep 2021 01:15:05 GMT
thumbnail: 'https://picsum.photos/400/300?random=8174'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>摸着石头过河的滋味不好受啊，听说大厂的大佬们都在忙着用vue3在升级项目，我也没事凑一波热闹。身处某小厂还是不甘于折腾。新做一个项目，直接上vue3 ，头脑发热 ，可能有人不计后果，但是跌跌撞撞还是基本搞完了，那记录一下吧</p>
</blockquote>
<p>今天说一下开发过程中的某一个功能吧！反正耗费不少时间，先说说功能需求吧：在上传文件之后的文件列表中能够点击进行预览，包含文件媒体类型包括 图片 、word excel等文档文件、pdf、视频、音频 的预览针对pc端</p>
<h4 data-id="heading-0">1.office文档类型的预览</h4>
<p>首先看到的是word excel 等文档文件的预览，针对改问题开始还是网上搜寻了一些方法，毕竟我这经验甚少，有人推荐a标签直接下载预览，显然不符合我们预期，有人推荐excel 使用sheetjs 但是我们word 也需要另找他法，最终我还是确定了使用微软的在线预览，使用iframe作为载体进行</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><iframe  frameborder=<span class="hljs-string">"0"</span> 
:src=<span class="hljs-string">"'https://view.officeapps.live.com/op/view.aspx?src=' + fileUrl"</span> width=<span class="hljs-string">'100%'</span>>
</iframe>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要考虑的是我当时element-plus的dialog 弹框里，iframe不能很好的撑开父元素所以又填充一些代码。并且加载过程比较慢，由于时间原因就没有考虑进行其他方法的尝试</p>
<h4 data-id="heading-1">2.pdf类型的预览</h4>
<p>对于这种pdf的预览，感觉好解决啊，使用原来使用过的 npm install pdfjs-dist ，开搞就完了，万万没想到我这个目前还没有支持vue3 所以理所当然的上来一跑就报错也是理所应当的，果断百度啊，百度告诉我说，这个pdfjs-dist vue3 不支持呐还，换个方法吧，我***，用你说 我想找解决办法，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fmozilla.github.io%2Fpdf.js%2Fgetting_started%2F%23download" target="_blank" rel="nofollow noopener noreferrer" title="https://mozilla.github.io/pdf.js/getting_started/#download" ref="nofollow noopener noreferrer">主角来了</a>下载之后将build和web文件夹放在我们的public文件下 做一下引用，注意自己的地址是不是对，我放在了一个embed 里</p>
<pre><code class="hljs language-js copyable" lang="js">  data.pdfUrl = <span class="hljs-string">'./pdf/web/viewer.html?file='</span>+type;  <span class="hljs-comment">// 线上预览</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"> <embed  :src=<span class="hljs-string">"pdfUrl"</span> style=<span class="hljs-string">"width: 100%; "</span>/>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">3. 图片类型</h4>
<p>我觉这种类型 ，我们都不必多说，直接上代码就可以了，处理一下url</p>
<pre><code class="hljs language-js copyable" lang="js"><div v-<span class="hljs-keyword">if</span>=<span class="hljs-string">"showImg == true"</span> <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"dialog-body-content-base-style"</span>>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">el-image</span>
        <span class="hljs-attr">class</span>=<span class="hljs-string">"image-preview"</span>
        <span class="hljs-attr">:src</span>=<span class="hljs-string">"imgUrl"</span>
        /></span></span>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">4.视频类型</h4>
<p>对于视频类型本来是想直接使用 video元素直接放里的但是我是一个有追求的程序猿，追求自己的理想，没事就是折腾么，开始使用vue-video-palyer 进行视频预览，但是就是天不遂愿，完vue3 中报错 ，说白了又来了宝贝，没支持vue3 呗？ 没事我习惯了，推荐大家用一波vue-vam-video</p>
<pre><code class="hljs language-js copyable" lang="js">npm install vue-vam-video -s
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> VamVideo <span class="hljs-keyword">from</span> <span class="hljs-string">"vue-vam-video"</span>;
components: &#123;
    VamVideo,
&#125;,
<span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params">props,context</span>)</span> &#123;
    <span class="hljs-keyword">const</span> data = reactive(&#123;
        <span class="hljs-attr">videoOption</span>: &#123;
            <span class="hljs-attr">properties</span>: &#123;
                <span class="hljs-attr">poster</span>: <span class="hljs-string">''</span>,
                <span class="hljs-attr">src</span>:<span class="hljs-string">""</span>,
                <span class="hljs-attr">preload</span>: <span class="hljs-string">"auto"</span>,
                <span class="hljs-comment">// loop: "loop",</span>
                <span class="hljs-comment">// autoplay:"autoplay",</span>
                <span class="hljs-comment">// muted:true</span>
            &#125;,
            <span class="hljs-attr">videoStyle</span>: &#123;
                <span class="hljs-attr">width</span>: <span class="hljs-string">"100%"</span>,
                <span class="hljs-comment">// height: "600px",</span>
            &#125;,
            <span class="hljs-attr">controlsConfig</span>: &#123;
                <span class="hljs-attr">fullScreenTit</span>:<span class="hljs-string">"全屏"</span>,
                <span class="hljs-attr">EscfullScreenTit</span>:<span class="hljs-string">"退出全屏"</span>,
                <span class="hljs-attr">speedTit</span>:<span class="hljs-string">"倍速"</span>,
                <span class="hljs-attr">yinliangTit</span>:<span class="hljs-string">"音量"</span>,
                <span class="hljs-attr">jingyinTit</span>:<span class="hljs-string">"静音"</span>,
                <span class="hljs-attr">playTit</span>:<span class="hljs-string">"播放"</span>,
                <span class="hljs-attr">pauseTit</span>:<span class="hljs-string">"暂停"</span>,
                <span class="hljs-attr">fullScreen</span>:<span class="hljs-literal">true</span>,
                <span class="hljs-attr">speed</span>:<span class="hljs-literal">true</span>,
                <span class="hljs-attr">listen</span>:<span class="hljs-literal">true</span>
            &#125;
        &#125;,
    &#125;)
&#125;     
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><vam-video
    :properties=<span class="hljs-string">"videoOption.properties"</span>
    :videoStyle=<span class="hljs-string">"videoOption.videoStyle"</span>
    :controlsConfig=<span class="hljs-string">"videoOption.controlsConfig"</span>
    @play=<span class="hljs-string">"playVideo"</span>
    @canplay=<span class="hljs-string">"canplayVideo"</span>
    @pause=<span class="hljs-string">"pauseVideo"</span>
></vam-video>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-4">5. 音频类型</h5>
<p>吃了上边的亏，终于还是决定使用audio 这个标签了，直接使用就完了。</p>
<pre><code class="hljs language-js copyable" lang="js"><audio :src=<span class="hljs-string">"musicUrl"</span> controls></audio>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>综上建议大家考虑周全 ，像大厂的大佬们有自己的组件库，丝毫不担心，但是小厂的我们还是谨慎一点。 希望vue更多的组件库、功能库更加完善，毕竟站在巨人肩膀上是方便的。没事多研究源码 。。。。。。</p></div>  
</div>
            
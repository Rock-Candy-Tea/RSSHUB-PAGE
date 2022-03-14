
---
title: 'flex常用布局'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/14011985-90f5754a8538a2ff.png'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/14011985-90f5754a8538a2ff.png'
---

<div>   
<h3>Sticky Footer</h3>
<p>当页面内容高度小于可视区域高度时，footer 吸附在底部；当页面内容高度大于可视区域高度时，footer 被撑开排在 content 下方；</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="576" data-height="768"><img data-original-src="//upload-images.jianshu.io/upload_images/14011985-90f5754a8538a2ff.png" data-original-width="576" data-original-height="768" data-original-format="image/png" data-original-filesize="4597" src="https://upload-images.jianshu.io/upload_images/14011985-90f5754a8538a2ff.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">360截图16240127357130.png</div>
</div>
<pre><code class="html"><style>
        body &#123;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
        &#125;
        header&#123;
            background: rgba(0,0,0,.1);
        &#125;
        article &#123;
            flex: auto;
        &#125;
        footer&#123;
            background: rgba(0,0,0,.1);
            height: 50px;
        &#125;
    </style>
    
    <header>HEADER</header>
    <article>CONTENT</article>
    <footer>FOOTER</footer>
</code></pre>
<h3>Fixed-Width Sidebar</h3>
<p>在上-中-下布局的基础上，加了左侧定宽 sidebar。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="576" data-height="767"><img data-original-src="//upload-images.jianshu.io/upload_images/14011985-da2d733473340f49.png" data-original-width="576" data-original-height="767" data-original-format="image/png" data-original-filesize="4912" src="https://upload-images.jianshu.io/upload_images/14011985-da2d733473340f49.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">2.png</div>
</div>
<pre><code class="html"><style>
        body &#123;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
        &#125;

        .content &#123;
            flex: auto;
            display: flex;
        &#125;
        header&#123;
            background: rgba(0,0,0,.1);
        &#125;
        aside&#123;
            background: rgba(0,0,0,.2);
        &#125;
        article &#123;
            flex: auto;
            /* height: 1400px; */
        &#125;
        footer&#123;
            background: rgba(0,0,0,.1);
        &#125;
    </style>

    <header>HEADER</header>
    <div class="content">
        <aside>ASIDE</aside>
        <article>CONTENT</article>
    </div>
    <footer>FOOTER</footer>
</code></pre>
<h3>Sidebar</h3>
<p>左边是定宽 sidebar，右边是上-中-下布局。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="574" data-height="768"><img data-original-src="//upload-images.jianshu.io/upload_images/14011985-60df278251c7ca60.png" data-original-width="574" data-original-height="768" data-original-format="image/png" data-original-filesize="7305" src="https://upload-images.jianshu.io/upload_images/14011985-60df278251c7ca60.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">3.png</div>
</div>
<pre><code class="html">     <style>
        * &#123;
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        &#125;

        body &#123;
            min-height: 100vh;
            display: flex;
        &#125;

        aside &#123;
            flex: none;
            width: 200px;
            background: rgba(0, 0, 0, .2);
        &#125;

        .content &#123;
            flex: auto;
            display: flex;
            flex-direction: column;
        &#125;

        .content article &#123;
            flex: auto;
            background: rgba(0, 0, 0, .1);
        &#125;
    </style>

    <aside>ASIDE</aside>
    <div class="content">
        <header>HEADER</header>
        <article>CONTENT</article>
        <footer>FOOTER</footer>
    </div>
</code></pre>
<h3>Sticky Sidebar</h3>
<p>左侧 sidebar 固定在左侧且与视窗同高，当内容超出视窗高度时，在 sidebar 内部出现滚动条。左右两侧滚动条互相独立。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="576" data-height="765"><img data-original-src="//upload-images.jianshu.io/upload_images/14011985-0c61e73709804e8c.png" data-original-width="576" data-original-height="765" data-original-format="image/png" data-original-filesize="7848" src="https://upload-images.jianshu.io/upload_images/14011985-0c61e73709804e8c.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">4.png</div>
</div>
<pre><code class="html">    <style>
        * &#123;
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        &#125;

        body &#123;
            height: 100vh;
            display: flex;
        &#125;

        aside &#123;
            flex: none;
            width: 200px;
            overflow-y: auto;
            display: block;
            background: rgba(0, 0, 0, .2);
        &#125;
        aside p&#123;
            height: 350px;
        &#125;
        .content &#123;
            flex: auto;
            display: flex;
            flex-direction: column;
            overflow-y: auto;
        &#125;

        .content article &#123;
            flex: auto;
            background: rgba(0, 0, 0, .1);
        &#125;
    </style>

    <aside>
        ASIDE
        <p>item</p>
        <p>item</p>
        <p>item</p>
    </aside>
    <div class="content">
        <header>HEADER</header>
        <article>CONTENT</article>
        <footer>FOOTER</footer>
    </div>
</code></pre>
<h3>flex属性</h3>
<p>flex 是 flex-grow、flex-shrink、flex-basis的缩写。 flex 的默认值是 0 1 auto。</p>
<ol>
<li>flex-grow -----用来“瓜分”父项的“剩余空间”。</li>
</ol>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1200" data-height="661"><img data-original-src="//upload-images.jianshu.io/upload_images/14011985-8a23cfbf9b151954.jpg" data-original-width="1200" data-original-height="661" data-original-format="image/jpeg" data-original-filesize="45125" src="https://upload-images.jianshu.io/upload_images/14011985-8a23cfbf9b151954.jpg" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">12904618-3e41b8713610e6e8_看图王.web.jpg</div>
</div>
<p>容器的宽度为400px, 子项1的占用的基础空间(flex-basis)为50px，子项2占用的基础空间是70px，子项3占用基础空间是100px，剩余空间为 400-50-70-100 = 180px。</p>
<p>其中子项1的flex-grow: 0(未设置默认为0)， 子项2flex-grow: 2，子项3flex-grow: 1，剩余空间分成3份，子项2占2份(120px)，子项3占1份(60px)。</p>
<p>所以 子项1真实的占用空间为: 50+0 = 50px， 子项2真实的占用空间为: 70+120 = 190px， 子项3真实的占用空间为: 100+60 = 160px。</p>
<ol start="2">
<li>flex-shrink ----用来“吸收”超出的空间</li>
</ol>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1200" data-height="664"><img data-original-src="//upload-images.jianshu.io/upload_images/14011985-5cfc75fd605e349e.jpg" data-original-width="1200" data-original-height="664" data-original-format="image/jpeg" data-original-filesize="47396" src="https://upload-images.jianshu.io/upload_images/14011985-5cfc75fd605e349e.jpg" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">12904618-ed1819e7b3415dec_看图王.web.jpg</div>
</div>
<p>容器的宽度为400px, 子项1的占用的基准空间(flex-basis)为250px，子项2占用的基准空间是150px，子项3占用基准空间是100px，总基准空间为 250+150+100=500px。</p>
<p>容器放不下，多出来的空间需要被每个子项根据自己设置的flex-shrink 进行吸收。 子项1的flex-shrink: 1(未设置默认为1)， 子项2 flex-shrink: 2，子项3 flex-shrink: 2。</p>
<p>子项1需要吸收的的空间为 (250<em>1)/(250</em>1+150<em>2+100</em>2) * 100 = 33.33px，子项1真实的空间为 250-33.33 = 216.67px。</p>
<p>同理子项2吸收的空间为(150<em>2)/(250</em>1+150<em>2+100</em>2) * 100=40px，子项2真实空间为 150-40 = 110px。</p>
<p>子项3吸收的空间为(100<em>2)/(250</em>1+150<em>2+100</em>2) * 100 = 26.67px，真实的空间为100-26.67=73.33px。</p>
<ol start="3">
<li>flex-basis</li>
</ol>
<p>flex-basis 用于设置子项的占用空间。如果设置了值，则子项占用的空间为设置的值；如果没设置或者为 auto，那子项的空间为width/height 的值。</p>
<h4>当 flex 取值为 none，则计算值为 0 0 auto</h4>
<pre><code class="css">.item &#123;flex: none;&#125;
.item &#123;
    flex-grow: 0;
    flex-shrink: 0;
    flex-basis: auto;
&#125;
</code></pre>
<h4>当 flex 取值为 auto，则计算值为 1 1 auto</h4>
<pre><code class="css">.item &#123;flex: auto;&#125;
.item &#123;
    flex-grow: 1;
    flex-shrink: 1;
    flex-basis: auto;
&#125;
</code></pre>
<h4>当 flex 取值为一个非负数字，则该数字为 flex-grow 值，flex-shrink 取 1，flex-basis 取 0%</h4>
<pre><code class="css">.item &#123;flex: 1;&#125;
.item &#123;
    flex-grow: 1;
    flex-shrink: 1;
    flex-basis: 0%;
&#125;

</code></pre>
<h3>扩展：</h3>
<h4>基本网格布局</h4>
<p>最简单的网格布局，就是平均分布。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="800" data-height="88"><img data-original-src="//upload-images.jianshu.io/upload_images/14011985-1f653a56e12cf3ee.png" data-original-width="800" data-original-height="88" data-original-format="image/png" data-original-filesize="5897" src="https://upload-images.jianshu.io/upload_images/14011985-1f653a56e12cf3ee.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">aIVfIn.png</div>
</div>
<p>这里最关键的就是flex:1使得各个子元素可以等比伸缩</p>
<pre><code class="html"><div class="Grid">
    <div class="Grid-cell">1/2</div>
    <div class="Grid-cell">1/2</div>
  </div>
  <div class="Grid">
    <div class="Grid-cell">1/3</div>
    <div class="Grid-cell">1/3</div>
    <div class="Grid-cell">1/3</div>
  </div>

<style>
.Grid &#123;
  display: flex;
&#125;

.Grid-cell &#123;
  flex: 1;
  background: #eee;
  margin: 10px;
&#125;
</style>
</code></pre>
<h4>百分比布局</h4>
<p>某个网格的宽度为固定的百分比，其余网格平均分配剩余的空间。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="800" data-height="82"><img data-original-src="//upload-images.jianshu.io/upload_images/14011985-0578c4a4a903144f.png" data-original-width="800" data-original-height="82" data-original-format="image/png" data-original-filesize="7066" src="https://upload-images.jianshu.io/upload_images/14011985-0578c4a4a903144f.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">mQF3i2.png</div>
</div>
<p>这里最关键的是通过flex的第三个属性，也就是flex-basis来定义元素占据的空间。</p>
<pre><code class="html"><div class="Grid">
    <div class="Grid-cell col2">50%</div>
    <div class="Grid-cell">auto</div>
    <div class="Grid-cell ">auto</div>
</div>
<div class="Grid">
    <div class="Grid-cell">auto</div>
    <div class="Grid-cell col2">50%</div>
    <div class="Grid-cell clo3">1/3</div>
</div>

<style>
.col2 &#123;
  flex: 0 0 50%;
&#125;
.col3 &#123;
  flex: 0 0 33.3%;
&#125;
</style>
</code></pre>
  
</div>
            
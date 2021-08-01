
---
title: '自适应布局之初识flex（一）｜8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3cfdef3dbf5445fdae6a8564a7ac33b2~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 31 Jul 2021 17:58:23 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3cfdef3dbf5445fdae6a8564a7ac33b2~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">自适应布局之初识flex</h1>
<p>说起自适应、恐怕对于flex那是无人不知无人不晓了吧（如果你真的没听过....emmm 大哥我错了），下面将结合一些例子来简单描述下flex</p>
<h2 data-id="heading-1">初识flex</h2>
<h3 data-id="heading-2">案例一</h3>
<ul>
<li>三行代码简单实现下子元素垂直、水平居中
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3cfdef3dbf5445fdae6a8564a7ac33b2~tplv-k3u1fbpfcp-watermark.image" alt="image-20210727232159208.png" loading="lazy" referrerpolicy="no-referrer"></li>
</ul>
<pre><code class="copyable"> .father &#123;
    // 三行水平垂直居中
    display: flex;
    align-items: center;
    justify-content: center;
     
    width: 300px;
    height: 300px;
    background-color: pink;     // pink老师，yyds！！！
 &#125;
​
<div class="father">
    <span class=“son”>我是子元素</span>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">案例二</h3>
<ul>
<li>
<p>上下 固定高度，中间自适应</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/806de8fa795e42aeaea8ec68f44c980b~tplv-k3u1fbpfcp-watermark.image" alt="image-20210728205120614.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">* &#123;
    margin: 0;
    padding: 0;
&#125;
body &#123;
    display: flex;
    flex-direction: column;
    width: 100vw;
    min-height: 100vh;
    background-color: pink;
&#125;
// 三种写法在当前的情况下一样的效果，其实发生作用的是 flex-grow 属性
main &#123;
    /* flex: 1; */
    /* flex: auto; */
    flex-grow: 1;
&#125;
footer,
header &#123;
    background-color: skyblue;
    height: 50px;
&#125;
​
<body>
    <header>header</header>
    <main>main</main>
    <footer>footer</footer>
</body>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-4">案例三</h3>
<ul>
<li>
<p>左边侧边栏(包含滚动条)，右边上下 固定高度，中间自适应</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a34c067887e44dda669f0f0d7be75c2~tplv-k3u1fbpfcp-watermark.image" alt="image-20210728210813837.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable"> * &#123;
        margin: 0;
        padding: 0;
    &#125;
    body &#123;
        display: flex;
        flex-direction: column;
        width: 100vw;
        min-height: 100vh;
        background-color: pink;
    &#125;
    // 三种写法在当前的情况下一样的效果，其实发生作用的是 flex-grow 属性
    main &#123;
        /* flex: 1; */
        /* flex: auto; */
        flex-grow: 1;
    &#125;
    footer,
    header &#123;
        background-color: skyblue;
        height: 50px;
    &#125;

    ----------------新增样式-----------------------
    aside &#123;
        width: 100px;
        height: 100vh;
        background-color: greenyellow;
        flex: none;
        overflow-y: auto;
    &#125;
    li &#123;
        height: 200px;
    &#125;
    .main-container &#123;
        flex: 1;
        display: flex;
        flex-direction: column;
    &#125;
     ----------------------------------------------
    <body>
        <aside>
            <ul>
                <li>item</li>
                <li>item</li>
                <li>item</li>
                <li>item</li>
                <li>item</li>
                <li>item</li>
                <li>item</li>
                <li>item</li>
            </ul>
        </aside>
        <div class="main-container">
            <header>header</header>
            <main>main</main>
            <footer>footer</footer>
        </div>
    </body>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h2 data-id="heading-5">定义</h2>
<p>先说说flex定义、简单来说flex包含<strong>两部分</strong>，一部分是<strong>容器（父容器）</strong> 、另一部分是<strong>项目（子项）</strong> ，就像下面的结构一样，那明白了么？就是一个容器包含了几个子项目，这两部分可以通过flex的一些属性进行<strong>控制项目（子项）的位置</strong>、<strong>对齐方式</strong>、<strong>响应式的变化方式</strong></p>
<pre><code class="copyable"><div class="father" style="display: flex">
    <span class=“son”>我是子元素</span>
    ......
    <span class=“son”>我是子元素</span>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有了<a href="https://juejin.cn/%E5%88%9D%E8%AF%86flex" target="_blank" title="/%E5%88%9D%E8%AF%86flex">如上</a>的简单展示，那么开始学习一下flex的具体属性值，其实并不复杂，只要多用即可掌握，记住<strong>容器（父元素）6个属性</strong>、<strong>项目（子项）6个属性值</strong>，都是6个，66大顺，很好记对吧。</p>
<h3 data-id="heading-6">容器（父元素）</h3>
<ul>
<li><strong>flex-direction</strong> （主轴方向）</li>
<li>flex-wrap （子元素超出是否换行）</li>
<li>flex-flow （上面两个属性的综合体，可以只写这个，代替上面两个，就像字体的font属性一样）</li>
<li><strong>justify-content</strong> （定义子项在<strong>主轴上的对齐方式</strong>）</li>
<li><strong>align-items</strong> （定义子项在<strong>交叉轴上的对齐方式</strong>）</li>
<li>align-content （定义<strong>多根</strong>轴线时的<strong>轴线对齐方式</strong>，只有一根轴线时，设置无效）</li>
</ul>
<p>以上6个属性，一般常用的我加粗了，其他的少用</p>
<h3 data-id="heading-7">项目（子元素）</h3>
<ul>
<li>order （定义子元素的排序，<strong>数值越小越靠前</strong>）</li>
<li>flex-grow （定义子元素在容器<strong>还有剩余空间时</strong>的放大比例，默认为0，即不放大）</li>
<li>flex-shrink（与grow相反，定义子元素在容器<strong>没有剩余空间时</strong>的缩小比例，默认为1，即所有子元素缩小一样）</li>
<li>flex-basis （定义子项在<strong>主轴上的对齐方式</strong>）</li>
<li><strong>flex</strong> （定义子项在<strong>交叉轴上的对齐方式</strong>）</li>
<li>align-self （允许当前项设置 <strong>align-items</strong> 并覆盖父元素的设置 ）</li>
</ul>
<h2 data-id="heading-8">本章小结</h2>
<p>好嘞，这章节主要就是有个大概的印象，flex能做什么，flex大概有哪些属性，下一章节讲详细讲述 <strong>66大顺</strong> 的属性含义。如有不对之处欢迎评论区指正，谢谢~</p></div>  
</div>
            
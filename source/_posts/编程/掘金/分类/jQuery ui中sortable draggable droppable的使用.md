
---
title: 'jQuery ui中sortable draggable droppable的使用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96803653736d4ab58123433da25f3473~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 26 May 2021 18:46:22 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96803653736d4ab58123433da25f3473~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>大家好，我是前端队长Daotin，想要获取更多前端精彩内容，关注我，解锁前端成长新姿势。</p>
<p>以下正文：</p>
<p>最近工作中用到了jQuery UI中排序和拖拽功能，花了大概一天的时间，搞清楚了大概的参数配置，以及遇到的一些问题，总结如下。</p>
<h2 data-id="heading-0">sortable</h2>
<p>简单的配置如下：</p>
<pre><code class="hljs language-js copyable" lang="js">$(<span class="hljs-string">'#subs-box'</span>).sortable(&#123;
    <span class="hljs-attr">axis</span>: <span class="hljs-string">'y'</span>,
    <span class="hljs-attr">cursor</span>: <span class="hljs-string">'ns-resize'</span>,
    <span class="hljs-attr">placeholder</span>: <span class="hljs-string">"ui-state-highlight"</span>, <span class="hljs-comment">// 排序过程中占位符的class样式设置</span>
    <span class="hljs-attr">forcePlaceholderSize</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 强迫占位符有一个尺寸大小。</span>
    <span class="hljs-attr">handle</span>:<span class="hljs-string">'.sort-at'</span>, <span class="hljs-comment">// 在对象内指定的元素上开始拖动，而不是整个元素都可以拖动</span>
    <span class="hljs-attr">distance</span>: <span class="hljs-number">10</span>,
    <span class="hljs-attr">opacity</span>: <span class="hljs-number">0.8</span>,
    containment：<span class="hljs-string">'parent'</span>, <span class="hljs-comment">// 元素可以拖动排序的范围</span>
    <span class="hljs-comment">// helper: 'clone', // 是否clone一个元素进行拖动</span>
    <span class="hljs-attr">items</span>: <span class="hljs-string">'.subject'</span>,  <span class="hljs-comment">// 指定哪些元素可以排序</span>
    <span class="hljs-attr">stop</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">e, ui</span>) </span>&#123;
        <span class="hljs-comment">// 排序后元素的顺序（前提每个元素都需要有id属性）</span>
        <span class="hljs-keyword">let</span> newSubArr = $(<span class="hljs-string">"#subs-box"</span>).sortable(<span class="hljs-string">'toArray'</span>); 
        <span class="hljs-built_in">console</span>.log(newSubArr);
    &#125;,
&#125;).disableSelection(); <span class="hljs-comment">// 拖动时禁止选中元素</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>还有一些排序时候的事件和方法，都在参考链接的文档里面。</p>
<h2 data-id="heading-1">draggable</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">dragInit</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">let</span> me = <span class="hljs-built_in">this</span>;
    <span class="hljs-keyword">let</span> selector = <span class="hljs-string">'.ptype-'</span>+me.selectedSubType;

    <span class="hljs-comment">// 题目拖动</span>
    $(<span class="hljs-string">'#subs-box .subject'</span>).draggable(&#123;
        <span class="hljs-comment">// appendTo: ".ptype-item.radio", // 当进行拖动时，拖动组件助手应该被添加到的元素。</span>
        <span class="hljs-comment">// connectToSortable: "#subs-box", // 允许draggable被拖拽到指定的sortables中。</span>

        <span class="hljs-comment">// 拖动时使用的是clone的元素。如果值设置为"clone", 那么该元素将会被复制，并且被复制的元素将被拖动。</span>
        <span class="hljs-comment">// 之所以不使用 helper: 'clone', 是因为clone的元素没有样式，所以我们需要自定义样式，所以使用了自定义函数。</span>
        <span class="hljs-attr">helper</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
            <span class="hljs-keyword">let</span> helper = $(<span class="hljs-built_in">this</span>).clone();
            helper.css(&#123;<span class="hljs-string">'width'</span>: $(<span class="hljs-built_in">this</span>).width(), <span class="hljs-string">'background'</span>: <span class="hljs-string">'#fff'</span>&#125;); <span class="hljs-comment">// 设置clone元素的样式</span>
            <span class="hljs-keyword">return</span> helper;
        &#125;,
        <span class="hljs-attr">handle</span>: <span class="hljs-string">".drag-at"</span>, <span class="hljs-comment">// 指定在特定的元素上触发鼠标按下事件时，才可以拖动。</span>
        <span class="hljs-attr">cursor</span>: <span class="hljs-string">'move'</span>,
        <span class="hljs-comment">// containment: '.sub-box', // 可以限制draggable只能在指定的元素或区域的边界以内进行拖动。</span>
        <span class="hljs-attr">revert</span>: <span class="hljs-string">'invalid'</span>, <span class="hljs-comment">// 如果设置为true，当拖动停止时，元素位置将被重置。</span>
        <span class="hljs-attr">revertDuration</span>: <span class="hljs-number">200</span>,
        <span class="hljs-attr">distance</span>: <span class="hljs-number">10</span>,
        <span class="hljs-attr">opacity</span>: <span class="hljs-number">0.8</span>,
        <span class="hljs-attr">zIndex</span>: <span class="hljs-number">10000</span>,
        <span class="hljs-attr">refreshPositions</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 所有的可拖动位置在每次鼠标移动时都会被计算。（设置该值使得drop的位置更加精确）</span>
        <span class="hljs-function"><span class="hljs-title">start</span>(<span class="hljs-params">event, ui</span>)</span> &#123;
            $(selector).addClass(<span class="hljs-string">'allow'</span>); <span class="hljs-comment">// 元素拖拽的时候，设置可放置元素的样式，示意你可以拖拽到那里去</span>
            <span class="hljs-comment">// 开始拖拽的时候，初始化drop</span>
            me.$nextTick(<span class="hljs-function">()=></span>&#123;
                me.dropInit();
            &#125;);
        &#125;,
        <span class="hljs-function"><span class="hljs-title">stop</span>(<span class="hljs-params">event, ui</span>)</span> &#123;
            $(selector).removeClass(<span class="hljs-string">'allow'</span>);
            <span class="hljs-comment">// 拖拽停止的时候，销毁drop函数。</span>
            me.dropDestory();
        &#125;
    &#125;).disableSelection();

&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意事项：</p>
<p><strong>每次dropInit函数初始化后，如果需要再次初始化，需要先销毁之前的放置对象</strong>。否则第一次初始化后，比如某个地方A可以放置拖拽的元素，但是第二次初始化后，地方A就不可以放置了。然而实际上，如果你不把第一次初始化的dropInit函数销毁掉，地方A在第二次初始化后还是可以放置的。所以需要在拖拽停止的时候，销毁上一次的dropInit对象。</p>
</blockquote>
<h2 data-id="heading-2">dropable</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">dropInit</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">let</span> me = <span class="hljs-built_in">this</span>;
    <span class="hljs-comment">// 题目放置（设置题目根据不同类型可以放置不同的分页）</span>
    <span class="hljs-comment">// selector是可变的，也就是每次可拖拽元素可放置的元素是不同的。所以需要每次拖拽后清除之前dropInit对象。</span>
    <span class="hljs-keyword">let</span> selector = <span class="hljs-string">'.ptype-'</span>+me.selectedSubType;

    $(selector).droppable(&#123;
        <span class="hljs-comment">// accept: selector,</span>
        <span class="hljs-comment">// accept: function(d) &#123;</span>
        <span class="hljs-comment">//     if($(this).hasClass('ptype'+me.selectedSubType))&#123;</span>
        <span class="hljs-comment">//         console.log('d>>>>>>',$(this)[0]);</span>
        <span class="hljs-comment">//         return true;</span>
        <span class="hljs-comment">//     &#125;</span>
        <span class="hljs-comment">// &#125;,</span>
        <span class="hljs-comment">// hoverClass: "drop-hover",</span>
        <span class="hljs-attr">tolerance</span>: <span class="hljs-string">'pointer'</span>, <span class="hljs-comment">// 指定使用那种模式来测试一个拖动(draggable)元素"经过"一个放置（droppable）对象</span>
        <span class="hljs-attr">drop</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"> event, ui </span>) </span>&#123;
            <span class="hljs-comment">// $(this) 填充到的元素</span>
            <span class="hljs-comment">// ui.draggable.context 填充的元素</span>
            <span class="hljs-keyword">let</span> dragId = $(ui.draggable.context).attr(<span class="hljs-string">'id'</span>);
            <span class="hljs-keyword">let</span> dropId = $(<span class="hljs-built_in">this</span>).attr(<span class="hljs-string">'id'</span>);

            <span class="hljs-comment">// 移动到新的分页</span>
            <span class="hljs-keyword">if</span>(dropId === <span class="hljs-string">'newpage'</span>) &#123;
                me.moveAddPage(dragId);
            &#125; <span class="hljs-keyword">else</span> &#123; <span class="hljs-comment">// 移动题目到另一个分页</span>
                <span class="hljs-keyword">if</span>(dropId === me.selectedPage.id) &#123; <span class="hljs-comment">// 移动到自己的分组，不做处理</span>

                &#125; <span class="hljs-keyword">else</span> &#123;
                    <span class="hljs-keyword">let</span> index = me.selectedPage.subs.indexOf(dragId);
                    <span class="hljs-keyword">if</span>(index > -<span class="hljs-number">1</span>) &#123;
                        me.selectedPage.subs.splice(index, <span class="hljs-number">1</span>);

                        me.pages.forEach(<span class="hljs-function"><span class="hljs-params">page</span>=></span>&#123;
                            <span class="hljs-keyword">if</span>(page.id === dropId) &#123;
                                page.subs.push(dragId);
                            &#125;
                        &#125;);

                        me.$openNotice(<span class="hljs-string">'移动成功'</span>);

                        <span class="hljs-comment">// 其他操作...</span>
                    &#125;
                &#125;
            &#125;

            $(<span class="hljs-built_in">this</span>).removeClass(<span class="hljs-string">'allow-hover'</span>);
        &#125;,
        <span class="hljs-function"><span class="hljs-title">over</span>(<span class="hljs-params">event, ui</span>)</span> &#123;
            $(<span class="hljs-built_in">this</span>).addClass(<span class="hljs-string">'allow-hover'</span>); <span class="hljs-comment">// 当拖拽元素进入可放元素时，可放置元素本身的样式</span>
        &#125;,
        <span class="hljs-function"><span class="hljs-title">out</span>(<span class="hljs-params"></span>)</span> &#123;
            $(<span class="hljs-built_in">this</span>).removeClass(<span class="hljs-string">'allow-hover'</span>); <span class="hljs-comment">// 设置拖拽元素离开可放元素时，清除可放置元素本身的样式</span>
        &#125;
    &#125;);
&#125;,
<span class="hljs-function"><span class="hljs-title">dropDestory</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">let</span> selector = <span class="hljs-string">'.ptype-'</span>+me.selectedSubType;
    $(selector).droppable(<span class="hljs-string">"destroy"</span>);
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">参考链接</h2>
<ul>
<li><a href="https://www.html.cn/jquery-ui-api/sortable/" target="_blank" rel="nofollow noopener noreferrer">www.html.cn/jquery-ui-a…</a></li>
<li><a href="https://www.html.cn/jquery-ui-api/draggable/" target="_blank" rel="nofollow noopener noreferrer">www.html.cn/jquery-ui-a…</a></li>
<li><a href="https://www.html.cn/jquery-ui-api/droppable" target="_blank" rel="nofollow noopener noreferrer">www.html.cn/jquery-ui-a…</a></li>
</ul>
<p>（完）</p>
<blockquote>
<p><strong>最近热门文章：</strong></p>
<ul>
<li><a href="https://juejin.cn/post/6963071339108237319" target="_blank">图片瀑布流，就是如此简单（so easy）</a></li>
<li><a href="https://juejin.cn/post/6961968236837470216" target="_blank">梳理ajax跨域常用4种解决方案（简单易懂）</a></li>
<li><a href="https://juejin.cn/post/6961226664869101605" target="_blank">Vue.js命名风格指南（易记版）</a></li>
</ul>
</blockquote>
<hr>
<p>想看更多精彩内容，关注我获取更多前端技术与个人成长相关内容，我相信有趣的人终会相遇！</p>
<p>听说点赞的人，一个月后都会运气爆棚，升职加薪哦~</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96803653736d4ab58123433da25f3473~tplv-k3u1fbpfcp-watermark.image" alt="微信图片_20210427113225.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            
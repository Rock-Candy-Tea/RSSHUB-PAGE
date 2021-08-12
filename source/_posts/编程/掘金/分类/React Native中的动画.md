
---
title: 'React Native中的动画'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=987'
author: 掘金
comments: false
date: Wed, 11 Aug 2021 18:05:30 GMT
thumbnail: 'https://picsum.photos/400/300?random=987'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第12天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831?utm_campaign=31day&utm_medium=web&utm_source=20210801%22" title="https://juejin.cn/post/6987962113788493831?utm_campaign=31day&utm_medium=web&utm_source=20210801%22" target="_blank">8月更文挑战</a></strong></p>
<blockquote>
<p>流畅、有意义的动画对于移动应用用户体验来说是非常重要的。React Native 提供了两个互补的动画系统：用于创建精细的交互控制动画的<code>Animated</code>和用于全局布局动画的<code>LayoutAnimation</code></p>
</blockquote>
<h2 data-id="heading-0">Animated</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Freactnative.cn%2Fdocs%2Fanimated" target="_blank" rel="nofollow noopener noreferrer" title="https://reactnative.cn/docs/animated" ref="nofollow noopener noreferrer"><code>Animated</code></a>使得开发者可以简洁地实现各种各样的动画和交互方式，并且具备极高的性能。<code>Animated</code>旨在以声明的形式来定义动画的输入与输出，在其中建立一个可配置的变化函数，然后使用<code>start/stop</code>方法来控制动画按顺序执行。 <code>Animated</code>仅封装了 6 个可以动画化的组件：<code>View</code>、<code>Text</code>、<code>Image</code>、<code>ScrollView</code>、<code>FlatList</code>和<code>SectionList</code>，不过你也可以使用<code>Animated.createAnimatedComponent()</code>来封装你自己的组件。</p>
<p>下面是一个在加载时带有淡入动画效果的视图：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123; useRef, useEffect &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> &#123; Animated, Text, View &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-native'</span>

<span class="hljs-keyword">const</span> LinAnimate = <span class="hljs-function"><span class="hljs-params">props</span> =></span> &#123;
    <span class="hljs-keyword">const</span> fadeAnim = useRef(<span class="hljs-keyword">new</span> Animated.Value(<span class="hljs-number">0</span>)).current <span class="hljs-comment">// 透明度初始值设为0</span>

    useEffect(<span class="hljs-function">() =></span> &#123;
        Animated.timing(
            <span class="hljs-comment">// 随时间变化而执行动画</span>
            fadeAnim, <span class="hljs-comment">// 动画中的变量值</span>
            &#123;
                <span class="hljs-attr">toValue</span>: <span class="hljs-number">1</span>, <span class="hljs-comment">// 透明度最终变为1，即完全不透明</span>
                <span class="hljs-attr">duration</span>: <span class="hljs-number">10000</span> <span class="hljs-comment">// 让动画持续一段时间</span>
            &#125;
        ).start() <span class="hljs-comment">// 开始执行动画</span>
    &#125;, [fadeAnim])

    <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Animated.View</span> // 使用专门的可动画化的<span class="hljs-attr">View</span>组件
            <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span>
                <span class="hljs-attr">...props.style</span>,
                <span class="hljs-attr">opacity:</span> <span class="hljs-attr">fadeAnim</span> // 将透明度绑定到动画变量值
            &#125;&#125;
        ></span>
            &#123;props.children&#125;
        <span class="hljs-tag"></<span class="hljs-name">Animated.View</span>></span></span>
    )
&#125;

<span class="hljs-comment">// 然后你就可以在组件中像使用`View`那样去使用`FadeInView`了</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> () => &#123;
    <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">View</span>
            <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">flex:</span> <span class="hljs-attr">1</span>, <span class="hljs-attr">alignItems:</span> '<span class="hljs-attr">center</span>', <span class="hljs-attr">justifyContent:</span> '<span class="hljs-attr">center</span>' &#125;&#125;
        ></span>
            <span class="hljs-tag"><<span class="hljs-name">LinAnimate</span>
                <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span>
                    <span class="hljs-attr">width:</span> <span class="hljs-attr">250</span>,
                    <span class="hljs-attr">height:</span> <span class="hljs-attr">50</span>,
                    <span class="hljs-attr">backgroundColor:</span> '<span class="hljs-attr">powderblue</span>'
                &#125;&#125;
            ></span>
                <span class="hljs-tag"><<span class="hljs-name">Text</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">fontSize:</span> <span class="hljs-attr">28</span>, <span class="hljs-attr">textAlign:</span> '<span class="hljs-attr">center</span>', <span class="hljs-attr">margin:</span> <span class="hljs-attr">10</span> &#125;&#125;></span>
                    Fading in
                <span class="hljs-tag"></<span class="hljs-name">Text</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">LinAnimate</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">View</span>></span></span>
    )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">配置动画</h2>
<p>动画拥有非常灵活的配置项。自定义的或预定义的 <code>easing</code>函数、延迟、持续时间、衰减系数、弹性常数等都可以在对应类型的动画中进行配置。</p>
<p><code>Animated</code>提供了多种动画类型，其中最常用的要属<a href="https://link.juejin.cn/?target=https%3A%2F%2Freactnative.cn%2Fdocs%2Fanimated%23timing" target="_blank" rel="nofollow noopener noreferrer" title="https://reactnative.cn/docs/animated#timing" ref="nofollow noopener noreferrer"><code>Animated.timing()</code></a>。它可以使用一些预设的<code>easing</code>曲线函数来控制动画值的变化速度，也支持自定义的曲线函数。动画中通常使用<code>easing</code>曲线函数来控制物体的加速或减速变化。</p>
<p>默认情况下<code>timing</code>使用<code>easeInOut</code>曲线，它使动画体逐渐加速到最大然后逐渐减速到停止。你可以通过传递<code>easing</code>参数来指定不同的变化速度，还支持自定义<code>duration</code>持续时间，甚至是动画开始前的<code>delay</code>延迟。</p>
<p>示例：创建了一个 时长 2 秒的动画，在移动目标到最终位置前会稍微往后退一点：</p>
<pre><code class="hljs language-js copyable" lang="js">Animated.timing(<span class="hljs-built_in">this</span>.state.xPosition, &#123;
    <span class="hljs-attr">toValue</span>: <span class="hljs-number">100</span>,
    <span class="hljs-attr">easing</span>: Easing.back(),
    <span class="hljs-attr">duration</span>: <span class="hljs-number">2000</span>
&#125;).start()
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">组合动画</h2>
<p>多个动画可以通过<code>parallel</code>（同时执行）、<code>sequence</code>（顺序执行）、<code>stagger</code>和<code>delay</code>来组合使用。它们中的每一个都接受一个要执行的动画数组，并且自动在适当的时候调用<code>start/stop</code>。</p>
<p>例如，下面的动画滑行到一个停止点，然后它在平行旋转时弹回:</p>
<pre><code class="hljs language-js copyable" lang="js">Animated.sequence([
    <span class="hljs-comment">// decay, then spring to start and twirl</span>
    Animated.decay(position, &#123;
        <span class="hljs-comment">// coast to a stop</span>
        <span class="hljs-attr">velocity</span>: &#123; <span class="hljs-attr">x</span>: gestureState.vx, <span class="hljs-attr">y</span>: gestureState.vy &#125;, <span class="hljs-comment">// velocity from gesture release</span>
        <span class="hljs-attr">deceleration</span>: <span class="hljs-number">0.997</span>
    &#125;),
    Animated.parallel([
        <span class="hljs-comment">// after decay, in parallel:</span>
        Animated.spring(position, &#123;
            <span class="hljs-attr">toValue</span>: &#123; <span class="hljs-attr">x</span>: <span class="hljs-number">0</span>, <span class="hljs-attr">y</span>: <span class="hljs-number">0</span> &#125; <span class="hljs-comment">// return to start</span>
        &#125;),
        Animated.timing(twirl, &#123;
            <span class="hljs-comment">// and twirl</span>
            <span class="hljs-attr">toValue</span>: <span class="hljs-number">360</span>
        &#125;)
    ])
]).start() <span class="hljs-comment">// start the sequence group</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            

---
title: '继🔥Vue 转 React不完全指北(俊劫)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3708'
author: 掘金
comments: false
date: Wed, 21 Apr 2021 22:50:44 GMT
thumbnail: 'https://picsum.photos/400/300?random=3708'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;position:relative;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#282d36&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px;color:#2f845e&#125;.markdown-body h2&#123;font-size:24px;display:inline-block;font-weight:700;background:#2f845e;color:#fff;padding:6px 8px 0 0;border-top-right-radius:6px;margin-right:2px;box-shadow:6px 3px 0 0 rgba(47,132,194,.2)&#125;.markdown-body h2:before&#123;content:" ";display:inline-block;width:8px&#125;.markdown-body h2:after&#123;content:" ";position:absolute;display:block;width:calc(100% - 40px);border-bottom:3px solid #2f845e&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%;box-shadow:6px 6px 6px #888&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-top:6px solid #2f845e&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#262626;background:linear-gradient(180deg,rgba(66,185,131,.1),transparent)!important&#125;.markdown-body strong&#123;background-color:inherit;color:#2f845e&#125;.markdown-body em&#123;background-color:inherit;color:#949415&#125;.markdown-body a&#123;text-decoration:none;color:#2f8e54;border-bottom:1px solid #3f9e64&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#3f9e64&#125;.markdown-body a[class^=footnote]&#123;margin-left:4px&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:100%;max-width:100%;overflow:auto;border:2px solid #2f8e54&#125;.markdown-body thead&#123;background:#2f8e54;color:#fff;text-align:left;font-weight:700&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;width:100%;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;padding:1px 22px;margin:22px 0;border-left:6px solid #2f845e;background-color:rgba(66,185,131,.1);border-radius:4px&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body del&#123;color:#2f845e&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>和我面基(还没)的俊劫发表了一篇这样的文章，地址：<a href="https://juejin.cn/post/6953482028188860424" target="_blank">掘金</a>
虽然我的个人经验没有俊劫多，但其不然我也提提我对于两者之间的看法</p>
</blockquote>
<h2 data-id="heading-0">一、vue和react</h2>
<p>作为目前前端最流行的两大框架，两者之间肯定是存在差异性的，不然两者双剑合璧得了(其实我也挺想的，毕竟现在要学的东西太多了)， 而差异性无非就体现在两个框架对于自己是怎么定义的。</p>
<h3 data-id="heading-1">vue</h3>
<p><a href="https://cn.vuejs.org/" target="_blank" rel="nofollow noopener noreferrer">vue</a> 其官网豁然开亮的几行大字，渐进式框架，灵活，易用，高效，所以在vue当中开发者只需要关注你的试图即可，通过getter，setter，不用去
特意的去优化就能够达到很好的效果，并且有一套官方维护的生态系统。</p>
<h3 data-id="heading-2">react</h3>
<p><a href="https://react.docschina.org/" target="_blank" rel="nofollow noopener noreferrer">react</a> 作为Facebook的亲儿子一样，虽然这个亲儿子是由社区维护，且其生态也是社区维护，但也很难取代他的地位。
在 <a href="https://react.docschina.org/" target="_blank" rel="nofollow noopener noreferrer">react</a> 当中其实可以把任何的东西都看作是组件，整个页面都是由一个个组件拼接而成。</p>
<p>像俊劫说的vue只适合开发小中型项目，而大型项目的话只能用react来开发，其实并不然。其实就一个项目选择开发框架而言来说，
这个项目后期的维护性难度大不大，以及这个项目的可迭代问题完全取决于开发这个项目的人愿不愿意去好好写了🐶保命，虽然react在代码颗粒度上确实要比
vue来的要好，但是两者框架内部的原理其实都是大同小异的。所以说我认为并没有什么vue只能开发小中型项目，而react适合开发大型项目之类的。毕竟存在即合理🐶🐶🐶。</p>
<h2 data-id="heading-3">二、核心概念</h2>
<p>核心概念就不讲了可以去看<a href="https://juejin.cn/post/6953482028188860424" target="_blank">俊劫</a> 的掘金</p>
<h2 data-id="heading-4">三、组件定义</h2>
<h3 data-id="heading-5">1、vue</h3>
<pre><code class="copyable">个人写vue通常使用的是jsx,所以写起来两者区别并不是很大
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//jsx </span>
<span class="hljs-comment">// 父组件</span>
<span class="hljs-keyword">const</span> SonComponent = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'SomComponent'</span>,
    <span class="hljs-attr">inject</span>: [<span class="hljs-string">'fatherDescription'</span>],
    <span class="hljs-attr">props</span>: &#123;
        <span class="hljs-attr">fatherProp</span>: &#123;
            <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
            <span class="hljs-attr">default</span>: <span class="hljs-string">''</span>
        &#125;
    &#125;,
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">description</span>: <span class="hljs-string">'i am son'</span>
        &#125;
    &#125;,
    <span class="hljs-attr">methods</span>: &#123;
        <span class="hljs-function"><span class="hljs-title">buttonClick</span>(<span class="hljs-params"></span>)</span> &#123;
            <span class="hljs-keyword">const</span> &#123;description&#125; = <span class="hljs-built_in">this</span>;
            <span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">'sonClick'</span>, description)
        &#125;
    &#125;,
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">const</span> &#123;description, buttonClick&#125; = <span class="hljs-built_in">this</span>;
        <span class="hljs-keyword">const</span> &#123;fatherProp&#125; = <span class="hljs-built_in">this</span>.$props;
        <span class="hljs-keyword">const</span> &#123;<span class="hljs-attr">default</span>: slots&#125; = <span class="hljs-built_in">this</span>.$slots;
        <span class="hljs-keyword">const</span> &#123;<span class="hljs-attr">default</span>: defaultSlot, mySlotName&#125; = <span class="hljs-built_in">this</span>.$scopedSlots;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.fatherDescription);
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                &#123;description&#125;
                &#123;slots&#125;
                &#123;defaultSlot()&#125;
                &#123;mySlotName()&#125;
                &#123;fatherProp&#125;
                <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;buttonClick&#125;</span>></span>子组件传递信息至父组件<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        )
    &#125;
&#125;;
<span class="hljs-keyword">const</span> ParentComponent = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'ParentComponent'</span>,
    <span class="hljs-attr">components</span>: &#123;
        SonComponent,
    &#125;,
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">description</span>: <span class="hljs-string">'i am father'</span>
        &#125;
    &#125;,
    <span class="hljs-comment">//多层级组件嵌套可以用provide/inject获取到祖父级别的信息</span>
    <span class="hljs-function"><span class="hljs-title">provide</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">fatherDescription</span>: <span class="hljs-built_in">this</span>.description
        &#125;
    &#125;,
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">const</span> &#123;description&#125; = <span class="hljs-built_in">this</span>;
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                &#123;description&#125;
                <span class="hljs-tag"><<span class="hljs-name">son-component</span>
                    // 默认插槽和具名插槽
                    <span class="hljs-attr">scopedSlots</span>=<span class="hljs-string">&#123;&#123;</span>
                        <span class="hljs-attr">default:</span> () =></span> &#123;
                            return (
                                <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                                    这也是默认插槽
                                <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
                            )
                        &#125;,
                        mySlotName: () => &#123;
                            return (
                                <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                                    这是具名插槽
                                <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
                            )
                        &#125;
                    &#125;&#125;
                    fatherProp=&#123;description&#125;
                    onsonClick=&#123;(description) => &#123;
                        console.log(description);
                    &#125;&#125;
                >
                    &#123;/*  默认插槽  */&#125;
                    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                        这是插槽
                    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"></<span class="hljs-name">son-component</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        )
    &#125;
&#125;;
<span class="hljs-comment">//函数式组件</span>

<span class="hljs-keyword">const</span> SonComponent_1 = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">return</span>(
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            函数式组件
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    )
&#125;

<span class="hljs-comment">//template</span>
<span class="hljs-comment">// 父组件</span>
<template>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        &#123;&#123;description&#125;&#125;
        <span class="hljs-tag"><<span class="hljs-name">son</span> <span class="hljs-attr">:fatherDescription</span>=<span class="hljs-string">"description"</span> @<span class="hljs-attr">sonClick</span>=<span class="hljs-string">"sonClick"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            我是默认插槽
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"mySlot"</span>></span>
            我是具名插槽
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">son</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="hljs-keyword">import</span> Son <span class="hljs-keyword">from</span> <span class="hljs-string">'Son.vue'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"Father"</span>,
    <span class="hljs-attr">components</span>: &#123;
        <span class="hljs-comment">//子组件</span>
        Son,
        <span class="hljs-comment">//或</span>
        <span class="hljs-attr">SonComponent</span>: &#123;
            <span class="hljs-attr">name</span>: <span class="hljs-string">'SonComponent'</span>,
            <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
                <span class="hljs-keyword">return</span> &#123;
                    <span class="hljs-attr">description</span>: <span class="hljs-string">'i am son'</span>,
                &#125;
            &#125;,
            <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
                <span class="hljs-keyword">const</span> &#123;description&#125; = <span class="hljs-built_in">this</span>;
                <span class="hljs-keyword">return</span> (
                    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                        &#123;description&#125;
                    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
                )
            &#125;
        &#125;
    &#125;,
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">description</span>: <span class="hljs-string">'i am father'</span>,
        &#125;
    &#125;,
    <span class="hljs-attr">methods</span>: &#123;
        <span class="hljs-function"><span class="hljs-title">sonClick</span>(<span class="hljs-params">description</span>)</span> &#123;
            <span class="hljs-built_in">console</span>.log(description);
        &#125;
    &#125;
&#125;

<span class="hljs-comment">// Son</span>
<template>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        &#123;&#123;description&#125;&#125;
        <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"buttonClick"</span>></span>子组件传递至父组件<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
        &#123;&#123;fatherDescription&#125;&#125;
        <span class="hljs-tag"><<span class="hljs-name">slot</span>/></span>
        <span class="hljs-tag"><<span class="hljs-name">slot</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"mySlot"</span>/></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"Son"</span>,
    <span class="hljs-attr">props</span>: &#123;
        <span class="hljs-attr">fatherDescription</span>: &#123;
            <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
            <span class="hljs-attr">default</span>: <span class="hljs-string">''</span>
        &#125;
    &#125;,
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">description</span>: <span class="hljs-string">'i am son'</span>
        &#125;
    &#125;,
    <span class="hljs-attr">methods</span>: &#123;
        <span class="hljs-function"><span class="hljs-title">buttonClick</span>(<span class="hljs-params"></span>)</span> &#123;
            <span class="hljs-keyword">const</span> &#123;description&#125; = <span class="hljs-built_in">this</span>;
            <span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">'sonClick'</span>, description);
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>vue函数式组件具体可以参考<a href="https://cn.vuejs.org/v2/guide/render-function.html#%E5%87%BD%E6%95%B0%E5%BC%8F%E7%BB%84%E4%BB%B6" target="_blank" rel="nofollow noopener noreferrer">函数式组件</a></p>
<h3 data-id="heading-6">2、react</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// calss</span>
<span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> &#123;Button&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'antd'</span>;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">SonComponent</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">super</span>();
        <span class="hljs-built_in">this</span>.state = &#123;
            <span class="hljs-attr">description</span>: <span class="hljs-string">'i am son'</span>
        &#125;;
    &#125;
    <span class="hljs-function"><span class="hljs-title">clickButton</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'点击事件'</span>);
    &#125;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">const</span> &#123;description&#125; = <span class="hljs-built_in">this</span>.state;
        <span class="hljs-keyword">const</span> &#123;clickButton&#125; = <span class="hljs-built_in">this</span>;
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                &#123;description&#125;
                <span class="hljs-tag"><<span class="hljs-name">Button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;clickButton&#125;</span>></span>点击我<span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        )
    &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">FatherComponent</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">super</span>();
        <span class="hljs-built_in">this</span>.state = &#123;
            <span class="hljs-attr">description</span>: <span class="hljs-string">'i am Father'</span>
        &#125;;
    &#125;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">const</span> &#123;description&#125; = <span class="hljs-built_in">this</span>.state;
        <span class="hljs-keyword">return</span>(
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                &#123;description&#125;
                <span class="hljs-tag"><<span class="hljs-name">SonComponent</span>/></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        )
    &#125;
&#125;

<span class="hljs-comment">//FunctionComponent</span>
<span class="hljs-keyword">import</span> React, &#123;useState, createContext, useContext&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> &#123;Button&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'antd'</span>;

<span class="hljs-keyword">const</span> ParentContext: React.Context<&#123;
    fatherClick?: <span class="hljs-function">(<span class="hljs-params">dispath: React.Dispatch<React.SetStateAction<string>></span>) =></span> <span class="hljs-keyword">void</span>;
&#125;> = createContext(&#123;&#125;)

<span class="hljs-comment">//React.FunctionComponent<props类型> = React.FC;</span>
<span class="hljs-keyword">const</span> SonComponent: React.FunctionComponent<&#123;
    <span class="hljs-comment">//子组件接受父组件参数</span>
    <span class="hljs-attr">fatherClick</span>: <span class="hljs-function">(<span class="hljs-params">diapatch: React.Dispatch<React.SetStateAction<string>></span>) =></span> <span class="hljs-keyword">void</span>;
    children: React.ReactNode
&#125;> = <span class="hljs-function">(<span class="hljs-params">&#123;
          <span class="hljs-regexp">//</span> fatherClick
          children
      &#125;</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> [description, changeDescription] = useState<string>(<span class="hljs-string">'i am son'</span>);
    <span class="hljs-keyword">const</span> &#123;fatherClick&#125; = useContext(ParentContext);
    <span class="hljs-keyword">const</span> clickButton = <span class="hljs-function">() =></span> &#123;
        <span class="hljs-comment">//通过props进行父子级通讯</span>
        <span class="hljs-comment">// fatherClick(changeDescription);</span>
        <span class="hljs-comment">//通过context进行父子级通讯</span>
        fatherClick&&fatherClick(changeDescription);
        <span class="hljs-comment">// changeDescription('点击事件');</span>
    &#125;;
    <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">ParentContext.Consumer</span>></span>
                &#123;
                    (&#123;
                         fatherClick
                     &#125;) => (
                        <span class="hljs-tag"><></span>
                            &#123;description&#125;
                            <span class="hljs-tag"><<span class="hljs-name">Button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> fatherClick&&fatherClick(changeDescription)&#125;>点击事件<span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
                            <span class="hljs-tag"><<span class="hljs-name">Button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;clickButton&#125;</span>></span>点击事件<span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
                            &#123;children&#125;
                        <span class="hljs-tag"></></span>
                    )
                &#125;
            <span class="hljs-tag"></<span class="hljs-name">ParentContext.Consumer</span>></span></span>

        </div>
    )
&#125;;

<span class="hljs-keyword">const</span> FatherComponent: React.FC<&#123;&#125;> = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> [description] = useState<string>(<span class="hljs-string">'i am father'</span>);
    <span class="hljs-keyword">const</span> fatherClick = <span class="hljs-function">(<span class="hljs-params">dispatch: React.Dispatch<React.SetStateAction<string>></span>) =></span> &#123;
        <span class="hljs-comment">//改变子组件里面的description</span>
        dispatch(<span class="hljs-string">'点击事件'</span>);
    &#125;
    <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">ParentContext.Provider</span>
                <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;</span>
                    &#123;
                        <span class="hljs-attr">fatherClick</span>
                    &#125;
                &#125;

            ></span>
                &#123;description&#125;
                <span class="hljs-tag"><<span class="hljs-name">SonComponent</span> <span class="hljs-attr">fatherClick</span>=<span class="hljs-string">&#123;fatherClick&#125;</span>></span>
                    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                        我是插槽
                    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"></<span class="hljs-name">SonComponent</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">ParentContext.Provider</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    )
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">四、组件通讯</h2>
<h3 data-id="heading-8">vue</h3>
<p>1.props/$emit;</p>
<p>2.provide/inject;</p>
<p>3.vuex;</p>
<p>4.localstorage;</p>
<p>5.event bus</p>
<h3 data-id="heading-9">react</h3>
<p>1.props</p>
<p>2.redux</p>
<p>3.context</p>
<p>4.event bus(库);</p>
<p>以上除了vuex, redux, localstorage, event bus 基本上都写了一遍</p>
<h2 data-id="heading-10">五、我的总体感受</h2>
<ul>
<li>
<p>就像<a href="https://juejin.cn/post/6953482028188860424" target="_blank">俊劫</a> 说的一样vue更加的能上手，开箱即用并且能够灵活的配置webpack，不像react一样需要eject一下将配置文件全部抛出来，并且还是不可逆的，虽然多多少少有一些插件可以重构webpack但还是vue直接添加一个vue.config.js来的香。</p>
</li>
<li>
<p>其实在我写vue和react来说其实并没有太大的区别感受，可能和我都是写jsx语法有关系吧，但是vue+ts,和react+ts，emm两者区别还是挺大的，但是没关系噢，vue3已经灰度测试了，并且引入了组件API(Composition API)，能够更好的支持ts，虽然我还没用过🐶保命，但是我还是挺期待vue3的(尤大🐂🍺);</p>
</li>
</ul>
<h2 data-id="heading-11">六、资源分享</h2>
<p><a href="https://juejin.cn/post/6953482028188860424" target="_blank">俊劫</a> 直接去他掘金地址里面找吧，我反正找不到🐶🐶🐶。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            
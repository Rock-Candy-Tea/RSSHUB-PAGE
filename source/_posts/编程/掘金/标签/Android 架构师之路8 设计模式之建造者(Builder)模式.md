
---
title: 'Android 架构师之路8 设计模式之建造者(Builder)模式'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e084d7b8a2e14b5bbbe2a4148bd71d6b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 30 Aug 2021 22:09:11 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e084d7b8a2e14b5bbbe2a4148bd71d6b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">前言</h4>
<blockquote>
<p>建造者模式是设计模式的一种，将一个复杂对象的构建与它的表示分离，使得同样的构建过程可以创建不同的表示。</p>
</blockquote>
<h4 data-id="heading-1">1、建造者模式特征</h4>
<h5 data-id="heading-2">1.1 建造者模式UML图</h5>
<div align="center">
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e084d7b8a2e14b5bbbe2a4148bd71d6b~tplv-k3u1fbpfcp-watermark.image" alt="Builder设计模式UML图" loading="lazy" referrerpolicy="no-referrer">
</div>
<h5 data-id="heading-3">1.2 建造者模式角色</h5>
<p>在这样的设计模式中，有以下几个角色：</p>
<ul>
<li><strong>builder：</strong> 为创建一个产品对象的各个部件指定抽象接口。</li>
<li><strong>ConcreteBuilder：</strong> 实现Builder的接口以构造和装配该产品的各个部件，定义并明确它所创建的表示，并 提供一个检索产品的接口。</li>
<li><strong>Director：</strong> 构造一个使用Builder接口的对象。</li>
<li><strong>Product：</strong> 表示被构造的复杂对象。ConcreteBuilder创建该产品的内部表示并定义它的装配过程，包含定义组成部件的类，包括将这些部件装配成最终产品的接口。</li>
</ul>
<h5 data-id="heading-4">1.3 建造者模式使用场景</h5>
<ol>
<li>创建复杂对象的算法独立于组成对象的部件</li>
<li>同一个创建过程需要有不同的内部表象的产品对象</li>
</ol>
<h4 data-id="heading-5">2、建造者模式代码实现</h4>
<h5 data-id="heading-6">2.1 标准写法</h5>
<h6 data-id="heading-7">builder:</h6>
<hr>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">/**
 * 抽象建造者
 * Created by Administrator on 2018/1/24.
 */</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">interface</span> <span class="hljs-title">Builder</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">makeWindow</span><span class="hljs-params">()</span></span>;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">makeFloor</span><span class="hljs-params">()</span></span>;

    <span class="hljs-function"><span class="hljs-keyword">public</span> Room <span class="hljs-title">build</span><span class="hljs-params">()</span></span>;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-8">ConcreteBuilder:</h6>
<hr>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">/**
 * Created by Administrator on 2018/1/24.
 * 持有对房子的引用
 */</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">WorkBuilder</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">Builder</span> </span>&#123;
    Room room = <span class="hljs-keyword">new</span> Room();
    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">makeWindow</span><span class="hljs-params">()</span> </span>&#123;
        room.setWindow(<span class="hljs-string">"欧式窗户"</span>);
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">makeFloor</span><span class="hljs-params">()</span> </span>&#123;
        room.setFloor(<span class="hljs-string">"日式地板"</span>);
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> Room <span class="hljs-title">build</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">return</span> room;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-9">Director:</h6>
<hr>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">/**
 * Created by Administrator on 2018/1/24.
 * 设计者(指导者)
 *
 * 他知道 房屋怎么设计
 * 他肯定对 工人所具备的能力有所理解
 */</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Designer</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-keyword">public</span> Room <span class="hljs-title">build</span><span class="hljs-params">(Builder builder)</span></span>&#123;
        builder.makeFloor();
        builder.makeWindow();
        <span class="hljs-keyword">return</span> builder.build();
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-10">Product:</h6>
<hr>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">/**
 * Created by Administrator on 2018/1/24.
 */</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Room</span> </span>&#123;
    <span class="hljs-keyword">private</span> String window;

    <span class="hljs-keyword">private</span> String floor;

    <span class="hljs-function"><span class="hljs-keyword">public</span> String <span class="hljs-title">getWindow</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">return</span> window;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">setWindow</span><span class="hljs-params">(String window)</span> </span>&#123;
        <span class="hljs-keyword">this</span>.window = window;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> String <span class="hljs-title">getFloor</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">return</span> floor;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">setFloor</span><span class="hljs-params">(String floor)</span> </span>&#123;
        <span class="hljs-keyword">this</span>.floor = floor;
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> String <span class="hljs-title">toString</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-string">"Room&#123;"</span> +
                <span class="hljs-string">"window='"</span> + window + <span class="hljs-string">''</span><span class="hljs-string">' +
                ", floor='</span><span class="hljs-string">" + floor + ''' +
                '&#125;';
    &#125;
&#125;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-11">Client调用:</h6>
<hr>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Client</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String[] args)</span> </span>&#123;
        Builder build = <span class="hljs-keyword">new</span> WorkBuilder();
        Designer designer = <span class="hljs-keyword">new</span> Designer();
        Room room = designer.build(build);
        System.out.println(room.toString());
        <span class="hljs-comment">//房间暴露了构建过程不合理</span>
        room.setFloor(<span class="hljs-string">"XXXXX"</span>);
        room.setWindow(<span class="hljs-string">"XXXXX"</span>);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-12">运行结果:</h6>
<hr>
<pre><code class="hljs language-java copyable" lang="java">Room&#123;window=<span class="hljs-string">'欧式窗户'</span>, floor=<span class="hljs-string">'日式地板'</span>&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-13">注意：Product本身暴露了产品构建过程不合理</h6>
<h5 data-id="heading-14">2.2 变种优化写法</h5>
<h6 data-id="heading-15">Product:</h6>
<hr>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Room</span> </span>&#123;
    <span class="hljs-keyword">private</span> String window;

    <span class="hljs-keyword">private</span> String floor;

    <span class="hljs-keyword">private</span> String lamp;

    <span class="hljs-function"><span class="hljs-keyword">public</span> Room <span class="hljs-title">apply</span><span class="hljs-params">(WorkBuilder.RoomParams params)</span></span>&#123;
        window = params.window;
        floor = params.floor;
        lamp = params.floor;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">this</span>;
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> String <span class="hljs-title">toString</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-string">"Room&#123;"</span> +
                <span class="hljs-string">"window='"</span> + window + <span class="hljs-string">''</span><span class="hljs-string">' +
                ", floor='</span><span class="hljs-string">" + floor + ''' +
                "</span>, lamp=<span class="hljs-string">'" + lamp + '</span><span class="hljs-string">''</span> +
                <span class="hljs-string">'&#125;'</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-16">ConcreteBuilder:</h6>
<h6 data-id="heading-17">含有和Product同样参数的内部类RoomParams</h6>
<hr>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">WorkBuilder</span> </span>&#123;
    Room room = <span class="hljs-keyword">new</span> Room();
    <span class="hljs-keyword">private</span> RoomParams params = <span class="hljs-keyword">new</span> RoomParams();

    <span class="hljs-function"><span class="hljs-keyword">public</span> WorkBuilder <span class="hljs-title">makeWindow</span><span class="hljs-params">(String window)</span></span>&#123;
        params.window = window;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">this</span>;
    &#125;
    <span class="hljs-function"><span class="hljs-keyword">public</span> WorkBuilder <span class="hljs-title">makeFloor</span><span class="hljs-params">(String floor)</span></span>&#123;
        params.floor = floor;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">this</span>;
    &#125;
    <span class="hljs-function"><span class="hljs-keyword">public</span> WorkBuilder <span class="hljs-title">makeLamp</span><span class="hljs-params">(String lamp)</span></span>&#123;
        params.lamp = lamp;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">this</span>;
    &#125;
    <span class="hljs-comment">/**
     * 隐藏构建过程
     *真正的构建者
     *  */</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> Room <span class="hljs-title">build</span><span class="hljs-params">()</span></span>&#123;
        room.apply(params);
        <span class="hljs-keyword">return</span> room;
    &#125;

   <span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">RoomParams</span></span>&#123;
       <span class="hljs-keyword">public</span> String window;

       <span class="hljs-keyword">public</span> String floor;

       <span class="hljs-keyword">public</span> String lamp;


    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-18">Client调用:</h6>
<hr>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Client</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String[] args)</span></span>&#123;
        <span class="hljs-comment">//隐藏了构建过程合理</span>
        Room room = <span class="hljs-keyword">new</span> WorkBuilder()
                .makeFloor(<span class="hljs-string">"日式地板"</span>)
                .makeWindow(<span class="hljs-string">"欧式窗户"</span>)
                .makeLamp(<span class="hljs-string">"中式吊灯"</span>)
                .build() ;

        System.out.println(room.toString());
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-19">运行结果:</h6>
<hr>
<pre><code class="hljs language-java copyable" lang="java">Room&#123;window=<span class="hljs-string">'欧式窗户'</span>, floor=<span class="hljs-string">'日式地板'</span>, lamp=<span class="hljs-string">'日式地板'</span>&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-20">Product类隐藏构建过程，设计合理</h6>
<h4 data-id="heading-21">3、Android源码中使用</h4>
<p>建造者典型例子是AlertDialog，它的基本写法是:</p>
<hr>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">AlertDialog</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Dialog</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">DialogInterface</span> </span>&#123;
    <span class="hljs-keyword">private</span> AlertController mAlert;

    <span class="hljs-function"><span class="hljs-keyword">protected</span> <span class="hljs-title">AlertDialog</span><span class="hljs-params">(Context context)</span> </span>&#123;
        <span class="hljs-keyword">this</span>(context, resolveDialogTheme(context, <span class="hljs-number">0</span>), <span class="hljs-keyword">true</span>);
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">setTitle</span><span class="hljs-params">(CharSequence title)</span> </span>&#123;
        <span class="hljs-keyword">super</span>.setTitle(title);
        mAlert.setTitle(title);
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">setMessage</span><span class="hljs-params">(CharSequence message)</span> </span>&#123;
        mAlert.setMessage(message);
    &#125;

    <span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Builder</span> </span>&#123;
        <span class="hljs-keyword">private</span> <span class="hljs-keyword">final</span> AlertController.AlertParams P;
        <span class="hljs-keyword">private</span> <span class="hljs-keyword">int</span> mTheme;

        <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-title">Builder</span><span class="hljs-params">(Context context, <span class="hljs-keyword">int</span> theme)</span> </span>&#123;
            P = <span class="hljs-keyword">new</span> AlertController.AlertParams(<span class="hljs-keyword">new</span> ContextThemeWrapper(
                    context, resolveDialogTheme(context, theme)));
            mTheme = theme;
        &#125;

        <span class="hljs-function"><span class="hljs-keyword">public</span> Builder <span class="hljs-title">setTitle</span><span class="hljs-params">(<span class="hljs-keyword">int</span> titleId)</span> </span>&#123;
            P.mTitle = P.mContext.getText(titleId);
            <span class="hljs-keyword">return</span> <span class="hljs-keyword">this</span>;
        &#125;

        <span class="hljs-function"><span class="hljs-keyword">public</span> Builder <span class="hljs-title">setMessage</span><span class="hljs-params">(CharSequence message)</span> </span>&#123;
            P.mMessage = message;
            <span class="hljs-keyword">return</span> <span class="hljs-keyword">this</span>;
        &#125;

        <span class="hljs-function"><span class="hljs-keyword">public</span> Builder <span class="hljs-title">setOnCancelListener</span><span class="hljs-params">(OnCancelListener onCancelListener)</span> </span>&#123;
            P.mOnCancelListener = onCancelListener;
            <span class="hljs-keyword">return</span> <span class="hljs-keyword">this</span>;
        &#125;

        <span class="hljs-function"><span class="hljs-keyword">public</span> AlertDialog <span class="hljs-title">create</span><span class="hljs-params">()</span> </span>&#123;
            <span class="hljs-keyword">final</span> AlertDialog dialog = <span class="hljs-keyword">new</span> AlertDialog(P.mContext, mTheme, <span class="hljs-keyword">false</span>);
            P.apply(dialog.mAlert);
            dialog.setCancelable(P.mCancelable);
            <span class="hljs-keyword">if</span> (P.mCancelable) &#123;
                dialog.setCanceledOnTouchOutside(<span class="hljs-keyword">true</span>);
            &#125;
            dialog.setOnCancelListener(P.mOnCancelListener);
            ...
            <span class="hljs-keyword">return</span> dialog;
        &#125;

        <span class="hljs-function"><span class="hljs-keyword">public</span> AlertDialog <span class="hljs-title">show</span><span class="hljs-params">()</span> </span>&#123;
            AlertDialog dialog = create();
            dialog.show();
            <span class="hljs-keyword">return</span> dialog;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            
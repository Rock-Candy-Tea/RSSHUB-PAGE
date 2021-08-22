
---
title: 'vue之mixin理解与使用🍉'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5dd222786424fc0a4bb919e622752ec~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 21 Aug 2021 17:14:04 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5dd222786424fc0a4bb919e622752ec~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第22天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h2 data-id="heading-0">🍕 前言</h2>
<ul>
<li>最近确实是有点忙，天天日更确实有点不知道写什么了，所以就把以前自己记录的文章拿出来吧。</li>
<li>可能会有点水，大家如果有需要的可以看看。</li>
<li><code>mixin</code>可以让我们的组件复用一些我们配置相同的生命周期或者方法，当然这个<code>mixin</code>只能在<code>vue 2.x</code>使用，<code>vue 3.0</code>已经不需要了。</li>
</ul>
<h2 data-id="heading-1">🥪 使用场景</h2>
<ul>
<li>
<p>当有两个非常相似的组件，除了一些个别的异步请求外其余的配置都一样，甚至父组件传的值也是一样的，但他们之间又存在着足够的差异性，这时候就不得不拆分成两个组件，如果拆分成两个组件，你就不得不冒着一旦功能变动就要在两个文件中更新代码的风险。</p>
</li>
<li>
<p>这时候就可以使用<code>mixin</code>（混入）了，混入 (<code>mixin</code>) 提供了一种非常灵活的方式，来分发 Vue 组件中的可复用功能。一个混入对象可以包含任意组件选项。当组件使用混入对象时，所有混入对象的选项将被“混合”进入该组件本身的选项。可能听起来比较抽象，现在举个简单的例子吧。</p>
</li>
</ul>
<h2 data-id="heading-2">🥧 实际案例</h2>
<ul>
<li>对比这两个组件的<code>script</code>有什么不同和相同之处</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//组件一</span>
<script>
<span class="hljs-keyword">import</span> &#123; findClassHourByCurricid &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/api/system/class'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'AllClassHour'</span>,
    <span class="hljs-attr">props</span>: &#123;
        <span class="hljs-attr">recordDeatil</span>: &#123;
        <span class="hljs-attr">type</span>: <span class="hljs-built_in">Object</span>,
        <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>
        &#125;,
        <span class="hljs-attr">detailShow</span>: &#123;
            <span class="hljs-attr">type</span>: <span class="hljs-built_in">Boolean</span>,
            <span class="hljs-attr">require</span>: <span class="hljs-literal">true</span>,
            <span class="hljs-attr">default</span>: <span class="hljs-literal">false</span>
        &#125;
    &#125;,
    data () &#123;
        <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">data</span>: [],
            <span class="hljs-attr">columns</span>: [
                        &#123;
                            <span class="hljs-attr">title</span>: <span class="hljs-string">'序号'</span>,
                            <span class="hljs-attr">dataIndex</span>: <span class="hljs-string">'index'</span>,
                            <span class="hljs-attr">key</span>: <span class="hljs-string">'index'</span>,
                            <span class="hljs-attr">align</span>: <span class="hljs-string">'center'</span>,
                            <span class="hljs-attr">width</span>: <span class="hljs-string">'10%'</span>,
                            <span class="hljs-attr">customRender</span>: <span class="hljs-function">(<span class="hljs-params">text, record, index</span>) =></span> <span class="hljs-string">`<span class="hljs-subst">$&#123;index + <span class="hljs-number">1</span>&#125;</span>`</span>
                        &#125;,
                        &#123;
                            <span class="hljs-attr">dataIndex</span>: <span class="hljs-string">'classname'</span>,
                            <span class="hljs-attr">title</span>: <span class="hljs-string">'课时名称'</span>,
                            <span class="hljs-attr">key</span>: <span class="hljs-string">'classname'</span>,
                            <span class="hljs-attr">width</span>: <span class="hljs-string">'50%'</span>,
                            <span class="hljs-comment">// align: 'center',</span>
                            <span class="hljs-attr">scopedSlots</span>: &#123; <span class="hljs-attr">customRender</span>: <span class="hljs-string">'classname'</span> &#125;
                        &#125;,
                        &#123;
                            <span class="hljs-attr">title</span>: <span class="hljs-string">'创建日期'</span>,
                            <span class="hljs-attr">dataIndex</span>: <span class="hljs-string">'crtime'</span>,
                            <span class="hljs-attr">key</span>: <span class="hljs-string">'crtime'</span>,
                            <span class="hljs-attr">width</span>: <span class="hljs-string">'50%'</span>,
                            <span class="hljs-comment">// align: 'center',</span>
                            <span class="hljs-attr">scopedSlots</span>: &#123; <span class="hljs-attr">customRender</span>: <span class="hljs-string">'crtime'</span> &#125;
                        &#125;
                    ],
            <span class="hljs-attr">pagination</span>: <span class="hljs-literal">false</span>,
            <span class="hljs-attr">loading</span>: <span class="hljs-literal">false</span>,
            <span class="hljs-attr">status</span>: <span class="hljs-literal">false</span>
        &#125;
    &#125;,
    mounted () &#123;
    <span class="hljs-built_in">this</span>.getClassHour()
        <span class="hljs-built_in">this</span>.test()
    &#125;,

    <span class="hljs-attr">methods</span>: &#123;
        test () &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'测试公共组件'</span>)
        &#125;,
        getClassHour () &#123;
            <span class="hljs-built_in">this</span>.data = []
            <span class="hljs-keyword">const</span> params = &#123;
                <span class="hljs-attr">curricid</span>: <span class="hljs-built_in">this</span>.recordDeatil.curricid
            &#125;
            <span class="hljs-built_in">this</span>.loading = <span class="hljs-literal">true</span>
            findClassHourByCurricid(params).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
                <span class="hljs-keyword">const</span> classHourDetail = res.data.data
                <span class="hljs-built_in">this</span>.data = classHourDetail
                <span class="hljs-built_in">this</span>.loading = <span class="hljs-literal">false</span>
                &#125;
            )
        &#125;
    &#125;
&#125;

</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//组件二</span>
<script>
<span class="hljs-keyword">import</span> &#123; findStudentByCurricid &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/api/system/class'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'AllStudent'</span>,
    <span class="hljs-attr">props</span>: &#123;
        <span class="hljs-attr">recordDeatil</span>: &#123;
        <span class="hljs-attr">type</span>: <span class="hljs-built_in">Object</span>,
        <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>
        &#125;,
        <span class="hljs-attr">detailShow</span>: &#123;
            <span class="hljs-attr">type</span>: <span class="hljs-built_in">Boolean</span>,
            <span class="hljs-attr">require</span>: <span class="hljs-literal">true</span>,
            <span class="hljs-attr">default</span>: <span class="hljs-literal">false</span>
        &#125;
    &#125;,
    data () &#123;
        <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">data</span>: [],
            <span class="hljs-attr">columns</span>: [
                        &#123;
                            <span class="hljs-attr">title</span>: <span class="hljs-string">'序号'</span>,
                            <span class="hljs-attr">dataIndex</span>: <span class="hljs-string">'index'</span>,
                            <span class="hljs-attr">key</span>: <span class="hljs-string">'index'</span>,
                            <span class="hljs-attr">align</span>: <span class="hljs-string">'center'</span>,
                            <span class="hljs-attr">width</span>: <span class="hljs-string">'10%'</span>,
                            <span class="hljs-attr">customRender</span>: <span class="hljs-function">(<span class="hljs-params">text, record, index</span>) =></span> <span class="hljs-string">`<span class="hljs-subst">$&#123;index + <span class="hljs-number">1</span>&#125;</span>`</span>
                        &#125;,
                        &#123;
                            <span class="hljs-attr">dataIndex</span>: <span class="hljs-string">'truename'</span>,
                            <span class="hljs-attr">title</span>: <span class="hljs-string">'真实姓名'</span>,
                            <span class="hljs-attr">key</span>: <span class="hljs-string">'truename'</span>,
                            <span class="hljs-attr">width</span>: <span class="hljs-string">'50%'</span>,
                            <span class="hljs-comment">// align: 'center',</span>
                            <span class="hljs-attr">scopedSlots</span>: &#123; <span class="hljs-attr">customRender</span>: <span class="hljs-string">'truename'</span> &#125;
                        &#125;,
                        &#123;
                            <span class="hljs-attr">title</span>: <span class="hljs-string">'中文名'</span>,
                            <span class="hljs-attr">dataIndex</span>: <span class="hljs-string">'chanema'</span>,
                            <span class="hljs-attr">width</span>: <span class="hljs-string">'50%'</span>,
                            <span class="hljs-comment">// align: 'center',</span>
                            <span class="hljs-attr">key</span>: <span class="hljs-string">'chanema'</span>
                        &#125;
                    ],
            <span class="hljs-attr">pagination</span>: <span class="hljs-literal">false</span>,
            <span class="hljs-attr">loading</span>: <span class="hljs-literal">false</span>,
            <span class="hljs-attr">status</span>: <span class="hljs-literal">false</span>
        &#125;
    &#125;,
    mounted () &#123;
        <span class="hljs-built_in">this</span>.getStudent()
        <span class="hljs-built_in">this</span>.test()
    &#125;,
    <span class="hljs-attr">methods</span>: &#123;
        test () &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'测试公共组件'</span>)
        &#125;,
        getStudent () &#123;
            <span class="hljs-built_in">this</span>.data = []
            <span class="hljs-keyword">const</span> params = &#123;
                <span class="hljs-attr">curricid</span>: <span class="hljs-built_in">this</span>.recordDeatil.curricid
            &#125;
            <span class="hljs-built_in">this</span>.loading = <span class="hljs-literal">true</span>
            findStudentByCurricid(params).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
                <span class="hljs-keyword">const</span> studentDetail = res.data.data
                <span class="hljs-built_in">this</span>.data = studentDetail
                <span class="hljs-built_in">this</span>.loading = <span class="hljs-literal">false</span>
                &#125;
            )
        &#125;
    &#125;
&#125;

</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以发现，除了获取表格的数据所调用的异步请求外其余配置基本上相同 于是我们可以在这里提取逻辑并创建可以被重用的项：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> publish = &#123;
    <span class="hljs-attr">props</span>: &#123;
        <span class="hljs-attr">recordDeatil</span>: &#123;
        <span class="hljs-attr">type</span>: <span class="hljs-built_in">Object</span>,
        <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>
        &#125;,
        <span class="hljs-attr">detailShow</span>: &#123;
            <span class="hljs-attr">type</span>: <span class="hljs-built_in">Boolean</span>,
            <span class="hljs-attr">require</span>: <span class="hljs-literal">true</span>,
            <span class="hljs-attr">default</span>: <span class="hljs-literal">false</span>
        &#125;
    &#125;,
    data () &#123;
        <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">data</span>: [],
            <span class="hljs-attr">pagination</span>: <span class="hljs-literal">false</span>,
            <span class="hljs-attr">loading</span>: <span class="hljs-literal">false</span>,
            <span class="hljs-attr">status</span>: <span class="hljs-literal">false</span>
        &#125;
    &#125;,
    <span class="hljs-attr">methods</span>: &#123;
        test () &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'测试公共方法'</span>)
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>然后我们把组件中重复的配置和方法全部去掉，引用这个<code>mixin</code></li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5dd222786424fc0a4bb919e622752ec~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>运行代码会发现 结果是一样的</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fab9f97d76ea4318a8cc7b9f7ee3c058~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>即便我们使用的是一个对象而不是一个组件，生命周期函数对我们来说仍然是可用的，理解这点很重要。我们也可以这里使用<code>mounted()</code>钩子函数，它将被应用于组件的生命周期上。这种工作方式真的很灵活也很强大。</li>
</ul>
<h2 data-id="heading-3">👋 写在最后</h2>
<ul>
<li>在一些我们需要做同样配置或者相似度极高的组件时，我们不妨可以试试<code>Mixin</code>混入你所需要的相同配置或者方法，这样会使我们的开发效率大大提高。</li>
<li>当然这个<code>mixin</code>只适用于<code>vue 2.x</code>,<code>vue 3.0</code>的<code>Composition API</code>已经很强大了。</li>
</ul>
<h2 data-id="heading-4">🌅 往期精彩</h2>
<p><a href="https://juejin.cn/post/6997978246839042079" target="_blank" title="https://juejin.cn/post/6997978246839042079">一文搞定echarts地图轮播高亮⚡</a></p>
<p><a href="https://juejin.cn/post/6998389354271866910" target="_blank" title="https://juejin.cn/post/6998389354271866910">看完还分不清重绘和重排过来捶我👊，我说的！！！</a></p>
<p><a href="https://juejin.cn/post/6991267694678900772" target="_blank" title="https://juejin.cn/post/6991267694678900772">如何优雅的使用Vuepress编写组件示例（上）👈</a></p>
<p><a href="https://juejin.cn/post/6991646499775971359" target="_blank" title="https://juejin.cn/post/6991646499775971359">如何优雅的使用Vuepress编写组件示例（下）👈</a></p></div>  
</div>
            
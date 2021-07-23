
---
title: 'uni-app引入echarts-for-wx，formatter 自定义函数不起作用的问题'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c5af6b2b674f4770ae55161f68752bdf~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 22 Jul 2021 22:08:04 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c5af6b2b674f4770ae55161f68752bdf~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>原因：vue的data里不能放函数，会被序列化</p>
<p>解决方法：</p>
<p>只能手动setOptions，需要通过获取实例$curChart后。</p>
<p>通过this.<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>r</mi><mi>e</mi><mi>f</mi><mi>s</mi><msup><mo stretchy="false">[</mo><mo mathvariant="normal" lspace="0em" rspace="0em">′</mo></msup><mi>u</mi><mi>n</mi><mi>i</mi><mo>−</mo><mi>e</mi><mi>c</mi><mo>−</mo><mi>c</mi><mi>a</mi><mi>n</mi><mi>v</mi><mi>a</mi><msup><mi>s</mi><mo mathvariant="normal" lspace="0em" rspace="0em">′</mo></msup><mo stretchy="false">]</mo><mi mathvariant="normal">.</mi></mrow><annotation encoding="application/x-tex">refs['uni-ec-canvas'].</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1.001892em;vertical-align:-0.25em;"></span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">e</span><span class="mord mathnormal" style="margin-right:0.10764em;">f</span><span class="mord mathnormal">s</span><span class="mopen"><span class="mopen">[</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">′</span></span></span></span></span></span></span></span></span><span class="mord mathnormal">u</span><span class="mord mathnormal">n</span><span class="mord mathnormal">i</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span><span class="mbin">−</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span></span><span class="base"><span class="strut" style="height:0.66666em;vertical-align:-0.08333em;"></span><span class="mord mathnormal">e</span><span class="mord mathnormal">c</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span><span class="mbin">−</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span></span><span class="base"><span class="strut" style="height:1.001892em;vertical-align:-0.25em;"></span><span class="mord mathnormal">c</span><span class="mord mathnormal">a</span><span class="mord mathnormal">n</span><span class="mord mathnormal" style="margin-right:0.03588em;">v</span><span class="mord mathnormal">a</span><span class="mord"><span class="mord mathnormal">s</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">′</span></span></span></span></span></span></span></span></span><span class="mclose">]</span><span class="mord">.</span></span></span></span></span>curChart.setOption来设置echart配置</p>
<pre><code class="hljs language-mounted() copyable" lang="mounted()">      this.$nextTick(function()&#123;
        console.log(this.$refs['uni-ec-canvas'])
        console.log(this.$refs['uni-ec-canvas'].$curChart)
      &#125;)
    &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c5af6b2b674f4770ae55161f68752bdf~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b9478fc7657b48fc95f7f787dbd0ee80~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
发现 this.<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>r</mi><mi>e</mi><mi>f</mi><mi>s</mi><msup><mo stretchy="false">[</mo><mo mathvariant="normal" lspace="0em" rspace="0em">′</mo></msup><mi>u</mi><mi>n</mi><mi>i</mi><mo>−</mo><mi>e</mi><mi>c</mi><mo>−</mo><mi>c</mi><mi>a</mi><mi>n</mi><mi>v</mi><mi>a</mi><msup><mi>s</mi><mo mathvariant="normal" lspace="0em" rspace="0em">′</mo></msup><mo stretchy="false">]</mo><mtext>这个对象中存在</mtext></mrow><annotation encoding="application/x-tex">refs['uni-ec-canvas']这个对象中存在</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1.001892em;vertical-align:-0.25em;"></span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">e</span><span class="mord mathnormal" style="margin-right:0.10764em;">f</span><span class="mord mathnormal">s</span><span class="mopen"><span class="mopen">[</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">′</span></span></span></span></span></span></span></span></span><span class="mord mathnormal">u</span><span class="mord mathnormal">n</span><span class="mord mathnormal">i</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span><span class="mbin">−</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span></span><span class="base"><span class="strut" style="height:0.66666em;vertical-align:-0.08333em;"></span><span class="mord mathnormal">e</span><span class="mord mathnormal">c</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span><span class="mbin">−</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span></span><span class="base"><span class="strut" style="height:1.001892em;vertical-align:-0.25em;"></span><span class="mord mathnormal">c</span><span class="mord mathnormal">a</span><span class="mord mathnormal">n</span><span class="mord mathnormal" style="margin-right:0.03588em;">v</span><span class="mord mathnormal">a</span><span class="mord"><span class="mord mathnormal">s</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">′</span></span></span></span></span></span></span></span></span><span class="mclose">]</span><span class="mord cjk_fallback">这</span><span class="mord cjk_fallback">个</span><span class="mord cjk_fallback">对</span><span class="mord cjk_fallback">象</span><span class="mord cjk_fallback">中</span><span class="mord cjk_fallback">存</span><span class="mord cjk_fallback">在</span></span></span></span></span>curChart这个属性，但是输出确是undefined</p>
<pre><code class="hljs language-mounted() copyable" lang="mounted()">      this.$nextTick(function()&#123;
        console.log(this.$refs['uni-ec-canvas'])
        setTimeout(()=>&#123;
          console.log(this.$refs['uni-ec-canvas'].$curChart)
        &#125;, 2000)
      &#125;)
    &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>加了个延迟后，发现可以获取到</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a13db26a711449a085f659df540fd315~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
发现setOption又是undefined</p>
<pre><code class="hljs language-mounted() copyable" lang="mounted()">      this.$nextTick(function()&#123;
        console.log(this.$refs['uni-ec-canvas'])
        console.log(this.$refs['uni-ec-canvas'].$curChart)
        setTimeout(()=>&#123;
          console.log(this.$refs['uni-ec-canvas'].$curChart)
          console.log(this.$refs['uni-ec-canvas'].$curChart.setOption)
          // this.$refs['uni-ec-canvas'].$curChart.setOption(this.getOption())
        &#125;, 2000)
      &#125;)
    &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此法行不通。。。</p>
<p>通过观察发现，this.$refs['uni-ec-canvas']中存在ec属性和init，尝试通过以下的方式</p>
<pre><code class="hljs language-mounted() copyable" lang="mounted()">        this.initChart()
       
    &#125;,
    methods: &#123;
      initChart() &#123;
        this.$refs['uni-ec-canvas'].ec.option = this.getOption()
        this.$refs['uni-ec-canvas'].init()
      &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ojbk。。。成功了</p>
<p>自定义 的formatter生效</p></div>  
</div>
            

---
title: 'vue2.6踩坑之vchart的使用（图表）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a32cab6e595f4539b7cae50e2a326a40~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 08 Jun 2021 07:00:50 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a32cab6e595f4539b7cae50e2a326a40~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto;border:3px solid rgba(62,175,124,.2)&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-weight:700;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-radius:6px;border:2px solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c&#125;.markdown-body a:active,.markdown-body a:hover&#123;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a:before&#123;content:"⇲"&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(62,175,124,.2)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:.5rem solid;border-color:#42b983;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none&#125;.markdown-body ul li:before&#123;content:"•";margin-right:4px;color:#3eaf7c&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第8天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<h2 data-id="heading-0">介绍</h2>
<p><a href="https://v-charts.js.org/#/" target="_blank" rel="nofollow noopener noreferrer">vchart 官网地址</a></p>
<blockquote>
<p>在使用 echarts 生成图表时，经常需要做繁琐的数据类型转化、修改复杂的配置项，v-charts 的出现正是为了解决这个痛点。基于 Vue2.0 和 echarts 封装的 v-charts 图表组件，只需要统一提供一种对前后端都友好的数据格式设置简单的配置项，便可轻松生成常见的图表。</p>
</blockquote>
<p>图表种类如下图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a32cab6e595f4539b7cae50e2a326a40~tplv-k3u1fbpfcp-zoom-1.image" alt="20200525001955" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">引入</h2>
<p>官网上有非常多图表类型给我们选择，我们在main.js中按需引入即可,如折线图：</p>
<pre><code class="hljs language-vue copyable" lang="vue">import 'v-charts/lib/style.css'
import VeLine from 'v-charts/lib/line.common'
Vue.component(VeLine.name, VeLine)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">使用</h2>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <ve-line :data="chartData"></ve-line>
</template>

<script>
  export default &#123;
    data: function () &#123;
      return &#123;
        chartData: &#123;
          columns: ['日期', '访问用户', '下单用户', '下单率'],
          rows: [
            &#123; '日期': '1/1', '访问用户': 1393, '下单用户': 1093, '下单率': 0.32 &#125;,
            &#123; '日期': '1/2', '访问用户': 3530, '下单用户': 3230, '下单率': 0.26 &#125;,
            &#123; '日期': '1/3', '访问用户': 2923, '下单用户': 2623, '下单率': 0.76 &#125;
          ]
        &#125;
      &#125;
    &#125;
  &#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果图表不复杂，那么这个好像还挺简单地就结束了。。</p>
<h2 data-id="heading-3">图表属性</h2>
<p><a href="https://v-charts.js.org/#/props" target="_blank" rel="nofollow noopener noreferrer">v-charts.js.org/#/props</a>  <strong>非常重要！</strong></p>
<p>下图是一些图表的公有属性，</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e36563ce6ded46c9bfda05eb5a99691b~tplv-k3u1fbpfcp-zoom-1.image" alt="20200525010028" loading="lazy" referrerpolicy="no-referrer"></p>
<p>假如要修改图表的legend，使用虚线和实线相结合的方式去表示数据。。。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8aa4d9aafd92469399fd61f6ab7f8b8d~tplv-k3u1fbpfcp-zoom-1.image" alt="20200525002942" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如图这个红框的就是图例 <code>Legend</code>。</p>
<p>这时我们要用到 <code>extend</code> 属性，在上面图表属性的链接中有介绍</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/16ca786812984e439ba5ce0077f0a852~tplv-k3u1fbpfcp-zoom-1.image" alt="20200525011251" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>通过该属性 我们可以使用echarts中setOption的所有参数</strong></p>
<p><a href="https://echarts.apache.org/zh/option.html#legend" target="_blank" rel="nofollow noopener noreferrer">echarts.apache.org/zh/option.h…</a>   <strong>非常重要！</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/058f73f1eba54714be75e757144af640~tplv-k3u1fbpfcp-zoom-1.image" alt="20200525012640" loading="lazy" referrerpolicy="no-referrer"></p>
<p>代码如下：</p>
<p><code>echart</code>有自带的<code>icon</code>给我们使用，如前两个，但是没有这个虚线。。</p>
<p>我们可以用 <code>svg</code> 简单画一条虚线，然后根据要求转出图片的Data URI 。</p>
<p>可以直接参考菜鸟教程的 <code>svg</code> 教程 <a href="https://www.runoob.com/svg/svg-stroke.html" target="_blank" rel="nofollow noopener noreferrer">www.runoob.com/svg/svg-str…</a></p>
<p>但是画出来的虚线颜色好像固定了。。暂时只能多画几条不同颜色的虚线了</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <ve-line :data="chartData" :extend="extend"></ve-line>
</template>

<script>
  export default &#123;
    data () &#123;
      this.extend = &#123;
        'yAxis.0.name': 'y轴名字',
        'yAxis.0.nameLocation': 'middle',
        'yAxis.0.nameTextStyle.padding': 14,
        'yAxis.0.nameTextStyle.fontSize': 14,
        'series.0.type': 'line',
        'series.0.name': '访问用户',
        'series.0.lineStyle':&#123;color:'#ef55a7',type: 'dashed'&#125; ,
        'series.0.itemStyle.color': '#ef55a7',
        series: &#123;
          label: &#123;
            normal: &#123;
              show: true
            &#125;
          &#125;
        &#125;,
         legend: &#123;
          textStyle: &#123;
          &#125;,
          data: [
            &#123;name:'访问用户',icon:'circle'&#125;,    
            &#123;name:'下单用户',icon:'roundRect'&#125;,
  &#123;name:'下单率',icon: 'image://data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTEiIGhlaWdodD0iMTAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CgogIDxsaW5lIHgxPSIwIiB5MT0iNSIgeDI9IjEwMCIgeTI9IjUiIHN0cm9rZS1kYXNoYXJyYXk9IjMgMSIgc3Ryb2tlPSIjZWY1NWE3Ii8+Cgo8L3N2Zz4='&#125;,  
          ]
        &#125;
      &#125;
      return &#123;
        chartData: &#123;
          columns: ['日期', '访问用户', '下单用户', '下单率'],
          rows: [
            &#123; '日期': '1/1', '访问用户': 1393, '下单用户': 1093, '下单率': 0.32 &#125;,
            &#123; '日期': '1/2', '访问用户': 3530, '下单用户': 3230, '下单率': 0.26 &#125;,
            &#123; '日期': '1/3', '访问用户': 2923, '下单用户': 2623, '下单率': 0.76 &#125;,
            &#123; '日期': '1/4', '访问用户': 1723, '下单用户': 1423, '下单率': 0.49 &#125;,
            &#123; '日期': '1/5', '访问用户': 3792, '下单用户': 3492, '下单率': 0.323 &#125;,
            &#123; '日期': '1/6', '访问用户': 4593, '下单用户': 4293, '下单率': 0.78 &#125;
          ]
        &#125;
      &#125;
    &#125;
  &#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然不止这个图例可以改变， 还可以改变线的颜色，形状等等</p>
<p>具体可以通过这个echart的官方文档查看：<a href="https://echarts.apache.org/zh/option.html" target="_blank" rel="nofollow noopener noreferrer">echarts.apache.org/zh/option.h…</a></p>
<p>不过配置 <code>series</code> 的时候 <code>vchart</code>无法像 <code>echart</code> 那样子直接用数组表示，需要使用上面代码中的格式 <code>'series.0.type'</code> 才可以</p>
<h2 data-id="heading-4">最后</h2>
<blockquote>
<p>如果你觉得本篇文章还不错的话，那拜托再点点赞支持一下呀😝</p>
<p><strong>让我们开始这一场意外的相遇吧！~</strong></p>
<p>欢迎留言！谢谢支持！ヾ(≧▽≦*)o 冲冲冲！！</p>
<p><strong>我是4ye 咱们下期很快再见！！</strong></p>
</blockquote></div>  
</div>
            
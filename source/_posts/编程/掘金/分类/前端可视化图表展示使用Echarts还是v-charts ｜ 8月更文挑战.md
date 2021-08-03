
---
title: '前端可视化图表展示使用Echarts还是v-charts ｜ 8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://tech.taiji.com.cn/ui/api/upload/b894c660ca334cdc87d69b90366a8c81_-_echartsnpm%E4%B8%8B%E8%BD%BD.png'
author: 掘金
comments: false
date: Mon, 02 Aug 2021 21:51:15 GMT
thumbnail: 'https://tech.taiji.com.cn/ui/api/upload/b894c660ca334cdc87d69b90366a8c81_-_echartsnpm%E4%B8%8B%E8%BD%BD.png'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">介绍</h4>
<p>Echarts和v-charts都是用来做图形展示的</p>
<p>Echarts功能强大、丰富，但是数据转换很麻烦</p>
<p>v-charts功能较少，但是基本够用，数据简单。</p>
<p>Echarts官网 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fecharts.apache.org%2Fzh" target="_blank" rel="nofollow noopener noreferrer" title="https://echarts.apache.org/zh" ref="nofollow noopener noreferrer">echarts.apache.org/zh</a></p>
<p>V-charts官网 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fv-charts.js.org%2F%23%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://v-charts.js.org/#/" ref="nofollow noopener noreferrer">v-charts.js.org/#/</a></p>
<p>v-charts是基于 Vue2.0 和 echarts 封装的 v-charts 图表组件，只需要统一提供一种对前后端都友好的数据格式设置简单的配置项，便可轻松生成常见的图表。</p>
<p>npm包下载量对比</p>
<p><img src="https://tech.taiji.com.cn/ui/api/upload/b894c660ca334cdc87d69b90366a8c81_-_echartsnpm%E4%B8%8B%E8%BD%BD.png" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://tech.taiji.com.cn/ui/api/upload/6735769137044592ab44e5af66177d97_-_v-charts%E4%B8%8B%E8%BD%BD.png" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-1">Echarts</h4>
<h5 data-id="heading-2">下载</h5>
<p>你可以通过以下几种方式获取 Apache ECharts (incubating)TM。</p>
<ul>
<li>从 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fecharts.apache.org%2Fzh%2Fdownload.html" target="_blank" rel="nofollow noopener noreferrer" title="https://echarts.apache.org/zh/download.html" ref="nofollow noopener noreferrer">Apache ECharts (incubating) 官网下载界面</a> 获取官方源码包后构建。</li>
<li>在 ECharts 的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fapache%2Fincubator-echarts%2Freleases" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/apache/incubator-echarts/releases" ref="nofollow noopener noreferrer">GitHub</a> 获取。</li>
<li>通过 npm 获取 echarts，<code>npm install echarts --save</code>，详见“<a href="https://link.juejin.cn/?target=https%3A%2F%2Fecharts.apache.org%2Fzh%2Ftutorial.html%23%25E5%259C%25A8%2520webpack%2520%25E4%25B8%25AD%25E4%25BD%25BF%25E7%2594%25A8%2520ECharts" target="_blank" rel="nofollow noopener noreferrer" title="https://echarts.apache.org/zh/tutorial.html#%E5%9C%A8%20webpack%20%E4%B8%AD%E4%BD%BF%E7%94%A8%20ECharts" ref="nofollow noopener noreferrer">在 webpack 中使用 echarts</a>”</li>
<li>通过 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jsdelivr.com%2Fpackage%2Fnpm%2Fecharts" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jsdelivr.com/package/npm/echarts" ref="nofollow noopener noreferrer">jsDelivr</a> 等 CDN 引入</li>
</ul>
<h5 data-id="heading-3">引入</h5>
<p>全局引入</p>
<p>在vue的main.js中</p>
<pre><code class="copyable">// 引入echarts
import echarts from 'echarts'
Vue.prototype.$echarts = echarts
<span class="copy-code-btn">复制代码</span></code></pre>
<p>局部引入</p>
<p>在需要使用echarts的组件中引入echarts</p>
<pre><code class="copyable">import echarts from ‘echarts’;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运用</p>
<pre><code class="copyable"><div id="myChart" ref="myChart" :style="&#123;width: '300px', height: '300px'&#125;"/>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>静态数据使用js代码</p>
<pre><code class="copyable">export default &#123;
  name: 'hello',
  data () &#123;
    return &#123;
      msg: 'Welcome to Your Vue.js App'
    &#125;
  &#125;,
  mounted()&#123;
    this.drawLine();
  &#125;,
  methods: &#123;
    drawLine()&#123;
        // 基于准备好的dom，初始化echarts实例
         const myChart = echarts.init(this.$refs.myChart)
        // 绘制图表
        myChart.setOption(&#123;
            title: &#123; text: '在Vue中使用echarts' &#125;,
            tooltip: &#123;&#125;,
            xAxis: &#123;
                data: ["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]
            &#125;,
            yAxis: &#123;&#125;,
            series: [&#123;
                name: '销量',
                type: 'line',
                data: [5, 20, 36, 10, 10, 20]
            &#125;]
        &#125;);
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意：我们要在mounted生命周期函数中实例化echarts对象。因为我们要确保dom元素已经挂载到页面中</p>
<p>显示效果</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1bc9f77419c646408b1c48702808b96f~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-4">动态引用</h5>
<p>Echarts在与后端联调的时候，根据后端返回的数据经常需要做繁琐的数据类型转化、修改复杂的配置项 ，v-charts的出现可以解决这个痛点</p>
<h4 data-id="heading-5">v-charts</h4>
<p>在使用 echarts 生成图表时，经常需要做繁琐的数据类型转化、修改复杂的配置项，v-charts 的出现正是为了解决这个痛点。基于  Vue2.0 和 echarts 封装的 v-charts  图表组件，只需要统一提供一种对前后端都友好的数据格式设置简单的配置项，便可轻松生成常见的图表。</p>
<h5 data-id="heading-6">npm安装</h5>
<pre><code class="copyable">npm i v-charts echarts -S
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-7">引入</h5>
<p>全局引入</p>
<pre><code class="copyable">// 在main中引入 v - charts
import VCharts from 'v-charts'
Vue.use(VCharts)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>按需引入</p>
<p>v-charts的每种图表组件，都已经单独打包到lib文件夹下了</p>
<pre><code class="copyable">|- lib/
    |- line.common.js  -------------- 折线图
    |- bar.common.js  --------------- 条形图
    |- histogram.common.js  --------- 柱状图
    |- pie.common.js  --------------- 饼图
    |- ring.common.js  -------------- 环图
    |- funnel.common.js  ------------ 漏斗图
    |- waterfall.common.js  --------- 瀑布图
    |- radar.common.js  ------------- 雷达图
    |- map.common.js  --------------- 地图
    |- sankey.common.js  ------------ 桑基图
    |- heatmap.common.js  ----------- 热力图
    |- scatter.common.js  ----------- 散点图
    |- candle.common.js  ------------ k线图
    |- gauge.common.js  ------------- 仪表盘
    |- tree.common.js  -------------- 树图
    |- bmap.common.js  -------------- 百度地图
    |- amap.common.js  -------------- 高德地图
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">import VeLine from 'v-charts/lib/line.common' //折线图
Vue.component(VeLine.name, VeLine)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>v-charts 的数据由指标和维度组成。 维度类似我们X轴的参数，指标就是我们当前维度我们需要展示的数据，所以注意我们的数据结构。</p>
<ul>
<li>columns 中是维度和指标的集合，v-charts 中的大部分图表都是单维度多指标，所以默认第一个值为 维度，剩余的值为指标</li>
<li>rows 中是数据的集合。</li>
</ul>
<p>图表的 setting 属性中统一有两个配置：</p>
<ul>
<li>dimension 用于指定维度</li>
<li>metrics 用于指定指标</li>
</ul>
<p>给出一个例子</p>
<p>按需引入折线图</p>
<pre><code class="copyable"><template>
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
<p>页面显示效果</p>
<p><img src="https://tech.taiji.com.cn/ui/api/upload/466d7ce9db274cc79e9b662fe07461d6_-_v-chartsdemo%E5%B1%95%E7%A4%BA.png" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-8">动态引入</h5>
<p>对于v-charts的使用，在动态引入数据时，基本上不需要做转换数据格式等，按照v-charts官网demo格式数据与后端商量好返回数据类型即可。</p>
<p>v-charts还有个好处是可以做图表切换，也就是一种数据可以用多种图形展示  可参考官网<a href="https://link.juejin.cn/?target=https%3A%2F%2Fv-charts.js.org%2F%23%2Ftoggle" target="_blank" rel="nofollow noopener noreferrer" title="https://v-charts.js.org/#/toggle" ref="nofollow noopener noreferrer">v-charts.js.org/#/toggle</a></p>
<p>结论：v-charts相比Echarts做简单展示还是比较好的，学习成本和前端与后端联调配置成本较低。日常需求常见的一些图表展示使用v-charts即可。</p>
<p><em><strong>小调研一下，大家在做可视化展示的时候，使用echarts还是v-charts呀？可在评论区回复哦~</strong></em></p></div>  
</div>
            
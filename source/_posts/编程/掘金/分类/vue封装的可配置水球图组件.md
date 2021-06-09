
---
title: 'vue封装的可配置水球图组件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fbf54f71df644655a6c2936714490399~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 09 Jun 2021 00:30:43 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fbf54f71df644655a6c2936714490399~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>基于 echarts-liquidfill 开发的适用于大屏可视化的水球图组件，根据传入的数值决定水球图水量高度，可定义水球图的三条水波纹的颜色色值、水球图的背景颜色、边框颜色以及外发光阴影的颜色等属性。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fbf54f71df644655a6c2936714490399~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">1. 引入echart、echarts-liquidfill 包</h2>
<ul>
<li>cnpm i echart echarts-liquidfill element-resize-detector -S</li>
</ul>
<blockquote>
<p>我这里 echart 引入的还是 ^4.8.0的版本，如果你 npm install echart 安装的话，应该是最新的echart5版本之后的包。</p>
</blockquote>
<h2 data-id="heading-2">2. 组件的属性定义和数据定义</h2>
<ul>
<li>每个属性都给了一个默认值，这样即使引入水球图组件不传属性时也能展示一个默认的水球图图表</li>
</ul>
<pre><code class="copyable">data() &#123;
    return &#123;
      option: null,
      chart: null
    &#125;;
  &#125;,
  props: &#123;
    data: &#123;
      type: Number,
      default: 0.52
    &#125;,
    colors: &#123;
      type: Array,
      default: () => ['rgba(14, 71, 120, 1)', 'rgba(58, 160, 235, 1)', 'rgba(107, 211, 253, 1)']
    &#125;,
    backgroundColor: &#123;
      type: String,
      default: 'rgba(2, 31, 64, 1)'
    &#125;,
    borderColor: &#123;
      type: String,
      default: 'rgba(27, 114, 177, 1)'
    &#125;,
    shadowColor: &#123;
      type: String,
      default: 'rgba(107, 211, 253, 1)'
    &#125;,
    radius: &#123;
      type: String,
      default: '47%'
    &#125;
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">3. 水球图的初始化以及元素尺寸监听</h2>
<ul>
<li>this.$el 当前元素对象</li>
<li>在mounted生命周期中初始化水球图图表后进行当前元素的容器尺寸的监听</li>
</ul>
<pre><code class="copyable">const dataArr = [this.data, this.data, this.data];
    this.option = &#123;
      title: &#123;
        show: true,
        text: this.data * 100 + '%',
        textStyle: &#123;
          fontSize: 23,
          fontFamily: 'Microsoft Yahei',
          fontWeight: 'normal',
          color: '#fff'
        &#125;,
        x: '30%',
        y: '45%'
      &#125;,
      series: [
        &#123;
          type: 'liquidFill',
          radius: this.radius,
          center: ['50%', '53%'],
          // shape: 'roundRect',
          data: dataArr,
          color: this.colors,
          backgroundStyle: &#123;
            color: this.backgroundColor
          &#125;,
          outline: &#123;
            borderDistance: 0,
            itemStyle: &#123;
              borderWidth: 3,
              borderColor: this.borderColor,
              shadowBlur: 15,
              shadowColor: this.shadowColor
            &#125;
          &#125;,
          label: &#123;
            normal: &#123;
              formatter: ''
            &#125;
          &#125;
        &#125;
      ]
    &#125;;
    this.chart = echarts.init(this.$el);
    this.chart.setOption(this.option);
    window.addEventListener('resize', this.handleWindowResize);
    this.addChartResizeListener();
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">4. element-resize-detector 做 echart动态适配</h2>
<blockquote>
<p>当外层的容器变化时，图表会监听到容器元素的尺寸变化进行图表的调整适配，类似于监听浏览器的窗口改变事件。</p>
</blockquote>
<pre><code class="copyable">methods: &#123;
    /**
     * 对chart元素尺寸进行监听，当发生变化时同步更新echart视图
     */
    addChartResizeListener() &#123;
      const instance = ResizeListener(&#123;
        strategy: 'scroll',
        callOnAdd: true
      &#125;);

      instance.listenTo(this.$el, () => &#123;
        if (!this.chart) return;
        this.chart.resize();
      &#125;);
    &#125;,
    /**
     * 当窗口缩放时，echart动态调整自身大小
     */
    handleWindowResize() &#123;
      if (!this.chart) return;
      this.chart.resize();
    &#125;
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">5. 水球图的数据监听更新</h2>
<ul>
<li>当传入组件的data数据改变之后，图表是不能自动更新的，这个时候我们需要监听echart图表，手动去更新</li>
</ul>
<pre><code class="copyable">watch: &#123;
    data(newVal) &#123;
      this.option.series[0].data = newVal;
      // 更新之前先清空图表 不然会有数字重叠的问题
      this.chart.clear();
      this.chart.setOption(this.option, true);
      this.handleItemMouseover(0);
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">6. 调用组件方式</h2>
<pre><code class="copyable"><liquid-chart
  radius="60%"
  :data="21.8"
  :colors="['rgba(1, 105, 110, 1)', 'rgba(65, 233, 204, 1)', 'rgba(0, 217, 180, 1)']"
  borderColor="rgba(32, 170, 149, 1)"
  shadowColor="rgba(0, 217, 180, 1)">
</liquid-chart>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">7. 完整组件代码</h2>
<pre><code class="copyable"><template>
  <div class="liquid-chart"></div>
</template>

<script>
import echarts from 'echarts';
import 'echarts-liquidfill';
import ResizeListener from 'element-resize-detector';
export default &#123;
  name: 'Liquid-Chart',
  data() &#123;
    return &#123;
      option: null,
      chart: null
    &#125;;
  &#125;,
  props: &#123;
    data: &#123;
      type: Number,
      default: 0.52
    &#125;,
    colors: &#123;
      type: Array,
      default: () => ['rgba(14, 71, 120, 1)', 'rgba(58, 160, 235, 1)', 'rgba(107, 211, 253, 1)']
    &#125;,
    backgroundColor: &#123;
      type: String,
      default: 'rgba(2, 31, 64, 1)'
    &#125;,
    borderColor: &#123;
      type: String,
      default: 'rgba(27, 114, 177, 1)'
    &#125;,
    shadowColor: &#123;
      type: String,
      default: 'rgba(107, 211, 253, 1)'
    &#125;,
    radius: &#123;
      type: String,
      default: '47%'
    &#125;
  &#125;,
  mounted() &#123;
    const dataArr = [this.data, this.data, this.data];
    this.option = &#123;
      title: &#123;
        show: true,
        text: this.data * 100 + '%',
        textStyle: &#123;
          fontSize: 23,
          fontFamily: 'Microsoft Yahei',
          fontWeight: 'normal',
          color: '#fff'
        &#125;,
        x: '30%',
        y: '45%'
      &#125;,
      series: [
        &#123;
          type: 'liquidFill',
          radius: this.radius,
          center: ['50%', '53%'],
          // shape: 'roundRect',
          data: dataArr,
          color: this.colors,
          backgroundStyle: &#123;
            color: this.backgroundColor
          &#125;,
          outline: &#123;
            borderDistance: 0,
            itemStyle: &#123;
              borderWidth: 3,
              borderColor: this.borderColor,
              shadowBlur: 15,
              shadowColor: this.shadowColor
            &#125;
          &#125;,
          label: &#123;
            normal: &#123;
              formatter: ''
            &#125;
          &#125;
        &#125;
      ]
    &#125;;
    this.chart = echarts.init(this.$el);
    this.chart.setOption(this.option);
    window.addEventListener('resize', this.handleWindowResize);
    this.addChartResizeListener();
  &#125;,
  beforeDestroy() &#123;
    window.removeEventListener('resize', this.handleWindowResize);
  &#125;,
  methods: &#123;
    /**
     * 对chart元素尺寸进行监听，当发生变化时同步更新echart视图
     */
    addChartResizeListener() &#123;
      const instance = ResizeListener(&#123;
        strategy: 'scroll',
        callOnAdd: true
      &#125;);

      instance.listenTo(this.$el, () => &#123;
        if (!this.chart) return;
        this.chart.resize();
      &#125;);
    &#125;,
    /**
     * 当窗口缩放时，echart动态调整自身大小
     */
    handleWindowResize() &#123;
      if (!this.chart) return;
      this.chart.resize();
    &#125;
  &#125;,
  watch: &#123;
    data(newVal) &#123;
      this.option.series[0].data = newVal;
      // 更新之前先清空图表 不然会有数字重叠的问题
      this.chart.clear();
      this.chart.setOption(this.option, true);
      this.handleItemMouseover(0);
    &#125;
  &#125;
&#125;;
</script>

<style lang="scss" scoped>
.liquid-chart &#123;
  width: 100%;
  height: 100%;
&#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>码字不易，欢迎大家批评指导，互相学习。</p>
</blockquote></div>  
</div>
            
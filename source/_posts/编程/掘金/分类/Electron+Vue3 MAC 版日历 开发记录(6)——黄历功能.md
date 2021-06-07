
---
title: 'Electron+Vue3 MAC 版日历 开发记录(6)——黄历功能'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/844c86d5923d4420bf0b7f3cec1b8d92~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 06 Jun 2021 06:52:15 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/844c86d5923d4420bf0b7f3cec1b8d92~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第6天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/844c86d5923d4420bf0b7f3cec1b8d92~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>今天是周日，得让自己睡个懒觉，晚上才有时间写写代码，还好想起来了需要更新文章，做个记录。</p>
<p>今天就写个简单的「黄历」功能吧。</p>
<h2 data-id="heading-0">数据来源</h2>
<p>在之前的文章：<a href="https://juejin.cn/post/6969743835253604388" target="_blank">Electron+Vue3 MAC 版日历 开发记录(4)——农历功能</a>里，我们介绍过农历的获取，主要使用 lunar-typescript，今天我们开发的黄历功能大部分数据来自它：</p>
<p>主要使用的功能有：</p>
<pre><code class="copyable">getDateViewDate() &#123;
    const nongliString =  `农历$&#123;this.lunar.getMonthInChinese()&#125;月$&#123;this.lunar.getDayInChinese()&#125;`;
    
    const ganzhi = [
      `$&#123;this.lunar.getYearInGanZhi()&#125;$&#123;this.lunar.getYearShengXiao()&#125;年`,
      `$&#123;this.lunar.getMonthInGanZhi()&#125;月`,
      `$&#123;this.lunar.getDayInGanZhi()&#125;日`
    ];
    
    const yangliString = this.solar.toFullString();
    
    const yi = this.lunar.getDayYi();
    
    const ji = this.lunar.getDayJi();
    
    return &#123;
      nongliString: nongliString,
      ganzhi: ganzhi,
      yangliString: yangliString,
      yi: yi,
      ji: ji,
    &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中，使用了农历的干支年、月、日，阳历的全量显示 (时间、星期和星座)，还有的就是我们每天关心的「宜」和「忌」，看看每天适宜干什么和最好不干什么。</p>
<p>同样的，代码放在 <code>LunarService</code> 下。</p>
<h2 data-id="heading-1">显示布局</h2>
<p>这里布局主要使用 <a href="https://primefaces.org/primevue/showcase/#/grid" target="_blank" rel="nofollow noopener noreferrer">PrimeVue Grid</a> 布局，界面也比较简单：</p>
<pre><code class="copyable"><template>
  <Sidebar
    class="p-grid nested-grid"
    v-model:visible="sidebarVisible"
    :base-z-index="1000"
    position="full"
    @click="$emit('update:visibleFullDateView', sidebarVisible)"
  >
    <h1>黄历</h1>
    <div class="p-grid p-ai-center vertical-container nested-grid border">
      <div class="p-col-2">
        <div class="nongliString">
          &#123;&#123; lunarData.nongliString &#125;&#125;
        </div>
      </div>
      <div class="p-col-1">
        <div class="p-col-12 onecn" v-for="item in lunarData.ganzhi" :key="item">
          &#123;&#123; item &#125;&#125;
        </div>
      </div>
      <div class="p-col-9">
        <div class="p-col-12">
          <div class="p-text-bold p-text-center">
            &#123;&#123; lunarData.yangliString &#125;&#125;
          </div>
        </div>
        <div class="p-col-12">
          <Tag class="p-mr-2" icon="pi pi-check" severity="success" value="宜"></Tag>
          <Tag severity="success" :value="item" rounded v-for="item in lunarData.yi" :key="item"></Tag>
        </div>
        <div class="p-col-12">
          <Tag class="p-mr-2" icon="pi pi-times" severity="danger" value="忌"></Tag>
          <Tag severity="danger" :value="item" rounded v-for="item in lunarData.ji" :key="item"></Tag>
        </div>
      </div>
    </div>
  </Sidebar>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要说明的是，</p>
<ol>
<li>在「宜」和「忌」的展示上，是使用了 <a href="https://primefaces.org/primevue/showcase/#/tag" target="_blank" rel="nofollow noopener noreferrer">Tag 组件</a>，比较直观呈现。</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d768d09f0d90422d860c5364271af555~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="2">
<li>在这个黄历布局上，直接使用了 <a href="https://primefaces.org/primevue/showcase/#/sidebar" target="_blank" rel="nofollow noopener noreferrer">Sidebar</a>，全屏呈现。</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/373e165ab3ae4798af3da5104e17b494~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="3">
<li>最后，就是为了让农历和干支成垂直展示，增加了 css (只要保证字体大小大于宽度即可)：</li>
</ol>
<pre><code class="copyable">.nongliString &#123;
  display: flex;
  /*实现垂直居中*/
  align-items: center;
  margin: 0 auto;
  width: 2.5rem;
  font-size: 2.5em;
  color: #000;
&#125;

.onecn &#123;
  display: flex;
  /*实现垂直居中*/
  align-items: center;
  font-size: 1.4em;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">控制开关</h2>
<p>在主界面上，监听每个日期组件 Click 事件，在 <code>FullcalendarSub</code> 组件中：</p>
<pre><code class="copyable">// config：
dateClick: this.dateClick,

// methods：
dateClick(target: any) &#123;
  this.$emit('dateClick', target.date);
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同时在 <code>FullCalendarMain</code> 组件中：</p>
<pre><code class="copyable">// template
<fullcalendar-sub
  v-model:changeShowFestivals="changeShowFestivals"
  v-model:changeShowWeather="changeShowWeather"
  v-model:weather="weather"
  v-model:location="location"
  @settingClick="visibleFullSetting = true"
  @dateClick="dateClick"
/>

// 黄页组件布局
<date-view-sub
  v-model:visibleFullDateView="visibleFullDateView"
  v-model:date="date"
/>
// methods，拿到 click 的 View 中 date 值，
// 赋值，并显示「黄页」界面
dateClick(date: string) &#123;
  this.date = new Date(date);
  this.visibleFullDateView = true;
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最终显示结果如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/338bc82736974cf290a1ec3858d43d48~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">小结</h2>
<p>由于时间仓促，没有把天气预报和节假日等信息放进去，以及页面布局和样式好好调一调 (代码已经同步到 <a href="https://github.com/fanly/fanlymenu" target="_blank" rel="nofollow noopener noreferrer">github.com/fanly/fanly…</a>，欢迎查看)，等着下一步好好继续优化。</p>
<p>未完待续！</p></div>  
</div>
            
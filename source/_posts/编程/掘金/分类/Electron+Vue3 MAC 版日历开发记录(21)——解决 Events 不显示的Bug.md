
---
title: 'Electron+Vue3 MAC 版日历开发记录(21)——解决 Events 不显示的Bug'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/844c86d5923d4420bf0b7f3cec1b8d92~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 21 Jun 2021 07:31:21 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/844c86d5923d4420bf0b7f3cec1b8d92~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第21天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/844c86d5923d4420bf0b7f3cec1b8d92~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>今天是周一，相信大家都很忙，晚上我才有时间坐下来想一想写写代码，在整理的过程中，我发现这几天一直没解决的一个问题：那就是没显示「事件」。</p>
<h2 data-id="heading-0">Events 不显示问题排查</h2>
<p>我把 Events 参考<a href="https://codesandbox.io/s/github/fullcalendar/fullcalendar-example-projects/tree/master/vue3-typescript?file=/src/Demo.vue:899-913" target="_blank" rel="nofollow noopener noreferrer">官网 Demo</a> 加上 Events 显示：</p>
<pre><code class="copyable"><template>
  <full-calendar
    ref="fullcalendar"
    :options="calendarOptions"
  >
    <template #eventContent="arg">
      <i>&#123;&#123; arg.event.title &#125;&#125;</i>
    </template>
  </full-calendar>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但发现还是显示不了。我打了一个 log 看了看，有数据回调啊：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a0fe2e8e35c84698978be2365482a361~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>但就是无法显示 Events，我后来把 Prop Events 加入到 calendarOptions：</p>
<pre><code class="copyable">calendarOptions: &#123;
    plugins: [dayGridPlugin, interactionPlugin],
    headerToolbar: &#123;
      left: 'prev,next',
      center: 'title',
      right: '',
    &#125;,
    initialEvents: this.event, // 看这里
    selectable: true,
    select: this.dateClick,
    eventClick: this.eventClick,
    eventChange: this.updateView,
    editable: false,
    // height: Number(import.meta.env.VITE_APP_HEIGHT) - 10,
    aspectRatio: 1.31,
    views: this.dayCellNewContent(),
    locale: zhLocale,
&#125; as CalendarOptions,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这时候是有时候显示，有时候不显示。</p>
<p>对于这个问题，其实马上就能定位出毛病在哪：由于获取的数据是异步的，所以新数据并没有被重新加载。</p>
<p>这让我很难受了，Vue 不就是因为 MVVM 模式而出名的吗？在我百思不得其解的时候，只能看看 FullCalendar 官网，找找问题所在了：</p>
<p>在官网上<a href="https://fullcalendar.io/docs/initialEvents" target="_blank" rel="nofollow noopener noreferrer">initialEvents</a>还真有这么一段话来说明：</p>
<blockquote>
<p>This is exactly like specifying event as an array except that if the supplied value changes, the calendar will NOT be updated to reflect. Only applicable to declarative front-end frameworks such as React, Vue, and Angular.</p>
</blockquote>
<blockquote>
<p>Useful for when you want to supply an initial set of events and then manipulate these events via the API. If you use initialEvents, when your component receives new props, your changes will not be overwritten with the original event array.</p>
</blockquote>
<p>此时此刻，我只有一个念头，我想办法自己整 Calender，不用这个 FullCalender，完全不符合 Vue 数据同步更新 View 的理念嘛。</p>
<h2 data-id="heading-1">Events 显示方法</h2>
<p>好在，还是有办法解决的，官网提供了两个接口：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e2bffb63eeee4a02b55bd848ca637fd2~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>先看看我们的 Events Prop：</p>
<pre><code class="copyable">props: &#123;
  events: &#123;
    type: Array,
    default() &#123;
      return [];
    &#125;,
  &#125;,
  ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为我把 <code>events</code> 定义为 <code>Array</code>，提示类型不匹配的 <code>typecheck</code> 的错误：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca2bb55552c54a0ebef578d05757be85~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>所以需要加上一个 “类型”：</p>
<pre><code class="copyable">events: &#123;
  type: Array,
  default: [] as EventInput[],
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>具体同步数据到 View 上，只需要监听 Events 数据变化，在 Watch 里增加逻辑：</p>
<p>第一种<a href="https://fullcalendar.io/docs/Calendar-addEvent" target="_blank" rel="nofollow noopener noreferrer">Calendar::addEvent</a> 方法实现：</p>
<pre><code class="copyable">watch: &#123;
  events(): void &#123;
    const calendarArray = this.$refs['fullcalendar'] as any;
    const calendarApi = calendarArray.getApi();
    this.events?.forEach((event: any) => &#123;
      return calendarApi.addEvent(event);
   &#125;)
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看似能解决问题：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/31bbc8a3a06d4344b78220889a11bd1b~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>但这种方法不能保证是不是会重复 add Event，而且我觉得效果不一定好。</p>
<p>接着寻找，我们发现fullcalender 提供了第二种接口：
<code>calendarApi.addEventSource</code>，而需要的 <code>EventSourceInput</code> 类型为：</p>
<pre><code class="copyable">declare type EventSourceInput = EventSourceInputObject | 
EventInput[] | EventSourceFunc | 
string;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这类型本身也包含了数组类型，所以，可以用一条语句代替上面的代码：</p>
<pre><code class="copyable">      // this.events?.forEach((event: any) => &#123;
      //   return calendarApi.addEvent(event);
      // &#125;)
      // const eventsTemp: EventInput[] = this.events;
      calendarApi.addEventSource(this.events);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>达到相同的目标：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6104177d50f743f3b56123294aeabdb1~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">小结</h2>
<p>今天在重构部分主要把 <code>FullCalendarMain</code> 主界面的三个 NDrawerContent 放到对应的页面布局上，这样看起来显得统一一些，而且只留下了，每个布局的 <code>NDrawer</code> 头部：</p>
<pre><code class="copyable"><n-drawer
    v-model:show="visibleFullSetting"
    :width="settingDrawerWidth"
    placement="left"
  >
    <setting-sub
      v-model:changeShowWeather="changeShowWeather"
      v-model:changeShowFestivals="changeShowFestivals"
      v-model:location="location"
      @focusClick="focusClick"
    />
  </n-drawer>
  <n-drawer
    v-model:show="visibleFullDateView"
    :width="hlDrawerWidth"
    placement="left"
  >
    <date-view-sub
      v-model:date="date"
    />
  </n-drawer>
  <n-drawer
    v-model:show="visibleECSub"
    :width="ecDrawerWidth"
    placement="left"
  >
    <event-create-sub
      v-model:event="event"
      @addEventClick="addEventClick"
    />
  </n-drawer>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相信大家也能看出来这段代码还有值得继续重构：去除相同的代码，让代码保持简洁。</p>
<p>每天进步一点点，是我的目标，相信今晚发现问题到解决问题，能让自己处理 Bug 上有所记录和总结。</p>
<p>未完待续！</p>
<blockquote>
<p>代码已同步到 github 上了：<a href="https://github.com/fanly/fanlymenu" target="_blank" rel="nofollow noopener noreferrer">github.com/fanly/fanly…</a></p>
</blockquote></div>  
</div>
            
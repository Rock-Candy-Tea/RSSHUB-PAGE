
---
title: 'Electron+Vue3 MAC 版日历开发记录(29)——知识篇使用Template Refs'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/844c86d5923d4420bf0b7f3cec1b8d92~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 29 Jun 2021 01:19:50 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/844c86d5923d4420bf0b7f3cec1b8d92~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第29天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/844c86d5923d4420bf0b7f3cec1b8d92~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>其实在重构过程，也是自我学习和了解 Vue 3 的一些深入知识的过程。比如：</p>
<p>在我们的 Location 坐标通过 <code>computed</code> 后：</p>
<pre><code class="copyable">  provide() &#123;
    return &#123;
      flocation: computed(() => this.store.state.location),
    &#125;;
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们在子组件中拿到这个数据：</p>
<pre><code class="copyable">const flocation: ComputedRef<FLocation> | undefined = inject('flocation');
    console.log(flocation);
    const longitude = flocation?.value.longitude;
    const latitude = flocation?.value.latitude;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d793526791cc4f2ba9c23457debc9fb5~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>得到的数据类型是：<code>ComputedRefImpl</code> 类型，这时候可以通过定义类型：<code>ComputedRef<FLocation> | undefined</code> 来匹配，之前我们都出一刀切直接用 <code>any</code>。现在看起来严谨多了。</p>
<h2 data-id="heading-0">Template Refs</h2>
<p>说回今天的核心：使用 Template Refs 来做重构，先看看这个案例：</p>
<pre><code class="copyable">// FullcalendarSub.vue

    events(): void &#123;
      const calendarArray = this.$refs['fullcalendar'] as any;
      const calendarApi = calendarArray.getApi();
      calendarApi.addEventSource(this.events);
    &#125;,
  &#125;,
  methods: &#123;
    updateColors() &#123;
      this.calendarOptions.eventColor = this.themeVars.primaryColor;
    &#125;,
    updateView() &#123;
      const calendarArray = this.$refs['fullcalendar'] as any;
      console.log(calendarArray);
      const calendarApi = calendarArray.getApi();
      const viewContent = this.dayCellNewContent();
      calendarApi.changeView('dayGridMonth', viewContent['dayGridMonth']);
      // 这种成本可能更高
      // this.calendarApi.render();
    &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在多处都使用到了 <code>const calendarArray = this.$refs['fullcalendar'] as any;</code>，而这里也是使用了 <code>$refs</code>，自从 Vue 3 开始不建议使用 this 了，而提供了本文开始说的 <code>Template Refs</code>。</p>
<h2 data-id="heading-1">自定义 fullcalendar 变量</h2>
<pre><code class="copyable"><full-calendar
  ref="fullcalendar"
  :options="calendarOptions"
>
  <template #eventContent="arg">
    <i>&#123;&#123; arg.event.title &#125;&#125;</i>
  </template>
</full-calendar>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>setup</code> 自定义一个和 ref 一样的变量名：</p>
<pre><code class="copyable">  setup() &#123;
    const weather = inject('weather');
    const store = useStore();
    const themeVars = ref(useThemeVars());
    const fullcalendar = ref(null);

    onMounted(() => &#123;
      // the DOM element will be assigned to the ref after initial render
      console.log(fullcalendar.value);// <div>This is a root element</div>
    &#125;);
    return &#123;
      weather,
      darkTheme,
      store,
      themeVars,
      fullcalendar,
    &#125;;
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们看看 mounted 后是不是可以拿到数据了：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/464bd2cbfb64492f9f7957b6b6838b1f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">获取 FullCalendar API</h2>
<p>现在就可以重构上述的代码，用一个统一变量拿到我们的 FullCalendar API。</p>
<pre><code class="copyable">let fullcalendarApi = ref<InstanceType<typeof CalendarApi>>();
    onMounted(() => &#123;
      fullcalendarApi = Object.getOwnPropertyDescriptor(fullcalendar.value, 'getApi')?.value();
    &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注：这里我是有 Proxy 直接获取函数，老报错。有知道方法的伙伴告诉我，我太缺乏 vue3 Proxy 相关知识了.</p>
</blockquote>
<p>所以，我采用了 <code>Object.getOwnPropertyDescriptor</code>，拿到我们所需要的 CalendarApi 了。</p>
<h2 data-id="heading-3">重构</h2>
<p>对于之前的方法里，我直接可调用：</p>
<pre><code class="copyable">    events(): void &#123;
      if (this.fullcalendarApi == null) &#123;
        this.fullcalendarApi = Object.getOwnPropertyDescriptor(this.fullcalendar, 'getApi')?.value();
      &#125;
      this.fullcalendarApi.addEventSource(this.events as EventSourceInput);
    &#125;,
    
        updateView() &#123;
      if (this.fullcalendarApi == null) &#123;
        this.fullcalendarApi = Object.getOwnPropertyDescriptor(this.fullcalendar, 'getApi')?.value();
      &#125;
      const viewContent = this.dayCellNewContent();
      this.fullcalendarApi.changeView('dayGridMonth', viewContent['dayGridMonth'] as DateRangeInput | DateInput);
    &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注：这里 this.fullcalendarApi 这个只我老拿到的是 <code>null</code>，有知道原因的伙伴麻烦告知～</p>
</blockquote>
<h2 data-id="heading-4">小结</h2>
<p>今天零零碎碎修改了一些 warning，降了 20 两个，有待于进一步优化。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/000a549058f942e7a6362c162f6729f9~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>未完待续！</p></div>  
</div>
            

---
title: 'Electron+Vue3 MAC 版日历开发记录(13)——事件功能重构'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/844c86d5923d4420bf0b7f3cec1b8d92~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 13 Jun 2021 06:50:19 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/844c86d5923d4420bf0b7f3cec1b8d92~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第13天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/844c86d5923d4420bf0b7f3cec1b8d92~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这几天核心功能放在了 Event 事件功能开发上，本来想把 Event 删除功能补充上去，但我发现在 Notion API 里似乎没有提供 <code>delete API</code>，有发现的伙伴们，欢迎在评论里告诉我。</p>
<p>因为之前两天代码有点乱，所以今天重新重构下，把一些重复的代码放在一起。也让代码看起来清晰一点，为后续的「插件化 」开发做准备。</p>
<h2 data-id="heading-0">重构 Event 功能</h2>
<p>之前把 Events 获取和创建 Event 分别在列表页和创建页面上操作，这回统一放在 Main 页面上，理由如下：</p>
<ol>
<li>同样的数据操作，尽可能放在一起，便于统一管理；</li>
<li>对于创建一个 Event 后，可以在 Main 页面上同步更新 list 数据。而且不需要再发送一个信号到列表页去触发更新。</li>
</ol>
<pre><code class="copyable">// FullCalendarMain.vue

<fullcalendar-sub
  v-model:changeShowFestivals="changeShowFestivals"
  v-model:changeShowWeather="changeShowWeather"
  v-model:events="events"
  v-model:weather="weather"
  v-model:location="location"
  @menuClick="menuClick"
  @dateClick="dateClick"
/>

... 

setup() &#123;
    // 调用 event service
    const eventService = ref(new EventService());
    const events:any = ref([]);
    const visibleFullSetting = ref(false);
    const store = useStore();
    
    return &#123;
      eventService,
      events,
      visibleFullSetting,
      store,
    &#125;;
&#125;,

...

methods: &#123;
  updateEvents(): any &#123;
    this.eventService.getEvents().then((data) => &#123;
    this.events = data;
      &#125;);
  &#125;,
  
    ...
  addEventClick(data: any) &#123;
      this.eventService.postEvent(data.title, data.start, data.end)
        .then((response: any) => &#123;
          this.$toast.add(&#123;severity:'success', summary: 'Success Message', detail:'Order submitted', life: 3000&#125;);
          this.updateEvents();
    &#125;);
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样至少可以保证子模块只负责页面展示，数据怎么获取的交给上一层去思考了。同时，也增加了一个 Toast 组件，便于一些异步操作的更新结果显示：</p>
<pre><code class="copyable"><Toast />

this.$toast.add(&#123;severity:'success', summary: 'Success Message', detail:'event submitted', life: 3000&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一样的，在子布局上，只需要一个 <code>events prop</code> 即可：</p>
<pre><code class="copyable">// FullcalendarSub.vue
props: &#123;
events: &#123;&#125;,
changeShowFestivals: Boolean,
changeShowWeather: Boolean,
weather: &#123;&#125;,
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在创建 Event 页面上，把提交 Notion 服务器代码移除，只留下本页面需要的操作：</p>
<pre><code class="copyable">emits: [
  'addEventClick',
  'update:visibleFullDialog',
],

...

add(): void &#123;
  const start: Date = this.dates[0];
  const end: Date = this.dates[1] == null ? this.dates[0] : this.dates[1];

  this.$emit('addEventClick',&#123;
    title: this.eventText,
    start: start,
    end: end,
  &#125;);
  this.dates = [];
  this.eventText = '';
  this.$emit('update:visibleFullDialog', false);
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">更新 Event</h2>
<p>更新 Event 就很简单了，Notion 官方提供的接口满足 Restful，所以更新的请求就是 <code>patch</code>，我们利用 <code>Postman</code> 模拟下就知道了：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6a5eec25a74b448ba90034813bc98d97~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>执行看看后台的变化：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f8049289352f4c42b4b80d97af2addd8~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>一样的，代码实现也很简单了：</p>
<pre><code class="copyable">/**
* 更新 title 或者 start、end 到 Notion API
*/
async patchEvent(
id: string,
title: string,
start: Date,
end: Date,
) &#123;
  const http = wrapper(axios, &#123;
    maxCacheSize: 15,
  &#125;);
  const res = await http(&#123;
    url: import.meta.env.VITE_NOTION_PAGE_API + '/' + id,
    method: 'patch',
    headers: this.headers,
    data: &#123;
      'properties': &#123;
        'title': &#123;
          'type': 'rich_text',
          'rich_text': [&#123;
            'type': 'text',
            'text': &#123; 'content': title &#125;,
          &#125;],
        &#125;,
        'start': &#123;
          'type': 'date',
          'date': &#123; 'start': start &#125;,
        &#125;,
        'end': &#123;
          'type': 'date',
          'date': &#123; 'start': end &#125;,
        &#125;,
      &#125;,
    &#125;,
  &#125;);

  return res;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在布局上，我们增加一个 Event 点击事件：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2b5df1dc82264c4199b7a75b5991c104~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>具体做法和之前点击时间事件 (<code>dateClick</code>) 一样，过程代码就不重复了，只有在 Event 创建页面增加了 <code>Event Prop</code> 为了获取更新 Event 的属性值：</p>
<pre><code class="copyable">// EventCreateDialog.vue
props: &#123;
  visibleFullDialog: Boolean,
  event: Object,
&#125;,
emits: [
  'addEventClick',
  'update:visibleFullDialog',
],

...

watch: &#123;
  event(): void &#123;
      if (this.event != null) &#123;
        this.eventText = this.event.title;
        this.dates = [this.event.start, this.event.end];
      &#125; else &#123;
        this.eventText = '';
        this.dates = [];
      &#125;
    &#125;
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们点击一个 Event 看看是否调出页面，以及内容是否填充：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bf34911dd3354be38a7eed217f54e0fa~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>最后，就是提交更新事件，根据是否有 <code>event id</code> 来判断是增加 Event 还是更新 Event：</p>
<pre><code class="copyable">addEventClick(data: any) &#123;
  if (data.id) &#123;
    this.eventService.patchEvent(data.id, data.title, data.start, data.end)
    .then((response: any) => &#123;
      this.$toast.add(&#123;severity:'success', summary: 'Success Message', detail:'event submitted', life: 3000&#125;);
      this.updateEvents();
    &#125;);
  &#125; else &#123;
    this.eventService.postEvent(data.title, data.start, data.end)
    .then((response: any) => &#123;
      this.$toast.add(&#123;severity:'success', summary: 'Success Message', detail:'event submitted', life: 3000&#125;);
      this.updateEvents();
    &#125;);
  &#125;
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注：整个代码已放在 Github 上了，<code>tag</code> 为 <code>0.6.13</code>。</p>
</blockquote>
<h2 data-id="heading-2">小结</h2>
<p>到目前为止除了「删除 Event」未实现之外，基本完成了 Event 的「增加、更新、获取」。</p>
<p>明天是端午节了，这两天开始着手就之前开发的功能做一个修修补补，把一个产品该有的都补上了，具体核心功能估计需要放一放了，就目前的功能足够第一版使用了，未完待续！</p>
<blockquote>
<p>这个项目的所有记录基本放进专栏里了，欢迎查看：
<a href="https://juejin.cn/column/6968672386895839269" target="_blank">Electron+Vue3 MAC 版日历开发记录</a>
最近有伙伴问代码链接：代码已同步到 github 上了：<a href="https://github.com/fanly/fanlymenu" target="_blank" rel="nofollow noopener noreferrer">github.com/fanly/fanly…</a></p>
</blockquote></div>  
</div>
            